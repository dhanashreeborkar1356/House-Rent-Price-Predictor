# RentWise AI — Smart House Rent Predictor

> *“Find your perfect rent with confidence.”*

A modern, responsive, and aesthetically polished frontend web application for real-estate valuation and neighborhood analytics built using **Streamlit**, **Plotly**, and **Python**.

Designed specifically for academic demonstrations, capstone projects, and machine learning portfolio showcases.

---

## 🌟 Key Highlights & Design Aesthetic

- **Color Palette:** Clean white and light-grey background (`#F8FAFC`, `#FFFFFF`) accented with deep navy-blue (`#0F172A`, `#1E293B`) and teal (`#0D9488`, `#14B8A6`, `#5EEAD4`).
- **Modern UI Elements:** Elevated metric cards, high-resolution architectural photography, custom pill badges, subtle shadows, and smooth hover animations.
- **Responsive Layout:** Optimized across desktop, laptop, tablet, and mobile browsers.
- **Frontend Demonstration Architecture:** Fully interactive client-side simulation with instant filtering, sorting, interactive charts, and heuristic valuation without needing heavy backend or external database dependencies.

---

## 🧭 Pages & Features Overview

### 1. 🏠 Dashboard
- **Welcome Hero Banner:** *"Find the Right Rent for Your Next Home"* with executive overview.
- **Four Key Metric Cards:**
  - *Average Monthly Rent* (`₹38,400 / mo`)
  - *Properties Listed* (`4,850+ Active Homes`)
  - *Top Neighborhood* (`Koramangala, Bangalore`)
  - *Estimated Rent Range* (`₹18k – ₹1.4L`)
- **Quick Rent Search:** Instant filtering across metro cities, property configurations, and budget thresholds.
- **Featured Property Cards:** Curated apartment and villa cards displaying BHK, bathrooms, super built-up area, furnishing, and pricing.
- **Market Rent Distribution Chart:** Interactive Plotly distribution chart illustrating listing frequencies across price brackets.

### 2. 💰 Rent Estimator
- **Multi-Factor Valuation Form:**
  - **Location:** Metro city (Mumbai, Bangalore, Pune, Delhi NCR, Hyderabad) and dynamic locality selector.
  - **Property Type:** Apartment, Independent House, Studio, Villa / Penthouse.
  - **Dimensions & Configuration:** Bedrooms (BHK), Bathrooms, Super Built-up Area (350 to 4,500 sq.ft slider), Floor elevation (Ground to 50th floor), and Property Age.
  - **Parking & Amenities:** Reserved parking options, Lift, Gym, 24/7 Security, Balcony, Air Conditioning, Power Backup, Clubhouse, etc.
- **Interactive Feedback:** Visual loading feedback (`st.spinner`) simulating model inference.
- **Comprehensive Valuation Card:**
  - Sample monthly rent quote in Indian Rupees (`₹36,500 / month`).
  - Minimum–Maximum fair market tolerance band (`₹33,500 – ₹39,500`).
  - Rate per square foot calculation.
  - Itemized breakdown: Base space value, Furnishing differential, Amenities & parking value, and Model Confidence Indicator.

### 3. 📍 Neighborhood Explorer
- **Multi-Dimensional Filters:**
  - City dropdown and locality/keyword text search.
  - Property type selector and BHK configuration filters.
  - Interactive dual-handle Monthly Rent Budget slider (`₹15,000` to `₹1,00,000+`).
  - Dynamic sort controls: *Popularity & Rating*, *Rent: Lowest First*, *Rent: Highest First*, *Area: Largest First*.
- **Live Inventory Counter & Average Rent Metric:** Instant feedback on the number of matching homes and the average rent of filtered results.
- **3-Column Property Grid:** Responsive card layout with locality tags, rating chips, specifications, and descriptions.
- **Empty State Handler:** Helpful empty state with recovery advice when no properties match strict filter criteria.

### 4. 📊 Market Insights
- **Key Trend Indicators:** Highest-rent city, fastest-growing corridor, furnishing premium percentage, and average leasing velocity.
- **12-Month Rental Price Index:** Multi-line spline chart tracking Bangalore, Mumbai, Delhi NCR, Pune, and Hyderabad from Nov 2023 to Oct 2024.
- **Average Rent by Neighborhood:** Horizontal gradient bar chart comparing prime localities.
- **Property Type & Configuration Comparison:** Grouped bar chart illustrating rent scaling across BHK tiers.
- **Furnished vs. Unfurnished Dynamics:** Donut chart illustrating listing shares alongside average rent and turnover metrics.
- **Bedroom-Wise Rent Distribution:** Statistical box plot highlighting median values, interquartile ranges, and outlier distributions.

### 5. ℹ️ About Project
- **Project Mission & Academic Context:** Background on rental opacity and automated valuation models.
- **Three-Step Workflow:**
  1. *Enter Property Details* $\rightarrow$ 2. *Analyze Features* $\rightarrow$ 3. *Estimate Rent*.
- **Planned Technology Stack:** Python, Pandas & NumPy, XGBoost Regressor, and Streamlit.
- **Feature Importance Hierarchy:** Relative feature weighting planned for supervised machine learning pipelines (Locality, Area, BHK, Furnishing, Amenities, Elevation).
- **Prototype Notice:** Prominent disclaimer highlighting that all values are demonstration figures.

---

## 📁 Repository Structure

```
HouseRent/
├── app.py                      # Main application entry point & router
├── requirements.txt            # Python dependencies (Streamlit, Plotly, Pandas, NumPy)
├── README.md                   # Complete documentation & project guide
├── style/
│   └── custom.css              # Custom CSS design system (Navy/Teal theme, cards, animations)
├── data/
│   └── mock_data.py            # Real estate dataset, market indices, and heuristic estimator
├── views/
│   ├── __init__.py
│   ├── dashboard.py            # Dashboard view with KPI cards & distribution
│   ├── estimator.py            # Valuation estimator view with multi-factor form
│   ├── neighborhood.py         # Neighborhood exploration view with filters & sorting
│   ├── insights.py             # Market insights with 5 Plotly charts
│   └── about.py                # About page with ML architecture & workflow
└── components/
    ├── __init__.py
    └── cards.py                # Reusable HTML card renderers, banners & disclaimers
```

---

## 🚀 How to Run Locally

### 1. Prerequisites
Ensure you have **Python 3.9+** installed on your system.

### 2. Clone or Navigate to the Project Folder
```bash
cd /Users/netraborkar/Downloads/HouseRent
```

### 3. (Optional) Create and Activate a Virtual Environment
```bash
python3 -m venv venv

# On macOS / Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Launch the Streamlit App
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## ⚠️ Important Prototype Disclaimer
This project is an **interactive frontend prototype**. All rental price estimates, market metrics, trends, and property listings are simulated demonstration figures designed for interface presentation and portfolio evaluation. No real machine learning model is trained, loaded, or executed in this phase, and no backend or database is connected.
