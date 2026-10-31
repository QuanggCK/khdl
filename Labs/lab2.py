# Work with Scatter plot

# Ex: Load study hours

import pandas as pd
import matplotlib.pyplot as plt

studyhours_df = pd.read_csv('FileExcel/studyhours.csv')

print(studyhours_df.head(5))

print(studyhours_df.describe())

# Male a scatter plot of study hours and final grades

plt.figure(figsize=(10, 6))
study_hours = studyhours_df['Study Hours']
exam_score = studyhours_df['Exam Score']
plt.scatter(study_hours, exam_score, alpha=0.75, label='Study Hours vs Exam Score')
plt.xlabel("Study hours")
plt.ylabel("Exam Score")
plt.show()

# Load the Iris dataset and make scatter plot