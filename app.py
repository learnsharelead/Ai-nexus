"""
AI Nexus - The Complete AI Transformation Ecosystem
Main Application Entry Point
"""
import streamlit as st
import sys
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add root to path
ROOT_DIR = Path(__file__).parent
sys.path.insert(0, str(ROOT_DIR))

from styles.custom_css import CUSTOM_CSS
from config.settings import APP_NAME, APP_TAGLINE, APP_VERSION

# FORCE RELOAD DATA MODULES
# This is required to fix the persistent "dummy data" issue caused by stale sys.modules cache
import importlib
import data.final_tutorials
importlib.reload(data.final_tutorials)

# Initialize database
try:
    from database.db import init_db, check_db_exists
    from database.operations import DatabaseOperations
    
    @st.cache_resource
    def initialize_database():
        """Initialize database with caching to prevent repeated initialization"""
        if not check_db_exists():
            logger.info("Initializing database for first time...")
            init_db()
        return True
    
    DB_AVAILABLE = initialize_database()
except Exception as e:
    logger.error(f"Database initialization failed: {e}")
    DB_AVAILABLE = False

# Page configuration
# Page configuration
st.set_page_config(
    page_title=f"{APP_NAME} - {APP_TAGLINE}",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/ainexus',
        'Report a bug': 'https://github.com/ainexus/issues',
        'About': f"# {APP_NAME}\n{APP_TAGLINE}"
    }
)

# Note: Cache clearing removed - use proper cache invalidation via TTL or keys instead
# If data issues persist, implement versioned caching in individual functions

# Inject custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Initialize session state
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = None
if 'onboarding_complete' not in st.session_state:
    st.session_state.onboarding_complete = False
if 'selected_role' not in st.session_state:
    st.session_state.selected_role = None

@st.cache_resource
def get_or_create_default_user():
    """Get or create default user with caching to prevent repeated DB queries"""
    if DB_AVAILABLE:
        try:
            # Try to get default user
            default_user = DatabaseOperations.get_user_by_username('default_user')
            if not default_user:
                # Create default user
                default_user = DatabaseOperations.create_user(
                    username='default_user',
                    email='user@ainexus.local'
                )
            if default_user:
                # default_user is already a dict with 'id' key
                logger.info(f"User session initialized: {default_user['id']}")
                return default_user['id']
        except Exception as e:
            logger.error(f"Error initializing user: {e}")
            return None
    return None

if 'user_id' not in st.session_state:
    st.session_state.user_id = get_or_create_default_user()


# What's New Modal removed for compact UI

def render_top_nav():
    """Render horizontal top navigation with global search"""
    cols = st.columns([1.2, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 1.2])
    
    with cols[0]:
        st.markdown("<h3 style='margin:0; padding:0; background: linear-gradient(90deg, #6366F1, #EC4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: Outfit; font-weight:800;'>AI Nexus</h3>", unsafe_allow_html=True)
    
    pages = [
        ("Home", "home", "🏠"),
        ("Learn", "learning", "📚"),
        ("Tools", "tools", "🔧"),
        ("Prompts", "prompts", "💡"),
        ("Hacks", "hacks", "🔥"),
        ("News", "news", "📰"),
        ("Profile", "profile", "👤"),
        ("Dash", "dashboard", "📊")
    ]
    
    for i, (name, key, icon) in enumerate(pages):
        with cols[i + 1]:
            label = f"{icon} {name}"
            if st.button(label, key=f"topnav_{key}", use_container_width=True):
                st.session_state.current_page = key
                st.rerun()
    
    # Global Search in last column
    with cols[9]:
        search_query = st.text_input("🔍", placeholder="Search...", key="global_search", label_visibility="collapsed")
        if search_query:
            st.session_state.global_search_query = search_query
            st.session_state.current_page = "search_results"
            st.rerun()




def render_home():
    """Render the home page"""
    from data.final_assets import get_all_tools
    from data.final_prompts import get_all_prompts
    from data.final_tutorials import get_all_tutorials
    from datetime import datetime

    st.markdown("<h1>System Overview</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748B; font-size: 1.1rem; margin-bottom: 1rem;'>Architecting the future of professional AI integration.</p>", unsafe_allow_html=True)

    # Tip of the Day
    tips = [
        ("💡", "Start prompts with the role you want the AI to play: 'You are an expert...'"),
        ("🎯", "Always provide context before asking a question - AI works better with background info."),
        ("🔄", "Iterate on prompts! First attempts are rarely perfect."),
        ("📝", "Use Chain of Thought for complex reasoning: 'Think step by step...'"),
        ("⚡", "Lower temperature (0.1-0.3) for factual tasks, higher (0.7-1.0) for creative ones."),
        ("🛡️", "Always review AI output before using it in production code."),
        ("📊", "Break large tasks into smaller, focused prompts for better results."),
        ("🔍", "Include example inputs and outputs to guide the AI's response format."),
        ("🚀", "Use system prompts to set persistent behavior and constraints."),
        ("💎", "Specific instructions beat vague ones: 'Write 3 bullet points' vs 'Write briefly'."),
    ]
    
    day_of_year = datetime.now().timetuple().tm_yday
    tip = tips[day_of_year % len(tips)]
    
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(236, 72, 153, 0.1)); padding: 1rem 1.5rem; border-radius: 12px; border-left: 4px solid #6366F1; margin-bottom: 1.5rem;">
            <span style="font-weight: 700; color: #6366F1;">💡 Tip of the Day:</span>
            <span style="color: #334155;">{tip[1]}</span>
        </div>
    """, unsafe_allow_html=True)

    # Dynamic Stats
    tool_count = len(get_all_tools())
    prompt_count = len(get_all_prompts())
    tutorial_count = len(get_all_tutorials())

    # Removed stats banner for compact layout
    st.markdown("## 🎯 Strategic Modules")
    
    # Feature cards - First row
    cols = st.columns(3)
    
    features_row1 = [
        ("Learning Hub", "learning", "🎓", "Personalized courses designed to help you master professional AI tools.", "linear-gradient(135deg, #6366F1 0%, #818CF8 100%)"),
        ("AI Tool Universe", "tools", "🛠️", "A curated directory of 1,200+ industry-leading AI resources.", "linear-gradient(135deg, #EC4899 0%, #F472B6 100%)"),
        ("Prompt Library", "prompts", "💡", "Expert-grade prompt engineering frameworks for elite results.", "linear-gradient(135deg, #F59E0B 0%, #FB923C 100%)")
    ]
    
    for i, (title, key, icon, desc, gradient) in enumerate(features_row1):
        with cols[i]:
            st.markdown(f"""
                <div class="glass-card" style="border-top: 4px solid white !important; background: {gradient}0A !important;">
                    <div style="font-family: Outfit; font-weight:800; font-size:1.2rem; color: #1E293B; margin-bottom: 12px; display: flex; align-items: center;">
                        <span style="background: {gradient}; -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{icon} {title}</span>
                    </div>
                    <div style="font-size:0.95rem; color:#475569; margin-bottom: 1.5rem; line-height: 1.5;">{desc}</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Dive Into {title}", key=f"btn_h_{key}", use_container_width=True):
                st.session_state.current_page = key
                st.rerun()
    
    # Feature cards - Second row (NEW!)
    cols2 = st.columns(3)
    
    features_row2 = [
        ("AI Hacks", "hacks", "🔥", "10x your productivity with curated AI tips, tricks, and workflows.", "linear-gradient(135deg, #EF4444 0%, #F87171 100%)"),
        ("AI Latest News", "news", "📰", "Real-time AI news from OpenAI, Anthropic, Google, and more.", "linear-gradient(135deg, #10B981 0%, #34D399 100%)"),
        ("", "", "", "", "")  # Empty placeholder
    ]
    
    for i, (title, key, icon, desc, gradient) in enumerate(features_row2):
        with cols2[i]:
            if title:  # Only render if not empty
                st.markdown(f"""
                    <div class="glass-card" style="border-top: 4px solid white !important; background: {gradient}0A !important;">
                        <div style="font-family: Outfit; font-weight:800; font-size:1.2rem; color: #1E293B; margin-bottom: 12px; display: flex; align-items: center;">
                            <span style="background: {gradient}; -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{icon} {title}</span>
                        </div>
                        <div style="font-size:0.95rem; color:#475569; margin-bottom: 1.5rem; line-height: 1.5;">{desc}</div>
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"Dive Into {title}", key=f"btn_h_{key}", use_container_width=True):
                    st.session_state.current_page = key
                    st.rerun()
    
    st.markdown("## ⚡ Quick Start")
    
    if not st.session_state.onboarding_complete:
        st.info("🎯 Complete your profile to get personalized recommendations!")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
                Get started in 3 simple steps:
                1. **Select your role** - Tell us what you do
                2. **Assess your skills** - Quick AI proficiency quiz
                3. **Get personalized path** - Tailored learning journey
            """)
        with col2:
            if st.button("🚀 Complete Profile", use_container_width=True, type="primary"):
                st.session_state.current_page = "profile"
                st.rerun()
    else:
        st.success("✅ Profile complete! Check your personalized dashboard.")
        
        # Quick Actions for returning users
        st.markdown("### ⚡ Quick Actions")
        qa_cols = st.columns(4)
        
        with qa_cols[0]:
            if st.button("📊 Take Assessment", use_container_width=True):
                st.session_state.current_page = "assessment"
                st.rerun()
        with qa_cols[1]:
            if st.button("💡 Browse Prompts", use_container_width=True):
                st.session_state.current_page = "prompts"
                st.rerun()
        with qa_cols[2]:
            if st.button("📈 My Dashboard", use_container_width=True):
                st.session_state.current_page = "dashboard"
                st.rerun()
        with qa_cols[3]:
            if st.button("🎓 Continue Learning", use_container_width=True):
                st.session_state.current_page = "learning"
                st.rerun()
    
    # Trending section - Dynamic Data
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## 🔥 Trending Now")
    
    from data.final_tutorials import get_popular_tutorials
    from data.final_assets import get_featured_tools
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Top Tutorials")
        top_tutorials = get_popular_tutorials(3)
        for t in top_tutorials:
            st.markdown(f"""
                <div class="tool-card" style="margin-bottom: 0.75rem; padding: 1rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #1E293B; font-weight: 600;">{t['icon']} {t['title']}</span>
                        <span style="color: #64748B; font-size: 0.8rem;">{t['duration']}</span>
                    </div>
                    <div style="color: #6366F1; font-size: 0.75rem; margin-top: 0.25rem;">{t.get('completions', 0):,} completions</div>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Featured Tools")
        featured_tools = get_featured_tools()[:3]
        for tool in featured_tools:
            stars = "★" * int(tool.get('rating', 5))
            st.markdown(f"""
                <div class="tool-card" style="margin-bottom: 0.75rem; padding: 1rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #1E293B; font-weight: 600;">{tool.get('icon', '🔧')} {tool['name']}</span>
                        <span style="color: #F59E0B; font-size: 0.8rem;">{stars}</span>
                    </div>
                    <div style="color: #6366F1; font-size: 0.75rem; margin-top: 0.25rem;">{tool.get('category', '').replace('_', ' ').title()}</div>
                </div>
            """, unsafe_allow_html=True)


def main():
    """Main application entry Point (V3 Stabilization)"""
    # Initialize current page
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "home"
    
    # Render top navigation
    render_top_nav()
    
    # What's New modal removed for compact UI
    
    # Page routing
    if st.session_state.current_page == "home":
        render_home()
    elif st.session_state.current_page == "learning":
        from pages import learning_hub
        learning_hub.render()
    elif st.session_state.current_page == "tools":
        tool_id = st.session_state.get('viewing_tool')
        if tool_id:
            from pages import tool_viewer
            tool_viewer.render_tool_detail(tool_id)
        else:
            from pages import ai_tools_final as ai_tools
            ai_tools.render()
    elif st.session_state.current_page == "prompts":
        from pages import prompt_library
        prompt_library.render()
    elif st.session_state.current_page == "profile":
        from pages import user_profile
        user_profile.render()
    elif st.session_state.current_page == "dashboard":
        from pages import dashboard
        dashboard.render()
    elif st.session_state.current_page == "assessment":
        from pages import assessment
        assessment.render()
    elif st.session_state.current_page == "tutorial_viewer":
        from pages import tutorial_viewer
        tutorial_id = st.session_state.get('viewing_tutorial')
        if tutorial_id:
            tutorial_viewer.render_tutorial(tutorial_id)
        else:
            st.error("No tutorial selected!")
            st.session_state.current_page = "learning"
            st.rerun()
    elif st.session_state.current_page == "hacks":
        from pages import ai_hacks
        ai_hacks.render()
    elif st.session_state.current_page == "news":
        from pages import ai_news
        ai_news.render()
    elif st.session_state.current_page == "search_results":
        render_search_results()
    else:
        render_home()
    
    # Footer
    render_footer()


def render_search_results():
    """Render global search results"""
    query = st.session_state.get('global_search_query', '')
    
    st.markdown(f"## 🔍 Search Results for: *{query}*")
    
    if not query:
        st.info("Enter a search term in the navigation bar above.")
        return
    
    from data.final_prompts import search_prompts
    from data.final_assets import search_tools
    from data.final_tutorials import search_tutorials
    
    # Search all sources
    found_prompts = search_prompts(query)
    found_tools = search_tools(query)
    found_tutorials = search_tutorials(query)
    
    total = len(found_prompts) + len(found_tools) + len(found_tutorials)
    
    if total == 0:
        st.warning(f"No results found for '{query}'. Try a different search term.")
        if st.button("🏠 Return Home"):
            st.session_state.global_search_query = ""
            st.session_state.current_page = "home"
            st.rerun()
        return
    
    st.success(f"Found **{total}** results across all categories")
    
    # Display results by category
    tab1, tab2, tab3 = st.tabs([f"💡 Prompts ({len(found_prompts)})", f"🔧 Tools ({len(found_tools)})", f"📚 Tutorials ({len(found_tutorials)})"])
    
    with tab1:
        if found_prompts:
            for p in found_prompts[:10]:
                with st.expander(f"{p['title']}", expanded=False):
                    st.markdown(f"**Category:** {p.get('category', 'General').replace('_', ' ').title()}")
                    st.code(p.get('prompt', '')[:300] + "...", language="markdown")
                    if st.button("View Full Prompt", key=f"sr_p_{p['id']}"):
                        st.session_state.current_page = "prompts"
                        st.rerun()
        else:
            st.info("No prompts found.")
    
    with tab2:
        if found_tools:
            for t in found_tools[:10]:
                with st.expander(f"{t.get('icon', '🔧')} {t['name']}", expanded=False):
                    st.markdown(f"**Category:** {t.get('category', 'General').replace('_', ' ').title()}")
                    st.markdown(t.get('description', '')[:200])
                    if st.button("View Tool", key=f"sr_t_{t['id']}"):
                        st.session_state.viewing_tool = t['id']
                        st.session_state.current_page = "tools"
                        st.rerun()
        else:
            st.info("No tools found.")
    
    with tab3:
        if found_tutorials:
            for tut in found_tutorials[:10]:
                with st.expander(f"{tut.get('icon', '📚')} {tut['title']}", expanded=False):
                    st.markdown(f"**Duration:** {tut.get('duration', 'N/A')} | **Difficulty:** {tut.get('difficulty', 'Beginner')}")
                    st.markdown(tut.get('description', '')[:200])
                    if st.button("Start Tutorial", key=f"sr_tut_{tut['id']}"):
                        st.session_state.viewing_tutorial = tut['id']
                        st.session_state.current_page = "tutorial_viewer"
                        st.rerun()
        else:
            st.info("No tutorials found.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Clear Search & Return Home", use_container_width=True):
        st.session_state.global_search_query = ""
        st.session_state.current_page = "home"
        st.rerun()


def render_footer():
    """Render application footer"""
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style="text-align: center; padding: 1.5rem; border-top: 1px solid rgba(0,0,0,0.05); margin-top: 2rem;">
            <span style="background: var(--prism-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800;">AI Nexus</span>
            <span style="color: #64748B; font-size: 0.85rem;"> v{APP_VERSION} | Enterprise Cognitive Architecture</span>
            <br>
            <span style="color: #94A3B8; font-size: 0.75rem;">© 2026 AI Nexus. Built for Professional AI Engineering.</span>
        </div>
    """, unsafe_allow_html=True)


# Force-reload update: 2026-01-09T17:15:00
if __name__ == "__main__":
    main()
