"""
Reusable UI component helpers for RentWise AI.
Renders polished HTML cards, badges, and banners with safety against injection.
"""

import streamlit as st
from typing import Dict, Any, Optional


def render_hero_banner(
    title_prefix: str,
    title_highlight: str,
    subtitle: str,
    badge_text: str = "AI-Powered Real Estate Analytics"
) -> None:
    """Renders a modern navy-and-teal hero header banner."""
    html_code = f"""
    <div class="hero-banner">
        <div class="hero-tag">
            <span>✨</span> {badge_text}
        </div>
        <h1 class="hero-title">{title_prefix} <span>{title_highlight}</span></h1>
        <p class="hero-subtitle">{subtitle}</p>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)


def render_stat_card(
    title: str,
    value: str,
    subtitle: str,
    icon: str,
    badge_text: Optional[str] = None
) -> None:
    """Renders an interactive KPI metric card."""
    badge_html = f'<span class="stat-badge-positive">{badge_text}</span>' if badge_text else ''
    html_code = f"""
    <div class="stat-card">
        <div>
            <div class="stat-header">
                <span class="stat-title">{title}</span>
                <div class="stat-icon">{icon}</div>
            </div>
            <div class="stat-value">{value}</div>
        </div>
        <div class="stat-footer">
            {badge_html}
            <span>{subtitle}</span>
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)


def render_property_card(prop: Dict[str, Any]) -> None:
    """Renders a responsive property card with badges, specifications, and pricing."""
    amenities_chips = "".join([f'<span class="spec-chip">✓ {a}</span>' for a in prop.get("amenities", [])[:3]])
    
    html_code = f"""
    <div class="property-card">
        <div class="property-image-box">
            <img class="property-image" src="{prop['image']}" alt="{prop['title']}" loading="lazy" />
            <div class="property-floating-badge">{prop.get('badge', 'Featured')}</div>
            <div class="property-floating-city">📍 {prop['city']}</div>
        </div>
        <div class="property-content">
            <div class="property-loc">{prop['locality']} • {prop['property_type']}</div>
            <div class="property-name">{prop['title']}</div>
            <p class="property-desc">{prop['description']}</p>
            <div class="property-specs-grid">
                <span class="spec-chip">🛏️ {prop['bhk']} BHK</span>
                <span class="spec-chip">🚿 {prop['bathrooms']} Bath</span>
                <span class="spec-chip">📐 {prop['area_sqft']} sq.ft</span>
                <span class="spec-chip">🛋️ {prop['furnishing']}</span>
                {amenities_chips}
            </div>
            <div class="property-footer-row">
                <div class="property-price-box">
                    <span class="price-label">Sample Monthly Rent</span>
                    <span class="price-amount">₹{prop['rent']:,}<span class="price-period">/mo</span></span>
                </div>
                <div style="font-size: 0.82rem; font-weight: 700; color: #0D9488; background: #F0FDFA; padding: 4px 10px; border-radius: 8px; border: 1px solid #CCFBF1;">
                    ★ {prop.get('rating', 4.8)} ({prop.get('reviews_count', 24)})
                </div>
            </div>
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)


def render_disclaimer(custom_text: Optional[str] = None) -> None:
    """Renders standard UI disclaimer noting mock frontend demonstration status."""
    text = custom_text or (
        "<strong>Prototype Demonstration:</strong> All rental price estimates, market metrics, and property cards "
        "are simulated sample frontend data designed for UI evaluation. No actual predictive ML model or real estate backend is linked."
    )
    html_code = f"""
    <div class="disclaimer-box">
        <span style="font-size: 1.25rem;">ℹ️</span>
        <div>{text}</div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)
