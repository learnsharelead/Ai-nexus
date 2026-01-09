"""
AI Nexus - Tool Viewer
Detailed profile and integration guide for AI tools
"""
import streamlit as st
from data.final_assets import get_tool_by_id, get_tools_by_category
from utils.helpers import add_to_favorites, is_favorite, track_activity

def render_tool_detail(tool_id: str):
    """Render the full detail page for a specific AI tool"""
    tool = get_tool_by_id(tool_id)
    
    if not tool:
        st.error("Tool not found in the NEXUS database.")
        if st.button("← Return to Directory"):
            st.session_state.pop('viewing_tool', None)
            st.rerun()
        return

    # Track view activity
    track_activity('tool_viewed', tool_id, {'name': tool['name']})

    # Header Section
    col1, col2 = st.columns([5, 1])
    with col1:
        st.markdown(f"## {tool.get('icon', '🔧')} {tool['name']}")
        category_display = tool.get('category', 'General AI').replace('_', ' ').title()
        st.markdown(f"**{category_display}** | {'★' * int(tool.get('rating', 5))} ({tool.get('rating', 5)}/5)")
    with col2:
        if st.button("← Back", use_container_width=True):
            st.session_state.pop('viewing_tool', None)
            st.rerun()

    st.markdown("---")

    # Main Overview
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.markdown("### 📋 Executive Summary")
        st.markdown(tool.get('description', 'No detailed description available.'))
        
        st.markdown("### ✨ Key Features")
        features = tool.get('features', ["Advanced AI Processing", "API Integration", "Cloud Deployment"])
        for feat in features:
            st.markdown(f"- ✅ {feat}")
            
        st.markdown("### 🔌 Native Integrations")
        integrations = tool.get('integrations', ["Standard APIs"])
        
        # Display as chips
        chip_html = ""
        for integ in integrations:
            chip_html += f'<span style="background: linear-gradient(135deg, #6366F1, #EC4899); color: white; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; margin-right: 8px; display: inline-block; margin-bottom: 8px;">{integ}</span>'
        st.markdown(chip_html, unsafe_allow_html=True)

    with c2:
        # Pricing Card
        pricing_colors = {
            "Free": "#10B981",
            "Freemium": "#F59E0B", 
            "Paid": "#6366F1",
            "Enterprise": "#EF4444"
        }
        pricing = tool.get('pricing', 'Contact for Price')
        pricing_color = pricing_colors.get(pricing, '#64748B')
        
        st.markdown(f"""
            <div class="glass-card" style="padding: 1.5rem; border-left: 4px solid {pricing_color};">
                <h4 style="margin-top:0; color: #1E293B;">💰 Acquisition Details</h4>
                <div style="margin: 1rem 0;">
                    <span style="background: {pricing_color}; color: white; padding: 0.4rem 1rem; border-radius: 20px; font-weight: 700;">{pricing}</span>
                </div>
                <div style="color: #64748B; font-size: 0.9rem; margin-top: 1rem;">
                    <strong>Rating:</strong> {'★' * int(tool.get('rating', 5))} ({tool.get('rating', 5)}/5)
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # External Link
        if tool.get('url'):
            st.markdown("<br>", unsafe_allow_html=True)
            st.link_button("🌐 Visit Official Website", tool['url'], use_container_width=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Interaction Actions
        is_saved = is_favorite('tools', tool_id)
        
        if is_saved:
            st.success("✅ In Your Library")
        else:
            if st.button("⭐ Add to Library", use_container_width=True, type="primary"):
                if add_to_favorites('tools', tool_id, tool):
                    st.success("✅ Added to your library!")
                    track_activity('tool_saved', tool_id, {'name': tool['name']})
                    st.rerun()
        
        if st.button("📧 Request Demo", use_container_width=True):
            st.info(f"Demo request for {tool['name']} - Feature coming soon!")

    # Use Cases Section
    st.markdown("---")
    st.markdown("### 🎯 Recommended Use Cases")
    
    best_for = tool.get('best_for', ["Professionals", "Enterprises", "Developers"])
    cols = st.columns(len(best_for))
    for i, item in enumerate(best_for):
        with cols[i]:
            st.markdown(f"""
                <div style="background: rgba(99, 102, 241, 0.1); padding: 1rem; border-radius: 12px; text-align: center;">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🎯</div>
                    <div style="font-weight: 700; color: #1E293B;">{item}</div>
                </div>
            """, unsafe_allow_html=True)

    # Quick Start Documentation
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("📚 Quick Start Integration Guide", expanded=False):
        st.markdown(f"""
        ### Getting Started with {tool['name']}
        
        **Step 1: Access**
        - Visit the official website and create an account
        - Navigate to the developer/API section
        
        **Step 2: Authentication**
        ```python
        # Example API setup
        import requests
        
        API_KEY = "your_api_key_here"
        headers = {{"Authorization": f"Bearer {{API_KEY}}"}}
        ```
        
        **Step 3: Basic Integration**
        ```python
        # Make your first API call
        response = requests.get(
            "https://api.{tool['name'].lower().replace(' ', '')}.com/v1/endpoint",
            headers=headers
        )
        print(response.json())
        ```
        
        **Pro Tips:**
        - Start with the free tier to evaluate
        - Review rate limits before production deployment
        - Check the changelog for new features
        """)

    # Related Tools Section
    st.markdown("---")
    st.markdown("### 🔗 Related Tools")
    
    related = get_tools_by_category(tool.get('category', ''))[:4]
    related = [t for t in related if t['id'] != tool_id][:3]  # Exclude current, limit to 3
    
    if related:
        cols = st.columns(3)
        for i, rel_tool in enumerate(related):
            with cols[i]:
                st.markdown(f"""
                    <div class="tool-card" style="padding: 1rem; min-height: 100px;">
                        <div style="font-weight: 700; color: #1E293B;">{rel_tool.get('icon', '🔧')} {rel_tool['name']}</div>
                        <div style="color: #64748B; font-size: 0.85rem;">{rel_tool.get('pricing', 'N/A')}</div>
                    </div>
                """, unsafe_allow_html=True)
                if st.button("View", key=f"rel_{rel_tool['id']}", use_container_width=True):
                    st.session_state.viewing_tool = rel_tool['id']
                    st.rerun()
    else:
        st.info("No related tools found in this category.")
