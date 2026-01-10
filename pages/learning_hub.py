"""
AI Nexus - Learning Hub Page
Hyper-Personalized Learning Engine
"""
import streamlit as st
from data.final_tutorials import (
    get_all_tutorials, get_tutorials_by_category, 
    get_tutorials_by_role, get_popular_tutorials, search_tutorials
)
from config.settings import ROLE_ARCHETYPES, LEARNING_PATHS, SKILL_LEVELS


def render():
    """Render the Learning Hub page"""
    st.markdown("<h2>Curriculum & Path Mastery</h2>", unsafe_allow_html=True)
    all_tutorials_count = len(get_all_tutorials())
    st.markdown(f"<p style='color: #64748B; margin-bottom: 1rem;'>Explore {all_tutorials_count} specialized tutorials designed for professional AI integration.</p>", unsafe_allow_html=True)
    
    # Search and filters with clear keys
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        search_query = st.text_input("🔍 Search Curriculum", placeholder="e.g., Prompt Engineering...", key="lh_search_input")
    with col2:
        category_filter = st.selectbox("Specialization", ["All", "Generative AI", "Coding", "Image Gen", "Business", "Audio/Video"], key="lh_category_select")
    with col3:
        difficulty_filter = st.selectbox("Proficiency", ["All", "Beginner", "Intermediate", "Advanced"], key="lh_diff_select")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## 🛰️ Strategic Learning Paths")
    
    path_cols = st.columns(4)
    for i, path in enumerate(LEARNING_PATHS):
        with path_cols[i]:
            st.markdown(f"""
                <div class="glass-card" style="text-align: center; border-bottom: 4px solid var(--primary) !important;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">{path['icon']}</div>
                    <div style="font-family: Outfit; font-weight: 700; color: #1E293B;">{path['name']}</div>
                    <div style="color: #64748B; font-size: 0.8rem; margin-top: 4px; font-weight: 600;">{path['duration']}</div>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tabs for content organization
    tab1, tab2, tab3, tab4 = st.tabs(["🔥 Trending", "📋 For Your Role", "⭐ Recommended", "📚 All Tutorials"])
    
    # Get tutorials based on filters with loading state
    with st.spinner("Loading tutorials..."):
        try:
            if search_query:
                tutorials = search_tutorials(search_query)
            elif category_filter != "All":
                tutorials = get_tutorials_by_category(category_filter)
            else:
                tutorials = get_all_tutorials()
            
            if difficulty_filter != "All":
                tutorials = [t for t in tutorials if t.get("difficulty") == difficulty_filter]
        except Exception as e:
            st.error(f"❌ Error loading tutorials: {str(e)}")
            tutorials = []
    
    with tab1:
        with st.spinner("Loading trending tutorials..."):
            try:
                trending = get_popular_tutorials(12)
                render_tutorial_grid(trending, "trending")
            except Exception as e:
                st.error(f"❌ Error loading trending tutorials: {str(e)}")
    
    with tab2:
        if st.session_state.get('selected_role'):
            with st.spinner("Loading role-specific tutorials..."):
                try:
                    role_tutorials = get_tutorials_by_role(st.session_state.selected_role)
                    if role_tutorials:
                        render_tutorial_grid(role_tutorials[:12], "role")
                    else:
                        st.info("No tutorials found for your role yet. Check back soon!")
                except Exception as e:
                    st.error(f"❌ Error loading role tutorials: {str(e)}")
        else:
            st.info("Complete your profile to see role-specific tutorials!")
            if st.button("Complete Profile", key="complete_profile_btn"):
                st.session_state.current_page = "profile"
                st.rerun()
    
    with tab3:
        st.markdown("### 🤖 Recommendations")
        with st.spinner("Loading..."):
            try:
                recommended = get_popular_tutorials(8)
                render_tutorial_grid(recommended, "recommended")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    with tab4:
        render_tutorial_grid(tutorials[:40], "all")
    
    # Skill Assessment Section
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("## 🎯 Skill Assessment")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            Take our AI proficiency assessment to:
            - **Discover your current AI skill level**
            - Get personalized learning paths
            - Track your progress over time
            - Earn skill badges and certifications
        """)
        
        with st.expander("📝 Quick Assessment Preview"):
            st.markdown("**Sample Question:**")
            st.markdown("*Which of these is the best practice when using AI for code generation?*")
            options = [
                "Copy-paste AI output directly without review",
                "Review, test, and adapt AI suggestions to your codebase",
                "Only use AI for simple tasks",
                "Avoid AI tools altogether"
            ]
            st.radio("Select your answer:", options, key="sample_q1", index=None)
    
    with col2:
        st.markdown("""
            <div class="glass-card" style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">📊</div>
                <h4 style="">Current Level</h4>
                <p style="color: #A78BFA; font-size: 1.5rem; font-weight: 700;">Intermediate</p>
                <p style="color: #A1A1AA; font-size: 0.8rem;">Based on your activity</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Take Full Assessment", use_container_width=True):
            st.session_state.show_assessment = True
            st.rerun()

    if st.session_state.get('show_assessment'):
        render_assessment()


def render_assessment():
    """Render the AI Proficiency Assessment"""
    st.markdown("---")
    st.markdown("## 🎯 AI Proficiency Assessment")
    st.markdown("Answer these 5 technical questions to calibrate your learning path.")
    
    questions = [
        {
            "q": "What is the primary function of a System Prompt in LLMs?",
            "options": ["To greet the user", "To define the AI's behavior, persona, and constraints", "To speed up the response time", "To save tokens"],
            "correct": 1
        },
        {
            "q": "Which technique involves providing examples to the AI within the prompt?",
            "options": ["Zero-shot prompting", "Temperature tuning", "Few-shot prompting", "Chain of thought"],
            "correct": 2
        },
        {
            "q": "What does RAG stand for in AI architecture?",
            "options": ["Random Access Generation", "Retrieval-Augmented Generation", "Recursive AI Gradient", "Rapid Automated Guidance"],
            "correct": 1
        },
        {
            "q": "When tokens are 'exhausted' in a session, what primarily happens?",
            "options": ["The AI starts lying", "The response is truncated or the session ends", "The model switches to a smaller version", "The price per token increases"],
            "correct": 1
        },
        {
            "q": "Which parameter controls the 'creativity' or randomness of an LLM?",
            "options": ["Top-P", "Max Tokens", "Temperature", "Presence Penalty"],
            "correct": 2
        }
    ]
    
    score = 0
    with st.form("assessment_form"):
        for i, q in enumerate(questions):
            st.markdown(f"**{i+1}. {q['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}", q['options'], key=f"q_ans_{i}", label_visibility="collapsed")
            if ans == q['options'][q['correct']]:
                score += 1
            st.markdown("<br>", unsafe_allow_html=True)
            
        if st.form_submit_button("Submit Assessment", use_container_width=True):
            st.session_state.assessment_score = score
            st.session_state.show_assessment = False
            
            # Determine level
            level = "Beginner"
            if score >= 5: level = "Expert"
            elif score >= 3: level = "Intermediate"
            
            st.session_state.ai_level = level
            st.success(f"Assessment Complete! Your Score: {score}/5. Level Assigned: {level}")
            st.balloons()
            st.rerun()
    
    if st.button("Cancel Assessment"):
        st.session_state.show_assessment = False
        st.rerun()


def render_tutorial_grid(tutorials: list, context: str = "default"):
    """Render a grid of tutorial cards"""
    if not tutorials:
        st.info("No tutorials found matching your criteria.")
        return
    
    # Create rows of 3 tutorials
    for i in range(0, len(tutorials), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(tutorials):
                tutorial = tutorials[i + j]
                with col:
                    render_tutorial_card(tutorial, context)


def render_tutorial_card(tutorial: dict, context: str = "default"):
    """Render a single tutorial card with completion status"""
    from utils.helpers import is_tutorial_complete
    import html
    
    difficulty_colors = {
        "Beginner": "#10B981",
        "Intermediate": "#F59E0B", 
        "Advanced": "#EF4444",
        "Comprehensive": "#6366F1"
    }
    diff_color = difficulty_colors.get(tutorial.get('difficulty', 'Beginner'), '#64748B')
    
    # Check completion status
    is_complete = is_tutorial_complete(tutorial['id'])
    
    # Pre-calculate styles
    border_left = "border-left: 3px solid #10B981 !important;" if is_complete else ""
    completion_badge = '<span style="background: #10B981; color: white; padding: 0.15rem 0.5rem; border-radius: 10px; font-size: 0.65rem; font-weight: 700; margin-left: 8px;">✓ DONE</span>' if is_complete else ''
    
    # Get clean description and escape HTML entities
    description = html.escape(tutorial.get('description', '')[:95])
    icon = tutorial.get('icon', '📚')
    title = html.escape(tutorial['title'])
    difficulty = tutorial.get('difficulty', 'Beginner')
    duration = tutorial['duration']
    
    # Build card HTML safely
    card_html = f'''
        <div class="tool-card" style="border-top: 4px solid {diff_color} !important; background: rgba(255, 255, 255, 0.6) !important; min-height: 160px; display: flex; flex-direction: column; {border_left}">
            <div style="font-family: Outfit; font-weight: 800; font-size: 1.1rem; margin-bottom: 8px; display: flex; align-items: flex-start;">
                <span style="margin-right: 10px; font-size: 1.3rem;">{icon}</span>
                <span style="background: var(--prism-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{title}</span>
                {completion_badge}
            </div>
            <div style="font-size: 0.9rem; color: #475569; margin-bottom: 12px; flex-grow: 1; overflow: hidden; line-height: 1.5;">
                {description}...
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 10px;">
                <span style="background: {diff_color}; color: white; padding: 0.2rem 0.6rem; border-radius: 20px; font-size: 0.75rem; font-weight: 700;">{difficulty}</span>
                <span style="color: #64748B; font-size: 0.85rem; font-weight: 700;">⏱️ {duration}</span>
            </div>
        </div>
    '''
    
    # Use st.html instead of st.markdown for better HTML rendering
    st.html(card_html)
    
    button_text = "📖 Review" if is_complete else "🚀 Start Learning"
    if st.button(button_text, key=f"btn_lh_{context}_{tutorial['id']}", use_container_width=True):
        st.session_state.viewing_tutorial = tutorial['id']
        st.session_state.current_page = "tutorial_viewer"
        st.rerun()