"""
AI Nexus - Database Operations
CRUD operations for all models
"""
from database.db import get_db_session, close_db_session
from database.models import User, Favorite, Progress, Activity, SavedPrompt, Badge, UserStats
from datetime import datetime
from typing import Optional, List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class DatabaseOperations:
    """Database operations wrapper"""
    
    # ==================== USER OPERATIONS ====================
    
    @staticmethod
    def create_user(username: str, email: str = None, **kwargs) -> Optional[Dict]:
        """Create a new user - returns dict with user data"""
        db = get_db_session()
        try:
            user = User(username=username, email=email, **kwargs)
            db.add(user)
            db.commit()
            db.refresh(user)
            
            user_id = user.id
            
            # Create user stats
            stats = UserStats(user_id=user_id)
            db.add(stats)
            db.commit()
            
            logger.info(f"Created user: {username}")
            
            # Return dict instead of ORM object
            return {
                'id': user_id,
                'username': username,
                'email': email
            }
        except Exception as e:
            db.rollback()
            logger.error(f"Error creating user: {e}")
            return None
        finally:
            close_db_session(db)
    
    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[Dict]:
        """Get user by ID - returns dict"""
        db = get_db_session()
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if user:
                return {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'role': user.role,
                    'industry': user.industry,
                    'skill_level': user.skill_level,
                    'tech_stack': user.tech_stack,
                    'learning_style': user.learning_style,
                    'preferences': user.preferences,
                    'created_at': user.created_at.isoformat() if user.created_at else None,
                    'updated_at': user.updated_at.isoformat() if user.updated_at else None
                }
            return None
        except Exception as e:
            logger.error(f"Error getting user: {e}")
            return None
        finally:
            close_db_session(db)
    
    @staticmethod
    def get_user_by_username(username: str) -> Optional[Dict]:
        """Get user by username - returns dict"""
        db = get_db_session()
        try:
            user = db.query(User).filter(User.username == username).first()
            if user:
                return {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'role': user.role,
                    'industry': user.industry,
                    'skill_level': user.skill_level,
                    'tech_stack': user.tech_stack,
                    'learning_style': user.learning_style,
                    'preferences': user.preferences,
                    'created_at': user.created_at.isoformat() if user.created_at else None,
                    'updated_at': user.updated_at.isoformat() if user.updated_at else None
                }
            return None
        except Exception as e:
            logger.error(f"Error getting user: {e}")
            return None
        finally:
            close_db_session(db)
    
    @staticmethod
    def update_user(user_id: int, **kwargs) -> bool:
        """Update user profile"""
        db = get_db_session()
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if user:
                for key, value in kwargs.items():
                    setattr(user, key, value)
                user.updated_at = datetime.utcnow()
                db.commit()
                return True
            return False
        except Exception as e:
            db.rollback()
            logger.error(f"Error updating user: {e}")
            return False
        finally:
            close_db_session(db)
    
    # ==================== FAVORITES OPERATIONS ====================
    
    @staticmethod
    def add_favorite(user_id: int, item_type: str, item_id: str, item_data: dict) -> bool:
        """Add item to favorites"""
        db = get_db_session()
        try:
            # Check if already favorited
            existing = db.query(Favorite).filter(
                Favorite.user_id == user_id,
                Favorite.item_type == item_type,
                Favorite.item_id == item_id
            ).first()
            
            if existing:
                return True  # Already favorited
            
            favorite = Favorite(
                user_id=user_id,
                item_type=item_type,
                item_id=item_id,
                item_data=item_data
            )
            db.add(favorite)
            db.commit()
            
            # Update stats
            if item_type == 'tool':
                DatabaseOperations._update_stats(user_id, tools_favorited=1)
            
            logger.info(f"Added favorite: {item_type} {item_id} for user {user_id}")
            return True
        except Exception as e:
            db.rollback()
            logger.error(f"Error adding favorite: {e}")
            return False
        finally:
            close_db_session(db)
    
    @staticmethod
    def remove_favorite(user_id: int, item_type: str, item_id: str) -> bool:
        """Remove item from favorites"""
        db = get_db_session()
        try:
            favorite = db.query(Favorite).filter(
                Favorite.user_id == user_id,
                Favorite.item_type == item_type,
                Favorite.item_id == item_id
            ).first()
            
            if favorite:
                db.delete(favorite)
                db.commit()
                return True
            return False
        except Exception as e:
            db.rollback()
            logger.error(f"Error removing favorite: {e}")
            return False
        finally:
            close_db_session(db)
    
    @staticmethod
    def get_favorites(user_id: int, item_type: str = None) -> List[Favorite]:
        """Get user favorites"""
        db = get_db_session()
        try:
            query = db.query(Favorite).filter(Favorite.user_id == user_id)
            if item_type:
                query = query.filter(Favorite.item_type == item_type)
            return query.order_by(Favorite.created_at.desc()).all()
        except Exception as e:
            logger.error(f"Error getting favorites: {e}")
            return []
        finally:
            close_db_session(db)
    
    @staticmethod
    def is_favorite(user_id: int, item_type: str, item_id: str) -> bool:
        """Check if item is favorited"""
        db = get_db_session()
        try:
            favorite = db.query(Favorite).filter(
                Favorite.user_id == user_id,
                Favorite.item_type == item_type,
                Favorite.item_id == item_id
            ).first()
            return favorite is not None
        except Exception as e:
            logger.error(f"Error checking favorite: {e}")
            return False
        finally:
            close_db_session(db)
    
    # ==================== PROGRESS OPERATIONS ====================
    
    @staticmethod
    def mark_tutorial_complete(user_id: int, tutorial_id: str) -> bool:
        """Mark tutorial as complete"""
        db = get_db_session()
        try:
            progress = db.query(Progress).filter(
                Progress.user_id == user_id,
                Progress.tutorial_id == tutorial_id
            ).first()
            
            if progress:
                if not progress.completed:
                    progress.completed = True
                    progress.progress_percent = 100
                    progress.completed_at = datetime.utcnow()
                    db.commit()
                    DatabaseOperations._update_stats(user_id, tutorials_completed=1)
            else:
                progress = Progress(
                    user_id=user_id,
                    tutorial_id=tutorial_id,
                    completed=True,
                    progress_percent=100,
                    completed_at=datetime.utcnow()
                )
                db.add(progress)
                db.commit()
                DatabaseOperations._update_stats(user_id, tutorials_completed=1)
            
            logger.info(f"Marked tutorial {tutorial_id} complete for user {user_id}")
            return True
        except Exception as e:
            db.rollback()
            logger.error(f"Error marking tutorial complete: {e}")
            return False
        finally:
            close_db_session(db)
    
    @staticmethod
    def get_completed_tutorials(user_id: int) -> List[str]:
        """Get list of completed tutorial IDs"""
        db = get_db_session()
        try:
            completed = db.query(Progress).filter(
                Progress.user_id == user_id,
                Progress.completed == True
            ).all()
            return [p.tutorial_id for p in completed]
        except Exception as e:
            logger.error(f"Error getting completed tutorials: {e}")
            return []
        finally:
            close_db_session(db)
    
    @staticmethod
    def is_tutorial_complete(user_id: int, tutorial_id: str) -> bool:
        """Check if tutorial is complete"""
        db = get_db_session()
        try:
            progress = db.query(Progress).filter(
                Progress.user_id == user_id,
                Progress.tutorial_id == tutorial_id,
                Progress.completed == True
            ).first()
            return progress is not None
        except Exception as e:
            logger.error(f"Error checking tutorial completion: {e}")
            return False
        finally:
            close_db_session(db)
    
    # ==================== ACTIVITY OPERATIONS ====================
    
    @staticmethod
    def track_activity(user_id: int, activity_type: str, item_id: str = None, details: dict = None) -> bool:
        """Track user activity"""
        db = get_db_session()
        try:
            activity = Activity(
                user_id=user_id,
                activity_type=activity_type,
                item_id=item_id,
                details=details or {}
            )
            db.add(activity)
            db.commit()
            
            # Update last activity date
            DatabaseOperations._update_last_activity(user_id)
            
            return True
        except Exception as e:
            db.rollback()
            logger.error(f"Error tracking activity: {e}")
            return False
        finally:
            close_db_session(db)
    
    @staticmethod
    def get_recent_activities(user_id: int, limit: int = 10) -> List[Activity]:
        """Get recent activities"""
        db = get_db_session()
        try:
            return db.query(Activity).filter(
                Activity.user_id == user_id
            ).order_by(Activity.created_at.desc()).limit(limit).all()
        except Exception as e:
            logger.error(f"Error getting activities: {e}")
            return []
        finally:
            close_db_session(db)
    
    # ==================== SAVED PROMPTS OPERATIONS ====================
    
    @staticmethod
    def save_prompt(user_id: int, prompt_id: str, prompt_data: dict, notes: str = None) -> bool:
        """Save prompt to library"""
        db = get_db_session()
        try:
            # Check if already saved
            existing = db.query(SavedPrompt).filter(
                SavedPrompt.user_id == user_id,
                SavedPrompt.prompt_id == prompt_id
            ).first()
            
            if existing:
                return True
            
            saved_prompt = SavedPrompt(
                user_id=user_id,
                prompt_id=prompt_id,
                prompt_data=prompt_data,
                custom_notes=notes
            )
            db.add(saved_prompt)
            db.commit()
            
            DatabaseOperations._update_stats(user_id, prompts_saved=1)
            
            logger.info(f"Saved prompt {prompt_id} for user {user_id}")
            return True
        except Exception as e:
            db.rollback()
            logger.error(f"Error saving prompt: {e}")
            return False
        finally:
            close_db_session(db)
    
    @staticmethod
    def get_saved_prompts(user_id: int) -> List[SavedPrompt]:
        """Get user's saved prompts"""
        db = get_db_session()
        try:
            return db.query(SavedPrompt).filter(
                SavedPrompt.user_id == user_id
            ).order_by(SavedPrompt.created_at.desc()).all()
        except Exception as e:
            logger.error(f"Error getting saved prompts: {e}")
            return []
        finally:
            close_db_session(db)
    
    # ==================== STATS OPERATIONS ====================
    
    @staticmethod
    def get_user_stats(user_id: int) -> Optional[UserStats]:
        """Get user statistics"""
        db = get_db_session()
        try:
            stats = db.query(UserStats).filter(UserStats.user_id == user_id).first()
            if not stats:
                # Create stats if not exists
                stats = UserStats(user_id=user_id)
                db.add(stats)
                db.commit()
                db.refresh(stats)
            return stats
        except Exception as e:
            logger.error(f"Error getting user stats: {e}")
            return None
        finally:
            close_db_session(db)
    
    @staticmethod
    def _update_stats(user_id: int, **kwargs) -> bool:
        """Internal method to update user stats"""
        db = get_db_session()
        try:
            stats = db.query(UserStats).filter(UserStats.user_id == user_id).first()
            if not stats:
                stats = UserStats(user_id=user_id)
                db.add(stats)
            
            for key, value in kwargs.items():
                if hasattr(stats, key):
                    current_value = getattr(stats, key) or 0
                    setattr(stats, key, current_value + value)
            
            stats.updated_at = datetime.utcnow()
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            logger.error(f"Error updating stats: {e}")
            return False
        finally:
            close_db_session(db)
    
    @staticmethod
    def _update_last_activity(user_id: int) -> bool:
        """Update last activity date"""
        db = get_db_session()
        try:
            stats = db.query(UserStats).filter(UserStats.user_id == user_id).first()
            if stats:
                stats.last_activity_date = datetime.utcnow()
                db.commit()
            return True
        except Exception as e:
            db.rollback()
            logger.error(f"Error updating last activity: {e}")
            return False
        finally:
            close_db_session(db)
