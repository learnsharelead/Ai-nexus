"""
AI Nexus - Database Connection and Session Management
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from database.models import Base
import os
from pathlib import Path

# Database configuration
DATABASE_DIR = Path(__file__).parent.parent / "data"
DATABASE_DIR.mkdir(exist_ok=True)
DATABASE_PATH = DATABASE_DIR / "ainexus.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Create engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # Needed for SQLite
    echo=False  # Set to True for SQL debugging
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create scoped session for thread safety
ScopedSession = scoped_session(SessionLocal)


def init_db():
    """Initialize database - create all tables"""
    try:
        Base.metadata.create_all(bind=engine)
        print(f"✅ Database initialized at: {DATABASE_PATH}")
        return True
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        return False


def get_db():
    """Get database session - use with context manager"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_db_session():
    """Get a new database session"""
    return SessionLocal()


def close_db_session(db):
    """Close database session"""
    if db:
        db.close()


def reset_db():
    """Reset database - drop all tables and recreate"""
    try:
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        print("✅ Database reset successfully")
        return True
    except Exception as e:
        print(f"❌ Error resetting database: {e}")
        return False


def check_db_exists():
    """Check if database file exists"""
    return DATABASE_PATH.exists()


def get_db_info():
    """Get database information"""
    return {
        "path": str(DATABASE_PATH),
        "exists": check_db_exists(),
        "url": DATABASE_URL,
        "size_bytes": DATABASE_PATH.stat().st_size if check_db_exists() else 0
    }
