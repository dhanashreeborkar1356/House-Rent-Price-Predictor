"""
RentWise AI — Smart House Rent Predictor
A modern, responsive, frontend-only real estate valuation and exploration platform built with Streamlit.
"""

import streamlit as st
import os
from views.dashboard import render_dashboard
from views.estimator import render_estimator
from views.neighborhood import render_neighborhood_explorer
from views.insights import render_market_insights
from views.about import render_about


def load_custom_css():
    """Loads and injects the custom stylesheet."""
    css_path = os.path.join(os.path.dirname(__file__), "style", "custom.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            custom_css = f.read()
        st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)


def main():
    # 1. Page Configuration
    st.set_page_config(
        page_title="RentWise AI — Smart House Rent Predictor",
        page_icon="🏠",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # 2. Inject Custom CSS
    load_custom_css()

    # 3. Sidebar Branding & Navigation
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-brand-box">
                <div class="brand-title">
                    <span style="font-size: 1.6rem;">🏙️</span> RentWise <span>AI</span>
                </div>
                <div class="brand-tagline">“Find your perfect rent with confidence.”</div>
                <div class="sidebar-badge">v1.0 • Frontend Prototype</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<p style='font-size: 0.78rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 8px;'>Navigation</p>", unsafe_allow_html=True)
        
        nav_selection = st.radio(
            label="Main Navigation",
            options=[
                "🏠 Dashboard",
                "💰 Rent Estimator",
                "📍 Neighborhood Explorer",
                "📊 Market Insights",
                "ℹ️ About Project"
            ],
            index=0,
            label_visibility="collapsed"
        )

        st.markdown("<div style='height: 35px;'></div>", unsafe_allow_html=True)

        # Quick Helper Widget in Sidebar
        st.markdown(
            """
            <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 14px 16px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                    <span style="font-size: 1.1rem;">💡</span>
                    <strong style="color: #5EEAD4; font-size: 0.85rem;">Did You Know?</strong>
                </div>
                <p style="font-size: 0.78rem; color: #CBD5E1; margin: 0; line-height: 1.45;">
                    Properties within 1 km of major metro stations in Bangalore and Mumbai command up to a 14% rental premium.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

        # Bottom Sidebar Metadata
        st.markdown(
            """
            <div style="border-top: 1px solid #1E293B; padding-top: 14px; font-size: 0.72rem; color: #64748B; text-align: center;">
                Built with <strong>Streamlit & Python</strong><br/>
                Modern Real Estate Analytics UI
            </div>
            """,
            unsafe_allow_html=True
        )

    # 4. View Router
    if "Dashboard" in nav_selection:
        render_dashboard()
    elif "Rent Estimator" in nav_selection:
        render_estimator()
    elif "Neighborhood Explorer" in nav_selection:
        render_neighborhood_explorer()
    elif "Market Insights" in nav_selection:
        render_market_insights()
    elif "About Project" in nav_selection:
        render_about()


if __name__ == "__main__":
    main()
