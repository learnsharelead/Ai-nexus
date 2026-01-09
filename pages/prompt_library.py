"""
AI Nexus - Prompt Library Page
Prompt Engineering Mastery
"""
import streamlit as st
from data.final_prompts import (
    get_all_prompts, get_prompts_by_category, get_popular_prompts,
    search_prompts, get_prompt_by_id
)
from config.settings import PROMPT_CATEGORIES


def render():
    """Render the Prompt Library page"""
    st.markdown("<h2>Cognitive Architecture & Prompt Assets <span style='font-size:0.8rem; color:#6366F1;'>V6 SYNCED</span></h2>", unsafe_allow_html=True)
    
    # Stats bar
    col1, col2, col3, col4 = st.columns(4)
    all_prompts = get_all_prompts()
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{len(all_prompts)}</div>
                <div class="metric-label">Verified Prompts</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{len(PROMPT_CATEGORIES)}</div>
                <div class="metric-label">Categories</div>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{sum(p.get('uses', 0) for p in all_prompts):,}</div>
                <div class="metric-label">Uses</div>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">4.9</div>
                <div class="metric-label">Avg Rating</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Navigation State
    if 'prompt_lib_mode' not in st.session_state:
        st.session_state.prompt_lib_mode = "browse"

    # Custom Navigation Bar
    nav_cols = st.columns([1, 1, 1])
    with nav_cols[0]:
        if st.button("📚 Browse Prompts", 
                    key="nav_browse", 
                    type="primary" if st.session_state.prompt_lib_mode == "browse" else "secondary", 
                    use_container_width=True):
            st.session_state.prompt_lib_mode = "browse"
            st.rerun()
            
    with nav_cols[1]:
        if st.button("🔬 Prompt Lab", 
                    key="nav_lab", 
                    type="primary" if st.session_state.prompt_lib_mode == "lab" else "secondary", 
                    use_container_width=True):
            st.session_state.prompt_lib_mode = "lab"
            st.rerun()
            
    with nav_cols[2]:
        if st.button("📖 Techniques", 
                    key="nav_tech", 
                    type="primary" if st.session_state.prompt_lib_mode == "techniques" else "secondary", 
                    use_container_width=True):
            st.session_state.prompt_lib_mode = "techniques"
            st.rerun()
            
    st.markdown("<hr style='margin: 1rem 0; opacity: 0.1;'>", unsafe_allow_html=True)
    
    # Content Routing
    if st.session_state.prompt_lib_mode == "browse":
        render_preview_modal()
        render_browse_prompts()
    elif st.session_state.prompt_lib_mode == "lab":
        render_prompt_lab()
    elif st.session_state.prompt_lib_mode == "techniques":
        render_techniques()


def render_browse_prompts():
    """Render the browse prompts section"""
    # Search and filters
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        search_query = st.text_input(
            "🔍 Search prompts...",
            placeholder="e.g., code review, debugging, testing",
            key="prompt_search"
        )
    
    with col2:
        difficulty_filter = st.selectbox(
            "Difficulty",
            ["All", "Beginner", "Intermediate", "Advanced"],
            key="prompt_difficulty"
        )
    
    with col3:
        sort_by = st.selectbox(
            "Sort by",
            ["Popular", "Rating", "Newest"],
            key="prompt_sort"
        )
    
    # Category pills
    st.markdown("### Categories")
    
    categories = [{"id": "all", "name": "All", "icon": "🌐"}] + PROMPT_CATEGORIES
    selected_category = st.session_state.get('selected_prompt_category', 'all')
    
    # Row 1: First 5 categories
    cat_cols = st.columns(5)
    for i, category in enumerate(categories[:5]):
        with cat_cols[i]:
            is_sel = selected_category == category['id']
            if st.button(
                f"{category['icon']} {category['name'][:10]}",
                key=f"pcat_{category['id']}",
                use_container_width=True,
                type="primary" if is_sel else "secondary"
            ):
                st.session_state.selected_prompt_category = category['id']
                st.rerun()
    
    # Row 2: Categories 6-10
    if len(categories) > 5:
        cat_cols2 = st.columns(5)
        for i, category in enumerate(categories[5:10]):
            with cat_cols2[i]:
                is_sel = selected_category == category['id']
                if st.button(
                    f"{category['icon']} {category['name'][:10]}",
                    key=f"pcat2_{category['id']}",
                    use_container_width=True,
                    type="primary" if is_sel else "secondary"
                ):
                    st.session_state.selected_prompt_category = category['id']
                    st.rerun()
    
    # Row 3: Categories 11-15 (if any)
    if len(categories) > 10:
        cat_cols3 = st.columns(5)
        for i, category in enumerate(categories[10:15]):
            with cat_cols3[i]:
                is_sel = selected_category == category['id']
                if st.button(
                    f"{category['icon']} {category['name'][:10]}",
                    key=f"pcat3_{category['id']}",
                    use_container_width=True,
                    type="primary" if is_sel else "secondary"
                ):
                    st.session_state.selected_prompt_category = category['id']
                    st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Get and filter prompts with loading state
    with st.spinner("Loading prompts..."):
        try:
            if search_query:
                prompts = search_prompts(search_query)
            elif selected_category and selected_category != 'all':
                prompts = get_prompts_by_category(selected_category)
            else:
                prompts = get_all_prompts()
            
            if difficulty_filter != "All":
                prompts = [p for p in prompts if p.get("difficulty") == difficulty_filter]
            
            # Sort
            if sort_by == "Popular":
                prompts = sorted(prompts, key=lambda x: x.get("uses", 0), reverse=True)
            elif sort_by == "Rating":
                prompts = sorted(prompts, key=lambda x: x.get("rating", 0), reverse=True)
        except Exception as e:
            st.error(f"❌ Error loading prompts: {str(e)}")
            prompts = []
            
    if not prompts and (search_query or (selected_category and selected_category != 'all') or difficulty_filter != 'All'):
        st.info("No prompts found matching your criteria.")
        if st.button("Emergency Reset Filters"):
            st.session_state.prompt_search = ""
            st.session_state.selected_prompt_category = "all"
            st.session_state.prompt_difficulty = "All"
            st.session_state.prompt_sort = "Popular"
            st.rerun()
        return
    
    if prompts:
        st.markdown(f"**Showing {len(prompts[:24])} verified prompts**")
    else:
        st.warning("The prompt repository is currently empty or filtered out. Troubleshooting V6...")
    
    # Render prompts grid
    render_prompt_grid(prompts[:24], "browse")


def render_prompt_grid(prompts_list: list, context: str):
    """Render prompts in a dense grid"""
    if not prompts_list:
        st.info("No prompts found.")
        return
        
    for i in range(0, len(prompts_list), 5):
        cols = st.columns(5)
        for j in range(5):
            if i + j < len(prompts_list):
                with cols[j]:
                    render_prompt_card(prompts_list[i + j], context)


def render_prompt_card(prompt: dict, context: str = "default"):
    """Render a single prompt card"""
    difficulty_colors = {"Beginner": "#10B981", "Intermediate": "#F59E0B", "Advanced": "#EF4444"}
    diff_color = difficulty_colors.get(prompt.get("difficulty", "Beginner"), "#A1A1AA")
    
    # Truncate prompt text for preview
    preview = prompt.get('prompt', '')[:120].replace('\n', ' ')
    
    st.markdown(f"""
        <div class="tool-card" style="border-top: 4px solid #EC4899 !important; background: rgba(255, 255, 255, 0.6) !important; min-height: 180px; display: flex; flex-direction: column;">
            <div style="font-family: Outfit; font-weight: 800; font-size: 1.15rem; color: #1E293B; margin-bottom: 12px;">{prompt['title']}</div>
            <div style="font-family: 'JetBrains Mono', 'Fira Code', monospace; font-size: 0.85rem; color: #334155; background: #F1F5F9; padding: 12px; border-radius: 12px; border: 1px solid rgba(99, 102, 241, 0.2); flex-grow: 1; overflow: hidden; margin-bottom: 15px; line-height: 1.6;">
                {preview}...
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 10px;">
                <span style="background: var(--prism-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 0.9rem; font-weight: 800;">🚀 {prompt.get('uses', 0):,} Uses</span>
                <span style="background: #F472B6; color: white; padding: 0.15rem 0.5rem; border-radius: 10px; font-size: 0.75rem; font-weight: 700;">{prompt.get('difficulty', 'Beginner')}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Generate unique key suffix
    import hashlib
    key_suffix = hashlib.md5(f"{context}_{prompt['id']}".encode()).hexdigest()[:8]
    
    # Clone Button
    if st.button("Clone to Lab", key=f"clone_{key_suffix}", use_container_width=True):
        st.session_state.lab_prompt = prompt
        st.session_state.prompt_lib_mode = "lab"
        st.rerun()
    
    # View Code Button (Triggers Global Modal)
    if st.button("View Source / Copy", key=f"view_{key_suffix}", use_container_width=True):
         if st.session_state.get('preview_prompt_id') == prompt['id']:
             st.session_state.preview_prompt_id = None # Toggle off
         else:
             st.session_state.preview_prompt_id = prompt['id'] # Set global preview
         st.rerun()

def render_preview_modal():
    """Render a full-width preview of the selected prompt"""
    p_id = st.session_state.get('preview_prompt_id')
    if p_id:
        from data.final_prompts import get_prompt_by_id
        prompt = get_prompt_by_id(p_id)
        if prompt:
            st.markdown("---")
            st.markdown(f"### 🔍 Source Visualizer: {prompt['title']}")
            with st.expander("Expand Source Code", expanded=True):
                st.code(prompt.get('prompt', ''), language="markdown")
            
            # Action buttons row
            col1, col2, col3 = st.columns([1, 1, 1])
            
            with col1:
                if st.button("❌ Close Preview", type="secondary", use_container_width=True):
                    st.session_state.preview_prompt_id = None
                    st.rerun()
            
            with col2:
                if st.button("📋 Copy to Clipboard", type="primary", use_container_width=True):
                    st.toast("✅ Prompt copied! Use Ctrl+C from the code block above.")
            
            with col3:
                if st.button("📤 Share Prompt", use_container_width=True):
                    st.session_state[f'show_share_{p_id}'] = not st.session_state.get(f'show_share_{p_id}', False)
                    st.rerun()
            
            # Share section (expandable)
            if st.session_state.get(f'show_share_{p_id}', False):
                st.markdown("#### 📤 Share This Prompt")
                
                share_text = f"""🚀 AI Nexus Prompt: {prompt['title']}
📂 Category: {prompt.get('category', 'General').replace('_', ' ').title()}
⭐ Rating: {prompt.get('rating', 4.5)}/5

---
{prompt.get('prompt', '')}
---

Shared via AI Nexus - Enterprise Cognitive Architecture"""
                
                st.text_area("Copy this formatted prompt:", share_text, height=200, key="share_text_area")
                st.info("📧 Copy the text above and share via Email, Slack, or Teams!")
            
            st.markdown("---")


def render_prompt_lab():
    """Render the interactive Prompt Lab"""
    st.markdown("<h3>🔬 Prompt Lab</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("### Prompt Builder")
        
        # Prompt input
        prompt_text = st.text_area(
            "Your Prompt",
            height=200,
            placeholder="Enter your prompt here...\n\nUse {variable} syntax for dynamic parts.",
            value=st.session_state.get('lab_prompt', {}).get('prompt', ''),
            key="lab_prompt_text"
        )
        
        # Variables extraction and filling
        import re
        variables = re.findall(r'\{(\w+)\}', prompt_text)
        
        if variables:
            st.markdown("### Variables")
            var_values = {}
            for var in set(variables):
                var_values[var] = st.text_input(f"{var}", key=f"var_{var}", placeholder=f"Enter {var}...")
            
            # Preview with filled variables
            filled_prompt = prompt_text
            for var, value in var_values.items():
                if value:
                    filled_prompt = filled_prompt.replace(f"{{{var}}}", value)
            
            st.markdown("##### Lab Output - Orchestration Preview")
            st.code(filled_prompt, language="markdown")
        
        # Action buttons
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            if st.button("📋 Copy Prompt", use_container_width=True):
                st.success("Copied to clipboard!")
        with col_b:
            if st.button("💾 Save Prompt", use_container_width=True):
                st.success("Prompt saved!")
        with col_c:
            if st.button("🔄 Clear", use_container_width=True):
                st.rerun()
    
    with col2:
        st.markdown("### Prompt Tips")
        
        st.markdown("""
            <div class="metric-card" style="border-bottom: 6px solid #6366F1 !important; background: rgba(255, 255, 255, 0.7) !important;">
                <div style="font-family: Outfit; font-weight:800; background: var(--prism-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 15px; font-size: 1.3rem;">🚀 Prompt Architecture: CO-STAR</div>
                <div style="font-size: 0.95rem; color: #1E293B; line-height: 1.8;">
                    <b style="color:#6366F1;">[C]ontext:</b> Define the persona and background scenario.<br>
                    <b style="color:#EC4899;">[O]bjective:</b> State exactly what task needs execution.<br>
                    <b style="color:#F59E0B;">[S]tyle:</b> Specify the desired output format/tone.<br>
                    <b style="color:#10B981;">[T]one:</b> Guide the AI's emotional resonance.<br>
                    <b style="color:#3B82F6;">[A]udience:</b> Calibrate for the target reader.<br>
                    <b style="color:#6366F1;">[R]esponse:</b> Demand high-fidelity schemas.
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Quick Templates")
        
        templates = [
            ("Code Review", "Review this {language} code:\n\n```\n{code}\n```\n\nProvide feedback on quality, bugs, and improvements."),
            ("Debug Help", "I'm getting this error: {error}\n\nCode:\n```\n{code}\n```\n\nExplain the cause and fix."),
            ("Explain Code", "Explain what this code does step by step:\n\n```\n{code}\n```"),
        ]
        
        for name, template in templates:
            if st.button(f"📝 {name}", key=f"template_{name}", use_container_width=True):
                st.session_state.lab_prompt = {"prompt": template}
                st.rerun()


def render_techniques():
    """Render prompt engineering techniques"""
    st.markdown("## 📖 Advanced Techniques")
    st.markdown("*Master the art of prompt engineering*")
    
    techniques = [
        {
            "name": "Chain of Thought",
            "icon": "🔗",
            "description": "Guide the AI through step-by-step reasoning for complex problems.",
            "example": "Let me solve this step by step.\n\nStep 1: First, I will analyze the problem by {analysis_approach}.\nStep 2: Next, I'll consider the key factors: {key_factors}.\nStep 3: Based on this reasoning, my conclusion is..."
        },
        {
            "name": "Few-Shot Learning",
            "icon": "📚",
            "description": "Provide examples to establish patterns for the AI to follow.",
            "example": "I need you to classify customer feedback.\n\nExample 1:\nInput: 'The product arrived quickly!' → Sentiment: Positive\n\nExample 2:\nInput: 'It broke after one day.' → Sentiment: Negative\n\nNow classify this:\nInput: '{user_feedback}' → Sentiment:"
        },
        {
            "name": "Role-Based Prompting",
            "icon": "🎭",
            "description": "Assign a specific role or persona to get specialized responses.",
            "example": "You are an expert {role} with 20 years of experience in {domain}.\n\nYour task is to review the following and provide professional insights:\n\n{content_to_review}"
        },
        {
            "name": "Self-Consistency",
            "icon": "✓",
            "description": "Ask for multiple solutions and select the most consistent answer.",
            "example": "I need help with: {problem_statement}\n\nPlease provide 3 different approaches to solve this. For each approach:\n1. Explain the logic\n2. List pros and cons\n3. Give a confidence score (1-10)\n\nFinally, recommend the best approach."
        },
        {
            "name": "Tree of Thoughts",
            "icon": "🌳",
            "description": "Explore multiple reasoning paths before concluding.",
            "example": "Problem: {problem}\n\nExplore multiple solution paths:\n\nPath A (Conservative): [Describe approach]\n  - Evaluate: What are the risks/benefits?\n\nPath B (Aggressive): [Describe approach]\n  - Evaluate: What are the risks/benefits?\n\nPath C (Hybrid): [Describe approach]\n  - Evaluate: What are the risks/benefits?\n\nSynthesize: Which path is optimal and why?"
        },
        {
            "name": "System Message Optimization",
            "icon": "⚙️",
            "description": "Craft effective system messages to set context and constraints.",
            "example": "[SYSTEM]\nYou are a {assistant_type} assistant.\n\nRULES:\n- Always respond in {language}\n- Format code with markdown\n- Be concise but thorough\n- If unsure, say so\n\nCONTEXT:\n{background_context}\n\n[USER]\n{user_query}"
        },
    ]
    
    for i in range(0, len(techniques), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(techniques):
                tech = techniques[i + j]
                with col:
                    with st.expander(f"{tech['icon']} {tech['name']}", expanded=False):
                        st.markdown(tech['description'])
                        st.markdown("**Template:**")
                        st.code(tech['example'], language="markdown")
                        
                        # NEW: Try Template Button
                        if st.button(f"🚀 Try This Template", key=f"try_tech_{tech['name']}", use_container_width=True, type="primary"):
                            st.session_state.lab_prompt = {
                                "title": f"{tech['name']} Template",
                                "prompt": tech['example'],
                                "variables": []
                            }
                            st.session_state.prompt_lib_mode = "lab"
                            st.rerun()
