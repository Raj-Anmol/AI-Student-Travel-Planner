import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests
import json
import folium
from streamlit_folium import st_folium
from streamlit.runtime import get_script_run_ctx

st.set_page_config(page_title="AI Student Travel Planner Pro", page_icon="🎒", layout="wide")

st.title("🎒 AI Student Travel Planner (Pro)")
st.write("Budget-first travel planning for students — instant breakdown, geospatial map, and group splitter.")

with st.sidebar:
    st.header("📋 Trip Inputs")
    destination = st.text_input("Kahan jana chahte ho?", value="Goa")
    total_budget = st.number_input("Total Budget (INR):", min_value=1000, value=5000, step=500)
    days = st.slider("Kitne dino ka trip hai?", min_value=1, max_value=7, value=3)
    group_size = st.number_input("Group Size (friends):", min_value=1, max_value=8, value=1, step=1)
    
    st.markdown("---")
    st.header("🏨 Hotel Preferences")
    hotel_type = st.selectbox("Hotel type", ["Budget Guesthouse", "Mid-range Hotel", "Premium Resort"])
    hotel_rating = st.slider("Minimum rating", 1, 5, 3)
    st.markdown("---")
    st.header("🎯 Travel Style")
    interests = st.multiselect("Interests", ["Sightseeing", "Beach", "Food Hunting", "Nightlife", "Adventure", "Culture"], default=["Food Hunting"])

# ---- LLM Simulation with Structured JSON Output ----
def generate_trip_plan(destination, total_budget, days, group_size):
    """Generate trip plan returning structured JSON from LLM simulation."""
    # Simulated LLM response - in production, this would call an actual LLM API
    # The key point: returns valid JSON, not raw markdown
    stays = {"Budget Guesthouse": 20, "Mid-range Hotel": 35, "Premium Resort": 50}
    hotel_pct = stays[hotel_type] / 100
    
    # Budget split per person
    per_person_budget = total_budget / group_size
    stay_split = int(per_person_budget * 0.35)
    food_split = int(per_person_budget * 0.30)
    transport_split = int(per_person_budget * 0.20)
    buffer_split = int(per_person_budget * 0.15)
    
    # Itinerary spots with coordinates
    places_by_destination = {
        "Goa": [
            {"name": "Baga Beach", "lat": 15.5097, "lon": 73.9257, "cost": 800, "hack": "Free sunset access"},
            {"name": "Calangute Beach", "lat": 15.5712, "lon": 73.9241, "cost": 700, "hack": "Free public beach"},
            {"name": "Fort Aguada", "lat": 15.6274, "lon": 73.8760, "cost": 150, "hack": "Free entry, sunset view"},
            {"name": "Anjuna Flea Market", "lat": 15.5789, "lon": 73.9291, "cost": 500, "hack": "Bargain at closing time"},
            {"name": "Dudhsagar Falls", "lat": 15.3500, "lon": 74.7000, "cost": 1200, "hack": "Shared taxi splits cost"},
        ],
        "Manali": [
            {"name": "Rohtang Pass", "lat": 32.6200, "lon": 77.4700, "cost": 2000, "hack": "Overnight sleeper train to Manali"},
            {"name": "Solang Valley", "lat": 32.2367, "lon": 77.3320, "cost": 1500, "hack": "Free skiing viewpoints"},
            {"name": "Hadimba Temple", "lat": 32.2384, "lon": 77.1847, "cost": 200, "hack": "Free temple entry"},
            {"name": "Vashisht Temple", "lat": 32.2453, "lon": 77.1789, "cost": 300, "hack": "Hot water spring free"},
            {"name": "Old Manali", "lat": 32.2399, "lon": 77.1926, "cost": 1000, "hack": "Budget cafes, walk-in"},
        ],
        "Jaipur": [
            {"name": "Amber Fort", "lat": 26.9855, "lon": 75.8514, "cost": 1000, "hack": "Composite ticket includes entry"},
            {"name": "City Palace", "lat": 26.9208, "lon": 75.8562, "cost": 800, "hack": "Free entry with composite"},
            {"name": "Hawa Mahal", "lat": 27.0211, "lon": 75.8567, "cost": 500, "hack": "Free from outside"},
            {"name": "Jantar Mantar", "lat": 26.9126, "lon": 75.8239, "cost": 200, "hack": "Student discount"},
            {"name": "Nahargarh Fort", "lat": 26.9913, "lon": 75.8210, "cost": 800, "hack": "Sunset free entry"},
        ],
        "Default": [
            {"name": "Local Market", "lat": 28.6139, "lon": 77.2090, "cost": 600, "hack": "Haggle for better prices"},
            {"name": "City Center", "lat": 28.7041, "lon": 77.1025, "cost": 500, "hack": "Free walking tours"},
            {"name": "Main Square", "lat": 28.5726, "lon": 77.1025, "cost": 400, "hack": "Street food budget"},
            {"name": "Park", "lat": 28.5355, "lon": 77.2570, "cost": 300, "hack": "Free entry"},
            {"name": "Restaurant District", "lat": 28.6448, "lon": 77.2167, "cost": 700, "hack": "Lunch thalis"},
        ]
    }
    
    default_places = places_by_destination["Default"]
    day_places = places_by_destination.get(destination, default_places)
    
    # Build days array
    days_list = []
    for day in range(1, days + 1):
        # Select 3 places per day rotating through available spots
        selected = day_places[((day - 1) % len(day_places)):((day - 1) % len(day_places)) + 3]
        if len(selected) < 3:
            selected = day_places + default_places  # fallback
        selected = selected[:3]
        day_entry = {
            "day_number": day,
            "places": [
                {
                    "name": p["name"],
                    "latitude": p["lat"],
                    "longitude": p["lon"],
                    "estimated_cost_inr": p["cost"],
                    "student_hack": p["hack"]
                }
                for p in selected
            ]
        }
        days_list.append(day_entry)
    
    # Group saving tips
    tips = [
        "Book overnight sleeper trains to save accommodation cost for one night",
        "Look for composite tourist tickets - often 20-30% cheaper than individual entries",
        "Student ID cards get discounted entry at museums, forts, and cultural sites",
        "Eat at local thalis/tiffins instead of tourist restaurants - authentic and cheap",
        "Shared taxis/auto-rickshaws split costs among group members",
        "Free walking tours in most cities - tip what you can afford",
        "Stay in hostel dorms instead of private rooms for budget travel",
        "Book accommodation with kitchen access to prepare some meals"
    ]
    
    plan = {
        "destination": destination,
        "per_person_budget_split": {
            "stay": stay_split,
            "local_transport": transport_split,
            "food": food_split,
            "emergency_buffer": buffer_split
        },
        "days": days_list,
        "group_saving_tips": tips[:5]  # Return top 5 tips
    }
    
    return plan

# ---- Main App Logic ----
if st.button("Generate Smart Plan ✨", type="primary"):
    with st.spinner("🚌 Crafting your premium itinerary and charts..."):
        try:
            plan = generate_trip_plan(destination, total_budget, int(days), int(group_size))
        except Exception as e:
            st.error(f"Error generating plan: {str(e)}")
            plan = {
                "destination": destination,
                "per_person_budget_split": {"stay": 0, "local_transport": 0, "food": 0, "emergency_buffer": 0},
                "days": [],
                "group_saving_tips": ["Book trains early", "Use student discounts", "Shared transport"]
            }
    
    st.success("🎉 Aapka Fully Advanced Plan Ready Hai!")
    
    # ---- Summary Cards (Per-Person Budget) ----
    st.markdown("### 📊 Per-Person Budget Breakdown")
    split = plan.get("per_person_budget_split", {"stay": 0, "local_transport": 0, "food": 0, "emergency_buffer": 0})
    col_a, col_b, col_c, col_d = st.columns(4)
    with col_a:
        st.metric("Stay (per person)", f"₹{split['stay']:,.0f}")
    with col_b:
        st.metric("Food & Drinks (per person)", f"₹{split['food']:,.0f}")
    with col_c:
        st.metric("Local Transport (per person)", f"₹{split['local_transport']:,.0f}")
    with col_d:
        st.metric("Emergency/Buffer (per person)", f"₹{split['emergency_buffer']:,.0f}")
    
    # ---- Detailed Breakdown Table ----
    st.markdown("### 📊 Detailed Breakdown")
    chart_data = pd.DataFrame({
        "Expense Category": ["Stay", "Food & Drinks", "Local Transport", "Emergency/Buffer"],
        "Amount (₹) [per person]": [split['stay'], split['food'], split['local_transport'], split['emergency_buffer']]
    })
    st.dataframe(chart_data, use_container_width=True)
    
    # ---- Daily Budget Summary ----
    st.markdown("### 📅 Daily Budget Summary")
    st.info(f"**Destination:** {plan.get('destination', destination)}")
    st.info(f"**Duration:** {days} days")
    st.info(f"**Group Size:** {group_size} friends")
    st.info(f"**Total Budget:** ₹{total_budget:,.0f}")
    st.info(f"**Per-Head Budget:** ₹{total_budget / group_size:,.0f}")
    
    # ---- Itinerary generation ----
    st.markdown("### 📅 Day-by-Day Itinerary")
    days_data = plan.get("days", [])
    for day_entry in days_data:
        day_num = day_entry.get("day_number", 0)
        st.markdown(f"**Day {day_num}**")
        places = day_entry.get("places", [])
        if places:
            place_names = ", ".join([p["name"] for p in places])
            st.write(f"**Suggested activities:** {place_names}")
            with st.expander(f"Day {day_num} details"):
                for p in places:
                    st.write(f"- **{p['name']}** (₹{p['estimated_cost_inr']:,.0f}) - {p['student_hack']}")
        else:
            st.write("No places generated. Please check the configuration.")
    
    # ---- Packing Checklist ----
    st.markdown("### 🎒 Packing Checklist")
    base_items = ["Shoes", "Comfortable clothes", "Toiletries", "Documents", "Phone charger"]
    st.write(f"**Essential items:** {', '.join(base_items)}")
    dest_items = {
        "Goa": ["Swimwear", "Sunscreen", "Beach towel", "Hat"],
        "Manali": ["Warm clothes", "Jacket", "Thermals", "Gloves"],
        "Jaipur": ["Light cotton clothes", "Sunscreen", "Comfortable walking shoes"]
    }
    for item in dest_items.get(destination, []):
        st.checkbox(item, value=True, key=f"pack_{item}")
    
    # ---- Folium Geospatial Map ----
    st.markdown("### 🗺️ Interactive Geospatial Map")
    try:
        # Extract all coordinates from itinerary
        all_coords = []
        for day_entry in days_data:
            for p in day_entry.get("places", []):
                lat = p.get("latitude")
                lon = p.get("longitude")
                if lat and lon and isinstance(lat, (int, float)) and isinstance(lon, (int, float)):
                    all_coords.append((lat, lon, p["name"], p["estimated_cost_inr"], p["student_hack"]))
        
        if not all_coords:
            # Fallback coordinates based on destination
            fallback_coords = {
                "Goa": (15.5097, 73.9257),
                "Manali": (32.2384, 77.1847),
                "Jaipur": (26.9126, 75.8239)
            }
            fc = fallback_coords.get(destination, (28.6139, 77.2090))
            all_coords = [(fc[0], fc[1], destination, 0, "Default location")]
        
        # Create map centered on first location
        center_lat = all_coords[0][0]
        center_lon = all_coords[0][1]
        m = folium.Map(location=[center_lat, center_lon], zoom_start=12, tiles="OpenStreetMap")
        
        # Color palette for days
        day_colors = ["red", "blue", "green", "purple", "orange", "dark:red", "light:red"]
        
        # Add markers for each place
        for idx, (lat, lon, name, cost, hack) in enumerate(all_coords):
            # Determine color based on day index
            day_idx = 0  # Simplified: all get same color or cycle
            color = day_colors[idx % len(day_colors)]
            
            popup_text = f"""
            <b>{name}</b><br/>
            Estimated Cost: ₹{cost:,.0f}<br/>
            Student Hack: {hack}
            """
            folium.Marker(
                location=[lat, lon],
                popup=popup_text,
                icon=folium.Icon(color=color, icon="info", prefix="fa")
            ).add_to(m)
        
        # Display map in Streamlit
        st_data = st_folium(m, width=None, height=500)
        
    except Exception as e:
        st.error(f"Map generation error: {str(e)}")
        st.write("Showing fallback text map information instead.")
        st.write(f"Would display {len(all_coords) if 'all_coords' in dir() else 0} itinerary spots on map.")
    
    # ---- Visual Chart (Plotly) ----
    st.markdown("### 📊 Budget Distribution Chart (Plotly)")
    fig = go.Figure(data=[go.Pie(
        labels=["Stay", "Food & Drinks", "Local Transport", "Emergency/Buffer"],
        values=[split['stay'], split['food'], split['local_transport'], split['emergency_buffer']],
        hole=0.4,
        marker_colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    )])
    fig.update_layout(title="Per-Person Budget Allocation", width=500, height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # ---- Group Saving Tips ----
    st.markdown("### 💡 Group Saving Tips")
    for tip in plan.get("group_saving_tips", []):
        st.write(f"• {tip}")