"""
AI Nexus - Database Models
SQLAlchemy models for data persistence
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON, Text, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime, timezone


class Base(DeclarativeBase):
    """Base class for all database models"""
    pass


def utc_now():
    """Return current UTC time with timezone info (replaces deprecated datetime.utcnow)"""
    return datetime.now(timezone.utc)


class User(Base):
    """User profile and preferences"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, index=True)
    role = Column(String(100))
    industry = Column(String(100))
    skill_level = Column(String(50))
    tech_stack = Column(JSON)
    learning_style = Column(String(50))
    preferences = Column(JSON)
    created_at = Column(DateTime(timezone=True), default=utc_now)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)
    
    # Relationships
    favorites = relationship("Favorite", back_populates="user", cascade="all, delete-orphan")
    progress = relationship("Progress", back_populates="user", cascade="all, delete-orphan")
    activities = relationship("Activity", back_populates="user", cascade="all, delete-orphan")
    saved_prompts = relationship("SavedPrompt", back_populates="user", cascade="all, delete-orphan")
    badges = relationship("Badge", back_populates="user", cascade="all, delete-orphan")
    stats = relationship("UserStats", back_populates="user", uselist=False, cascade="all, delete-orphan")


class Favorite(Base):
    """User favorites (tools, prompts, tutorials)"""
    __tablename__ = 'favorites'
    __table_args__ = (
        UniqueConstraint('user_id', 'item_type', 'item_id', name='unique_user_favorite'),
    )
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    item_type = Column(String(50), nullable=False)  # 'tool', 'prompt', 'tutorial'
    item_id = Column(String(100), nullable=False)
    item_data = Column(JSON)
    created_at = Column(DateTime(timezone=True), default=utc_now)
    
    user = relationship("User", back_populates="favorites")


class Progress(Base):
    """Tutorial completion progress"""
    __tablename__ = 'progress'
    __table_args__ = (
        UniqueConstraint('user_id', 'tutorial_id', name='unique_user_progress'),
    )
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    tutorial_id = Column(String(100), nullable=False)
    completed = Column(Boolean, default=False)
    progress_percent = Column(Integer, default=0)
    completed_at = Column(DateTime(timezone=True))
    started_at = Column(DateTime(timezone=True), default=utc_now)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)
    
    user = relationship("User", back_populates="progress")


class Activity(Base):
    """User activity tracking"""
    __tablename__ = 'activities'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    activity_type = Column(String(100), nullable=False)
    item_id = Column(String(100))
    details = Column(JSON)
    created_at = Column(DateTime(timezone=True), default=utc_now, index=True)
    
    user = relationship("User", back_populates="activities")


class SavedPrompt(Base):
    """User's saved prompts library"""
    __tablename__ = 'saved_prompts'
    __table_args__ = (
        UniqueConstraint('user_id', 'prompt_id', name='unique_user_prompt'),
    )
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    prompt_id = Column(String(100), nullable=False)
    prompt_data = Column(JSON)
    custom_notes = Column(Text)
    created_at = Column(DateTime(timezone=True), default=utc_now)
    
    user = relationship("User", back_populates="saved_prompts")


class Badge(Base):
    """User achievements and badges"""
    __tablename__ = 'badges'
    __table_args__ = (
        UniqueConstraint('user_id', 'badge_id', name='unique_user_badge'),
    )
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    badge_id = Column(String(100), nullable=False)
    earned_at = Column(DateTime(timezone=True), default=utc_now)
    
    user = relationship("User", back_populates="badges")


class UserStats(Base):
    """User statistics and metrics"""
    __tablename__ = 'user_stats'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), unique=True, nullable=False, index=True)
    total_xp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    tutorials_completed = Column(Integer, default=0)
    prompts_saved = Column(Integer, default=0)
    tools_favorited = Column(Integer, default=0)
    current_streak = Column(Integer, default=0)
    longest_streak = Column(Integer, default=0)
    last_activity_date = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)
    
    user = relationship("User", back_populates="stats")
