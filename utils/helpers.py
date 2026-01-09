"""
AI Nexus - Utility Functions
Helper functions for the application with database persistence
"""
import streamlit as st
import json
import logging
from datetime import datetime
from typing import Optional, List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import database operations
try:
    from database.operations import DatabaseOperations
    DB_AVAILABLE = True
except ImportError:
    logger.warning("Database not available, using session state fallback")
    DB_AVAILABLE = False


def get_current_user_id() -> Optional[int]:
    """Get current user ID from session state"""
    return st.session_state.get('user_id')


def copy_to_clipboard(text: str, success_message: str = "Copied to clipboard!"):
    """Display text with a copy button - user can select and copy manually"""
    st.code(text, language="text")
    col1, col2 = st.columns([4, 1])
    with col2:
        if st.button("📋 Copy", key=f"copy_{hash(text)}", use_container_width=True):
            st.toast("✅ Text displayed above - use Ctrl+C to copy", icon="✅")
            st.info("💡 **Tip:** Select the text above and press Ctrl+C (or Cmd+C on Mac) to copy")
            return True
    return False


def save_to_local_storage(key: str, value: any):
    """Save data to session state (fallback when DB not available)"""
    try:
        if 'local_storage' not in st.session_state:
            st.session_state.local_storage = {}
        st.session_state.local_storage[key] = value
    except Exception as e:
        logger.error(f"Error saving to local storage: {e}")


def get_from_local_storage(key: str, default=None):
    """Get data from session state (fallback when DB not available)"""
    try:
        if 'local_storage' not in st.session_state:
            st.session_state.local_storage = {}
        return st.session_state.local_storage.get(key, default)
    except Exception as e:
        logger.error(f"Error getting from local storage: {e}")
        return default


def add_to_favorites(item_type: str, item_id: str, item_data: dict) -> bool:
    """Add an item to favorites"""
    try:
        user_id = get_current_user_id()
        if not user_id:
            logger.warning("No user ID, using session state")
            # Fallback to session state
            favorites = get_from_local_storage('favorites', {})
            if item_type not in favorites:
                favorites[item_type] = {}
            favorites[item_type][item_id] = {
                'data': item_data,
                'added_at': datetime.now().isoformat()
            }
            save_to_local_storage('favorites', favorites)
            return True
        
        if DB_AVAILABLE:
            success = DatabaseOperations.add_favorite(user_id, item_type, item_id, item_data)
            if success:
                track_activity('favorite_added', item_id, {'type': item_type})
            return success
        else:
            # Fallback to session state
            favorites = get_from_local_storage('favorites', {})
            if item_type not in favorites:
                favorites[item_type] = {}
            favorites[item_type][item_id] = {
                'data': item_data,
                'added_at': datetime.now().isoformat()
            }
            save_to_local_storage('favorites', favorites)
            return True
    except Exception as e:
        logger.error(f"Error adding to favorites: {e}")
        st.error(f"❌ Error saving favorite: {str(e)}")
        return False


def remove_from_favorites(item_type: str, item_id: str) -> bool:
    """Remove an item from favorites"""
    try:
        user_id = get_current_user_id()
        if not user_id:
            # Fallback to session state
            favorites = get_from_local_storage('favorites', {})
            if item_type in favorites and item_id in favorites[item_type]:
                del favorites[item_type][item_id]
                save_to_local_storage('favorites', favorites)
                return True
            return False
        
        if DB_AVAILABLE:
            return DatabaseOperations.remove_favorite(user_id, item_type, item_id)
        else:
            favorites = get_from_local_storage('favorites', {})
            if item_type in favorites and item_id in favorites[item_type]:
                del favorites[item_type][item_id]
                save_to_local_storage('favorites', favorites)
                return True
            return False
    except Exception as e:
        logger.error(f"Error removing from favorites: {e}")
        st.error(f"❌ Error removing favorite: {str(e)}")
        return False


def is_favorite(item_type: str, item_id: str) -> bool:
    """Check if an item is in favorites"""
    try:
        user_id = get_current_user_id()
        if not user_id:
            favorites = get_from_local_storage('favorites', {})
            return item_type in favorites and item_id in favorites[item_type]
        
        if DB_AVAILABLE:
            return DatabaseOperations.is_favorite(user_id, item_type, item_id)
        else:
            favorites = get_from_local_storage('favorites', {})
            return item_type in favorites and item_id in favorites[item_type]
    except Exception as e:
        logger.error(f"Error checking favorite: {e}")
        return False


def get_all_favorites(item_type: str = None) -> Dict:
    """Get all favorites, optionally filtered by type"""
    try:
        user_id = get_current_user_id()
        if not user_id:
            favorites = get_from_local_storage('favorites', {})
            if item_type:
                return favorites.get(item_type, {})
            return favorites
        
        if DB_AVAILABLE:
            favorites_list = DatabaseOperations.get_favorites(user_id, item_type)
            # Convert to dict format
            result = {}
            for fav in favorites_list:
                if fav.item_type not in result:
                    result[fav.item_type] = {}
                result[fav.item_type][fav.item_id] = {
                    'data': fav.item_data,
                    'added_at': fav.created_at.isoformat()
                }
            if item_type:
                return result.get(item_type, {})
            return result
        else:
            favorites = get_from_local_storage('favorites', {})
            if item_type:
                return favorites.get(item_type, {})
            return favorites
    except Exception as e:
        logger.error(f"Error getting favorites: {e}")
        return {} if item_type else {}


def mark_tutorial_complete(tutorial_id: str) -> bool:
    """Mark a tutorial as complete"""
    try:
        user_id = get_current_user_id()
        if not user_id:
            completed = get_from_local_storage('completed_tutorials', [])
            if tutorial_id not in completed:
                completed.append(tutorial_id)
                save_to_local_storage('completed_tutorials', completed)
            return True
        
        if DB_AVAILABLE:
            success = DatabaseOperations.mark_tutorial_complete(user_id, tutorial_id)
            if success:
                track_activity('tutorial_completed', tutorial_id)
            return success
        else:
            completed = get_from_local_storage('completed_tutorials', [])
            if tutorial_id not in completed:
                completed.append(tutorial_id)
                save_to_local_storage('completed_tutorials', completed)
            return True
    except Exception as e:
        logger.error(f"Error marking tutorial complete: {e}")
        st.error(f"❌ Error saving progress: {str(e)}")
        return False


def is_tutorial_complete(tutorial_id: str) -> bool:
    """Check if a tutorial is complete"""
    try:
        user_id = get_current_user_id()
        if not user_id:
            completed = get_from_local_storage('completed_tutorials', [])
            return tutorial_id in completed
        
        if DB_AVAILABLE:
            return DatabaseOperations.is_tutorial_complete(user_id, tutorial_id)
        else:
            completed = get_from_local_storage('completed_tutorials', [])
            return tutorial_id in completed
    except Exception as e:
        logger.error(f"Error checking tutorial completion: {e}")
        return False


def get_completed_tutorials() -> List[str]:
    """Get all completed tutorials"""
    try:
        user_id = get_current_user_id()
        if not user_id:
            return get_from_local_storage('completed_tutorials', [])
        
        if DB_AVAILABLE:
            return DatabaseOperations.get_completed_tutorials(user_id)
        else:
            return get_from_local_storage('completed_tutorials', [])
    except Exception as e:
        logger.error(f"Error getting completed tutorials: {e}")
        return []


def save_prompt_to_library(prompt_id: str, prompt_data: dict) -> bool:
    """Save a prompt to user's personal library"""
    try:
        user_id = get_current_user_id()
        if not user_id:
            library = get_from_local_storage('prompt_library', {})
            library[prompt_id] = {
                'data': prompt_data,
                'saved_at': datetime.now().isoformat()
            }
            save_to_local_storage('prompt_library', library)
            return True
        
        if DB_AVAILABLE:
            success = DatabaseOperations.save_prompt(user_id, prompt_id, prompt_data)
            if success:
                track_activity('prompt_saved', prompt_id)
            return success
        else:
            library = get_from_local_storage('prompt_library', {})
            library[prompt_id] = {
                'data': prompt_data,
                'saved_at': datetime.now().isoformat()
            }
            save_to_local_storage('prompt_library', library)
            return True
    except Exception as e:
        logger.error(f"Error saving prompt: {e}")
        st.error(f"❌ Error saving prompt: {str(e)}")
        return False


def get_saved_prompts() -> Dict:
    """Get all saved prompts"""
    try:
        user_id = get_current_user_id()
        if not user_id:
            return get_from_local_storage('prompt_library', {})
        
        if DB_AVAILABLE:
            prompts_list = DatabaseOperations.get_saved_prompts(user_id)
            result = {}
            for prompt in prompts_list:
                result[prompt.prompt_id] = {
                    'data': prompt.prompt_data,
                    'saved_at': prompt.created_at.isoformat(),
                    'notes': prompt.custom_notes
                }
            return result
        else:
            return get_from_local_storage('prompt_library', {})
    except Exception as e:
        logger.error(f"Error getting saved prompts: {e}")
        return {}


def track_activity(activity_type: str, item_id: str, details: dict = None) -> bool:
    """Track user activity for analytics"""
    try:
        user_id = get_current_user_id()
        if not user_id:
            activities = get_from_local_storage('activities', [])
            activity = {
                'type': activity_type,
                'item_id': item_id,
                'timestamp': datetime.now().isoformat(),
                'details': details or {}
            }
            activities.append(activity)
            # Keep only last 100 activities
            if len(activities) > 100:
                activities = activities[-100:]
            save_to_local_storage('activities', activities)
            return True
        
        if DB_AVAILABLE:
            return DatabaseOperations.track_activity(user_id, activity_type, item_id, details)
        else:
            activities = get_from_local_storage('activities', [])
            activity = {
                'type': activity_type,
                'item_id': item_id,
                'timestamp': datetime.now().isoformat(),
                'details': details or {}
            }
            activities.append(activity)
            if len(activities) > 100:
                activities = activities[-100:]
            save_to_local_storage('activities', activities)
            return True
    except Exception as e:
        logger.error(f"Error tracking activity: {e}")
        return False


def get_recent_activities(limit: int = 10) -> List[Dict]:
    """Get recent activities"""
    try:
        user_id = get_current_user_id()
        if not user_id:
            activities = get_from_local_storage('activities', [])
            return activities[-limit:][::-1]
        
        if DB_AVAILABLE:
            activities_list = DatabaseOperations.get_recent_activities(user_id, limit)
            return [{
                'type': a.activity_type,
                'item_id': a.item_id,
                'timestamp': a.created_at.isoformat(),
                'details': a.details
            } for a in activities_list]
        else:
            activities = get_from_local_storage('activities', [])
            return activities[-limit:][::-1]
    except Exception as e:
        logger.error(f"Error getting activities: {e}")
        return []


def calculate_ai_score() -> int:
    """Calculate user's AI proficiency score based on activities"""
    try:
        user_id = get_current_user_id()
        
        if user_id and DB_AVAILABLE:
            stats = DatabaseOperations.get_user_stats(user_id)
            if stats:
                # Calculate score from stats
                score = min(100, (
                    stats.tutorials_completed * 5 +
                    stats.prompts_saved * 2 +
                    stats.tools_favorited * 1
                ))
                return int(score)
        
        # Fallback calculation
        completed_tutorials = len(get_completed_tutorials())
        saved_prompts = len(get_saved_prompts())
        favorites = get_all_favorites()
        total_favorites = sum(len(items) for items in favorites.values())
        activities = get_from_local_storage('activities', [])
        
        score = min(100, (
            completed_tutorials * 5 +
            saved_prompts * 2 +
            total_favorites * 1 +
            len(activities) * 0.5
        ))
        
        return int(score)
    except Exception as e:
        logger.error(f"Error calculating AI score: {e}")
        return 0

