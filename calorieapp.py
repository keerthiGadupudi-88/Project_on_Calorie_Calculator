import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Calorie Calculator",
    page_icon="🍎",
    layout="centered"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666;
    margin-bottom: 25px;
}

.result-box {
    border: 2px solid #333;
    border-radius: 15px;
    padding: 25px;
    text-align: center;
    margin-top: 20px;
}

.calorie-number {
    font-size: 36px;
    font-weight: 700;
}

.info-box {
    border: 1px solid #ddd;
    border-radius: 12px;
    padding: 18px;
    margin-top: 15px;
}

.footer {
    text-align: center;
    color: #666;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🍎 Calorie Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Estimate your daily energy requirement</div>',
    unsafe_allow_html=True
)

st.info(
    "ℹ️ This calculator provides a general educational estimate. "
    "It is not medical advice and should not be used to diagnose "
    "or treat a health condition."
)

# =========================================================
# PERSONAL DETAILS
# =========================================================

st.subheader("👤 Personal Details")

age = st.number_input(
    "Age (years)",
    min_value=13,
    max_value=100,
    value=18,
    step=1
)

sex = st.selectbox(
    "Select biological sex used by the calculator",
    ["Female", "Male"]
)

# =========================================================
# BODY DETAILS
# =========================================================

st.subheader("📏 Body Details")

weight = st.number_input(
    "Weight (kg)",
    min_value=20.0,
    max_value=300.0,
    value=60.0,
    step=0.5
)

height = st.number_input(
    "Height (cm)",
    min_value=100.0,
    max_value=250.0,
    value=165.0,
    step=0.5
)

# =========================================================
# ACTIVITY LEVEL
# =========================================================

st.subheader("🏃 Activity Level")

activity_options = {
    "Sedentary - little or no exercise": 1.2,
    "Lightly active - light exercise 1-3 days/week": 1.375,
    "Moderately active - exercise 3-5 days/week": 1.55,
    "Very active - hard exercise 6-7 days/week": 1.725,
    "Extra active - very hard training/physical work": 1.9
}

activity_level = st.selectbox(
    "Choose your typical activity level",
    list(activity_options.keys())
)

# =========================================================
# CALCULATE
# =========================================================

if st.button("🧮 Calculate Estimate", use_container_width=True):

    # -----------------------------------------------------
    # BMR CALCULATION
    # Mifflin-St Jeor equation
    # -----------------------------------------------------

    if sex == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    # -----------------------------------------------------
    # ESTIMATED DAILY ENERGY REQUIREMENT
    # -----------------------------------------------------

    activity_factor = activity_options[activity_level]

    estimated_calories = bmr * activity_factor

    # -----------------------------------------------------
    # RESULT
    # -----------------------------------------------------

    st.success("✅ Calculation completed!")

    st.markdown(
        f"""
        <div class="result-box">
            <div>Estimated Daily Energy Requirement</div>
            <div class="calorie-number">
                {estimated_calories:,.0f} kcal/day
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # BMR
    # -----------------------------------------------------

    st.markdown(
        f"""
        <div class="info-box">
            <b>Estimated BMR:</b> {bmr:,.0f} kcal/day
            <br><br>
            BMR is an estimate of the energy your body uses
            for basic functions at rest.
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # SIMPLE INTERPRETATION
    # -----------------------------------------------------

    st.subheader("📊 Simple Interpretation")

    st.write(
        f"Based on the information entered, your estimated "
        f"daily energy requirement is approximately "
        f"**{estimated_calories:,.0f} kcal/day**."
    )

    st.write(
        "This number is an estimate of the energy needed to "
        "support your usual activity level. Actual energy "
        "needs can vary between individuals."
    )

    st.warning(
        "⚠️ Calorie needs can be different during growth, "
        "pregnancy, illness, intense training, or other "
        "health situations. For personalized guidance, "
        "speak with a qualified healthcare or nutrition professional."
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div class="footer">
        🍎 Calorie Calculator
        <br>
        Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)