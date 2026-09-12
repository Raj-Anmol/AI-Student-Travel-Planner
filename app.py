import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests
import json

st.set_page_config(page_title="Advance Student Travel Planner", page_icon="🎒", layout="wide")
st.title("🎒 AI-Style Student Travel Planner (Pro)")
st.write("Apna budget dalo, mast sasta plan aur expense breakdown pao!")

with st.sidebar:
    st.header("📋 Trip Inputs")
    destination = st.text_input("Kahan jana chahte ho?", value="Goa")
    budget = st.number_input("Aapka Budget (INR):", min_value=1000, value=5000, step=500)
    days = st.slider("Kitne dino ka trip hai?", min_value=1, max_value=7, value=3)
    
    st.markdown("---")
    st.header("🏨 Hotel Preferences")
    hotel_type = st.selectbox("Hotel type", ["Budget Guesthouse", "Mid-range Hotel", "Premium Resort"])
    hotel_rating = st.slider("Minimum rating", 1, 5, 3)
    st.markdown("---")
    st.header("🎯 Travel Style")
    interests = st.multiselect("Interests", ["Sightseeing", "Beach", "Food Hunting", "Nightlife", "Adventure", "Culture"], default=["Food Hunting"])

col1, col2 = st.columns(2)
with col1:
    daily_budget = budget / days
with col2:
    per_day_food = int(daily_budget * 0.30)

if st.button("Generate Smart Plan ✨", type="primary"):
    with st.spinner("🚌 Crafting your premium itinerary and charts..."):
        # Budget allocation
        stay_cost = int(budget * 0.35)
        food_cost = int(budget * 0.30)
        transport_cost = int(budget * 0.20)
        buffer_cost = int(budget * 0.15)
        
        # Hotel cost estimation based on type
        hotel_price_map = {"Budget Guesthouse": 20, "Mid-range Hotel": 35, "Premium Resort": 50}
        hotel_pct = hotel_price_map[hotel_type] / 100
        estimated_hotel_cost = int(budget * hotel_pct)
        
        st.success("🎉 Aapka Fully Advanced Plan Ready Hai!")
        
        # Summary cards
        st.markdown("### 📊 Budget Overview")
        col_a, col_b, col_c, col_d = st.columns(4)
        with col_a:
            st.metric("Hotel/Stay", f"₹{estimated_hotel_cost:,.0f}", f"{hotel_pct*100:.0f}%")
        with col_b:
            st.metric("Food & Drinks", f"₹{food_cost:,.0f}", "30%")
        with col_c:
            st.metric("Local Transport", f"₹{transport_cost:,.0f}", "20%")
        with col_d:
            st.metric("Emergency/Buffer", f"₹{buffer_cost:,.0f}", "15%")
        
        # Budget breakdown table
        st.markdown("### 📊 Detailed Breakdown")
        chart_data = pd.DataFrame({
            "Expense Category": ["Hotel/Stay", "Food & Drinks", "Local Transport", "Emergency/Buffer"],
            "Amount (₹)": [estimated_hotel_cost, food_cost, transport_cost, buffer_cost]
        })
        st.dataframe(chart_data, use_container_width=True)
        
        # Daily budget
        st.markdown("### 📅 Daily Budget Summary")
        st.info(f"**Destination:** {destination}")
        st.info(f"**Duration:** {days} days")
        st.info(f"**Daily Total Budget:** ₹{daily_budget:,.0f}")
        st.info(f"**Per-day Food Allocation:** ₹{per_day_food:,.0f}")
        st.info(f"**Hotel Type:** {hotel_type} (₹{int(daily_budget*hotel_pct):,.0f}/day approx.)")
        
        # Itinerary generation
        st.markdown("### 📅 Day-by-Day Itinerary")
        places = {
            "Goa": ["Baga Beach", "Calangute Beach", "Fort Aguada", "Anjuna Flea Market", "Dudhsagar Falls"],
            "Manali": ["Rohtang Pass", "Solang Valley", "Hadimba Temple", "Vashisht Temple", "Old Manali"],
            "Jaipur": ["Amber Fort", "City Palace", "Hawa Mahal", "Jantar Mantar", "Nahargarh Fort"],
            "Default": ["Local Market", "City Center", "Main Square", "Park", "Restaurant District"]
        }
        day_places = places.get(destination, places["Default"])
        
        for day in range(1, days + 1):
            st.markdown(f"**Day {day}**")
            st.write(f"**Suggested activities:** {', '.join(day_places[:3])}")
            with st.expander(f"Day {day} details"):
                st.write(f"Morning: Explore {day_places[0]}")
                st.write(f"Afternoon: {day_places[1]}")
                st.write(f"Evening: {day_places[2] if len(day_places) > 2 else 'Local exploration'}")
        
        # Packing checklist
        st.markdown("### 🎒 Packing Checklist")
        base_items = ["Shoes", "Comfortable clothes", "Toiletries", "Documents", "Phone charger"]
        dest_items = {
            "Goa": ["Swimwear", "Sunscreen", "Beach towel", "Hat"],
            "Manali": ["Warm clothes", "Jacket", "Thermals", "Gloves"],
            "Jaipur": ["Light cotton clothes", "Sunscreen", "Comfortable walking shoes"]
        }
        st.write(f"**Essential items:** {', '.join(base_items)}")
        for item in dest_items.get(destination, []):
            st.checkbox(item, value=True, key=f"pack_{item}")
        
        # Visual chart
        st.markdown("### 📊 Budget Distribution Chart")
        fig = go.Figure(data=[go.Pie(
            labels=["Hotel/Stay", "Food & Drinks", "Local Transport", "Emergency/Buffer"],
            values=[estimated_hotel_cost, food_cost, transport_cost, buffer_cost],
            hole=0.4,
            marker_colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
        )])
        fig.update_layout(title="Budget Allocation Percentage", width=500, height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Weather info (basic)
        st.markdown("### 🌤️ Weather Overview")
        try:
            # Using a basic weather API
            weather_resp = requests.get(f"https://wttr.in/{destination.lower().replace(' ', '')}?format=j1", timeout=5)
            if weather_resp.status_code == 200:
                wdata = weather_resp.json()
                current = wdata["current_condition"][0]
                st.info(f"🌡️ Current: {current['temp_C']}°C, {current['weatherDesc'][0]['value']}")
                st.info(f"💨 Wind: {current['winddir16Point']} at {current['windspd']} km/h")
            else:
                st.write(tips.get(destination, tips["Default"]))
        except:
            tips = {
                "Goa": "🏖️ Don't miss the beach sunsets! Visit Baga and Calangute beaches.",
                "Manali": "❄️ Car warm clothes! Snow chances in December-January.",
                "Jaipur": "🏛️ Visit Amer Fort early morning to avoid crowds.",
                "Default": "📝 Pack comfortable shoes and a reusable water bottle."
            }
            st.write(tips.get(destination, tips["Default"]))

