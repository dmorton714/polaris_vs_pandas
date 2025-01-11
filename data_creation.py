import pandas as pd
import random

first_names = [
    "James", "Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia",
    "Benjamin", "Isabella", "Elijah", "Mia", "Lucas", "Amelia", "Mason",
    "Harper", "Ethan", "Evelyn", "Alexander", "Charlotte"
]

last_names = [
    "Johnson", "Smith", "Williams", "Brown", "Taylor", "Anderson", "Martinez",
    "White", "Harris", "Lewis", "Clark", "Walker", "Hall", "Allen", "Young",
    "King", "Scott", "Green", "Baker", "Carter"
]

# Generate random student data
data = {
    "First_Name": [random.choice(first_names) for _ in range(2000000)],
    "Last_Name": [random.choice(last_names) for _ in range(2000000)],
    "Student_ID": [f"S{str(i).zfill(5)}" for i in range(1, 2000001)]
}


students = pd.DataFrame(data)
students.head()

students.to_csv("data/students.csv", index=False)

# ___________________________________________________________________________

num_students = 2000000
num_assignments = 10

# Generate assignment names
assignment_names = [f"Assignment_{i+1}" for i in range(num_assignments)]

# Generate random grades data
grades_data = {
    "Student_ID": [f"S{str(i).zfill(5)}" for i in range(1, num_students + 1)]
}

for assignment in assignment_names:
    grades_data[assignment] = [random.randint(50, 100) for _ in range(num_students)]


grades_df = pd.DataFrame(grades_data)
grades_df.head()


grades_df.to_csv("data/grades.csv", index=False)

# ___________________________________________________________________________

num_students = 2000000
num_weeks = 10

# Generate week names 
week_names = [f"Week_{i+1}" for i in range(num_weeks)]

# Generate random attendance data
attendance_data = {
    "Student_ID": [f"S{str(i).zfill(5)}" for i in range(1, num_students + 1)]
}
for week in week_names:
    attendance_data[week] = [random.choice(["Present", "Absent"]) for _ in range(num_students)]


attendance_df = pd.DataFrame(attendance_data)
attendance_df.head()


attendance_df.to_csv("data/attendance.csv", index=False)
