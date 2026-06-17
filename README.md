# 🎒 AI Student Travel Planner (Pro)

> A budget-first, student-friendly travel planning web app built with Streamlit — turn any budget into a smart expense breakdown in seconds.

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**Live Demo:** _[Add your deployed Streamlit/Render/Vercel link here]_  
**Repository:** [github.com/Raj-Anmol/AI-Student-Travel-Planner](https://github.com/Raj-Anmol)

---

## 📌 Overview

**AI Student Travel Planner** is a lightweight, interactive Streamlit application designed to solve a very real problem for college students: *"I have a fixed budget — how do I actually spend it on a trip?"*

Instead of relying on expensive third-party travel APIs, the app uses a **rule-based allocation engine** to instantly split a student's travel budget into realistic categories — Stay, Food, Local Transport, and an Emergency Buffer — and presents it as a clean, easy-to-read data table.

The goal is simplicity and speed: enter a destination, budget, and number of days, click a button, and get an instant financial breakdown for the trip — no sign-up, no API keys, no complexity.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 💰 **Smart Budget Allocation** | Automatically splits the entered budget into Stay (35%), Food (30%), Transport (20%), and Emergency Buffer (15%) using a simple, transparent rule-based model. |
| 📊 **Instant Expense Table** | Renders a clean, sortable `pandas` DataFrame showing exactly how much to allocate to each category in INR (₹). |
| 🎛️ **Interactive Inputs** | Destination text field, budget number input, and a trip-length slider (1–7 days) for quick, on-the-fly recalculation. |
| ⚡ **Zero-API Dependency** | All logic runs locally using simple arithmetic — no external travel/finance APIs, no rate limits, no API keys required. |
| 🖥️ **Minimal, Centered UI** | Built on Streamlit's centered layout for a clean, distraction-free, mobile-friendly experience. |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend / UI** | [Streamlit](https://streamlit.io/) — Python-based reactive web framework |
| **Data Handling** | [Pandas](https://pandas.pydata.org/) — for structuring and displaying expense breakdowns |
| **Logic Engine** | Rule-based percentage allocation (pure Python, no ML model in current version) |
| **Language** | Python 3.x |

---

## 📂 Project Structure

```
AI-Student-Travel-Planner/
│
├── app.py          # Main Streamlit application (UI + budget allocation logic)
└── README.md       # Project documentation
```

---

## ⚙️ How It Works

1. The user enters a **destination**, a **total budget (INR)**, and the **number of trip days** (1–7) via Streamlit input widgets.
2. On clicking **"Generate Smart Plan ✨"**, the app runs a rule-based allocation:
   - `Stay = 35% of budget`
   - `Food & Drinks = 30% of budget`
   - `Local Transport = 20% of budget`
   - `Emergency / Buffer = 15% of budget`
3. The results are compiled into a `pandas.DataFrame` and rendered instantly as an interactive table inside the app.

This approach keeps the app fast, predictable, and easy to extend — every allocation rule lives in one place in `app.py`.

---

## 💻 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Raj-Anmol/AI-Student-Travel-Planner.git
cd AI-Student-Travel-Planner

# 2. (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install streamlit pandas

# 4. Run the app
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🗺️ Roadmap

Planned enhancements for future versions:

- [ ] Day-by-day itinerary generator (morning/afternoon/evening activity suggestions based on trip length)
- [ ] Destination-aware smart packing checklist (e.g., warm clothes for hill stations, sunscreen for beaches)
- [ ] Safety dashboard with emergency contacts and cash-splitting tips for group trips
- [ ] Visual charts (bar/pie) alongside the existing data table
- [ ] Persistent trip history using local storage or a lightweight database
- [ ] Multi-language (Hindi/English) interface toggle

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Raj-Anmol) or open a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Anmol Raj**  
B.Tech CSE Student | AI & Cloud Computing Intern (Edunet Foundation × AICTE × IBM SkillsBuild)

- GitHub: [@Raj-Anmol](https://github.com/Raj-Anmol)
- LinkedIn: [linkedin.com/in/raj-anmol](https://www.linkedin.com/in/raj-anmol/)

---

<p align="center">Made with ❤️ and ☕ for budget-conscious student travelers</p>
