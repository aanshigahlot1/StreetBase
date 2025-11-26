# feedback.py (Final Code with Post-Submission Rating Removed)

# ---------------- IMPORTS ----------------
from pathlib import Path
from components.chatbot_ui import chatbot_popup
import streamlit.components.v1 as components
import sys
import streamlit as st
import qrcode
import io

# Standard path setup
ROOT = Path(__file__).resolve().parents[0]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
# ---------------------------------------------------

def load_single_page():
    
    # --- Page Configuration ---
    st.set_page_config(
        page_title="About StreetBase", 
        layout="wide",
        initial_sidebar_state="collapsed" 
    )

    # ---------------- CSS (Complete Styles) ----------------
    st.markdown(
        """
    <style>
    /* Global Streamlit Overrides */
    #MainMenu, header, footer {
        visibility: hidden; 
        height: 0;
        margin: 0;
        padding: 0;
    }
    body, .block-container, p, div, span, li {
        color: #2b2b2b !important; 
        background-color: #FFFDF2 !important; 
        font-family: 'Segoe UI', sans-serif; 
        max-width: none; 
        padding: 0 1rem;
    }

    /* Hero Section Styling (MAXIMIZED BOX) */
    .hero-wrapper {
        margin-top: 2rem; 
        margin-bottom: 3rem; 
        padding: 3.5rem 3rem; 
        border-radius: 24px;
        background: radial-gradient(circle at top left, #F5B895 0, #FFFDF2 45%, #EDE9D5 100%); 
        box-shadow: 0 15px 40px rgba(0,0,0,0.15); 
        border: 2px solid rgba(226,114,91,0.4); 
    }
    .title {
        font-size: 4rem !important; 
        font-weight: 900 !important; 
        color: #004D00 !important; 
        margin-bottom: 1rem;
    }
    .title span.highlight {
        color: #E2725B !important; 
    }
    .subtitle {
        font-size: 1.3rem !important; 
        color: #3f3f3f !important;
        line-height: 1.7; 
    }
    .hero-tag {
        background: #E2725B; 
        color: #FFFDF2;
        padding: 0.5rem 1rem;
        font-size: 0.9rem;
    }
    .hero-pills {
        margin-top: 2rem;
    }

    /* Hero Metrics */
    .metric-card {
        background: #FFFFFF !important; 
        border-radius: 12px; 
        padding: 1.2rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        border-left: 5px solid #E2725B; 
        margin-bottom: 1rem;
    }
    .metric-value {
        font-size: 1.6rem; 
        font-weight: 800;
        color: #004D00 !important; 
    }
    .metric-label {
        font-size: 0.95rem;
        color: #555 !important;
    }

    /* General Section Titles & Subtitles */
    .section-title {
        color: #004D00 !important; 
        font-weight: 800 !important;
        font-size: 2.5rem; 
        margin-top: 3.5rem; 
        margin-bottom: 0.8rem;
    }
    .section-subtitle {
        color: #3f3f3f !important;
        font-size: 1.1rem; 
        line-height: 1.6;
    }

    /* Form Labels & Inputs (Outline Boxes & Visibility) */
    .stForm label p {
        font-weight: 700 !important; 
        color: #004D00 !important; 
        font-size: 1.05rem; 
    }
    .stTextInput > div > div > input,
    .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"] { 
        border: 4px solid #004D00 !important; 
        border-radius: 8px !important;
        padding: 10px !important;
        color: #000000 !important; 
        background-color: #FFFFFF !important;
        box-shadow: none !important;
    }
    .stButton button {
        background-color: #E2725B !important; 
        color: #FFFFFF !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
    }

    /* --- CONTACT CARD FIX: Equal Height & No Overflow --- */
    .contact-card-container {
        display: flex;
        gap: 20px; 
        margin-bottom: 2rem;
    }
    .contact-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E2E2;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        flex: 1; 
        text-align: center;
        transition: transform 0.2s;
        display: flex; 
        flex-direction: column; 
        justify-content: space-between; 
        min-height: 220px; 
        overflow: hidden; 
    }
    .contact-detail {
        color: #004D00 !important; 
        font-size: 1.4em; 
        flex-grow: 1; 
        display: flex;
        align-items: center; 
        justify-content: center; 
        word-break: break-word; 
        white-space: normal; 
    }
    .contact-title {
        color: #E2725B !important; 
        font-weight: bold;
    }
    .footer {
        background-color: #EDE9D5;
        color: #004D00 !important;
        border-top: 2px solid #E2725B;
        padding: 1.5rem 0;
        margin-top: 4rem; 
    }
    /* Hide standard Streamlit divider */
    hr {
        display: none; 
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    # ---------------- I. ABOUT US INFORMATIONAL CONTENT ----------------
    
    # --- HERO / INTRO SECTION ---
    hero_col1, hero_col2 = st.columns([2, 1], gap="large")
    with hero_col1:
        st.markdown(
            """
            <div class="hero-wrapper">
                <div class="hero-tag">About StreetBase</div>
                <div class="title">Smarter <span class="highlight">Real Estate Decisions</span> with Data & AI</div>
                <div class="subtitle">
                    StreetBase is an AI-powered real estate evaluation system that helps buyers, sellers,
                    and advisors estimate fair property values, understand market trends, and make
                    sustainable housing choices with confidence.
                </div>
                <div class="subtitle">
                    Instead of relying only on guesswork or brokers, StreetBase combines location data,
                    property attributes, and machine learning to give you transparent, explainable insights.
                </div>
                <div class="hero-pills">
                    <span class="pill">🏙 City-level & locality insights</span>
                    <span class="pill">📈 AI-driven price predictions</span>
                    <span class="pill">🌿 Sustainability-aware recommendations</span>
                    <span class="pill">🔍 Transparent & explainable outputs</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with hero_col2:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-value">₹</div>
                <div class="metric-label">Price intelligence for properties based on multiple factors like location, area, amenities, and historical trends.</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">24×7</div>
                <div class="metric-label">Digital assistant to help you explore “What-if” scenarios and compare properties.</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">Sustainable</div>
                <div class="metric-label">Designed to nudge users towards greener, energy-efficient homes and better long-term investments.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # --- WHY STREETBASE SECTION ---
    st.markdown("<h2 class='section-title'>Why StreetBase?</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p class='section-subtitle'>
        Real estate decisions in India are often influenced by hearsay, outdated listings, or biased suggestions. 
        StreetBase aims to change that by putting data, transparency, and sustainability at the center of every decision.
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-row">
            <div class="info-card">
                <div class="info-badge">The Challenge</div>
                <h4>Unclear Pricing & Market Noise</h4>
                <p>
                    Property prices can vary wildly even within the same locality. Traditional methods rarely
                    account for micro-location, connectivity, quality of construction, and future growth potential.
                </p>
            </div>
            <div class="info-card">
                <div class="info-badge">Our Approach</div>
                <h4>Data-Driven Evaluations</h4>
                <p>
                    StreetBase uses machine learning models trained on historical patterns and engineered features
                    to predict realistic price ranges and highlight the key drivers behind them.
                </p>
            </div>
            <div class="info-card">
                <div class="info-badge">The Impact</div>
                <h4>Confident, Sustainable Choices</h4>
                <p>
                    Buyers, sellers, and agents get a common reference point, reducing information asymmetry and
                    promoting decisions that are financially sound and environmentally conscious.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- HOW STREETBASE WORKS SECTION ---
    st.markdown("<h2 class='section-title'>How StreetBase Works</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p class='section-subtitle'>From raw property details to actionable insights, StreetBase follows a clear and explainable pipeline.</p>",
        unsafe_allow_html=True,
    )

    work_col1, work_col2 = st.columns(2, gap="large")
    with work_col1:
        st.markdown(
            """
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-item-title">1. Collect Property Inputs</div>
                    <div class="timeline-item-text">
                        Users provide details like location, area (sq.ft), BHK, age of building, amenities,
                        and connectivity. These become the core features for our models.
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-item-title">2. Feature Engineering</div>
                    <div class="timeline-item-text">
                        We enrich the inputs with locality scores, proximity to key landmarks, and sustainability
                        indicators such as access to public transport or green spaces.
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-item-title">3. ML-Based Price Prediction</div>
                    <div class="timeline-item-text">
                        Using trained regression models, StreetBase generates an estimated price range and
                        confidence band for the property.
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-item-title">4. Insight & Recommendation Layer</div>
                    <div class="timeline-item-text">
                        The system highlights why a price is high or low and suggests actions such as negotiation
                        room, comparable localities, and more sustainable alternatives if available.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with work_col2:
        st.markdown(
            """
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-tag">Price Intelligence</div>
                    <h4>Fair Value Estimation</h4>
                    <p>
                        Predicts a realistic price range instead of a single static number, helping you see the
                        upper and lower bounds of negotiations.
                    </p>
                </div>
                <div class="feature-card">
                    <div class="feature-tag">Scenario Analysis</div>
                    <h4>What-If Comparisons</h4>
                    <p>
                        Compare different property configurations, locations, or budgets to understand trade-offs
                        before making a commitment.
                    </p>
                </div>
                <div class="feature-card">
                    <div class="feature-tag">Sustainability</div>
                    <h4>Green Home Indicators</h4>
                    <p>
                        Incorporates aspects like daylight, ventilation, and connectivity to public transport to
                        encourage more sustainable living.
                    </p>
                </div>
                <div class="feature-card">
                    <div class="feature-tag">User-Centric</div>
                    <h4>Explainable AI</h4>
                    <p>
                        Uses interpretable techniques to show which features influence the predicted price the most,
                        building trust with end users.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # --- FUTURE SCOPE SECTION ---
    st.markdown("<h2 class='section-title'>🚀 Future Scope</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p class='section-subtitle'>We're continuously innovating to bring you even more powerful insights and features:</p>
        <ul>
            <li>🌍 **Live Real Estate API Integration** – Connect to real-time listings and transaction data from various platforms for up-to-the-minute market analysis.</li>  
            <li>☁️ **Cloud Deployment (AWS / GCP)** – Develop scalable infrastructure for city-level and pan-India property evaluations, ensuring high availability and performance.</li>  
            <li>🧠 **Explainable AI (SHAP, LIME)** – Implement advanced interpretability techniques to provide deeper, more understandable explanations for our AI's price predictions to end-users and partners.</li>  
            <li>📊 **Interactive Analytics Dashboard** – Design and launch a comprehensive dashboard for visualizing trends across cities, localities, and property types, empowering detailed market research.</li>  
            <li>🤖 **Integrated Chatbot Assistant** – Introduce an AI-powered chatbot to offer guided exploration for first-time buyers and investors, answering queries and providing personalized recommendations.</li>  
        </ul>
        """,
        unsafe_allow_html=True,
    )


    # ====================================================================
    # ---------------- II. FEEDBACK / CONTACT CONTENT ----------------
    # ====================================================================

    st.markdown("<div id='contact_section'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>📬 Submit Feedback or Get In Touch</h2>", unsafe_allow_html=True)
    st.markdown(
        "### We value your input! Use the form below to submit **feedback**, **report an issue**, or **get in touch**."
    )

    with st.form(key='feedback_form', clear_on_submit=False): 
        
        # 1. Inquiry Type Selector (Vertical Stack)
        query_type = st.selectbox(
            label="Reason for Contact*", 
            options=["Select a Reason", "General Inquiry", "Technical Support", "Partnership/Media", "Feedback/Suggestion"],
            key="query_selector"
        )

        # Form Layout (Vertical Stack)
        name = st.text_input(label="Your Name*", placeholder="Enter your full name", key="form_name")
        email = st.text_input(label="Your Email Address*", placeholder="e.g., streetbase@example.com", key="form_email")
        
        subject = st.text_input(label="Subject (Optional)", placeholder="What is your feedback or query about?", key="form_subject")
        message = st.text_area(label="Your Message/Feedback*", placeholder="Type your message here...", height=150, key="form_message")
        
        # Checkbox for privacy consent
        privacy_consent = st.checkbox(
            "I confirm that I have read and agree to the StreetBase Privacy Policy.", 
            value=False, 
            key="consent_check"
        )
        
        submit_button = st.form_submit_button(label='🚀 Send Feedback / Message')

    # ---------------- DIRECT CONTACT & MAP SECTION (Always Renders) ----------------
    
    st.markdown("<h2 class='section-title'>📞 Direct Contact Information</h2>", unsafe_allow_html=True)

    # --- CONTACT CARD: Three separate, equal-sized boxes ---
    st.markdown('<div class="contact-card-container">', unsafe_allow_html=True)
    
    # Define contact data with explicit HTML structure for flex control
    contact_data_html = [
        f"""
        <div class="contact-card">
            <div class="contact-title">📱 Call Us</div>
            <a href="tel:6264543645" style="text-decoration: none;">
                <div class="contact-detail">6264543645</div>
            </a>
            <div class="contact-hours">Available Mon-Fri, 9am - 5pm IST</div>
        </div>
        """,
        f"""
        <div class="contact-card">
            <div class="contact-title">📩 Support Email</div>
            <a href="mailto:contact_streetbase@gmail.com" style="text-decoration: none;">
                <div class="contact-detail">contact_streetbase@gmail.com</div>
            </a>
            <div class="contact-hours">We aim to reply within 24 hours</div>
        </div>
        """,
        f"""
        <div class="contact-card">
            <div class="contact-title">📍 Visit Our Office</div>
            <a href="https://maps.google.com/maps?q=Origin+Towers,+Hi-Tech+City,+Hyderabad,+Telangana&t=&z=15&ie=UTF8&iwloc=&output=embed2" target="_blank" style="text-decoration: none;">
                <div class="contact-detail">Titus Towers, Building No, 12, IT Park, Building Number, 10, Hitech City Rd, Madhapur, Hyderabad, Telangana 500081</div>
            </a>
            <div class="contact-hours">Office Hours: Mon-Fri, 9am - 6pm</div>
        </div>
        """
    ]

    # Use columns to render the custom HTML
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(contact_data_html[0], unsafe_allow_html=True)
    with col2:
        st.markdown(contact_data_html[1], unsafe_allow_html=True)
    with col3:
        st.markdown(contact_data_html[2], unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True) # Close the container

    # --- EMBEDDED MAP SECTION ---
    st.markdown("<h2 class='section-title'>🗺️ Find Our Location</h2>", unsafe_allow_html=True)
    st.markdown("<p class='section-subtitle'>View our office location and get directions directly on the map below.</p>", unsafe_allow_html=True)

    # ADDRESS FOR MAP EMBED
    address_query = "Titus Towers, Building No 12, IT Park, Hitech City Rd, Madhapur, Hyderabad, Telangana 500081"
    map_embed_url = f"https://maps.google.com/maps?q=Origin+Towers,+Hi-Tech+City,+Hyderabad,+Telangana&t=&z=15&ie=UTF8&iwloc=&output=embed3{address_query}&t=m&z=15&ie=UTF8&iwloc=&output=embed"

    st.markdown(
        f"""
        <iframe 
            width="100%" 
            height="450" 
            frameborder="0" 
            scrolling="no" 
            marginheight="0" 
            marginwidth="0" 
            src="{map_embed_url}"
            allowfullscreen
            style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);"
        >
        </iframe>
        <div style="font-size: 0.8em; text-align: right; margin-top: 5px;">
            <a href="https://maps.google.com/maps?q=Origin+Towers,+Hi-Tech+City,+Hyderabad,+Telangana&t=&z=15&ie=UTF8&iwloc=&output=embed4{address_query}" target="_blank">Open in Google Maps</a>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # ---------------- CONNECT WITH US ----------------
    st.markdown("<h2 class='section-title'>🌐 Connect With Us</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p class='section-subtitle'>
        Have ideas, data sources, or want to collaborate with StreetBase for your city or organization?
        Reach out and let's build smarter housing ecosystems together.
        </p>
        """,
        unsafe_allow_html=True,
    )

    col_contact, col_qr = st.columns([2, 1])
    with col_contact:
        st.write("📧 **Email:** streetbase5@gmail.com")
        st.write("🌍 **Website:** www.streetbase.ai")
        st.write(
            "📂 **Project Repo / Demo:** Scan the QR code to explore the codebase or live demo (if hosted)."
        )

    with col_qr:
        try:
            qr = qrcode.make("https://github.com/your-project-repo")
            buf = io.BytesIO()
            qr.save(buf, format="PNG")
            st.image(buf.getvalue(), width=130)
        except Exception:
<<<<<<< HEAD
            st.write("QR Code could not be generated")
            
    chatbot_popup()  # 👈 this will render the StreetBase chat section here

    # ---------------- FOOTER ----------------
    st.markdown("""
        <div class='footer'>
            © 2025 <b>StreetBase</b> | All Rights Reserved <br>
            Built with ❤️ using <a href='https://streamlit.io/' target='_blank'>Streamlit</a> and AI
        </div>
    """, unsafe_allow_html=True)
=======
            st.write("QR Code could not be generated (Ensure qrcode[pil] is installed)")


    # ---------------- FOOTER (Centered) ----------------
    st.markdown(
        """
        <div class="footer">
            <div style="text-align: center;">
                <b>StreetBase</b> © 2025 — Real Estate Intelligence for Smarter, Sustainable Cities
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # --- FINAL SUBMISSION HANDLER EXECUTION ---
    if submit_button:
        # Check current values of the form fields
        current_name = st.session_state.get("form_name", "")
        current_email = st.session_state.get("form_email", "")
        current_message = st.session_state.get("form_message", "")
        current_query_type = st.session_state.get("query_selector", "Select a Reason")
>>>>>>> 2726ff23d980c3cd8e735884dfae65e59eb16a71

        # --- VALIDATIONS (Category, Fields, Consent) ---
        if current_query_type == "Select a Reason":
            st.error("⚠️ Please select a valid **Reason for Contact**.")
        elif not current_name or not current_email or not current_message:
            st.error("🚨 Please fill in your Name, Email, and Message before submitting.")
        elif "@" not in current_email:
            st.error("❌ Please enter a valid Email address.")
        elif not st.session_state.get("consent_check"):
            st.error("🛑 Please agree to the Privacy Policy before submitting.")
        else:
            # --- SUCCESS ACTION (ONLY the success message remains) ---
            st.success(f"✅ Thank you, **{current_name}**! Your **{current_query_type}** has been submitted.")
            # The post-submission rating/feedback section has been removed below.
            
# --- EXECUTION BLOCK (Guaranteed to load) ---
load_single_page()
