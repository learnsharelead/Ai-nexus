"""
AI Nexus - Pytest Configuration
Fixtures and configuration for testing
"""
import pytest
import sys
from pathlib import Path

# Add project root to path
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))


@pytest.fixture
def sample_user_data():
    """Sample user data for testing"""
    return {
        "username": "test_user",
        "email": "test@example.com",
        "role": "fullstack_dev",
        "industry": "saas",
        "skill_level": "intermediate"
    }


@pytest.fixture
def sample_tutorial():
    """Sample tutorial data for testing"""
    return {
        "id": "qw-test",
        "title": "Test Tutorial",
        "category": "Testing",
        "duration": "5 min",
        "difficulty": "Beginner",
        "role": ["fullstack_dev"],
        "rating": 4.5,
        "completions": 100,
        "icon": "🧪",
        "description": "A test tutorial for unit testing.",
        "topics": ["Testing"]
    }


@pytest.fixture
def sample_prompt():
    """Sample prompt data for testing"""
    return {
        "id": "p-test",
        "title": "Test Prompt",
        "category": "testing",
        "prompt": "This is a test prompt for {variable}.",
        "variables": ["variable"],
        "difficulty": "Beginner",
        "uses": 10,
        "rating": 4.0,
        "tags": ["test"],
        "ai_models": ["GPT-4o"]
    }


@pytest.fixture
def sample_tool():
    """Sample tool data for testing"""
    return {
        "id": "tool-test",
        "name": "Test Tool",
        "category": "testing_qa",
        "description": "A test tool for unit testing.",
        "url": "https://example.com",
        "pricing": "Free",
        "rating": 4.5,
        "icon": "🔧"
    }
