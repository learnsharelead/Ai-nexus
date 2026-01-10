"""
AI Nexus - Database Connection and Session Management
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager
from database.models import Base
import os
import logging
from pathlib import Path

# Configure logging
logger = logging.getLogger(__name__)

# Database configuration
DATABASE_DIR = Path(__file__).parent.parent / "data"
DATABASE_DIR.mkdir(exist_ok=True)
DATABASE_PATH = DATABASE_DIR / "ainexus.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Create engine with connection pooling settings
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # Needed for SQLite
    echo=False,  # Set to True for SQL debugging
    pool_pre_ping=True,  # Verify connections before use
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create scoped session for thread safety
ScopedSession = scoped_session(SessionLocal)


def init_db():
    """Initialize database - create all tables"""
    try:
        Base.metadata.create_all(bind=engine)
        logger.info(f"Database initialized at: {DATABASE_PATH}")
        print(f"✅ Database initialized at: {DATABASE_PATH}")
        return True
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        print(f"❌ Error initializing database: {e}")
        return False


@contextmanager
def get_db_context():
    """
    Context manager for database sessions.
    
    Usage:
        with get_db_context() as db:
            user = db.query(User).first()
            # Changes are auto-committed on success
            # Auto-rollback on exception
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"Database error, rolling back: {e}")
        raise
    finally:
        db.close()


def get_db():
    """Get database session - use with context manager (FastAPI style)"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_db_session():
    """Get a new database session (legacy - prefer get_db_context)"""
    return SessionLocal()


def close_db_session(db):
    """Close database session (legacy - prefer get_db_context)"""
    if db:
        db.close()


def reset_db():
    """Reset database - drop all tables and recreate"""
    try:
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        logger.info("Database reset successfully")
        print("✅ Database reset successfully")
        return True
    except Exception as e:
        logger.error(f"Error resetting database: {e}")
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


def get_engine():
    """Get the SQLAlchemy engine"""
    return engine
