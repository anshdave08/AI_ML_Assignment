import json
import os
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Load student data
# -------------------------------
data_file = "data/student_score.json"

with open(data_file, "r") as file:
    students = json.load(file)

names = [student["name"] for student in students]
scores = [student["score"] for student in students]

# -------------------------------
# Step 2: Calculate average score
# -------------------------------
average_score = sum(scores) / len(scores)
print(f"Average Score: {average_score:.2f}")

# -------------------------------
# Step 3: Create output folder
# -------------------------------
os.makedirs("outputs", exist_ok=True)

# -------------------------------
# Step 4: Plot bar chart
# -------------------------------
plt.figure(figsize=(10, 6))
plt.bar(names, scores)
plt.axhline(
    y=average_score,
    linestyle="--",
    label=f"Average Score ({average_score:.2f})"
)

plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Test Scores")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# -------------------------------
# Step 5: Save chart
# -------------------------------
output_path = "outputs/student_scores_bar_chart.png"
plt.savefig(output_path)
plt.show()

print(f"Bar chart saved at: {output_path}")
