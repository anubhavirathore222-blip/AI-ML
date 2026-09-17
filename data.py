import pandas as pd
import numpy as np

np.random.seed(42)
n = 200

data = pd.DataFrame({
    'past_score':       np.random.randint(40, 100, n),
    'attendance_pct':   np.random.randint(50, 100, n),
    'sleep_hours':      np.random.uniform(4, 9, n).round(1),
    'subject_difficulty': np.random.randint(1, 6, n)  # 1=easy, 5=hard
    
})
data['study_hours_needed'] = (
    (100 - data['past_score']) * 0.05 +
    (100 - data['attendance_pct']) * 0.03 +
    (9 - data['sleep_hours']) * 0.4 +
    data['subject_difficulty'] * 0.6 +
    np.random.normal(0, 0.5, n)  # small noise
).round(1).clip(1, 10)

data.to_csv('student_data.csv', index=False)
