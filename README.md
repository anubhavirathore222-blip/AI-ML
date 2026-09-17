# Student Study Time Predictor

A beginner Machine Learning project that predicts how many hours a student should study based on their academic profile — submitted as a BYOP capstone for the ML/AI course.

---

## Problem Statement

Students often misjudge how much time they need to prepare for exams, leading to poor planning and weak performance. This project uses Linear Regression to give a personalized study hour estimate based on simple, self-reported inputs.

---

##  Features Used

| Feature | Description |
|---|---|
| `past_score` | Average score in previous exams (40–100) |
| `attendance_pct` | Percentage of classes attended (50–100) |
| `sleep_hours` | Average hours of sleep per night (4–9) |
| `subject_difficulty` | Self-rated difficulty from 1 (Easy) to 5 (Hard) |
| `study_hours_needed` | **Target** — predicted study hours (1–10) |

---

##  Project Structure

```
student-study-predictor/
├── data/
│   └── student_data.csv
├── src/
│   ├── generate_data.py
│   └── model.py
├── results/
│   └── results_plot.png
├── notebooks/
│   └── exploration.ipynb
├── requirements.txt
└── README.md
```

---

##  Setup & Installation

```bash
# 1. Clone the repo
git clone https://github.com/Ayushh-00
cd student-study-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate dataset
python src/generate_data.py

# 4. Train and evaluate the model
python src/model.py
```

---

##  Results

| Metric | Value |
|---|---|
| Mean Absolute Error (MAE) |~2.4 – 2.6 hours|
| R² Score | ~0.75–0.85|

A scatter plot comparing actual vs predicted study hours is saved to results_plot.png

![results_plot.png](results_plot.png) <br>


OUTPUT SCREEN- 
![OUTPUT SCREEN WITH GIVEN MAE AND R VALUE](OUTPUT-SCREEN.png)
---

##  Tech Stack

Python · pandas · numpy · scikit-learn · matplotlib · seaborn

---

##  Future Improvements

- Collect real student data via a survey
- Try advanced models (Random Forest, XGBoost)
- Deploy as a Streamlit web app

---

##  Author

**AYUSH KUMAR SINGH** — BTECH-CSE, 25BCE11163, VIT BHOPAL UNIVERSITY 
GitHub: (https://github.com/Ayushh-00)

*Submitted on VITyarthi | Machine Learning / AI Course — BYOP Capstone*
