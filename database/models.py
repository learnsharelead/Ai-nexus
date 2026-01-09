"""
AI Nexus - Database Models
SQLAlchemy models for data persistence
"""
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, JSON, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class User(Base):
    """User profile and preferences"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True)
    role = Column(String(100))
    industry = Column(String(100))
    skill_level = Column(String(50))
    tech_stack = Column(JSON)
    learning_style = Column(String(50))
    preferences = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Favorite(Base):
    """User favorites (tools, prompts, tutorials)"""
    __tablename__ = 'favorites'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    item_type = Column(String(50), nullable=False)  # 'tool', 'prompt', 'tutorial'
    item_id = Column(String(100), nullable=False)
    item_data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)


class Progress(Base):
    """Tutorial completion progress"""
    __tablename__ = 'progress'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    tutorial_id = Column(String(100), nullable=False)
    completed = Column(Boolean, default=False)
    progress_percent = Column(Integer, default=0)
    completed_at = Column(DateTime)
    started_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Activity(Base):
    """User activity tracking"""
    __tablename__ = 'activities'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    activity_type = Column(String(100), nullable=False)
    item_id = Column(String(100))
    details = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)


class SavedPrompt(Base):
    """User's saved prompts library"""
    __tablename__ = 'saved_prompts'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    prompt_id = Column(String(100), nullable=False)
    prompt_data = Column(JSON)
    custom_notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class Badge(Base):
    """User achievements and badges"""
    __tablename__ = 'badges'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    badge_id = Column(String(100), nullable=False)
    earned_at = Column(DateTime, default=datetime.utcnow)


class UserStats(Base):
    """User statistics and metrics"""
    __tablename__ = 'user_stats'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, nullable=False)
    total_xp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    tutorials_completed = Column(Integer, default=0)
    prompts_saved = Column(Integer, default=0)
    tools_favorited = Column(Integer, default=0)
    current_streak = Column(Integer, default=0)
    longest_streak = Column(Integer, default=0)
    last_activity_date = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
