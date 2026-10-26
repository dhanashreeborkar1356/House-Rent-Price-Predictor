"""
Neighborhood Explorer View — RentWise AI
Interactive exploration interface with city/locality filters, property types,
budget range slider, sorting options, and dynamic property card grid.
"""

import streamlit as st
from data.mock_data import (
    CITIES_LOCALITIES,
    PROPERTY_TYPES,
    PROPERTIES_CATALOG
)
from components.cards import (
    render_hero_banner,
    render_property_card,
    render_disclaimer
)


def render_neighborhood_explorer():
    render_hero_banner(
        title_prefix="Discover High-Demand",
        title_highlight="Neighborhoods",
        subtitle="Explore vibrant residential hubs, compare micro-market rental yields, and filter listings by locality perks, bedroom configuration, and lifestyle amenities.",
        badge_text="Neighborhood Intelligence"
    )

    # 1. Filter Panel Box
    with st.container():
        st.markdown(
            """
            <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 18px; padding: 22px 24px 8px 24px; margin-bottom: 24px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03);">
            """,
            unsafe_allow_html=True
        )

        f_row1_c1, f_row1_c2, f_row1_c3 = st.columns([1.2, 1.2, 1.6])
        with f_row1_c1:
            city_filter = st.selectbox(
                "Filter Metro City",
                options=["All Cities"] + list(CITIES_LOCALITIES.keys()),
                index=0,
                key="explore_city"
            )
        with f_row1_c2:
            type_filter = st.selectbox(
                "Property Type",
                options=["All Types"] + PROPERTY_TYPES,
                index=0,
                key="explore_type"
            )
        with f_row1_c3:
            search_query = st.text_input(
                "Search Locality or Keyword",
                placeholder="e.g. Koramangala, Metro, Powai, Balcony...",
                key="explore_search"
            )

        f_row2_c1, f_row2_c2, f_row2_c3 = st.columns([1.2, 1.5, 1.3])
        with f_row2_c1:
            bhk_filter = st.selectbox(
                "Bedrooms (BHK)",
                options=["Any BHK", "1 BHK", "2 BHK", "3 BHK", "4+ BHK"],
                index=0,
                key="explore_bhk"
            )
        with f_row2_c2:
            budget_range = st.slider(
                "Monthly Rent Budget (₹)",
                min_value=15000,
                max_value=100000,
                value=(15000, 90000),
                step=5000,
                format="₹%d",
                key="explore_budget"
            )
        with f_row2_c3:
            sort_by = st.selectbox(
                "Sort Listings By",
                options=[
                    "Popularity & Rating",
                    "Rent: Lowest First",
                    "Rent: Highest First",
                    "Area: Largest First"
                ],
                index=0,
                key="explore_sort"
            )

        st.markdown("</div>", unsafe_allow_html=True)

    # 2. Filtering Logic
    filtered = PROPERTIES_CATALOG.copy()

    # City
    if city_filter != "All Cities":
        filtered = [p for p in filtered if p["city"] == city_filter]

    # Property Type
    if type_filter != "All Types":
        filtered = [p for p in filtered if p["property_type"] == type_filter]

    # BHK
    if bhk_filter != "Any BHK":
        bhk_num = int(bhk_filter.split()[0].replace("+", ""))
        if "+" in bhk_filter:
            filtered = [p for p in filtered if p["bhk"] >= bhk_num]
        else:
            filtered = [p for p in filtered if p["bhk"] == bhk_num]

    # Budget range
    min_b, max_b = budget_range
    filtered = [p for p in filtered if min_b <= p["rent"] <= max_b]

    # Search keyword
    if search_query.strip():
        q = search_query.strip().lower()
        filtered = [
            p for p in filtered
            if q in p["locality"].lower()
            or q in p["title"].lower()
            or q in p["description"].lower()
            or q in p.get("tag", "").lower()
            or any(q in a.lower() for a in p.get("amenities", []))
        ]

    # Sorting
    if sort_by == "Rent: Lowest First":
        filtered = sorted(filtered, key=lambda x: x["rent"])
    elif sort_by == "Rent: Highest First":
        filtered = sorted(filtered, key=lambda x: x["rent"], reverse=True)
    elif sort_by == "Area: Largest First":
        filtered = sorted(filtered, key=lambda x: x["area_sqft"], reverse=True)
    else:  # Popularity & Rating
        filtered = sorted(filtered, key=lambda x: x["rating"], reverse=True)

    # 3. Micro Summary Bar
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    
    avg_rent_current = int(sum(p["rent"] for p in filtered) / len(filtered)) if filtered else 0
    
    col_count, col_metric = st.columns([1.5, 1.5])
    with col_count:
        st.markdown(
            f"#### 🏘️ Listings Found: <span style='color: #0D9488;'>{len(filtered)}</span>",
            unsafe_allow_html=True
        )
    with col_metric:
        if filtered:
            st.markdown(
                f"<div style='text-align: right; color: #64748B; font-size: 0.9rem; padding-top: 4px;'>"
                f"Filtered Average Rent: <strong style='color: #0F172A;'>₹{avg_rent_current:,}/mo</strong>"
                f"</div>",
                unsafe_allow_html=True
            )

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    # 4. Property Grid Display
    if filtered:
        # Render cards in 3-column rows
        for i in range(0, len(filtered), 3):
            row_items = filtered[i:i+3]
            cols = st.columns(3)
            for j, prop in enumerate(row_items):
                with cols[j]:
                    render_property_card(prop)
    else:
        # Empty State
        st.markdown(
            """
            <div style="background: #FFFFFF; border: 2px dashed #CBD5E1; border-radius: 18px; padding: 48px 24px; text-align: center; margin: 20px 0;">
                <div style="font-size: 3rem; margin-bottom: 12px;">🏡</div>
                <h3 style="color: #0F172A; margin-bottom: 8px;">No Listings Match Your Selected Filters</h3>
                <p style="color: #64748B; font-size: 0.92rem; max-width: 440px; margin: 0 auto 20px auto;">
                    We couldn't find any rental properties within your selected criteria. Try broadening your monthly budget or clearing specific keyword filters.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 5. Disclaimer
    render_disclaimer()
