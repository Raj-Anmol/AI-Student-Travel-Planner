# 🎒 AI Student Travel Planner Pro

> A production-grade, portfolio-ready travel planning web app built for college students. 
> Drop in your budget, trip length, and group size — get a smart percentage-based expense breakdown,
> interactive geospatial map, and dynamic group splitter all in one page.

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://raj-anmol-ai-student-travel-planner.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#license)
[![Streamlit Folium](https://img.shields.io/badge/Folium%20Map-Enabled-green?logo=folium&logoColor=white)](https://folium.pydata.org/)

---

## 🚀 Features

### 1. Structured JSON Output from LLM
- The app generates a **strictly parsed JSON object** from the LLM simulation (not raw markdown).
- JSON structure includes:
  - `"destination"` (string)
  - `"per_person_budget_split"`: breakdown for stay, local transit, food, and emergency buffer (all INR values).
  - `"days"`: a list of days, each containing:
    - `"day_number"` (int)
    - `"places"`: list of spots with `"name"`, `"latitude"` (float), `"longitude"` (float), `"estimated_cost_inr"` (int), and `"student_hack"` (e.g., student ID discount, free entry hours).
  - `"group_saving_tips"`: list of actionable hacks (e.g., overnight sleeper train, composite tickets, student ID discounts).

### 2. Interactive Geospatial Map (Folium)
- Integrated `streamlit-folium` and `folium`.
- All itinerary spots are plotted as **interactive markers** on a Folium map, with **distinct colors by day**.
- Each marker popup displays the spot name, estimated cost, and the student hack.
- Fallback coordinates if the LLM JSON is missing or invalid.

### 3. Student Group Splitter & Dynamic Budget Dashboard
- **Sidebar inputs**: "Group Size" (1 to 8 friends) and "Total Budget (INR)".
- **Dynamic per-head cost calculation**: total budget divided by group size, then split into stay/food/transport/buffer percentages.
- Metrics displayed using `st.columns` and `st.metric` for clean visual presentation.
- Breakdown table/card for per-person stay vs shared travel costs.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **UI Framework** | [Streamlit](https://streamlit.io/) — Python-based interactive web app framework |
| **Geospatial** | [Folium](https://python-visualization.github.io/folium/) + [streamlit-folium](https://github.com/streamlit/streamlit-folium) |
| **Data Handling** | [Pandas](https://pandas.pydata.org/) — for structuring the expense breakdown table |
| **Visualization** | [Plotly](https://plotly.com/python/) — interactive pie chart |
| **Language** | Python 3.8+ |
| **Deployment** | Streamlit Community Cloud |

---

## 📂 Project Structure

```
AI-Student-Travel-Planner/
├ app.py              # Core Streamlit application with 3 portfolio-grade features
├ README.md           # Project documentation
└ requirements.txt    # Dependencies
```

The entire application lives in a single `app.py` file — keeping the codebase approachable for learning, review, and quick contributions.

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Raj-Anmol/AI-Student-Travel-Planner.git
   cd AI-Student-Travel-Planner
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit folium streamlit-folium pandas plotly requests
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. Open the local URL Streamlit prints in your terminal (typically `http://localhost:8501`) in your browser.

---

## 🖥️ Usage

1. **Enter your destination** (e.g., Goa, Manali, Jaipur).
2. **Set your total budget** in INR using the number input.
3. **Choose trip duration** (1–7 days) with the slider.
4. **Set group size** (1–8 friends) in the sidebar.
5. Click **"Generate Smart Plan ✨"**.
6. View your **instant per-person breakdown** of Stay, Food, Transport, and Buffer costs.
7. Scroll to see the **interactive Folium map** with all itinerary spots marked.
8. Check the **day-by-day itinerary** with places, costs, and student hacks.
9. Review **group saving tips** tailored for student travelers.

---

## 🗺️ Roadmap

Planned enhancements for future versions:

- [ ] Real LLM API integration (OpenAI/Anthropic) with structured output parsing
- [ ] User-authenticated saved trips and travel history
- [ ] Multi-currency support with live exchange rates
- [ ] Integration with real transportation APIs for live pricing
- [ ] Collaborative trip planning (multiple groups, shared editing)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to fork the repo, open a pull request, or raise an issue.

---

## 📄 License

This project is open-sourced under the [MIT License](LICENSE).

---

## 👤 Author

**Anmol Raj**

- 💻 GitHub: [@Raj-Anmol](https://github.com/Raj-Anmol)
- 🔗 LinkedIn: [linkedin.com/in/raj-anmol](https://www.linkedin.com/in/raj-anmol/)
- 🌐 Live Project: [raj-anmol-ai-student-travel-planner.streamlit.app](https://raj-anmol-ai-student-travel-planner.streamlit.app)

<p align="center">Made with ❤️ and ☕ by a student, for students.</p>