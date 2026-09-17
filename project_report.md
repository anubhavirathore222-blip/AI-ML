# Project Report — Student Study Time Predictor
### BYOP Capstone | Machine Learning / AI Course | VITyarthi

**Name:** **Anubhavi Rathore** | **Reg No:** 25MIM10018 | **Branch:** Integrated MTech AI

**GitHub:** https://github.com/Ayushh-00/AI-ML.git

---

## 1. Introduction

This project was built as part of the BYOP capstone for the ML/AI course. The goal was to identify a real problem, apply course concepts to solve it, and document the entire process. I chose to build a **Student Study Time Predictor** — a regression model that estimates how many hours a student needs to study before an exam.

---

## 2. Problem Statement

Students frequently misjudge how much preparation an exam requires. Without any data-driven guidance, they rely on guesswork or peer pressure, often leading to under-preparation or wasted time. There is no simple tool that accounts for a student's individual academic profile to suggest a personalized study plan.

---

## 3. Objective

Build a supervised ML regression model that predicts the required study hours based on four inputs: past exam score, attendance percentage, sleep hours, and subject difficulty,  applying the core ML pipeline taught in this course.

---

## 4. Dataset

Since no suitable public dataset existed, a **synthetic dataset of 200 records** was generated using `numpy` with a fixed seed (`42`) for reproducibility.

| Feature | Range | Description |
|---|---|---|
| `past_score` | 40–100 | Previous exam average |
| `attendance_pct` | 50–100 | Classes attended (%) |
| `sleep_hours` | 4.0–9.0 | Avg. sleep per night |
| `subject_difficulty` | 1–5 | Self-rated difficulty |
| `study_hours_needed` | 1.0–10.0 | **Target variable** |

---

## 5. Methodology

1. **Data Generation** — Synthetic CSV created with realistic distributions
2. **Preprocessing** — Checked for nulls, reviewed statistics, visualized distributions
3. **Train/Test Split** — 80% train, 20% test (`random_state=42`)
4. **Model Training** — Linear Regression (`sklearn.linear_model.LinearRegression`)
5. **Evaluation** — MAE and R² Score on the test set
6. **Visualization** — Actual vs Predicted scatter plot saved to `results/`

---

## 6. Key Decisions

**Why Linear Regression?** It is a core course algorithm, interpretable, and appropriate for a continuous output like study hours.

**Why synthetic data?** Real data collection was outside the project scope and would raise privacy concerns. Synthetic data allowed full focus on the ML pipeline.

**Why these 4 features?** They are the most commonly cited academic factors affecting exam preparation and are easy for any student to self-report.

---

## 7. Results

| Metric | Value |
|---|---|
| Mean Absolute Error (MAE) | ~2.4- 2.6 hours] |
| R² Score |~0.75- 0.85 |

The MAE shows average prediction error in hours. The R² score indicates how well the model explains variance in study hours. A scatter plot of Actual vs Predicted values is generated and saved automatically.



---

## 8. Challenges Faced

- **No real dataset** — required creating synthetic data and thinking carefully about realistic feature ranges.
- **Understanding metrics** — MAE and R² needed extra reading to interpret correctly together.
- **Project structure** — organizing code into folders and making meaningful Git commits was a new discipline.

---

## 9. What I Learned

- The end-to-end supervised ML workflow: data → model → evaluation → visualization
- How to use `scikit-learn` for regression tasks
- How to interpret MAE and R² Score meaningfully
- The importance of clean project structure, documentation, and version control

---

## 10. Future Scope

- Collect real student data through a department survey
- Compare with advanced models (Random Forest, XGBoost)
- Add cross-validation for more robust evaluation
- Deploy as a Streamlit web app for interactive use

---

## 11. Conclusion

This project applied supervised machine learning to a genuine, everyday problem faced by college students. Building it end-to-end — from defining the problem and creating data to training, evaluating, and documenting — was a practical and rewarding experience that consolidated everything learned in this course.

---

## 12. References

1. Scikit-learn Documentation — https://scikit-learn.org
2. pandas Documentation — https://pandas.pydata.org
3. NumPy Documentation — https://numpy.org/doc
4. Matplotlib Documentation — https://matplotlib.org

---
*Submitted on VITyarthi BY ANUBHAVI RATHORE 25MIM10018| Machine Learning / AI Course — BYOP Capstone*
