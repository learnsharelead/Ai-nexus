"""
AI Nexus - AI Tool Universe (FINAL HARDENED)
"""
import streamlit as st
from data.final_assets import (
    get_all_tools, get_tools_by_category, get_featured_tools,
    search_tools, get_tool_by_id
)
from config.settings import AI_TOOL_CATEGORIES
from utils.helpers import add_to_favorites, track_activity

def render_tool_card(tool_data, tool_context="final"):
    """Final hardened card renderer"""
    try:
        t_id = str(tool_data.get("id", "none"))
        t_name = str(tool_data.get("name", "AI Module"))
        t_icon = str(tool_data.get("icon", "🔧"))
        t_desc = str(tool_data.get("description", ""))[:120]
        t_rate = int(float(tool_data.get("rating", 5)))
        t_price = str(tool_data.get("pricing", "Paid"))
        
        p_map = {"Free": "#10B981", "Freemium": "#F59E0B", "Paid": "#6366F1", "Enterprise": "#EF4444"}
        c_hex = p_map.get(t_price, "#64748B")
        stars = "★" * t_rate
        
        st.markdown(f'''
            <div class="tool-card" style="border-top: 4px solid #6366F1 !important; background: rgba(255, 255, 255, 0.7) !important; min-height: 165px; display: flex; flex-direction: column; padding: 1.25rem !important; border-radius: 16px !important;">
                <div style="font-family: Outfit; font-weight: 800; font-size: 1.15rem; color: #1E293B; margin-bottom: 8px; display: flex; align-items: flex-start;">
                    <span style="margin-right: 12px; font-size: 1.4rem;">{t_icon}</span>
                    <span style="background: var(--prism-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{t_name}</span>
                </div>
                <div style="font-size: 0.9rem; color: #475569; margin-bottom: 12px; flex-grow: 1; overflow: hidden; line-height: 1.5;">
                    {t_desc}...
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 12px;">
                    <span style="background: {c_hex}; color: white; padding: 0.25rem 0.75rem; border-radius: 20px; font-size: 0.7rem; font-weight: 800; text-transform: uppercase;">{t_price}</span>
                    <span style="color: #FBBF24; font-size: 1.1rem;">{stars}</span>
                </div>
            </div>
        ''', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Launch", key=f"lch_final_{t_id}", use_container_width=True, type="primary"):
                st.session_state.viewing_tool = t_id
                st.rerun()
        with c2:
            if st.button("Favorite", key=f"fav_final_{t_id}", use_container_width=True):
                if add_to_favorites('tools', t_id, tool_data):
                    st.toast(f"✅ {t_name} saved!")
    except Exception as e:
        st.error(f"Card Error: {str(e)}")

def render():
    st.markdown("<h2>AI Ecosystem & Resource Directory <span style='font-size:0.8rem; vertical-align:middle; color:#6366F1;'>V5 PURGED</span></h2>", unsafe_allow_html=True)
    
    # Simple search
    q = st.text_input("🔍 Search Technical Assets...", key="final_search")
    
    # Sector filter
    st.markdown("### Intelligence Sectors")
    sel = st.session_state.get('final_sector', 'all')
    cats = [{"id": "all", "name": "Global", "icon": "🌐"}] + AI_TOOL_CATEGORIES
    
    ccols = st.columns(6)
    for i, cat in enumerate(cats[:12]): # Show first 12
        with ccols[i % 6]:
            if st.button(f"{cat['icon']} {cat['name'][:8]}", key=f"btn_cat_{cat['id']}", use_container_width=True, type="primary" if sel == cat['id'] else "secondary"):
                st.session_state.final_sector = cat['id']
                st.rerun()

    # Fetch
    if q: tools = search_tools(q)
    elif sel != 'all': tools = get_tools_by_category(sel)
    else: tools = get_all_tools()
    
    st.markdown(f"**Found {len(tools)} verified assets**")
    
    if not tools:
        st.info("No verified assets found matching your criteria.")
        if st.button("Clear Filters & Search"):
            st.session_state.final_search = ""
            st.session_state.final_sector = "all"
            st.rerun()
        return
    
    # Grid
    for i in range(0, len(tools), 4):
        cols = st.columns(4)
        for j in range(4):
            if i + j < len(tools):
                with cols[j]:
                    render_tool_card(tools[i+j])
