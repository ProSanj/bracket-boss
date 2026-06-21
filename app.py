import streamlit as st
import pandas as pd
import plotly.express as px

from src.predictor import (
    predict_match,
    get_team_dashboard
)

import src.simulator as simulator

st.set_page_config(
    page_title="Bracket Boss",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>

[data-testid="stHeaderActionElements"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)
# ==================================
# CUSTOM BACKGROUND
# ==================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        180deg,
        #050816 0%,
        #0B1736 50%,
        #12254D 100%
    );
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Hide Deploy Button */
.stDeployButton {
    display: none;
}

/* Rounded Inputs */
.stSelectbox > div > div {
    border-radius: 15px;
}

/* Better Buttons */
.stButton button {
    border-radius: 12px;
    font-weight: 700;
    padding: 0.6rem 1.4rem;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.05);
    border-radius: 15px;
    padding: 15px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(10,15,30,0.85);
}
.stButton button {
    background-color: #B22222;
    color: white;
    border-radius: 12px;
    border: none;
    font-weight: 700;
    padding: 0.6rem 1.4rem;
}

.stButton button:hover {
    background-color: #D62828;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ==================================
# HERO SECTION
# ==================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "⚽ Teams",
        "300+"
    )

with col2:
    st.metric(
        "🧠 Model",
        "ML + Elo"
    )

with col3:
    st.metric(
        "🏆 Simulations",
        "5000+"
    )

with col4:
    st.metric(
        "📊 Features",
        "13"
    )
    
col1, col2, col3 = st.columns([2.5,2,2.5])

with col2:

    st.image(
        "assets/logoforo.png",
        width=420
    )

st.markdown(
    """
    <h1 style='
        text-align:center;
        margin-top:-60px;
        margin-bottom:10px;
        font-size:84px;
        font-weight:900;
        letter-spacing:3px;
    '>
        BRACKET BOSS
    </h1>

    <h3 style='
        text-align:center;
        color:#C7C7C7;
        margin-bottom:25px;
        font-size:36px;
    '>
        Match Prediction • Team Analytics • Tournament Simulation
    </h3>

    <p style='
        text-align:center;
        font-size:22px;
        color:#E0E0E0;
        max-width:950px;
        margin:auto;
        line-height:1.7;
    '>
        Predict matches, compare teams, analyze team strength,
        and simulate entire World Cups using Machine Learning,
        Elo Ratings, and Monte Carlo Simulation.
    </p>

    <hr style='
        border:1px solid rgba(255,255,255,0.15);
        margin-top:40px;
        margin-bottom:25px;
    '>
    """,
    unsafe_allow_html=True
)
# ==================================
# HIDE STREAMLIT BRANDING
# ==================================

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(
    hide_streamlit_style,
    unsafe_allow_html=True
)

st.sidebar.title(
    "🏆 Bracket Boss"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Match Predictor",
        "World Cup Simulator",
        "Single Tournament",
        "Team Analytics",
        "Team Comparison"
    ]
)

# ==================================
# MATCH PREDICTOR
# ==================================

if page == "Match Predictor":
    
    df = pd.read_csv(
        "data/results.csv",
        encoding="latin1"
    )

    teams = sorted(
        list(
            set(df["home_team"])
            .union(
                set(df["away_team"])
            )
        )
    )

    home_team = st.selectbox(
        "Home Team",
        teams
    )

    away_team = st.selectbox(
        "Away Team",
        teams,
        index=min(1, len(teams) - 1)
    )

    if st.button("Predict Match"):

        if home_team == away_team:

            st.error(
                "Please select two different teams."
            )

        else:

            try:

                prediction, probabilities = (
                    predict_match(
                        home_team,
                        away_team
                    )
                )

                st.subheader(
                    f"{home_team} vs {away_team}"
                )

                st.success(
                    f"Prediction: {prediction}"
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "🏠 Home Win",
                        f"{probabilities[2] * 100:.2f}%"
                    )

                with col2:

                    st.metric(
                        "🤝 Draw",
                        f"{probabilities[1] * 100:.2f}%"
                    )

                with col3:

                    st.metric(
                        "✈️ Away Win",
                        f"{probabilities[0] * 100:.2f}%"
                    )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )
# ==================================
# WORLD CUP SIMULATOR
# ==================================

elif page == "World Cup Simulator":

    st.title("🏆 World Cup Simulator")

    st.write(
        "Run Monte Carlo World Cup simulations."
    )

    simulations = st.slider(
        "Number of Simulations",
        100,
        5000,
        1000,
        100
    )

    if st.button("Run Simulation"):

        with st.spinner(
            "Running simulations..."
        ):

            results = simulator.run_simulations(
                simulations
            )

        st.subheader(
            "🏆 World Cup Winner Odds"
        )

        results_df = pd.DataFrame(
            results,
            columns=[
                "Team",
                "Win Probability (%)"
            ]
        )

        st.dataframe(
            results_df,
            use_container_width=True
        )

        st.subheader(
            "📈 Winning Probability Chart"
        )

        fig = px.bar(
        results_df,
        x="Team",
        y="Win Probability (%)",
        title="World Cup Winner Odds"
        )

        fig.update_layout(
        template="plotly_dark",
        height=600
        )       

        st.plotly_chart(
        fig,
        use_container_width=True
        )

# ==================================
# SINGLE TOURNAMENT
# ==================================

elif page == "Single Tournament":

    st.title(
        "🏆 Single Tournament Simulator"
    )

    st.write(
        "Simulate one complete World Cup."
    )

    if st.button(
        "Run Tournament"
    ):

        with st.spinner(
            "Simulating tournament..."
        ):

            results = (
                simulator.simulate_tournament_results()
            )

        st.success(
            f"🏆 Champion: {results['champion']}"
        )

        st.subheader(
            "Final"
        )

        st.write(
            f"{results['finalists'][0]} vs {results['finalists'][1]}"
        )

        st.subheader(
            "Semifinalists"
        )

        for team in results["semifinalists"]:

            st.write(
                f"• {team}"
            )

        st.subheader(
            "Quarterfinalists"
        )

        for team in results["quarterfinalists"]:

            st.write(
                f"• {team}"
            )

        st.subheader(
            "Round of 16"
        )

        for team in results["round_of_16"]:

            st.write(
                f"• {team}"
            )

# ==================================
# TEAM ANALYTICS
# ==================================

elif page == "Team Analytics":

    st.title(
        "📊 Team Analytics"
    )

    df = pd.read_csv(
        "data/results.csv",
        encoding="latin1"
    )

    teams = sorted(
        list(
            set(df["home_team"])
            .union(
                set(df["away_team"])
            )
        )
    )

    selected_team = st.selectbox(
        "Select Team",
        teams
    )

    stats = get_team_dashboard(
        selected_team
    )

    st.subheader(
        selected_team
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "ELO Rating",
            stats["elo"]
        )

        st.metric(
            "Form",
            stats["form"]
        )

        st.metric(
            "Win Rate %",
            stats["win_rate"]
        )

    with col2:

        st.metric(
            "Goals Scored Avg",
            stats["goals_scored"]
        )

        st.metric(
            "Goals Conceded Avg",
            stats["goals_conceded"]
        )

    analytics_df = pd.DataFrame(
        {
            "Metric": [
                "Form",
                "Win Rate",
                "Goals Scored",
                "Goals Conceded"
            ],
            "Value": [
                stats["form"],
                stats["win_rate"],
                stats["goals_scored"],
                stats["goals_conceded"]
            ]
        }
    )

    st.subheader(
        "📈 Team Profile"
    )

    fig = px.bar(
    analytics_df,
    x="Metric",
    y="Value",
    title=f"{selected_team} Analytics"
    )

    fig.update_layout(
    template="plotly_dark",
    height=500
    )

    st.plotly_chart(
    fig,
    use_container_width=True
    )
# ==================================
# TEAM COMPARISON
# ==================================

elif page == "Team Comparison":

    st.title(
        "⚔️ Team Comparison"
    )

    df = pd.read_csv(
        "data/results.csv",
        encoding="latin1"
    )

    teams = sorted(
        list(
            set(df["home_team"])
            .union(
                set(df["away_team"])
            )
        )
    )

    col1, col2 = st.columns(2)

    with col1:

        team1 = st.selectbox(
            "Team 1",
            teams,
            key="team1"
        )

    with col2:

        team2 = st.selectbox(
            "Team 2",
            teams,
            index=min(1, len(teams) - 1),
            key="team2"
        )

    stats1 = get_team_dashboard(
        team1
    )

    stats2 = get_team_dashboard(
        team2
    )

    comparison_df = pd.DataFrame(
        {
            team1: [
                stats1["elo"],
                stats1["form"],
                stats1["win_rate"],
                stats1["goals_scored"],
                stats1["goals_conceded"]
            ],

            team2: [
                stats2["elo"],
                stats2["form"],
                stats2["win_rate"],
                stats2["goals_scored"],
                stats2["goals_conceded"]
            ]
        },
        index=[
            "ELO Rating",
            "Form",
            "Win Rate %",
            "Goals Scored Avg",
            "Goals Conceded Avg"
        ]
    )

    st.subheader(
        f"{team1} vs {team2}"
    )

    st.dataframe(
        comparison_df,
        use_container_width=True
    )

    st.subheader(
        "📊 Comparison Chart"
    )

    comparison_chart = (
        comparison_df
        .T
        .reset_index()
    )

    fig = px.bar(
        comparison_chart,
        x="index",
        y=[
            "ELO Rating",
            "Form",
            "Win Rate %",
            "Goals Scored Avg",
            "Goals Conceded Avg"
        ],
        barmode="group",
        title=f"{team1} vs {team2}"
    )

    fig.update_layout(
        template="plotly_dark",
        height=600,
        legend_title_text="Metrics"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )