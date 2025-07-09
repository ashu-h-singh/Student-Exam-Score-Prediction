import streamlit as st
import joblib
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# Load the model
model = joblib.load("best_model.pkl")

st.set_page_config(page_title="Student Exam Score Predictor", page_icon="🎓", layout="centered")

# ---------------------------- CSS Styling ----------------------------
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #f0f0f0;
    }

    /* 🔳 Header Styling */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(30, 30, 40, 0.7);
        padding: 20px 30px;
        border: 2px solid #673ab7;
        border-radius: 16px;
        margin-bottom: 25px;
        box-shadow: 0 0 15px rgba(103, 58, 183, 0.3);
    }
    .header-logo {
        font-size: 32px;
        font-weight: bold;
        color: #00c6ff;
        text-shadow: 0 0 10px rgba(0, 198, 255, 0.5);
    }
    .header-title {
        font-size: 28px;
        font-weight: bold;
        font-style: italic;
        background: linear-gradient(to right, #00c6ff, #7e57c2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 8px rgba(106, 27, 154, 0.4);
        text-align: center;
    }
    .header-tagline {
        font-size: 14px;
        color: #cccccc;
        text-align: right;
        font-style: italic;
    }
    @media (max-width: 768px) {
        .header-container {
            flex-direction: column;
            text-align: center;
        }
        .header-logo, .header-tagline {
            margin-bottom: 10px;
        }
    }

    /* 🔲 Main Box Styling */
    .main-box {
        border: 3px solid;
        border-image: linear-gradient(to right, #00c6ff, #0072ff, #8e2de2, #4a00e0) 1;
        border-radius: 20px;
        padding: 35px;
        margin: 20px auto;
        background: rgba(20, 20, 30, 0.85);
        box-shadow: 0 0 25px rgba(0, 200, 255, 0.2);
        backdrop-filter: blur(8px);
        max-width: 900px;
    }

    .quote-box {
        display: inline-block;
        font-size: 14px;
        color: #80d8ff;
        border: 1px dashed #00b0ff;
        border-radius: 8px;
        padding: 6px 12px;
        background-color: rgba(0, 183, 255, 0.05);
        margin-top: 10px;
    }

    /* 🎚 Sliders */
    .stSlider > div[data-baseweb='slider'] {
        background: linear-gradient(to right, #0d47a1, #1e88e5);
        border-radius: 10px;
        padding: 10px;
        box-shadow: inset 0 0 8px rgba(0,0,0,0.2);
    }

    /* 🔘 Button */
    .stButton>button {
        background-color: #00c6ff;
        color: #fff;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 30px;
        box-shadow: 0px 8px 25px rgba(0, 198, 255, 0.3);
        transition: all 0.3s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #0072ff;
        transform: scale(1.05);
        box-shadow: 0px 10px 30px rgba(0, 114, 255, 0.4);
    }

    /* 🔘 Circular Score */
    .circle-progress {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        font-weight: bold;
        color: white;
        margin: auto;
        background: conic-gradient(grey 0% 100%);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------- HEADER ----------------------------
st.markdown("""
    <style>
    .header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: 2px solid #7e57c2;
        border-radius: 16px;
        background: linear-gradient(to right, #1e1e2f, #2c2c3f);
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0 0 15px rgba(126, 87, 194, 0.3);
    }
    .header-logo {
        font-size: 36px;
        margin-bottom: 8px;
    }
    .header-title {
        font-size: 32px;
        font-weight: bold;
        font-style: italic;
        text-align: center;
        background: linear-gradient(to right, #00c6ff, #8e24aa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 8px rgba(142, 36, 170, 0.4);
    }
    </style>

    <div class="header-container">
        <div class="header-logo">📘</div>
        <div class="header-title">🎓 Student Exam Score Predictor</div>
    </div>
""", unsafe_allow_html=True)


# ---------------------------- SLIDERS ----------------------------
st.markdown("### 🧾 Enter your details:")

age = st.slider("📅 Age", 10, 30, 18)
study_hours = st.slider("📘 Study Hours per Day", 0.0, 12.0, 2.0)
social_media_hours = st.slider("📱 Social Media Usage (hrs)", 0.0, 12.0, 3.0)
netflix_hours = st.slider("📺 Netflix Hours (hrs)", 0.0, 12.0, 1.0)
attendance = st.slider("🏫 Attendance (%)", 0.0, 100.0, 80.0)
sleep_hours = st.slider("😴 Sleep Hours", 0.0, 12.0, 7.0)
exercise_frequency = st.slider("💪 Exercise Days/Week", 0, 7, 3)
mental_health = st.slider("🧠 Mental Health Rating (1-10)", 1, 10, 5)

# ---------------------------- BUTTON ----------------------------
center_button = st.columns([1, 1, 1])[1]

with center_button:
    if st.button("🎯 Predict Exam Score"):
        input_data = np.array([[age, study_hours, social_media_hours, netflix_hours,
                                attendance, sleep_hours, exercise_frequency, mental_health]])
        prediction = model.predict(input_data)[0]
        prediction = max(0, min(100, prediction))

        if prediction >= 75:
            bar_color = "#4CAF50"
        elif prediction >= 50:
            bar_color = "#FFC107"
        else:
            bar_color = "#F44336"

        st.markdown(
            f"""
            <style>
            .circle-progress {{
                background: conic-gradient({bar_color} {prediction}%, #e0e0e0 0%);
            }}
            </style>
            <div class="circle-progress">{prediction:.2f}%</div><br>
            """, unsafe_allow_html=True
        )

        st.success(f"✅ **Predicted Exam Score: {prediction:.2f} / 100**")

 # ---------------------------- STYLING FOR SUGGESTIONS ----------------------------
st.markdown("""
    <style>
    .suggestion-card {
        border: 1px solid #00e5ff;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        background: rgba(0, 229, 255, 0.05);
        backdrop-filter: blur(8px);
        box-shadow: 0 0 15px rgba(0, 229, 255, 0.2);
        transition: all 0.3s ease-in-out;
    }
    .suggestion-card:hover {
        box-shadow: 0 0 25px rgba(0, 229, 255, 0.4);
        transform: scale(1.01);
    }
    .suggestion-title {
        font-size: 22px;
        font-weight: bold;
        color: #00e5ff;
        margin-bottom: 10px;
    }
    .suggestion-line {
        font-size: 16px;
        color: #e0f7fa;
        padding: 4px 0;
    }
    .motivational-quote {
        text-align: center;
        margin-top: 15px;
        font-style: italic;
        font-size: 15px;
        color: #80deea;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------- DISPLAYING SUGGESTIONS ----------------------------
st.markdown('<div class="suggestion-title">📌 Personalized Suggestions:</div>', unsafe_allow_html=True)

suggestions = []

if study_hours < 3:
    suggestions.append("➕ Increase study hours to at least **3–4/day**.")
if social_media_hours > 4:
    suggestions.append("📵 Reduce social media below **4 hours/day**.")
if netflix_hours > 2:
    suggestions.append("📺 Try to limit Netflix to **< 2 hrs**.")
if attendance < 75:
    suggestions.append("📚 Improve attendance to **75% or more**.")
if sleep_hours < 6:
    suggestions.append("😴 Sleep at least **6-8 hrs/day**.")
if exercise_frequency < 3:
    suggestions.append("🏃 Exercise at least **3 times/week**.")
if mental_health < 5:
    suggestions.append("🧘 Focus on improving mental health.")

if not suggestions:
    st.markdown('<div class="suggestion-line">🎉 You are doing great! Keep it up! 💯</div>', unsafe_allow_html=True)
else:
    for s in suggestions:
        st.markdown(f'<div class="suggestion-line">• {s}</div>', unsafe_allow_html=True)

st.markdown('<div class="motivational-quote">💡 "Success is the sum of small efforts, repeated day in and day out."</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------- RADAR CHART FOR BEHAVIOR ----------------------------
st.markdown("### 🕸️ Behavioral Overview (Spider Radar Chart):")

import pandas as pd
import plotly.graph_objects as go

labels = ['Study Hours', 'Social Media', 'Netflix', 'Sleep', 'Exercise', 'Mental Health']
values = [study_hours, social_media_hours, netflix_hours, sleep_hours, exercise_frequency, mental_health]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=values,
    theta=labels,
    fill='toself',
    name='Current Behavior',
    line=dict(color='#00e5ff')
))

fig.update_layout(
    polar=dict(
        bgcolor="#1c1c1c",
        radialaxis=dict(visible=True, range=[0, 12], color="#888")
    ),
    showlegend=False,
    plot_bgcolor="#1c1c1c",
    paper_bgcolor="#1c1c1c",
    font=dict(color="#00e5ff"),
    margin=dict(l=40, r=40, t=40, b=40)
)

st.plotly_chart(fig, use_container_width=True)


# ---------------------------- STYLING FEEDBACK SECTION ----------------------------
st.markdown("""
    <style>
    .emoji-title {
        font-size: 26px;
        text-align: center;
        font-weight: bold;
        color: #00e5ff;
        margin-top: 40px;
        margin-bottom: 20px;
        text-shadow: 0 0 6px rgba(0, 229, 255, 0.3);
    }
    .stButton>button {
        background-color: #111827;
        border: 2px solid #00e5ff;
        color: #b2ebf2;
        border-radius: 12px;
        padding: 10px 15px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 0 10px rgba(0,229,255,0.1);
    }
    .stButton>button:hover {
        background-color: #00e5ff;
        color: black;
        border-color: #80d8ff;
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(0, 229, 255, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------- EMOJI FEEDBACK LOGIC ----------------------------
st.markdown('<div class="emoji-title">😃 How are you feeling about this prediction?</div>', unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("😎 Confident"):
        st.info("💪 Keep pushing forward — you're doing great!")
with col2:
    if st.button("📈 Motivated"):
        st.success("🚀 That’s the spirit! Keep the momentum!")
with col3:
    if st.button("📚 Gonna Study"):
        st.info("📅 Build a plan and study smart, not just hard!")
with col4:
    if st.button("😐 Okay"):
        st.warning("🙂 You’ve got this. A little push goes a long way.")
with col5:
    if st.button("😟 Need Help"):
        st.error("📬 Don't hesitate — talk to a friend, teacher, or mentor.")
        
        
st.markdown('<p style="text-align:center; font-style:italic; color:#80d8ff;">✨ "Small steps every day lead to big results."</p>', unsafe_allow_html=True)





# ---------------------------- CLOSE MAIN BOX ----------------------------
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------- FOOTER ----------------------------
st.markdown("---")
st.markdown("<p style='text-align:center; color:#999;'>© 2025 SmartScore AI | Designed with ❤️ in Ashutosh</p>", unsafe_allow_html=True)
