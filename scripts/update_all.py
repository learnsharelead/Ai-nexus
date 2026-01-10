"""
AI Nexus - Content Update Automation Script
Automatically updates content from various sources
"""
import sys
from pathlib import Path

# Add root to path
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

from data.ai_news import get_all_news, get_trending_topics
from datetime import datetime
import json


def update_news_cache():
    """Force update news cache"""
    print("🔄 Updating AI News cache...")
    
    try:
        # Clear cache and fetch fresh news
        import streamlit as st
        st.cache_data.clear()
        
        news = get_all_news()
        trending = get_trending_topics()
        
        print(f"✅ Fetched {len(news)} news articles")
        print(f"✅ Found {len(trending)} trending topics")
        
        # Save update timestamp
        timestamp_file = ROOT_DIR / "data" / "last_update.json"
        with open(timestamp_file, 'w') as f:
            json.dump({
                "last_news_update": datetime.now().isoformat(),
                "article_count": len(news),
                "trending_count": len(trending)
            }, f, indent=2)
        
        print(f"✅ Update timestamp saved")
        return True
        
    except Exception as e:
        print(f"❌ Error updating news: {e}")
        return False


def check_content_freshness():
    """Check how fresh the content is"""
    print("\n📊 Content Freshness Report")
    print("=" * 50)
    
    try:
        from data.final_tutorials import get_all_tutorials
        from data.final_prompts import get_all_prompts
        from data.final_assets import get_all_tools
        from data.ai_hacks import get_all_hacks
        
        tutorials = get_all_tutorials()
        prompts = get_all_prompts()
        tools = get_all_tools()
        hacks = get_all_hacks()
        news = get_all_news()
        
        print(f"📚 Tutorials: {len(tutorials)}")
        print(f"💡 Prompts: {len(prompts)}")
        print(f"🛠️  Tools: {len(tools)}")
        print(f"🔥 Hacks: {len(hacks)}")
        print(f"📰 News Articles: {len(news)}")
        
        # Check last update
        timestamp_file = ROOT_DIR / "data" / "last_update.json"
        if timestamp_file.exists():
            with open(timestamp_file, 'r') as f:
                data = json.load(f)
                last_update = datetime.fromisoformat(data['last_news_update'])
                hours_ago = (datetime.now() - last_update).total_seconds() / 3600
                print(f"\n⏰ Last news update: {hours_ago:.1f} hours ago")
        
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ Error checking freshness: {e}")


def suggest_new_content():
    """Suggest what content to add next"""
    print("\n💡 Content Suggestions")
    print("=" * 50)
    
    suggestions = [
        "🔥 Add hacks for: Gemini 2.0, Cursor Composer, Windsurf",
        "📚 Add tutorials for: LangGraph, CrewAI, AutoGen",
        "💡 Add prompts for: Code review, Architecture design, Testing",
        "🛠️  Add tools for: Bolt.new, Replit Agent, Lovable.dev",
        "📰 News is auto-updated via RSS feeds"
    ]
    
    for suggestion in suggestions:
        print(f"  {suggestion}")
    
    print("=" * 50)


def main():
    """Main update function"""
    print("🚀 AI Nexus Content Update Script")
    print("=" * 50)
    
    # Update news
    update_news_cache()
    
    # Check freshness
    check_content_freshness()
    
    # Suggestions
    suggest_new_content()
    
    print("\n✅ Update complete!")
    print("\nNext steps:")
    print("1. Review content suggestions above")
    print("2. Add new content following docs/CONTENT_UPDATE_GUIDE.md")
    print("3. Test locally with: streamlit run app.py")
    print("4. Commit changes: git add -A && git commit -m 'Content update'")


if __name__ == "__main__":
    main()
