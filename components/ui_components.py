"""
AI Nexus - UI Components Library
Reusable Streamlit components with premium styling
"""
import streamlit as st
from typing import Optional, List, Dict, Any


def render_hero_section(title: str, subtitle: str, show_cta: bool = True):
    """Render a hero section with animated gradient background"""
    st.markdown(f"""
        <div class="hero-section animate-fade-in">
            <div class="hero-title">{title}</div>
            <p class="hero-subtitle">{subtitle}</p>
        </div>
    """, unsafe_allow_html=True)


def render_metric_card(icon: str, value: str, label: str, color: str = "#7C3AED"):
    """Render a metric card with icon, value, and label"""
    st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
    """, unsafe_allow_html=True)


def render_feature_card(icon: str, title: str, description: str, link: Optional[str] = None):
    """Render a feature card with hover effects"""
    st.markdown(f"""
        <div class="glass-card" style="height: 100%;">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">{icon}</div>
            <h3 style="color: #FFFFFF; margin-bottom: 0.5rem; font-size: 1.25rem;">{title}</h3>
            <p style="color: #A1A1AA; font-size: 0.9rem; line-height: 1.6;">{description}</p>
        </div>
    """, unsafe_allow_html=True)


def render_tool_card(name: str, category: str, description: str, rating: float, 
                     pricing: str, icon: str = "🔧", is_featured: bool = False):
    """Render an AI tool card"""
    stars = "★" * int(rating) + "☆" * (5 - int(rating))
    featured_badge = '<span class="badge badge-primary" style="margin-left: 0.5rem;">Featured</span>' if is_featured else ''
    
    st.markdown(f"""
        <div class="tool-card">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <span style="font-size: 2rem; margin-right: 1rem;">{icon}</span>
                <div>
                    <div style="color: #FFFFFF; font-weight: 600; font-size: 1.1rem;">{name}{featured_badge}</div>
                    <div style="color: #A78BFA; font-size: 0.75rem; text-transform: uppercase;">{category}</div>
                </div>
            </div>
            <p style="color: #A1A1AA; font-size: 0.9rem; margin-bottom: 1rem;">{description}</p>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #F59E0B;">{stars}</span>
                <span class="badge badge-success">{pricing}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_prompt_card(title: str, category: str, prompt_text: str, 
                       uses: int, rating: float, difficulty: str = "Intermediate"):
    """Render a prompt card"""
    difficulty_colors = {"Beginner": "#10B981", "Intermediate": "#F59E0B", "Advanced": "#EF4444"}
    diff_color = difficulty_colors.get(difficulty, "#A1A1AA")
    
    st.markdown(f"""
        <div class="tool-card">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.75rem;">
                <span class="badge badge-primary">{category}</span>
                <span style="color: {diff_color}; font-size: 0.75rem; font-weight: 500;">{difficulty}</span>
            </div>
            <h4 style="color: #FFFFFF; margin-bottom: 0.5rem;">{title}</h4>
            <div style="background: #1A1A2E; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; font-family: monospace; font-size: 0.85rem; color: #A1A1AA; max-height: 80px; overflow: hidden;">
                {prompt_text[:150]}...
            </div>
            <div style="display: flex; justify-content: space-between; color: #A1A1AA; font-size: 0.8rem;">
                <span>👥 {uses:,} uses</span>
                <span style="color: #F59E0B;">{'★' * int(rating)} {rating}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_learning_path_card(title: str, duration: str, modules: int, 
                               progress: int = 0, icon: str = "📚"):
    """Render a learning path card"""
    st.markdown(f"""
        <div class="glass-card">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <span style="font-size: 2rem; margin-right: 1rem;">{icon}</span>
                <div>
                    <h4 style="color: #FFFFFF; margin: 0;">{title}</h4>
                    <span style="color: #A1A1AA; font-size: 0.85rem;">{duration} • {modules} modules</span>
                </div>
            </div>
            <div style="background: #1A1A2E; border-radius: 10px; height: 8px; overflow: hidden;">
                <div style="background: linear-gradient(135deg, #7C3AED 0%, #06B6D4 100%); height: 100%; width: {progress}%; transition: width 0.3s ease;"></div>
            </div>
            <div style="text-align: right; color: #A1A1AA; font-size: 0.8rem; margin-top: 0.5rem;">{progress}% complete</div>
        </div>
    """, unsafe_allow_html=True)


def render_role_card(role: Dict[str, str], is_selected: bool = False):
    """Render a role selection card"""
    border_color = "#7C3AED" if is_selected else "rgba(255, 255, 255, 0.1)"
    bg_color = "rgba(124, 58, 237, 0.1)" if is_selected else "rgba(255, 255, 255, 0.05)"
    
    st.markdown(f"""
        <div style="background: {bg_color}; border: 2px solid {border_color}; border-radius: 16px; padding: 1.25rem; text-align: center; cursor: pointer; transition: all 0.3s ease;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">{role['icon']}</div>
            <div style="color: #FFFFFF; font-weight: 600;">{role['name']}</div>
            <div style="color: #A1A1AA; font-size: 0.75rem;">{role.get('category', '')}</div>
        </div>
    """, unsafe_allow_html=True)


def render_stats_row(stats: List[Dict[str, Any]]):
    """Render a row of statistics"""
    cols = st.columns(len(stats))
    for col, stat in zip(cols, stats):
        with col:
            render_metric_card(stat['icon'], stat['value'], stat['label'])


def render_progress_ring(percentage: int, label: str, size: int = 120):
    """Render a circular progress indicator"""
    st.markdown(f"""
        <div style="text-align: center;">
            <div style="position: relative; width: {size}px; height: {size}px; margin: 0 auto;">
                <svg viewBox="0 0 36 36" style="transform: rotate(-90deg);">
                    <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="#1A1A2E" stroke-width="3"/>
                    <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="url(#gradient)" stroke-width="3" stroke-dasharray="{percentage}, 100"/>
                    <defs>
                        <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" style="stop-color:#7C3AED"/>
                            <stop offset="100%" style="stop-color:#06B6D4"/>
                        </linearGradient>
                    </defs>
                </svg>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 1.5rem; font-weight: 700; color: #FFFFFF;">{percentage}%</div>
            </div>
            <div style="color: #A1A1AA; margin-top: 0.5rem;">{label}</div>
        </div>
    """, unsafe_allow_html=True)


def render_search_box(placeholder: str = "Search..."):
    """Render a styled search box"""
    return st.text_input("", placeholder=placeholder, label_visibility="collapsed")


def render_filter_pills(options: List[str], selected: str) -> str:
    """Render filter pill buttons"""
    cols = st.columns(len(options))
    new_selected = selected
    for i, (col, option) in enumerate(zip(cols, options)):
        with col:
            if st.button(option, key=f"pill_{i}", use_container_width=True):
                new_selected = option
    return new_selected


def render_divider():
    """Render a styled divider"""
    st.markdown('<div style="height: 1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent); margin: 2rem 0;"></div>', unsafe_allow_html=True)


def render_empty_state(icon: str, title: str, description: str):
    """Render an empty state message"""
    st.markdown(f"""
        <div style="text-align: center; padding: 3rem; color: #A1A1AA;">
            <div style="font-size: 4rem; margin-bottom: 1rem; opacity: 0.5;">{icon}</div>
            <h3 style="color: #FFFFFF; margin-bottom: 0.5rem;">{title}</h3>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)
