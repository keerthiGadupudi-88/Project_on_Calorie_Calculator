# 🍎 Calorie Calculator

A simple and beginner-friendly **Calorie Calculator** built using **Python and Streamlit**.

The application collects basic personal and activity information and provides an estimated daily energy requirement.

> **Important:** This application is intended for educational purposes. The result is only a general estimate and is not medical advice.

## 🚀 Features

* 👤 Enter age
* ⚖️ Enter weight
* 📏 Enter height
* Select the biological sex used by the calculator
* 🏃 Select activity level
* 🧮 Calculate estimated BMR
* 🍎 Calculate estimated daily energy requirement
* 📊 Display a simple interpretation
* ✨ Clean and beginner-friendly interface
* 📱 Mobile-friendly Streamlit layout

## 🛠️ Technologies

* Python
* Streamlit

## 📁 Project Structure

```text
calorie-calculator/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🧮 Calculation Method

The application uses the **Mifflin-St Jeor equation** as a general estimation method.

For males:

```text
BMR = 10 × weight + 6.25 × height − 5 × age + 5
```

For females:

```text
BMR = 10 × weight + 6.25 × height − 5 × age − 161
```

The estimated daily energy requirement is then calculated using an activity factor:

```text
Estimated Daily Energy Requirement
= BMR × Activity Factor
```

## 🏃 Activity Factors

| Activity Level    | Factor |
| ----------------- | -----: |
| Sedentary         |    1.2 |
| Lightly Active    |  1.375 |
| Moderately Active |   1.55 |
| Very Active       |  1.725 |
| Extra Active      |    1.9 |

These are general estimation factors and do not account for every individual circumstance.

## 💻 Run Locally

Open the project folder in a terminal:

```bash
cd calorie-calculator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The application normally opens at:

```text
http://localhost:8501
```

## 🧪 Testing Cases

### Test Case 1 — Default Inputs

Use the default values and click:

```text
Calculate Estimate
```

Expected:

* Calculation completes
* BMR is displayed
* Estimated daily requirement is displayed
* Interpretation is displayed

### Test Case 2 — Different Age

Change the age and calculate again.

Expected:

* The calculated result changes appropriately.

### Test Case 3 — Different Activity Levels

Test each activity level:

```text
Sedentary
Lightly Active
Moderately Active
Very Active
Extra Active
```

Expected:

* The estimated daily requirement changes according to the selected activity factor.

### Test Case 4 — Different Body Measurements

Change height and weight.

Expected:

* BMR and estimated daily requirement are recalculated.

### Test Case 5 — Female Calculation

Select Female and calculate.

Expected:

* The female version of the Mifflin-St Jeor equation is used.

### Test Case 6 — Male Calculation

Select Male and calculate.

Expected:

* The male version of the Mifflin-St Jeor equation is used.

### Test Case 7 — Mobile Testing

Open the deployed application on a phone.

Verify:

* Inputs are readable
* Select boxes work
* Calculate button is visible
* Result is readable
* No important content is cut off

## 🚀 GitHub

Initialize Git:

```bash
git init
```

Add the files:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial commit - Calorie Calculator"
```

Set the main branch:

```bash
git branch -M main
```

Connect your GitHub repository:

```bash
git remote add origin YOUR_GITHUB_REPOSITORY_URL
```

Push the project:

```bash
git push -u origin main
```

## ☁️ Streamlit Community Cloud

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Sign in with GitHub.
4. Select **Create app**.
5. Choose the GitHub repository.
6. Select the `main` branch.
7. Select `app.py`.
8. Click **Deploy**.

Streamlit will install the dependency from:

```text
requirements.txt
```

After deployment, Streamlit provides a public URL.

## 📱 Mobile Testing

Open the deployed URL on a smartphone.

Test:

1. Enter the required information.
2. Select an activity level.
3. Click **Calculate Estimate**.
4. Check the result.
5. Confirm that the interpretation is readable.

## ⚠️ Disclaimer

This calculator provides a general estimate for educational purposes only.

Calorie and energy requirements vary among individuals. The result should not be treated as a diagnosis, prescription, or personalized medical/nutrition plan.

For personalized advice, consult an appropriately qualified healthcare or nutrition professional.

## 🔮 Future Improvements

Possible future additions:

* 📊 Results history
* 📈 Charts
* 💧 Hydration information
* 🥗 General nutrition education
* 📄 Downloadable results
* 🌐 Multiple unit systems
* 🧑‍⚕️ Professional guidance section

## 👨‍💻 Author

Calorie Calculator built using Python and Streamlit.
