"""
AI Nexus - User Profile Page
Hyper-Personalized Role Profiling
"""
import streamlit as st
from config.settings import (
    ROLE_ARCHETYPES, INDUSTRY_VERTICALS, TECH_STACKS,
    LEARNING_STYLES, SKILL_LEVELS
)


def render():
    """Render the User Profile page"""
    st.markdown("# 👤 Your AI Profile")
    st.markdown("*Personalize your AI learning journey*")
    
    # Check if profile exists
    if st.session_state.get('user_profile'):
        render_profile_view()
    else:
        render_onboarding()


def render_onboarding():
    """Render the onboarding wizard"""
    st.markdown("""
        <div class="hero-section" style="padding: 2rem;">
            <div class="hero-title" style="font-size: 2rem;">Let's Personalize Your Experience</div>
            <p class="hero-subtitle">Complete these steps to unlock AI-powered recommendations</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Progress indicator
    step = st.session_state.get('onboarding_step', 1)
    
    col1, col2, col3, col4 = st.columns(4)
    steps = [
        ("1. Role", step >= 1),
        ("2. Industry", step >= 2),
        ("3. Tech Stack", step >= 3),
        ("4. Learning Style", step >= 4)
    ]
    
    for i, (col, (label, completed)) in enumerate(zip([col1, col2, col3, col4], steps)):
        with col:
            color = "#7C3AED" if completed else "#A1A1AA"
            bg = "#7C3AED22" if step == i + 1 else "transparent"
            st.markdown(f"""
                <div style="text-align: center; padding: 0.75rem; border-radius: 12px; 
                           background: {bg}; border: 2px solid {color};">
                    <span style="color: {color}; font-weight: 600;">{label}</span>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Render current step
    if step == 1:
        render_role_selection()
    elif step == 2:
        render_industry_selection()
    elif step == 3:
        render_tech_stack_selection()
    elif step == 4:
        render_learning_style_selection()
    elif step == 5:
        complete_onboarding()


def render_role_selection():
    """Render role selection step"""
    st.markdown("## 🎯 What's Your Role?")
    st.markdown("Select the role that best describes your current position")
    
    # Group roles by category
    categories = {}
    for role in ROLE_ARCHETYPES:
        cat = role.get('category', 'Other')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(role)
    
    selected_role = st.session_state.get('temp_role', None)
    
    for category, roles in categories.items():
        st.markdown(f"### {category}")
        cols = st.columns(4)
        for i, role in enumerate(roles):
            with cols[i % 4]:
                is_selected = selected_role == role['id']
                border_color = "#7C3AED" if is_selected else "rgba(255,255,255,0.1)"
                bg_color = "rgba(124, 58, 237, 0.15)" if is_selected else "rgba(255,255,255,0.05)"
                
                st.markdown(f"""
                    <div style="background: {bg_color}; border: 2px solid {border_color}; 
                               border-radius: 16px; padding: 1rem; text-align: center; 
                               margin-bottom: 0.5rem; cursor: pointer;">
                        <div style="font-size: 2rem;">{role['icon']}</div>
                        <div style="font-weight: 600; font-size: 0.85rem;">{role['name']}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                if st.button("Select", key=f"role_{role['id']}", use_container_width=True):
                    st.session_state.temp_role = role['id']
                    st.session_state.selected_role = role['id']
                    st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col2:
        if st.session_state.get('temp_role'):
            if st.button("Next: Industry →", type="primary", use_container_width=True):
                st.session_state.onboarding_step = 2
                st.rerun()


def render_industry_selection():
    """Render industry selection step"""
    st.markdown("## 🏢 What Industry Are You In?")
    st.markdown("This helps us tailor content to your domain")
    
    selected_industry = st.session_state.get('temp_industry', None)
    
    cols = st.columns(4)
    for i, industry in enumerate(INDUSTRY_VERTICALS):
        with cols[i % 4]:
            is_selected = selected_industry == industry['id']
            border_color = "var(--primary)" if is_selected else "var(--border)"
            bg_color = "rgba(99, 102, 241, 0.05)" if is_selected else "var(--card-bg)"
            
            st.markdown(f"""
                <div class="glass-card" style="border: 1px solid {border_color} !important; 
                           background: {bg_color} !important; text-align: center; margin-bottom: 2px; padding: 4px !important;">
                    <div style="font-size: 1.25rem; margin-bottom: 2px;">{industry['icon']}</div>
                    <div style="font-weight: 700; color: #1D1D1F !important; font-size: 10px;">{industry['name']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("Pick", key=f"ind_{industry['id']}", use_container_width=True):
                st.session_state.temp_industry = industry['id']
                st.rerun()
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("Back", use_container_width=True):
            st.session_state.onboarding_step = 1
            st.rerun()
    with col3:
        if st.session_state.get('temp_industry'):
            if st.button("Next: Tech Stack →", type="primary", use_container_width=True):
                st.session_state.onboarding_step = 3
                st.rerun()


def render_tech_stack_selection():
    """Render tech stack selection step"""
    st.markdown("## 💻 What's Your Tech Stack?")
    st.markdown("Select the technologies you work with regularly")
    
    selected_tech = st.session_state.get('temp_tech_stack', {})
    
    for category, items in TECH_STACKS.items():
        st.markdown(f"### {category.replace('_', ' ').title()}")
        selected = st.multiselect(
            f"Select {category}",
            items,
            default=selected_tech.get(category, []),
            key=f"tech_{category}",
            label_visibility="collapsed"
        )
        selected_tech[category] = selected
    
    st.session_state.temp_tech_stack = selected_tech
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Back", use_container_width=True):
            st.session_state.onboarding_step = 2
            st.rerun()
    with col3:
        if st.button("Next: Learning Style →", type="primary", use_container_width=True):
            st.session_state.onboarding_step = 4
            st.rerun()


def render_learning_style_selection():
    """Render learning style selection step"""
    st.markdown("## 📚 How Do You Learn Best?")
    st.markdown("Select your preferred learning methods")
    
    selected_styles = st.session_state.get('temp_learning_styles', [])
    
    cols = st.columns(len(LEARNING_STYLES))
    for i, style in enumerate(LEARNING_STYLES):
        with cols[i]:
            is_selected = style['id'] in selected_styles
            border_color = "#7C3AED" if is_selected else "rgba(255,255,255,0.1)"
            bg_color = "rgba(124, 58, 237, 0.15)" if is_selected else "rgba(255,255,255,0.05)"
            
            st.markdown(f"""
                <div style="background: {bg_color}; border: 2px solid {border_color}; 
                           border-radius: 16px; padding: 1.5rem; text-align: center;">
                    <div style="font-size: 2.5rem;">{style['icon']}</div>
                    <div style="font-weight: 600; margin: 0.5rem 0;">{style['name']}</div>
                    <div style="color: #A1A1AA; font-size: 0.8rem;">{style['description']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("Toggle", key=f"style_{style['id']}", use_container_width=True):
                if style['id'] in selected_styles:
                    selected_styles.remove(style['id'])
                else:
                    selected_styles.append(style['id'])
                st.session_state.temp_learning_styles = selected_styles
                st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Back", use_container_width=True):
            st.session_state.onboarding_step = 3
            st.rerun()
    with col3:
        if st.button("Complete Profile ✓", type="primary", use_container_width=True):
            st.session_state.onboarding_step = 5
            st.rerun()


def complete_onboarding():
    """Complete the onboarding process"""
    # Save profile
    st.session_state.user_profile = {
        'role': st.session_state.get('temp_role'),
        'industry': st.session_state.get('temp_industry'),
        'tech_stack': st.session_state.get('temp_tech_stack', {}),
        'learning_styles': st.session_state.get('temp_learning_styles', []),
        'skill_level': 'intermediate',
        'ai_score': 65,
    }
    st.session_state.onboarding_complete = True
    
    st.markdown("""
        <div class="hero-section" style="padding: 3rem;">
            <div class="hero-title" style="font-size: 2rem;">Profile Setup Complete</div>
            <p class="hero-subtitle">Your personalized learning experience is ready</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Continue to Learning Hub", type="primary", use_container_width=True):
        st.session_state.current_page = "learning"
        st.rerun()


def render_profile_view():
    """Render the profile view for existing users"""
    profile = st.session_state.user_profile
    
    # Profile header
    role = next((r for r in ROLE_ARCHETYPES if r['id'] == profile.get('role')), {})
    industry = next((i for i in INDUSTRY_VERTICALS if i['id'] == profile.get('industry')), {})
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"""
            <div class="glass-card" style="text-align: center; padding: 10px;">
                <div style="font-size: 2rem; margin-bottom: 4px; background: #F8FAFC; width: 50px; height: 50px; 
                            line-height: 50px; border-radius: 50%; margin: 0 auto; border: 1px solid var(--border);">
                    {role.get('icon', '👤')}
                </div>
                <div style="font-weight:700; font-size: 13px;">{role.get('name', 'User')}</div>
                <div style="color: var(--primary) !important; font-weight: 600; font-size: 9px;">{industry.get('name', '')} {industry.get('icon', '')}</div>
                <div style="margin-top: 10px; padding: 6px; background: #F1F5F9; border-radius: 6px;">
                    <div style="font-size: 14px; font-weight:800; color:var(--primary);">{profile.get('ai_score', 65)}</div>
                    <div style="font-size: 8px; color:gray;">AI SCORE</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Your Tech Stack")
        tech_stack = profile.get('tech_stack', {})
        for category, items in tech_stack.items():
            if items:
                st.markdown(f"**{category.replace('_', ' ').title()}:** {', '.join(items)}")
        
        st.markdown("### Learning Preferences")
        styles = profile.get('learning_styles', [])
        style_names = [s['name'] for s in LEARNING_STYLES if s['id'] in styles]
        st.markdown(", ".join(style_names) if style_names else "Not set")
        
        st.markdown("### Skill Level")
        level = profile.get('skill_level', 'intermediate')
        level_info = next((l for l in SKILL_LEVELS if l['id'] == level), SKILL_LEVELS[1])
        st.progress(level_info['range'][1] / 100)
        st.markdown(f"**{level_info['name']}** - {level_info['description']}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Actions
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📝 Edit Profile", use_container_width=True):
            st.session_state.onboarding_step = 1
            st.session_state.user_profile = None
            st.rerun()
    with col2:
        if st.button("📊 Take Assessment", use_container_width=True):
            st.session_state.current_page = "assessment"
            st.rerun()
    with col3:
        if st.button("🏆 View Achievements", use_container_width=True):
            st.session_state.show_achievements = not st.session_state.get('show_achievements', False)
            st.rerun()
    
    # Achievements Section (Expandable)
    if st.session_state.get('show_achievements', False):
        st.markdown("---")
        st.markdown("## 🏆 Your Achievements")
        
        from utils.helpers import get_completed_tutorials, get_saved_prompts, get_all_favorites
        
        completed = len(get_completed_tutorials())
        saved = len(get_saved_prompts())
        favorites = get_all_favorites()
        tools_saved = len(favorites.get('tools', {}))
        ai_score = profile.get('ai_score', 0)
        
        # Define badges
        badges = [
            {"name": "First Steps", "icon": "🎯", "desc": "Complete your profile", "earned": True, "color": "#10B981"},
            {"name": "Scholar", "icon": "📚", "desc": "Complete 5 tutorials", "earned": completed >= 5, "color": "#6366F1"},
            {"name": "Collector", "icon": "💎", "desc": "Save 10 prompts", "earned": saved >= 10, "color": "#EC4899"},
            {"name": "Tool Master", "icon": "🔧", "desc": "Favorite 5 tools", "earned": tools_saved >= 5, "color": "#F59E0B"},
            {"name": "Rising Star", "icon": "⭐", "desc": "Reach AI Score 50+", "earned": ai_score >= 50, "color": "#3B82F6"},
            {"name": "Expert", "icon": "🧠", "desc": "Reach AI Score 80+", "earned": ai_score >= 80, "color": "#8B5CF6"},
            {"name": "Completionist", "icon": "🏅", "desc": "Complete 20 tutorials", "earned": completed >= 20, "color": "#EF4444"},
            {"name": "Power User", "icon": "⚡", "desc": "Save 25 prompts & 10 tools", "earned": saved >= 25 and tools_saved >= 10, "color": "#06B6D4"},
        ]
        
        earned_count = sum(1 for b in badges if b['earned'])
        st.markdown(f"**Earned: {earned_count}/{len(badges)} badges**")
        
        # Display badges in grid
        badge_cols = st.columns(4)
        for i, badge in enumerate(badges):
            with badge_cols[i % 4]:
                opacity = "1" if badge['earned'] else "0.4"
                border = f"2px solid {badge['color']}" if badge['earned'] else "2px dashed #CBD5E1"
                st.markdown(f"""
                    <div style="text-align: center; padding: 1rem; border-radius: 12px; border: {border}; opacity: {opacity}; margin-bottom: 1rem; background: rgba(255,255,255,0.8);">
                        <div style="font-size: 2rem;">{badge['icon']}</div>
                        <div style="font-weight: 700; color: #1E293B; font-size: 0.9rem;">{badge['name']}</div>
                        <div style="color: #64748B; font-size: 0.75rem;">{badge['desc']}</div>
                    </div>
                """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔒 Hide Achievements", use_container_width=True):
            st.session_state.show_achievements = False
            st.rerun()
