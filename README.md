# Bracket Boss 🏆

**Bracket Boss** is a machine learning-powered football analytics web app that predicts international match outcomes, simulates FIFA World Cup tournaments, and provides interactive team analytics dashboards.

Built with **Python, XGBoost, Streamlit, and Plotly**, the project combines historical football match data, feature engineering, predictive modeling, and tournament simulation into an end-to-end sports analytics application.

---

## 🚀 Live Demo

**Live App:** https://bracket-boss-htuplzwdnzmru2c52whxyu.streamlit.app/

**GitHub Repo:** https://github.com/ProSanj/bracket-boss

---

## 📌 Features

### 1) Match Predictor
Predicts international football match outcomes with probabilities for:
- **Home Win**
- **Draw**
- **Away Win**

### 2) World Cup Simulator
Runs large-scale **Monte Carlo simulations** of the FIFA World Cup to estimate tournament-winning probabilities for teams.

### 3) Single Tournament Simulation
Simulates one complete World Cup tournament and displays:
- Champion
- Finalists
- Semifinalists
- Quarterfinalists
- Round of 16 teams

### 4) Team Analytics Dashboard
Provides team-level metrics such as:
- **ELO rating**
- **Recent form**
- **Win rate**
- **Average goals scored**
- **Average goals conceded**

### 5) Team Comparison
Compares two teams side by side using analytics and visual charts.

---

## 🧠 Machine Learning Approach

The match prediction model is based on **historical international football match data** and engineered team-level features.

### Features used
- Recent team form
- Win rate
- Average goals scored
- Average goals conceded
- Goal difference
- Team ELO rating
- ELO difference
- Form difference
- Goal-difference difference
- Ranking-based features

### Model
- **XGBoost multiclass classifier**
- Predicts:
  - `Home Win`
  - `Draw`
  - `Away Win`

---

## 🎲 Monte Carlo Tournament Simulation

Bracket Boss includes a **Monte Carlo World Cup simulator** that repeatedly simulates tournament outcomes using the match prediction model’s probability outputs.

The simulator:
- simulates all group-stage matches
- selects knockout qualifiers
- runs knockout rounds
- estimates tournament-winning probabilities across many simulations

To improve performance, matchup probabilities are **precomputed and cached**, allowing the deployed app to handle large simulation counts much faster.

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **XGBoost**
- **Scikit-learn**
- **Joblib**
- **Streamlit**
- **Plotly**

---

## 📂 Project Structure

```bash
Bracket-Boss/
│
├── app.py
├── requirements.txt
├── runtime.txt
│
├── data/
│   ├── results.csv
│   └── ml_dataset.csv
│
├── models/
│   └── world_cup_model.pkl
│
├── src/
│   ├── predictor.py
│   └── simulator.py
│
└── assets/
    └── logoforo.png




⚙️ How It Works

Match Prediction

For a given matchup, the app:

1. Computes team-level features from historical data
2. Builds a feature vector for the two teams
3. Uses the trained XGBoost model to generate outcome probabilities
4. Returns a predicted result and probability breakdown

Team Analytics

The app calculates:

* recent form based on the last few matches
* scoring and conceding averages
* win rate
* ELO rating

Tournament Simulation

The simulator:

1. Simulates group-stage matches using predicted probabilities
2. Advances group winners, runners-up, and best third-place teams
3. Simulates knockout rounds until a champion is determined
4. Repeats the tournament many times to estimate winning odds

⸻

📈 Deployment

Bracket Boss is deployed using Streamlit Community Cloud and is accessible through the live web app link above.

⸻

📊 Model Performance

The project focuses on building a practical and interactive football prediction system rather than a perfect forecasting engine. The predictive model performs reasonably for a sports analytics project built on historical international football data, but match prediction remains an inherently uncertain problem due to the unpredictable nature of football.

The model’s output is best interpreted as probabilistic guidance rather than guaranteed match forecasts.

⸻

⚠️ Current Limitations

While the project is functional and deployed, there are several limitations:

* Predictions are based mainly on historical team-level trends
* The current version does not directly incorporate:
    * player injuries
    * squad announcements
    * live lineups
    * tactical context
    * real-time team news
* FIFA ranking features are simplified rather than fully live and dynamic
* Tournament simulation quality depends on the predictive quality of the underlying match model
* Monte Carlo simulation outputs can vary slightly between runs because tournament results are sampled probabilistically

⸻

🔄 Live Data Experimentation

During development, I explored integrating automated live football data APIs so the system could dynamically update team data and match context. However, the deployed version uses a curated dataset-based pipeline to ensure stability, reproducibility, and consistent model behavior.

This tradeoff was intentional: while live API-driven automation is attractive, the dataset-based version was more reliable for the final deployed application.

⸻

⚡ Performance Optimization

The World Cup simulator originally became slow when running large numbers of Monte Carlo simulations. To improve performance, I optimized the simulation pipeline by reducing repeated prediction overhead and precomputing reusable matchup probabilities, which significantly improved runtime in the deployed app.

This made it possible to run even large tournament simulation counts much faster while preserving the same prediction logic.

⸻

💡 Future Improvements

Possible future upgrades for Bracket Boss include:

* live football data API integration
* player-level features such as injuries, lineups, and squad strength
* dynamic FIFA / ELO ranking updates
* stronger tournament bracket visualizations
* support for club football competitions and domestic leagues
* a backend API for model inference
* more advanced tournament simulation logic
* experimentation with additional ML models and calibration methods

⸻

👨‍💻 Author

Sanjay Mahadevan
Computer Science Engineering, VIT Chennai

