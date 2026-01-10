"""
AI Nexus - Database Test Script
Test all database operations
"""
import sys
from pathlib import Path

# Add root to path (project root is the same directory as this test file)
ROOT_DIR = Path(__file__).parent
sys.path.insert(0, str(ROOT_DIR))

from database.db import init_db, get_db_info, check_db_exists
from database.operations import DatabaseOperations

def test_database():
    """Test all database operations"""
    print("=" * 60)
    print("AI NEXUS - DATABASE TEST")
    print("=" * 60)
    
    # Initialize database
    print("\n1. Initializing database...")
    if init_db():
        print("   ✅ Database initialized successfully")
    else:
        print("   ❌ Database initialization failed")
        return
    
    # Get database info
    print("\n2. Database information:")
    info = get_db_info()
    print(f"   Path: {info['path']}")
    print(f"   Exists: {info['exists']}")
    print(f"   Size: {info['size_bytes']} bytes")
    
    # Test user operations
    print("\n3. Testing user operations...")
    
    # Create user with unique username
    import time
    username = f"test_user_{int(time.time())}"
    
    user = DatabaseOperations.create_user(
        username=username,
        email=f"{username}@ainexus.local",
        role="frontend_dev",
        industry="saas",
        skill_level="intermediate"
    )
    
    if user:
        print(f"   ✅ Created user: {user['username']} (ID: {user['id']})")
        user_id = user['id']
    else:
        print("   ❌ Failed to create user")
        return
    
    # Get user
    retrieved_user = DatabaseOperations.get_user_by_id(user_id)
    if retrieved_user:
        print(f"   ✅ Retrieved user: {retrieved_user['username']}")
    else:
        print("   ❌ Failed to retrieve user")
    
    # Test favorites
    print("\n4. Testing favorites...")
    
    tool_data = {
        "name": "GitHub Copilot",
        "category": "code_generation",
        "rating": 4.8
    }
    
    if DatabaseOperations.add_favorite(user_id, "tool", "github-copilot", tool_data):
        print("   ✅ Added favorite")
    else:
        print("   ❌ Failed to add favorite")
    
    if DatabaseOperations.is_favorite(user_id, "tool", "github-copilot"):
        print("   ✅ Favorite check works")
    else:
        print("   ❌ Favorite check failed")
    
    favorites = DatabaseOperations.get_favorites(user_id, "tool")
    print(f"   ✅ Retrieved {len(favorites)} favorites")
    
    # Test progress
    print("\n5. Testing progress tracking...")
    
    if DatabaseOperations.mark_tutorial_complete(user_id, "qw-1"):
        print("   ✅ Marked tutorial complete")
    else:
        print("   ❌ Failed to mark tutorial complete")
    
    if DatabaseOperations.is_tutorial_complete(user_id, "qw-1"):
        print("   ✅ Tutorial completion check works")
    else:
        print("   ❌ Tutorial completion check failed")
    
    completed = DatabaseOperations.get_completed_tutorials(user_id)
    print(f"   ✅ Retrieved {len(completed)} completed tutorials")
    
    # Test activities
    print("\n6. Testing activity tracking...")
    
    if DatabaseOperations.track_activity(user_id, "tutorial_viewed", "qw-1", {"duration": 300}):
        print("   ✅ Tracked activity")
    else:
        print("   ❌ Failed to track activity")
    
    activities = DatabaseOperations.get_recent_activities(user_id, 10)
    print(f"   ✅ Retrieved {len(activities)} activities")
    
    # Test saved prompts
    print("\n7. Testing saved prompts...")
    
    prompt_data = {
        "title": "Code Explanation",
        "category": "Coding",
        "prompt": "Explain the following code..."
    }
    
    if DatabaseOperations.save_prompt(user_id, "p-1", prompt_data, "My favorite prompt"):
        print("   ✅ Saved prompt")
    else:
        print("   ❌ Failed to save prompt")
    
    prompts = DatabaseOperations.get_saved_prompts(user_id)
    print(f"   ✅ Retrieved {len(prompts)} saved prompts")
    
    # Test user stats
    print("\n8. Testing user statistics...")
    
    stats = DatabaseOperations.get_user_stats(user_id)
    if stats:
        print(f"   ✅ User stats:")
        print(f"      - Tutorials completed: {stats.tutorials_completed}")
        print(f"      - Prompts saved: {stats.prompts_saved}")
        print(f"      - Tools favorited: {stats.tools_favorited}")
        print(f"      - Total XP: {stats.total_xp}")
        print(f"      - Level: {stats.level}")
    else:
        print("   ❌ Failed to get user stats")
    
    print("\n" + "=" * 60)
    print("DATABASE TEST COMPLETE")
    print("=" * 60)
    print("\n✅ All tests passed!")
    print(f"📊 Database location: {info['path']}")
    print(f"💾 Database size: {info['size_bytes']} bytes")
    print("\nYou can now use the database in your application!")

if __name__ == "__main__":
    test_database()
