import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from components.NavBar.navbar import navbar
import requests

# Page configuration
st.set_page_config(page_title="News & Articles", layout="wide")

# Display navbar
navbar()

def load_articles_page():
    """Load and display the articles page"""

    # Page title
    st.title("📰 Real Estate News & Articles")
    st.markdown("Stay updated with the latest trends, insights, and news in the real estate industry.")

    # --- CSS Styling ---
    st.markdown("""
        <style>
        .article-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .article-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
        }
        .article-title {
            color: white;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .article-date {
            color: rgba(255, 255, 255, 0.7);
            font-size: 12px;
            margin-bottom: 8px;
        }
        .article-description {
            color: rgba(255, 255, 255, 0.9);
            font-size: 14px;
            line-height: 1.6;
            margin-bottom: 10px;
        }
        .article-category {
            display: inline-block;
            background-color: rgba(255, 255, 255, 0.2);
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            margin-right: 8px;
        }
        .featured-article {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
        }
        .featured-title {
            color: white;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 15px;
        }
        .featured-description {
            color: rgba(255, 255, 255, 0.95);
            font-size: 16px;
            line-height: 1.8;
            margin-bottom: 15px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar filters
    st.sidebar.header("🔍 Filter News")
    categories = ["All", "Market Trends", "Investment Tips", "Industry News", "Property Updates", "Technology", "Regulations"]
    selected_category = st.sidebar.selectbox("Category", categories, key="articles_category_filter")

    date_range = st.sidebar.slider(
        "Articles from last (days)",
        min_value=1, max_value=90, value=30, step=1, key="articles_date_range"
    )

    search_query = st.sidebar.text_input(
        "🔎 Search articles...", placeholder="Enter keywords...", key="articles_search_box"
    )

    # --- Sample Articles Data ---
    articles_data = [
        {
            "id": 1,
            "title": "The Rise of Smart Homes: Revolutionizing Real Estate",
            "description": "Discover how IoT and AI technologies are transforming residential properties and increasing their market value.",
            "category": "Technology",
            "date": datetime.now() - timedelta(days=2),
            "author": "Sarah Johnson",
            "image_url": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500",
            "content": "Smart home technology has become a game-changer in the real estate industry...",
            "featured": True
        },
        {
            "id": 2,
            "title": "2025 Real Estate Market Predictions",
            "description": "Experts forecast significant changes in property prices, interest rates, and market dynamics for the upcoming year.",
            "category": "Market Trends",
            "date": datetime.now() - timedelta(days=5),
            "author": "Michael Chen",
            "image_url": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=500",
            "content": "The real estate market is expected to shift dramatically in 2025...",
            "featured": False
        },
        {
            "id": 3,
            "title": "Investment Strategies for First-Time Buyers",
            "description": "Learn essential tips and strategies for making your first real estate investment wisely and profitably.",
            "category": "Investment Tips",
            "date": datetime.now() - timedelta(days=7),
            "author": "Emily Rodriguez",
            "image_url": "https://images.unsplash.com/photo-1554224311-beee415c15ac?w=500",
            "content": "First-time real estate investors often struggle with where to start...",
            "featured": False
        },
        {
            "id": 4,
            "title": "New Regulations Impact Property Ownership",
            "description": "Government announces new policies that could affect property taxes, ownership structures, and rental markets.",
            "category": "Regulations",
            "date": datetime.now() - timedelta(days=10),
            "author": "David Smith",
            "image_url": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=500",
            "content": "Recent government announcements have introduced new regulations...",
            "featured": False
        },
        {
            "id": 5,
            "title": "Sustainable Real Estate: Building the Future",
            "description": "Explore eco-friendly building practices and their impact on property values and environmental sustainability.",
            "category": "Industry News",
            "date": datetime.now() - timedelta(days=15),
            "author": "Jessica Lee",
            "image_url": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=500",
            "content": "Sustainability in real estate is no longer optional...",
            "featured": False
        },
        {
            "id": 6,
            "title": "Commercial Real Estate: Post-Pandemic Recovery",
            "description": "Analyzing how commercial property markets are recovering and adapting to the new work environment.",
            "category": "Market Trends",
            "date": datetime.now() - timedelta(days=20),
            "author": "Robert Williams",
            "image_url": "https://images.unsplash.com/photo-1479839672679-a46482f0b7d8?w=500",
            "content": "The commercial real estate sector continues to evolve...",
            "featured": False
        }
    ]

    # --- Filters ---
    filtered_articles = articles_data
    if selected_category != "All":
        filtered_articles = [a for a in filtered_articles if a["category"] == selected_category]

    cutoff_date = datetime.now() - timedelta(days=date_range)
    filtered_articles = [a for a in filtered_articles if a["date"] >= cutoff_date]

    if search_query:
        q = search_query.lower()
        filtered_articles = [a for a in filtered_articles if q in a["title"].lower() or q in a["description"].lower()]

    # --- Featured Article ---
    featured_articles = [a for a in filtered_articles if a["featured"]]
    if featured_articles:
        featured = featured_articles[0]
        st.markdown(f"""
            <div class="featured-article">
                <div class="featured-title">{featured['title']}</div>
                <div class="featured-description">{featured['description']}</div>
                <div style="color: rgba(255, 255, 255, 0.8); margin-bottom: 10px;">
                    By <strong>{featured['author']}</strong> | {featured['date'].strftime('%B %d, %Y')}
                </div>
                <div class="article-category">{featured['category']}</div>
            </div>
        """, unsafe_allow_html=True)

    # --- Stats ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Articles", len(articles_data))
    with col2:
        st.metric("Categories", len(categories) - 1)
    with col3:
        st.metric("Updated", "Today")

    # --- ARTICLE VIEW HANDLER ---
    open_article_id = None
    for article in articles_data:
        if st.session_state.get(f"article_{article['id']}", False):
            open_article_id = article["id"]
            break

    if open_article_id:
        # Show selected article
        article = next(a for a in articles_data if a["id"] == open_article_id)
        st.markdown("---")
        st.subheader(article['title'])

        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**Author:** {article['author']}")
            st.write(f"**Published:** {article['date'].strftime('%B %d, %Y')}")
            st.write(f"**Category:** {article['category']}")
        with col2:
            st.image(article['image_url'], use_container_width=True)

        st.markdown("---")
        st.write(article['content'])

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("👍 Like", key=f"like_{article['id']}"):
                st.success("You liked this article!")
        with col2:
            if st.button("💬 Comment", key=f"comment_{article['id']}"):
                st.info("Comments feature coming soon!")
        with col3:
            if st.button("🔗 Share", key=f"share_{article['id']}"):
                st.info("Share functionality coming soon!")

        if st.button("← Back to Articles", key=f"back_{article['id']}"):
            st.session_state[f"article_{article['id']}"] = False
            st.rerun()

    else:
        # --- Articles Grid ---
        st.subheader(f"📚 Articles ({len(filtered_articles)} results)")
        if filtered_articles:
            cols_per_row = 2
            for i in range(0, len(filtered_articles), cols_per_row):
                cols = st.columns(cols_per_row)
                for j, col in enumerate(cols):
                    if i + j < len(filtered_articles):
                        article = filtered_articles[i + j]
                        with col:
                            st.markdown(f"""
                                <div class="article-card">
                                    <div class="article-title">{article['title']}</div>
                                    <div class="article-date">{article['date'].strftime('%B %d, %Y')} | By {article['author']}</div>
                                    <div class="article-description">{article['description']}</div>
                                    <div class="article-category">{article['category']}</div>
                                </div>
                            """, unsafe_allow_html=True)

                            if st.button("Read More →", key=f"read_{article['id']}"):
                                st.session_state[f"article_{article['id']}"] = True
                                st.rerun()
        else:
            st.info("📭 No articles found matching your filters. Try adjusting your search criteria.")

    # --- Newsletter ---
    st.markdown("---")
    st.subheader("📧 Subscribe to Our Newsletter")
    col1, col2 = st.columns([3, 1])
    with col1:
        email = st.text_input("Enter your email to get weekly real estate news", key="newsletter_email")
    with col2:
        if st.button("Subscribe", key="newsletter_subscribe"):
            if email:
                st.success(f"✅ Subscribed! You'll receive updates at {email}")
            else:
                st.error("Please enter a valid email address")


