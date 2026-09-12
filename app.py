import streamlit as st
import pandas as pd

st.set_page_config(page_title="Advance Student Travel Planner", page_icon="🎒", layout="centered")
st.title("🎒 AI-Style Student Travel Planner (Pro)")
st.write("Apna budget dalo, mast sasta plan aur expense breakdown pao!")

destination = st.text_input("Kahan jana chahte ho?", value="Goa")
budget = st.number_input("Aapka Budget (INR):", min_value=1000, value=5000, step=500)
days = st.slider("Kitne dino ka trip hai?", min_value=1, max_value=7, value=3)

col1, col2 = st.columns(2)
with col1:
    daily_budget = budget / days
with col2:
    per_day_allocation = int(daily_budget * 0.30)

if st.button("Generate Smart Plan ✨"):
    with st.spinner("🚌 Crafting your premium itinerary and charts..."):
        stay_cost = int(budget * 0.35)
        food_cost = int(budget * 0.30)
        transport_cost = int(budget * 0.20)
        buffer_cost = int(budget * 0.15)
        
        st.success("🎉 Aapka Fully Advanced Plan Ready Hai!")
        
        st.markdown("### 📊 Budget Allocation Breakdown")
        
        chart_data = pd.DataFrame({
            "Expense Category": ["Hotel/Stay", "Food & Drinks", "Local Transport", "Emergency/Buffer"],
            "Amount (₹)": [stay_cost, food_cost, transport_cost, buffer_cost]
        })
        st.dataframe(chart_data, use_container_width=True)
        
        st.markdown("### 📅 Trip Summary")
        st.info(f"**Destination:** {destination}")
        st.info(f"**Duration:** {days} days")
        st.info(f"**Daily Budget:** ₹{daily_budget:,.0f} per day")
        st.info(f"**Per-day food allocation:** ₹{per_day_allocation:,.0f}")
        
        st.markdown("### 🍽️ Destination Tips")
        tips = {
            "Goa": "🏖️ Don't miss the beach sunsets! Visit Baga and Calangute beaches.",
            "Manali": "❄️ Car warm clothes! Snow chances in December-January.",
            "Jaipur": "🏛️ Visit Amer Fort early morning to avoid crowds.",
            "Default": "📝 Pack comfortable shoes and a reusable water bottle."
        }
        st.write(tips.get(destination, tips["Default"]))