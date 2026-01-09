"""
AI Nexus - Tutorial Viewer
Display full tutorial content with interactive elements
"""
import streamlit as st
from data.final_tutorials import get_all_tutorials
from data.tutorial_content import TUTORIAL_CONTENT
from utils.helpers import mark_tutorial_complete, is_tutorial_complete, track_activity


def render_tutorial(tutorial_id: str):
    """Render a full tutorial with content"""
    # Get tutorial metadata
    all_tutorials = get_all_tutorials()
    tutorial = next((t for t in all_tutorials if t['id'] == tutorial_id), None)
    
    if not tutorial:
        st.error("Tutorial not found!")
        if st.button("← Back to Learning Hub"):
            st.session_state.current_page = "learning"
            st.session_state.pop('viewing_tutorial', None)
            st.rerun()
        return
    
    # Header
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"# {tutorial['icon']} {tutorial['title']}")
        st.markdown(f"*{tutorial.get('description', '')}*")
    with col2:
        if st.button("← Back", use_container_width=True):
            st.session_state.current_page = "learning"
            st.session_state.pop('viewing_tutorial', None)
            st.rerun()
    
    # Tutorial info bar
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"**Duration:** {tutorial['duration']}")
    with col2:
        st.markdown(f"**Difficulty:** {tutorial['difficulty']}")
    with col3:
        st.markdown(f"**Rating:** {'★' * int(tutorial.get('rating', 4.5))}")
    with col4:
        is_complete = is_tutorial_complete(tutorial_id)
        if is_complete:
            st.success("Completed")
        else:
            st.info("In Progress")
    
    st.markdown("---")
    
    # Get tutorial content
    content = TUTORIAL_CONTENT.get(tutorial_id)
    
    if content:
        # Render sections
        for i, section in enumerate(content.get('sections', [])):
            st.markdown(f"## {section['title']}")
            st.markdown(section['content'])
            st.markdown("<br>", unsafe_allow_html=True)
        
        # Quiz section
        if 'quiz' in content:
            st.markdown("---")
            st.markdown("## Knowledge Check")
            
            for i, q in enumerate(content['quiz']):
                st.markdown(f"**Question {i+1}:** {q['question']}")
                answer = st.radio(
                    "Select your answer:",
                    q['options'],
                    key=f"quiz_{tutorial_id}_{i}",
                    index=None
                )
                
                if answer:
                    if q['options'].index(answer) == q['correct']:
                        st.success("Correct!")
                        if 'explanation' in q:
                            st.info(q['explanation'])
                    else:
                        st.error("Incorrect. Try again!")
        
        # Completion section
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col2:
            if not is_tutorial_complete(tutorial_id):
                if st.button("Mark as Complete", type="primary", use_container_width=True):
                    mark_tutorial_complete(tutorial_id)
                    track_activity('tutorial_complete', tutorial_id, {'title': tutorial['title']})
                    st.success("Tutorial completed successfully")
                    st.rerun()
            else:
                st.success("Completed")
    
    else:
        # Generic content for tutorials without detailed content
        st.info("Full tutorial content available soon")
        st.markdown(f"""
        **Learning Objectives:**
        - {tutorial.get('description', 'Core concepts and practical applications')}
        - Hands-on examples and exercises
        - Industry best practices
        - Real-world implementation
        """)
        
        st.markdown("---")
        
        # Placeholder sections
        with st.expander("Module 1: Introduction", expanded=True):
            st.markdown(f"Fundamentals of {tutorial['title'].lower()}")
            st.code("""
# Example implementation
def example():
    pass
            """, language="python")
        
        with st.expander("Module 2: Practical Application"):
            st.markdown("Real-world examples and use cases")
        
        with st.expander("Module 3: Best Practices"):
            st.markdown("Industry standards and recommendations")
        
        with st.expander("Module 4: Assessment"):
            st.markdown("Knowledge verification exercises")
        
        st.markdown("---")
        
        if not is_tutorial_complete(tutorial_id):
            if st.button("Mark as Complete", type="primary", use_container_width=True):
                mark_tutorial_complete(tutorial_id)
                track_activity('tutorial_complete', tutorial_id, {'title': tutorial['title']})
                st.success("Tutorial completed successfully")
                st.rerun()
