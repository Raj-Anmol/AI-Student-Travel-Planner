# 🎒 AI Student Travel Planner

> A lightweight, budget-first travel planning web app built for college students — drop in your budget and trip length, and instantly get a smart, percentage-based expense breakdown.

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://raj-anmol-ai-student-travel-planner.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#license)

**🔗 Live Demo:** [raj-anmol-ai-student-travel-planner.streamlit.app](https://raj-anmol-ai-student-travel-planner.streamlit.app)

---

## 📌 Overview

Planning a trip on a tight student budget usually means juggling spreadsheets and guesswork. **AI Student Travel Planner** removes that friction with a single-page Streamlit app: enter your destination, total budget, and number of days, and the app instantly generates a clear, categorized expense breakdown using a rule-based allocation engine — no external APIs, no sign-up, no complexity.

It's built as a clean, minimal MVP that's easy to read, easy to extend, and easy to deploy.

---

## 🚀 Features

- **Simple, guided inputs** — Destination (text), Budget in INR (number input, ₹1,000 minimum), and Trip Duration (slider, 1–7 days).
- **Instant budget allocation engine** — Splits your total budget into four practical categories the moment you click *Generate Smart Plan*:

  | Category | Allocation |
  |---|---|
  | 🏨 Hotel / Stay | 35% |
  | 🍔 Food & Drinks | 30% |
  | 🚌 Local Transport | 20% |
  | 🛟 Emergency / Buffer | 15% |

- **Clean tabular output** — Results are rendered in a responsive, full-width Pandas DataFrame inside Streamlit for easy reading on any screen size.
- **Zero-config, instant feedback** — A loading spinner keeps the experience smooth while the plan is "crafted," with a success message confirming the result.
- **No external API dependencies** — Runs entirely on local logic (Pandas + Streamlit), making it fast, free, and easy to self-host.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **UI Framework** | [Streamlit](https://streamlit.io/) — Python-based interactive web app framework |
| **Data Handling** | [Pandas](https://pandas.pydata.org/) — for structuring the expense breakdown table |
| **Language** | Python 3.x |
| **Deployment** | Streamlit Community Cloud |

---

## 📂 Project Structure

```
AI-Student-Travel-Planner/
├── app.py        # Core Streamlit application & budget allocation logic
└── README.md     # Project documentation
```

The entire application currently lives in a single, focused `app.py` file — keeping the codebase approachable for learning, review, and quick contributions.

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

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit pandas
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. Open the local URL Streamlit prints in your terminal (typically `http://localhost:8501`) in your browser.

---

## 🖥️ Usage

1. Enter your **destination** (e.g., Goa, Manali, Jaipur).
2. Set your **total budget** in INR using the number input.
3. Choose your **trip duration** (1–7 days) with the slider.
4. Click **"Generate Smart Plan ✨"**.
5. View your instant breakdown of Stay, Food, Transport, and Buffer costs in a clean data table.

---

## 🗺️ Roadmap

Planned enhancements for future versions:

- [ ] Day-by-day itinerary generator (morning/afternoon/evening activities)
- [ ] Dynamic packing checklist based on destination type (beach, hills, city)
- [ ] Visual charts (pie/bar) for the expense breakdown alongside the table
- [ ] Safety dashboard with emergency contacts and travel tips for students
- [ ] Multi-currency support for international student travelers

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

---

<p align="center">Made with ❤️ and ☕ by a student, for students.</p>
