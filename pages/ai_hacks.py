"""
AI Nexus - AI Hacks Page
Curated productivity hacks and tips for AI tools
"""
import streamlit as st
from data.ai_hacks import (
    get_all_hacks, get_hacks_by_category, get_hacks_by_tool,
    get_hacks_by_difficulty, search_hacks
)


def render():
    """Render the AI Hacks page"""
    st.markdown("<h2>🔥 AI Productivity Hacks</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748B; margin-bottom: 1.5rem;'>Curated tips, tricks, and workflows to 10x your AI productivity.</p>", unsafe_allow_html=True)
    
    # Search and filters
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        search_query = st.text_input("🔍 Search Hacks", placeholder="e.g., ChatGPT, prompting...", key="hack_search")
    
    with col2:
        category_filter = st.selectbox(
            "Category",
            ["All", "Productivity", "Coding", "Research", "Design", "Workflow", "Prompting", "Development"],
            key="hack_category"
        )
    
    with col3:
        difficulty_filter = st.selectbox(
            "Difficulty",
            ["All", "Beginner", "Intermediate", "Advanced"],
            key="hack_difficulty"
        )
    
    # Get filtered hacks
    if search_query:
        hacks = search_hacks(search_query)
    elif category_filter != "All":
        hacks = get_hacks_by_category(category_filter)
    elif difficulty_filter != "All":
        hacks = get_hacks_by_difficulty(difficulty_filter)
    else:
        hacks = get_all_hacks()
    
    st.markdown(f"**Found {len(hacks)} hacks**")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Render hacks in grid
    if not hacks:
        st.info("No hacks found matching your criteria.")
        return
    
    # Grid layout - 3 columns
    for i in range(0, len(hacks), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(hacks):
                with cols[j]:
                    render_hack_card(hacks[i + j], f"grid_{i}_{j}")


def render_hack_card(hack, context="default"):
    """Render a single hack card in grid format"""
    difficulty_colors = {
        "Beginner": "#10B981",
        "Intermediate": "#F59E0B",
        "Advanced": "#EF4444"
    }
    
    diff_color = difficulty_colors.get(hack['difficulty'], '#64748B')
    
    # Compact card
    st.html(f'''
        <div class="tool-card" style="border-top: 4px solid {diff_color} !important; background: rgba(255, 255, 255, 0.6) !important; min-height: 180px; display: flex; flex-direction: column;">
            <div style="font-family: Outfit; font-weight: 800; font-size: 1.05rem; margin-bottom: 8px; display: flex; align-items: flex-start;">
                <span style="margin-right: 8px; font-size: 1.2rem;">{hack['icon']}</span>
                <span style="background: var(--prism-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1.3;">{hack['title']}</span>
            </div>
            <div style="font-size: 0.85rem; color: #475569; margin-bottom: 10px; flex-grow: 1; overflow: hidden; line-height: 1.5;">
                {hack['description'][:100]}...
            </div>
            <div style="display: flex; gap: 0.4rem; flex-wrap: wrap; margin-bottom: 10px;">
                <span style="background: {diff_color}; color: white; padding: 0.15rem 0.5rem; border-radius: 10px; font-size: 0.7rem; font-weight: 700;">{hack['difficulty']}</span>
                <span style="background: #6366F1; color: white; padding: 0.15rem 0.5rem; border-radius: 10px; font-size: 0.7rem; font-weight: 700;">{hack['tool']}</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 8px;">
                <span style="color: #10B981; font-size: 0.75rem; font-weight: 700;">⏱️ Saves: {hack['time_saved']}</span>
                <span style="color: #64748B; font-size: 0.75rem; font-weight: 600;">{hack['category']}</span>
            </div>
        </div>
    ''')
    
    # Expandable details
    with st.expander("📖 View Full Hack", expanded=False):
        st.markdown(hack['hack'])
        
        # Tags
        st.markdown("**Tags:**")
        tag_html = " ".join([
            f'<span style="background: #F1F5F9; color: #475569; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.8rem; margin-right: 0.5rem;">#{tag}</span>'
            for tag in hack['tags']
        ])
        st.markdown(tag_html, unsafe_allow_html=True)
        
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📋 Copy", key=f"copy_{hack['id']}_{context}", use_container_width=True):
                st.toast("✅ Copied!")
        with col2:
            if st.button("⭐ Save", key=f"fav_{hack['id']}_{context}", use_container_width=True):
                st.toast("✅ Saved!")

