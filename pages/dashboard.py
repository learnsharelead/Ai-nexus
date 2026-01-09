"""
AI Nexus - Dashboard Page
Personal Analytics & Progress Tracking
"""
import streamlit as st
import json
import time
from datetime import datetime, timedelta
from data.final_tutorials import get_all_tutorials
from utils.helpers import (
    calculate_ai_score, get_completed_tutorials, 
    get_saved_prompts, get_all_favorites
)


def render():
    """Render the Dashboard page"""
    st.markdown("<h2>📊 Your Dashboard</h2>", unsafe_allow_html=True)
    
    # Check if user has profile
    if not st.session_state.get('user_profile'):
        st.warning("Complete your profile to unlock personalized dashboard!")
        if st.button("Complete Profile", type="primary"):
            st.session_state.current_page = "profile"
            st.rerun()
        return
    
    profile = st.session_state.user_profile
    
    # Get real user data with loading state
    with st.spinner("Loading your dashboard..."):
        try:
            ai_score = calculate_ai_score()
            completed_count = len(get_completed_tutorials())
            saved_prompts_count = len(get_saved_prompts())
            favorites = get_all_favorites()
            tools_mastered = len(favorites.get('tools', {}))
        except Exception as e:
            st.error(f"❌ Error loading dashboard data: {str(e)}")
            ai_score = 0
            completed_count = 0
            saved_prompts_count = 0
            tools_mastered = 0
    
    # Overview stats
    col1, col2, col3, col4 = st.columns(4)
    
    stats = [
        {"value": ai_score, "label": "AI Score", "icon": "🎯", "color": "#6366F1", "trend": "↑ Growing"},
        {"value": completed_count, "label": "Learner Progress", "icon": "🎓", "color": "#EC4899", "trend": "Keep it up!"},
        {"value": tools_mastered, "label": "Tools Mastery", "icon": "🛠️", "color": "#F59E0B", "trend": "Expansive"},
        {"value": saved_prompts_count, "label": "Prompt Assets", "icon": "💡", "color": "#10B981", "trend": "High Fidelity"},
    ]
    
    for i, stat in enumerate(stats):
        with [col1, col2, col3, col4][i]:
            st.markdown(f"""
                <div class="metric-card" style="border-bottom: 4px solid {stat['color']} !important;">
                    <div style="font-size: 1.8rem; font-weight: 800; background: var(--prism-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: Outfit;">{stat['value']}</div>
                    <div class="metric-label">{stat['label']}</div>
                    <div style="color: {stat['color']}; font-size: 0.85rem; font-weight: 700; margin-top: 8px;">{stat['icon']} {stat['trend']}</div>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Learning Progress
        st.markdown("### 📚 Learning Progress")
        
        # Dynamic Progress Calculation
        all_tutorials = get_all_tutorials()
        completed_ids = get_completed_tutorials()
        
        # Calculate totals
        total_qw = len([t for t in all_tutorials if t['id'].startswith('qw-')])
        total_dd = len([t for t in all_tutorials if t['id'].startswith('dd-')])
        total_mt = len([t for t in all_tutorials if t['id'].startswith('mt-')])
        
        # Calculate completed
        comp_qw = len([tid for tid in completed_ids if tid.startswith('qw-')])
        comp_dd = len([tid for tid in completed_ids if tid.startswith('dd-')])
        comp_mt = len([tid for tid in completed_ids if tid.startswith('mt-')])
        
        progress_data = [
            {"name": "Quick Wins", "completed": comp_qw, "total": total_qw, "color": "#10B981"},
            {"name": "Deep Dives", "completed": comp_dd, "total": total_dd, "color": "#F59E0B"},
            {"name": "Mastery Track", "completed": comp_mt, "total": total_mt, "color": "#7C3AED"},
        ]
        
        for item in progress_data:
            pct = (item['completed'] / item['total'] * 100) if item['total'] > 0 else 0
            st.markdown(f"""
                <div style="margin-bottom: 1.25rem;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span style="font-weight: 800; font-size: 0.95rem; color: #1E293B;">{item['name']}</span>
                        <span style="color: {item['color']}; font-weight: 800; font-size: 0.95rem;">{item['completed']}/{item['total']}</span>
                    </div>
                    <div style="background: rgba(0,0,0,0.05); border-radius: 20px; height: 10px; overflow: hidden; border: 1px solid rgba(0,0,0,0.02);">
                        <div style="background: {item['color']}; height: 100%; width: {pct}%; border-radius: 20px; box-shadow: 0 0 10px {item['color']}40;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Activity Chart - Real Data
        st.markdown("### 📈 Weekly Activity")
        
        # Fetch real activity data
        from utils.helpers import get_recent_activities
        from collections import defaultdict
        
        recent_activities = get_recent_activities(50)  # Get last 50 activities
        
        # Group by day of week
        day_counts = defaultdict(int)
        day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        
        for act in recent_activities:
            try:
                ts = datetime.fromisoformat(act.get('timestamp', ''))
                day_idx = ts.weekday()  # 0=Mon, 6=Sun
                day_counts[day_idx] += 1
            except:
                pass
        
        # Build activity list for chart
        activity = [day_counts.get(i, 0) for i in range(7)]
        
        if sum(activity) == 0:
            st.info("📊 Start completing tutorials, saving prompts, or favoriting tools to see your activity chart!")
        else:
            chart_html = '<div style="display: flex; align-items: flex-end; height: 140px; gap: 10px; padding: 1.5rem; background: rgba(255,255,255,0.7); border-radius: 16px; border: 1px solid rgba(0,0,0,0.05);">'
            max_val = max(activity) if max(activity) > 0 else 1
            colors = ["#6366F1", "#EC4899", "#F59E0B", "#10B981", "#3B82F6", "#F43F5E", "#06B6D4"]
            for i, (day, val) in enumerate(zip(day_names, activity)):
                height = (val / max_val * 100) if max_val > 0 else 0
                color = colors[i % len(colors)]
                chart_html += f'''
                    <div style="flex: 1; display: flex; flex-direction: column; align-items: center;">
                        <div style="background: {color}; width: 80%; height: {height}px; border-radius: 6px; box-shadow: 0 4px 10px {color}30;" title="{val} activities"></div>
                        <span style="color: #64748B !important; font-size: 0.75rem; margin-top: 10px; font-weight: 700;">{day}</span>
                        <span style="color: #1E293B; font-size: 0.65rem; font-weight: 600;">{val}</span>
                    </div>
                '''
            chart_html += '</div>'
            
            st.markdown(chart_html, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Recent Activity
        st.markdown("### 🕐 Recent Activity")
        
        with st.spinner("Loading recent activities..."):
            try:
                from utils.helpers import get_recent_activities
                from datetime import datetime
                
                activities = get_recent_activities(5)
                
                if activities:
                    for activity in activities:
                        # Parse timestamp
                        try:
                            timestamp = datetime.fromisoformat(activity['timestamp'])
                            time_ago = get_time_ago(timestamp)
                        except:
                            time_ago = "Recently"
                        
                        # Get icon based on activity type
                        icon_map = {
                            'tutorial_complete': '📚',
                            'prompt_saved': '💡',
                            'tool_favorite': '🔧',
                            'default': '✨'
                        }
                        icon = icon_map.get(activity['type'], icon_map['default'])
                        
                        # Get action text
                        action_map = {
                            'tutorial_complete': 'Completed tutorial',
                            'prompt_saved': 'Saved prompt',
                            'tool_favorite': 'Saved tool',
                            'default': 'Activity'
                        }
                        action = action_map.get(activity['type'], action_map['default'])
                        
                        item_name = activity.get('details', {}).get('title', activity.get('item_id', 'Unknown'))
                        
                        st.markdown(f"""
                            <div class="tool-card" style="padding: 1rem; margin-bottom: 0.5rem; display: flex; align-items: center;">
                                <span style="font-size: 1.5rem; margin-right: 1rem;">{icon}</span>
                                <div style="flex: 1;">
                                    <span style="">{action}: </span>
                                    <span style="color: #A78BFA;">{item_name}</span>
                                </div>
                                <span style="color: #A1A1AA; font-size: 0.8rem;">{time_ago}</span>
                            </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("No activities yet. Start learning to see your progress here!")
            except Exception as e:
                st.error(f"❌ Error loading activities: {str(e)}")


def get_time_ago(timestamp):
    """Convert timestamp to human-readable time ago"""
    from datetime import datetime, timedelta
    now = datetime.now()
    diff = now - timestamp
    
    if diff < timedelta(minutes=1):
        return "Just now"
    elif diff < timedelta(hours=1):
        mins = int(diff.total_seconds() / 60)
        return f"{mins} min ago" if mins == 1 else f"{mins} mins ago"
    elif diff < timedelta(days=1):
        hours = int(diff.total_seconds() / 3600)
        return f"{hours} hour ago" if hours == 1 else f"{hours} hours ago"
    elif diff < timedelta(days=7):
        days = diff.days
        return f"{days} day ago" if days == 1 else f"{days} days ago"
    else:
        return timestamp.strftime("%b %d")
    
    with col2:
        # Skill Radar
        st.markdown("### 🎯 Skill Distribution")
        
        skills = [
            {"name": "Code Generation", "level": 75},
            {"name": "Debugging", "level": 60},
            {"name": "Testing", "level": 45},
            {"name": "Documentation", "level": 80},
            {"name": "Prompt Engineering", "level": 65},
        ]
        
        for skill in skills:
            color = "#10B981" if skill['level'] >= 70 else "#F59E0B" if skill['level'] >= 50 else "#EF4444"
            st.markdown(f"""
                <div style="margin-bottom: 8px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 2px;">
                        <span style="font-size: 9px; font-weight: 600; color: #1E293B !important;">{skill['name']}</span>
                        <span style="color: {color} !important; font-size: 9px; font-weight: 800;">{skill['level']}%</span>
                    </div>
                    <div style="background: #F1F5F9; border-radius: 2px; height: 3px; overflow: hidden;">
                        <div style="background: {color}; height: 100%; width: {skill['level']}%;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Achievements
        st.markdown("### 🏆 Achievements")
        
        achievements = [
            {"icon": "🚀", "name": "Getting Started", "desc": "Completed profile"},
            {"icon": "📚", "name": "Quick Learner", "desc": "5 tutorials done"},
            {"icon": "💡", "name": "Prompt Pro", "desc": "10 prompts saved"},
            {"icon": "🔧", "name": "Tool Explorer", "desc": "Viewed 20 tools"},
        ]
        
        for achievement in achievements:
            st.markdown(f"""
                <div class="tool-card" style="padding: 0.75rem; margin-bottom: 0.5rem; display: flex; align-items: center;">
                    <span style="font-size: 1.5rem; margin-right: 0.75rem;">{achievement['icon']}</span>
                    <div>
                        <div style="font-weight: 600; font-size: 0.85rem;">{achievement['name']}</div>
                        <div style="color: #A1A1AA; font-size: 0.75rem;">{achievement['desc']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Recommendations
        st.markdown("### ✨ AI Recommendations")
        
        st.markdown("""
            <div class="glass-card" style="padding: 1rem;">
                <p style="color: #A1A1AA; font-size: 0.85rem; margin-bottom: 1rem;">Based on your progress:</p>
                <ul style="font-size: 0.85rem; padding-left: 1.25rem;">
                    <li style="margin-bottom: 0.5rem;">Try <span style="color: #A78BFA;">Cursor IDE</span> for faster coding</li>
                    <li style="margin-bottom: 0.5rem;">Complete <span style="color: #A78BFA;">Testing Deep Dive</span></li>
                    <li>Explore <span style="color: #A78BFA;">Chain of Thought prompts</span></li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Actions
    st.markdown("---")
    st.markdown("### ⚡ Quick Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📚 Continue Learning", use_container_width=True):
            st.session_state.current_page = "learning"
            st.rerun()
    
    with col2:
        if st.button("🔧 Explore Tools", use_container_width=True):
            st.session_state.current_page = "tools"
            st.rerun()
    
    with col3:
        if st.button("💡 Browse Prompts", use_container_width=True):
            st.session_state.current_page = "prompts"
            st.rerun()
    
    with col4:
        if st.button("📊 Take Assessment", use_container_width=True):
            st.session_state.current_page = "assessment"
            st.rerun()

    # Data Portability Section
    st.markdown("---")
    st.markdown("### 💾 Workspace Data")
    
    with st.expander("Export Your Data", expanded=False):
        st.markdown("Download a complete backup of your learning progress, saved prompts, and tool libraries.")
        
        # Prepare data
        export_data = {
            "metadata": {
                "version": "2.4.0",
                "export_date": datetime.now().isoformat(),
                "user_role": profile.get('role', 'Unknown')
            },
            "metrics": {
                "ai_score": ai_score,
                "tutorials_completed": completed_count,
                "prompts_saved": saved_prompts_count
            },
            "assets": {
                "saved_prompts": get_saved_prompts(),
                "favorite_tools": get_all_favorites('tools'),
                "completed_curriculum": get_completed_tutorials()
            }
        }
        
        json_data = json.dumps(export_data, indent=2)
        
        col1, col2 = st.columns([1, 2])
        with col1:
             st.download_button(
                label="📥 Download JSON Backup",
                data=json_data,
                file_name=f"nexus_workspace_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json",
                use_container_width=True
            )
        with col2:
            st.info("This file contains your entire personalized Nexus state. You can use it to migrate to other instances.")
    
    # Import Workspace Section
    with st.expander("Import Workspace Backup", expanded=False):
        st.markdown("Restore your learning progress from a previously exported JSON backup file.")
        
        uploaded_file = st.file_uploader(
            "Upload your nexus_workspace.json file",
            type=['json'],
            key="workspace_import"
        )
        
        if uploaded_file is not None:
            try:
                import_data = json.loads(uploaded_file.read().decode('utf-8'))
                
                # Validate structure
                if 'metadata' not in import_data or 'assets' not in import_data:
                    st.error("❌ Invalid backup file format. Missing required sections.")
                else:
                    st.success(f"✅ Valid backup detected (Version: {import_data['metadata'].get('version', 'Unknown')})")
                    
                    # Preview
                    st.markdown("**Backup Contents:**")
                    assets = import_data.get('assets', {})
                    prompts_count = len(assets.get('saved_prompts', {}))
                    tools_count = len(assets.get('favorite_tools', {}))
                    tutorials_count = len(assets.get('completed_curriculum', []))
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Saved Prompts", prompts_count)
                    with col2:
                        st.metric("Favorite Tools", tools_count)
                    with col3:
                        st.metric("Completed Tutorials", tutorials_count)
                    
                    st.warning("⚠️ Importing will merge with your existing data. Duplicates will be skipped.")
                    
                    if st.button("🔄 Import & Restore", type="primary", use_container_width=True):
                        from utils.helpers import save_to_local_storage, get_from_local_storage
                        
                        # Import saved prompts
                        existing_prompts = get_from_local_storage('prompt_library', {})
                        imported_prompts = assets.get('saved_prompts', {})
                        merged_prompts = {**existing_prompts, **imported_prompts}
                        save_to_local_storage('prompt_library', merged_prompts)
                        
                        # Import favorite tools
                        existing_favorites = get_from_local_storage('favorites', {})
                        if 'tools' not in existing_favorites:
                            existing_favorites['tools'] = {}
                        imported_tools = assets.get('favorite_tools', {})
                        existing_favorites['tools'] = {**existing_favorites.get('tools', {}), **imported_tools}
                        save_to_local_storage('favorites', existing_favorites)
                        
                        # Import completed tutorials
                        existing_completed = get_from_local_storage('completed_tutorials', [])
                        imported_completed = assets.get('completed_curriculum', [])
                        merged_completed = list(set(existing_completed + imported_completed))
                        save_to_local_storage('completed_tutorials', merged_completed)
                        
                        st.success(f"✅ Import complete! Restored {prompts_count} prompts, {tools_count} tools, {tutorials_count} tutorials.")
                        st.balloons()
                        
                        # Refresh
                        time.sleep(1)
                        st.rerun()
                        
            except json.JSONDecodeError:
                st.error("❌ Failed to parse JSON file. Please ensure it's a valid backup.")
            except Exception as e:
                st.error(f"❌ Import error: {str(e)}")
