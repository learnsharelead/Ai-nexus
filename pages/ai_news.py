"""
AI Nexus - AI Latest News Page
Real-time AI news aggregation from top sources
"""
import streamlit as st
from data.ai_news import (
    get_all_news, get_news_by_category, get_news_by_timeframe,
    search_news, get_trending_topics
)
from datetime import datetime


def render():
    """Render the AI Latest News page"""
    st.markdown("<h2>📰 AI Latest News</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748B; margin-bottom: 1.5rem;'>Real-time AI news from OpenAI, Anthropic, Google, and more. Updated every 10 minutes.</p>", unsafe_allow_html=True)
    
    # Trending Topics Banner
    with st.spinner("Loading trending topics..."):
        trending = get_trending_topics()
        if trending:
            st.markdown("### 🔥 Trending Now")
            trending_html = " ".join([
                f'<span style="background: linear-gradient(135deg, #6366F1, #EC4899); color: white; padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.85rem; font-weight: 700; margin-right: 0.5rem; display: inline-block; margin-bottom: 0.5rem;">{topic["topic"]} ({topic["count"]})</span>'
                for topic in trending[:8]
            ])
            st.markdown(f'<div style="margin-bottom: 1.5rem;">{trending_html}</div>', unsafe_allow_html=True)
    
    # Search and filters
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        search_query = st.text_input("🔍 Search News", placeholder="e.g., GPT-5, Claude...", key="news_search")
    
    with col2:
        category_filter = st.selectbox(
            "Source Type",
            ["All", "Company News", "Research", "Open Source", "Analysis", "Tech News", "Business", "Industry"],
            key="news_category"
        )
    
    with col3:
        timeframe = st.selectbox(
            "Timeframe",
            ["All Time", "Last 24 Hours", "Last 7 Days", "Last 30 Days"],
            key="news_timeframe"
        )
    
    # Get filtered news
    with st.spinner("Fetching latest news..."):
        if search_query:
            articles = search_news(search_query)
        elif timeframe == "Last 24 Hours":
            articles = get_news_by_timeframe(24)
        elif timeframe == "Last 7 Days":
            articles = get_news_by_timeframe(168)
        elif timeframe == "Last 30 Days":
            articles = get_news_by_timeframe(720)
        elif category_filter != "All":
            articles = get_news_by_category(category_filter)
        else:
            articles = get_all_news()
    
    st.markdown(f"**Found {len(articles)} articles**")
    
    # Refresh button
    if st.button("🔄 Refresh News", use_container_width=False):
        st.cache_data.clear()
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Render news in grid
    if not articles:
        st.info("No news articles found matching your criteria. Try adjusting your filters.")
        return
    
    # Grid layout - 3 columns
    for i in range(0, min(len(articles), 30), 3):  # Show latest 30
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(articles):
                with cols[j]:
                    render_news_card(articles[i + j], f"grid_{i}_{j}")


def render_news_card(article, context="default"):
    """Render a news card in grid format"""
    # Time ago calculation
    time_ago = ""
    if article['published']:
        delta = datetime.now() - article['published']
        if delta.days > 0:
            time_ago = f"{delta.days}d ago"
        elif delta.seconds // 3600 > 0:
            time_ago = f"{delta.seconds // 3600}h ago"
        else:
            time_ago = f"{delta.seconds // 60}m ago"
    
    category_colors = {
        "Company News": "#6366F1",
        "Research": "#EC4899",
        "Open Source": "#10B981",
        "Analysis": "#F59E0B",
        "Tech News": "#8B5CF6",
        "Business": "#EF4444",
        "Industry": "#06B6D4"
    }
    
    cat_color = category_colors.get(article['category'], '#64748B')
    
    # Compact card
    st.html(f'''
        <div class="tool-card" style="border-top: 4px solid {cat_color} !important; background: rgba(255, 255, 255, 0.6) !important; min-height: 200px; display: flex; flex-direction: column;">
            <div style="font-family: Outfit; font-weight: 800; font-size: 1.05rem; margin-bottom: 8px; line-height: 1.3;">
                <a href="{article['link']}" target="_blank" style="color: #1E293B; text-decoration: none;">
                    {article['icon']} {article['title'][:80]}{'...' if len(article['title']) > 80 else ''}
                </a>
            </div>
            <div style="font-size: 0.85rem; color: #475569; margin-bottom: 10px; flex-grow: 1; overflow: hidden; line-height: 1.5;">
                {article['summary'][:120]}...
            </div>
            <div style="display: flex; gap: 0.4rem; flex-wrap: wrap; margin-bottom: 10px;">
                <span style="background: {cat_color}; color: white; padding: 0.15rem 0.5rem; border-radius: 10px; font-size: 0.7rem; font-weight: 700;">{article['category']}</span>
                <span style="color: #64748B; font-size: 0.7rem; font-weight: 600;">{article['source']}</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 8px;">
                <span style="color: #94A3B8; font-size: 0.75rem;">{time_ago}</span>
                <a href="{article['link']}" target="_blank" style="color: #6366F1; text-decoration: none; font-weight: 700; font-size: 0.75rem;">
                    Read →
                </a>
            </div>
        </div>
    ''')
