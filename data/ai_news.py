"""
AI Nexus - AI News Aggregator
Real-time AI news from top sources using RSS feeds
"""
import feedparser
from datetime import datetime, timedelta
import streamlit as st

# Top AI News RSS Feeds
AI_NEWS_SOURCES = [
    {
        "name": "OpenAI Blog",
        "url": "https://openai.com/blog/rss.xml",
        "category": "Company News",
        "icon": "🤖"
    },
    {
        "name": "Anthropic News",
        "url": "https://www.anthropic.com/news/rss.xml",
        "category": "Company News",
        "icon": "🧠"
    },
    {
        "name": "Google AI Blog",
        "url": "https://blog.google/technology/ai/rss/",
        "category": "Research",
        "icon": "🔬"
    },
    {
        "name": "Hugging Face Blog",
        "url": "https://huggingface.co/blog/feed.xml",
        "category": "Open Source",
        "icon": "🤗"
    },
    {
        "name": "MIT Technology Review - AI",
        "url": "https://www.technologyreview.com/topic/artificial-intelligence/feed",
        "category": "Analysis",
        "icon": "📰"
    },
    {
        "name": "The Verge - AI",
        "url": "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml",
        "category": "Tech News",
        "icon": "📱"
    },
    {
        "name": "VentureBeat - AI",
        "url": "https://venturebeat.com/category/ai/feed/",
        "category": "Business",
        "icon": "💼"
    },
    {
        "name": "AI News (artificialintelligence-news.com)",
        "url": "https://www.artificialintelligence-news.com/feed/",
        "category": "Industry",
        "icon": "🌐"
    }
]


@st.cache_data(ttl=600)  # Cache for 10 minutes
def fetch_news_from_source(source):
    """Fetch news from a single RSS source"""
    try:
        feed = feedparser.parse(source['url'])
        articles = []
        
        for entry in feed.entries[:10]:  # Get latest 10 articles
            # Parse published date
            published = None
            if hasattr(entry, 'published_parsed') and entry.published_parsed:
                published = datetime(*entry.published_parsed[:6])
            elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                published = datetime(*entry.updated_parsed[:6])
            
            article = {
                'title': entry.get('title', 'No Title'),
                'link': entry.get('link', '#'),
                'summary': entry.get('summary', entry.get('description', 'No summary available'))[:300],
                'published': published,
                'source': source['name'],
                'category': source['category'],
                'icon': source['icon']
            }
            articles.append(article)
        
        return articles
    except Exception as e:
        st.warning(f"Could not fetch from {source['name']}: {str(e)}")
        return []


@st.cache_data(ttl=600)  # Cache for 10 minutes
def get_all_news():
    """Fetch news from all sources"""
    all_articles = []
    
    for source in AI_NEWS_SOURCES:
        articles = fetch_news_from_source(source)
        all_articles.extend(articles)
    
    # Sort by published date (newest first)
    all_articles.sort(key=lambda x: x['published'] if x['published'] else datetime.min, reverse=True)
    
    return all_articles


def get_news_by_category(category):
    """Get news filtered by category"""
    all_news = get_all_news()
    
    if category == "All":
        return all_news
    
    return [article for article in all_news if article['category'] == category]


def get_news_by_timeframe(hours=24):
    """Get news from the last N hours"""
    all_news = get_all_news()
    cutoff = datetime.now() - timedelta(hours=hours)
    
    return [article for article in all_news if article['published'] and article['published'] > cutoff]


def search_news(query):
    """Search news by title or summary"""
    if not query:
        return []
    
    all_news = get_all_news()
    query = query.lower()
    
    return [
        article for article in all_news
        if query in article['title'].lower() or query in article['summary'].lower()
    ]


def get_trending_topics():
    """Extract trending topics from news titles"""
    all_news = get_all_news()
    
    # Simple keyword extraction (can be enhanced with NLP)
    keywords = {}
    common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what', 'which', 'who', 'when', 'where', 'why', 'how', 'all', 'each', 'every', 'both', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'just', 'don', 'now', 'new'}
    
    for article in all_news[:50]:  # Analyze recent 50 articles
        words = article['title'].lower().split()
        for word in words:
            word = word.strip('.,!?;:()[]{}"\'-')
            if len(word) > 3 and word not in common_words:
                keywords[word] = keywords.get(word, 0) + 1
    
    # Get top 10 trending topics
    trending = sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:10]
    return [{'topic': word.title(), 'count': count} for word, count in trending]
