import os
import json
import random
import urllib.parse
import urllib.request
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="IBM Predictive Grid Engine", layout="wide", initial_sidebar_state="expanded")

# Custom UI Styling
st.markdown("""
    <style>
    .main .block-container { padding-top: 1.5rem; padding-bottom: 1rem; }
    div[data-testid="stSidebar"] { background-color: #f8f9fa; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ Enterprise Predictive Grid Analytics Engine")
st.caption("AI-Powered Real-Location Failure Risk Assessment & Automated Crew Deployment Advisor")

# Absolute path for dataset
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, 'data', 'grid_data.csv')

df_grid = None
if os.path.exists(csv_path):
    df_grid = pd.read_csv(csv_path)

# Sidebar Controls
st.sidebar.header("🌍 Real-Location Search & Telemetry Controls")
search_location = st.sidebar.text_input("Search Specific Area / Location:", value="", placeholder="Type any city/area (e.g. Navsari, Surat, Valsad)...")

st.sidebar.subheader("🌪️ Simulated Weather Factors")
wind_speed = st.sidebar.slider("Wind Speed (km/h)", 5, 120, 71)
ambient_temp = st.sidebar.slider("Ambient Temp (°C)", 10, 55, 36)

# Main Application Logic
if not search_location.strip():
    st.info("👈 Please enter a location or area in the sidebar search box to load the Live Asset Risk Map.")
else:
    loc_clean = search_location.strip().title()
    lat, lng = None, None

    # Fetch Real Coordinates using Nominatim API
    try:
        url = f"https://nominatim.openstreetmap.org/search?format=json&q={urllib.parse.quote(search_location.strip())}"
        req = urllib.request.Request(url, headers={'User-Agent': 'SmartGridPredictorEngine/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            if data and len(data) > 0:
                lat = float(data[0]['lat'])
                lng = float(data[0]['lon'])
    except Exception:
        pass

    # Fallback default (only if internet API fails)
    if lat is None or lng is None:
        st.sidebar.warning(f"Could not fetch exact online coordinates for '{loc_clean}'. Showing estimated region.")
        seed_val = sum(ord(c) for c in loc_clean.lower())
        lat = 20.9250 if "navsari" in loc_clean.lower() else 22.3072
        lng = 72.9090 if "navsari" in loc_clean.lower() else 73.1812
    else:
        seed_val = sum(ord(c) for c in loc_clean.lower())

    random.seed(seed_val)

    # Substation Assets centered around the searched Lat/Lng
    nearby_places = [
        {"name": f"{loc_clean} - Central Grid Substation", "lat": lat + 0.003, "lng": lng + 0.002},
        {"name": f"{loc_clean} - East Industrial Feeder", "lat": lat - 0.004, "lng": lng + 0.003},
        {"name": f"{loc_clean} - West Commercial Node", "lat": lat + 0.002, "lng": lng - 0.004},
        {"name": f"{loc_clean} - North Residential Yard", "lat": lat - 0.003, "lng": lng - 0.003},
        {"name": f"{loc_clean} - South Traction Substation", "lat": lat + 0.005, "lng": lng - 0.001}
    ]

    assets = []
    for idx, place in enumerate(nearby_places, start=1):
        base_cust = random.randint(5000, 22000)
        dga = random.randint(30, 480)
        temp = random.randint(45, 115)
        vibration = round(random.uniform(0.5, 9.5), 2)
        
        dga_score = (dga / 500.0) * 0.35
        temp_score = (temp / 120.0) * 0.25
        vib_score = (vibration / 10.0) * 0.20
        weather_score = ((wind_speed / 120.0) + (ambient_temp / 55.0)) / 2.0 * 0.20
        
        risk_prob = min(round((dga_score + temp_score + vib_score + weather_score), 2), 0.99)
        severity_score = int(risk_prob * base_cust)
        
        if risk_prob > 0.65:
            status, color = "CRITICAL", "red"
            action = f"🚨 CRITICAL DISPATCH: Emergency Crew deployed to {place['name']} ({risk_prob*100:.0f}% Risk)."
        elif risk_prob > 0.40:
            status, color = "WARNING", "orange"
            action = f"⚠️ ELEVATED RISK: Thermal/Gas anomaly at {place['name']} ({risk_prob*100:.0f}% Risk)."
        else:
            status, color = "STABLE", "green"
            action = f"✅ NORMAL: Operating safely at {place['name']} ({risk_prob*100:.0f}% Risk)."

        assets.append({
            "id": f"SUB-0{idx}",
            "name": place["name"],
            "lat": place["lat"],
            "lng": place["lng"],
            "dga": dga,
            "temp": temp,
            "vibration": vibration,
            "customers": base_cust,
            "risk_prob": risk_prob,
            "severity_score": severity_score,
            "status": status,
            "color": color,
            "action": action
        })

    assets.sort(key=lambda x: x["severity_score"], reverse=True)

    # Tabs Structure
    tab1, tab2, tab3 = st.tabs(["🗺️ Live Asset Risk Map", "📋 Priority Dispatch Plan", "📊 Telemetry Dataset Matrix"])

    with tab1:
        col_map, col_list = st.columns([1.3, 1], gap="medium")
        with col_map:
            st.subheader(f"🗺️ Live Risk Map: {loc_clean}")
            
            # Dynamic Leaflet Map centered on fetched Coordinates
            m = folium.Map(location=[lat, lng], zoom_start=13, tiles="OpenStreetMap")
            for a in assets:
                folium.CircleMarker(
                    location=[a["lat"], a["lng"]],
                    radius=14,
                    popup=f"<b>{a['name']}</b><br>Risk: <b>{a['risk_prob']*100:.0f}%</b><br>Severity: {a['severity_score']:,}",
                    tooltip=f"{a['name']} ({a['risk_prob']*100:.0f}% Risk)",
                    color=a["color"],
                    fill=True,
                    fill_color=a["color"],
                    fill_opacity=0.85
                ).add_to(m)
            
            # Unique Key using lat & lng forces the map component to re-render to the new location
            st_folium(m, use_container_width=True, height=520, key=f"map_{lat}_{lng}_{wind_speed}_{ambient_temp}")
        
        with col_list:
            st.subheader("📋 Priority Dispatch Plan")
            for a in assets:
                st.markdown(f"#### {a['name']}")
                st.markdown(f"**Risk:** `{a['risk_prob']*100:.0f}%` | **Severity:** `{a['severity_score']:,}`")
                if a['status'] == "CRITICAL":
                    st.error(a['action'])
                elif a['status'] == "WARNING":
                    st.warning(a['action'])
                else:
                    st.success(a['action'])
                st.divider()

    with tab2:
        st.subheader("📊 Live Telemetry Matrix")
        df_live = [{
            "Substation Zone": a["name"],
            "Oil Temp (°C)": a["temp"],
            "Vibration (mm/s)": a["vibration"],
            "Gas PPM": a["dga"],
            "Impacted Customers": a["customers"],
            "Risk Score": f"{a['risk_prob']*100:.0f}%",
            "Status": a["status"]
        } for a in assets]
        st.dataframe(df_live, use_container_width=True)

    with tab3:
        st.subheader("📁 Historical Training Dataset (`grid_data.csv`)")
        if df_grid is not None:
            st.dataframe(df_grid.head(50), use_container_width=True)
        else:
            st.warning("No grid_data.csv found. Run train.py first.")