import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('student_data.csv')

# Features and target
X = df[['past_score', 'attendance_pct', 'sleep_hours', 'subject_difficulty']]
y = df['study_hours_needed']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
print(f"MAE:  {mean_absolute_error(y_test, predictions):.2f}")
print(f"R²:   {r2_score(y_test, predictions):.2f}")

# Plot
plt.scatter(y_test, predictions, alpha=0.6)
plt.xlabel("Actual Study Hours")
plt.ylabel("Predicted Study Hours")
plt.title("Actual vs Predicted")
plt.savefig("results_plot.png")
plt.show()