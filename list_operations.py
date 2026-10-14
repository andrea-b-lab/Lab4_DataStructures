from student_identity import LAST_NAME, SEED_NUM, FAVORITE_ARTIST
from student_identity import TEST_SOURCES, MEASUREMENT_CATEGORIES

test_data = []

for i, source in enumerate(TEST_SOURCES):
    for j, category in enumerate(MEASUREMENT_CATEGORIES):
        artist_char = FAVORITE_ARTIST[(i + j) % len(FAVORITE_ARTIST)]
        value = ord(artist_char) + SEED_NUM + i + j

        test_data.append([source, category, value])

test_data.append(test_data[0].copy())

print("=== ENGINEERING TEST DATA ORGANIZER ===")
print(f"Student: {LAST_NAME}")
print(f"Seed Number: {SEED_NUM}")
print(f"Favorite Artist: {FAVORITE_ARTIST}")

print("\n--- GENERATED TEST DATA ---")
for record in test_data: 
    print(record)

organized_data = {}

for record in test_data:
    category = record[1]

if category not in organized_data:
    organized_data[category] = []

organized_data[category].append(record)

print("\n--- ORGANIZED TEST DATA ---") 
for category, records in organized_data.items():
    print(f"\n{category}:")
for record in records:
    print(record)

ordered_data = sorted(test_data, key=lambda record: (record[1], record[2]))

print("\n--- ORDERED TEST DATA ---")
for record in ordered_data:
    print(record)

values = [record[2] for record in test_data]

print("\n--- NUMERICAL SUMMARY ---")
print(f"Total records: {len(test_data)}")
print(f"Minimum value: {min(values)}")
print(f"Maximum value: {max(values)}")
print(f"Average value: {sum(values) / len(values):.2f}")

print("\nData organization complete.")

# LAB 4: STUDENT PERFORMANCE REPORT
# Data Structures

# -----------------------------------------
# 1. STUDENT-SPECIFIC INPUTS
# -----------------------------------------

LAST_NAME = input("Enter your last name: ").strip().upper()
FAVORITE_ARTIST = input("Enter your favorite artist: ").strip().upper()

while not LAST_NAME or not FAVORITE_ARTIST:
    print("Please enter both your last name and favorite artist.")
    LAST_NAME = input("Enter your last name: ").strip().upper()
    FAVORITE_ARTIST = input("Enter your favorite artist: ").strip().upper()

while True:
    try:
        SEED_NUM = int(input("Enter your seed number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# -----------------------------------------
# 2. GENERATE STUDENT NAMES AND SUBJECTS
# -----------------------------------------

STUDENT_LABELS = [
    "Student_1",
    "Student_2",
    "Student_3",
    "Student_4",
    "Student_5"
]

STUDENTS = [
    f"{LAST_NAME}_{label}"
    for label in STUDENT_LABELS
]

SUBJECTS = [
    "PROGRAMMING",
    "MATHEMATICS",
    "ELECTRONICS",
    "PHYSICS",
    "ENGLISH"
]

# -----------------------------------------
# 3. PERFORMANCE CATEGORY FUNCTION
# -----------------------------------------

def get_category(score):
    if score is None:
        return "INCOMPLETE"
    elif score >= 90:
        return "EXCELLENT"
    elif score >= 80:
        return "VERY GOOD"
    elif score >= 75:
        return "PASSED"
    else:
        return "FAILED"

# -----------------------------------------
# 4. GENERATE PERFORMANCE RECORDS
# -----------------------------------------

records = []

for i, student in enumerate(STUDENTS):
    for j, subject in enumerate(SUBJECTS):

        # Use artist character positions and seed number
        artist_char = FAVORITE_ARTIST[
            (i + j) % len(FAVORITE_ARTIST)
        ]

        score = (
            ord(artist_char) + SEED_NUM + i + j
        ) % 101

        records.append({
            "student": student,
            "subject": subject,
            "score": score
        })

# -----------------------------------------
# 5. INCLUDE AN INCOMPLETE RECORD
# -----------------------------------------

# Set one existing student's score to missing.
records[-1]["score"] = None

# -----------------------------------------
# 6. INCLUDE ONE REPEATED RECORD
# -----------------------------------------

# Repeat the first student-subject record.
records.append(records[0].copy())

# -----------------------------------------
# 7. IDENTIFY REPEATED AND INCOMPLETE RECORDS
# -----------------------------------------

seen = set()
repeated_records = []
incomplete_records = []
unique_records = []

for record in records:
    key = (record["student"], record["subject"])

    if key in seen:
        repeated_records.append(record)
    else:
        seen.add(key)
        unique_records.append(record)

    if record["score"] is None:
        incomplete_records.append(record)

# -----------------------------------------
# 8. ORGANIZE RECORDS
# -----------------------------------------

organized_records = sorted(
    records,
    key=lambda record: (
        record["student"],
        record["subject"]
    )
)

# -----------------------------------------
# 9. DISPLAY GENERATED PERFORMANCE RECORDS
# -----------------------------------------

print("\n" + "=" * 75)
print("             FINAL STUDENT PERFORMANCE REPORT")
print("=" * 75)

print(f"Last Name: {LAST_NAME}")
print(f"Favorite Artist: {FAVORITE_ARTIST}")
print(f"Seed Number: {SEED_NUM}")
print(f"Total Records: {len(records)}")

print("\n1. GENERATED PERFORMANCE RECORDS")
print("-" * 75)
print(f"{'STUDENT':<25}{'SUBJECT':<18}{'SCORE':<12}{'CATEGORY'}")
print("-" * 75)

for record in records:
    score = record["score"]
    score_display = "N/A" if score is None else str(score)

    print(
        f"{record['student']:<25}"
        f"{record['subject']:<18}"
        f"{score_display:<12}"
        f"{get_category(score)}"
    )

# -----------------------------------------
# 10. ORGANIZED STUDENT/SUBJECT DATA
# -----------------------------------------

print("\n2. ORGANIZED STUDENT/SUBJECT DATA")
print("-" * 75)

for record in organized_records:
    score = record["score"]
    score_display = "N/A" if score is None else str(score)

    print(
        f"{record['student']} | "
        f"{record['subject']} | "
        f"{score_display}"
    )

# -----------------------------------------
# 11. REPEATED AND INCOMPLETE RECORDS
# -----------------------------------------

print("\n3. REPEATED RECORDS")
print("-" * 75)

if repeated_records:
    for record in repeated_records:
        print(
            f"{record['student']} - "
            f"{record['subject']} - "
            f"Score: {record['score']}"
        )
else:
    print("No repeated records found.")

print("\nINCOMPLETE RECORDS")
print("-" * 75)

if incomplete_records:
    for record in incomplete_records:
        print(
            f"{record['student']} - "
            f"{record['subject']} - "
            "Missing score"
        )
else:
    print("No incomplete records found.")

# -----------------------------------------
# 12. PERFORMANCE CATEGORIES
# -----------------------------------------

print("\n4. PERFORMANCE CATEGORIES")
print("-" * 75)

category_counts = {
    "EXCELLENT": 0,
    "VERY GOOD": 0,
    "PASSED": 0,
    "FAILED": 0,
    "INCOMPLETE": 0
}

for record in records:
    category = get_category(record["score"])
    category_counts[category] += 1

for category, count in category_counts.items():
    print(f"{category:<15}: {count}")

# -----------------------------------------
# 13. STUDENT SUMMARIES
# -----------------------------------------

print("\n5. STUDENT SUMMARIES")
print("-" * 75)

for student in STUDENTS:
    student_records = [
        record for record in unique_records
        if record["student"] == student
    ]

    valid_scores = [
        record["score"] for record in student_records
        if record["score"] is not None
    ]

    if valid_scores:
        average = sum(valid_scores) / len(valid_scores)
        highest = max(valid_scores)
        lowest = min(valid_scores)

        print(f"\nStudent: {student}")
        print(f"Valid Scores: {len(valid_scores)}")
        print(f"Average: {average:.2f}")
        print(f"Highest Score: {highest}")
        print(f"Lowest Score: {lowest}")
    else:
        print(f"\nStudent: {student} - No valid scores")

# -----------------------------------------
# 14. SUBJECT SUMMARIES
# -----------------------------------------

print("\nSUBJECT SUMMARIES")
print("-" * 75)

for subject in SUBJECTS:
    subject_records = [
        record for record in unique_records
        if record["subject"] == subject
    ]

    valid_scores = [
        record["score"] for record in subject_records
        if record["score"] is not None
    ]

    if valid_scores:
        average = sum(valid_scores) / len(valid_scores)

        print(
            f"{subject:<18} "
            f"Average: {average:.2f} | "
            f"Highest: {max(valid_scores)} | "
            f"Lowest: {min(valid_scores)}"
        )
    else:
        print(f"{subject}: No valid scores")

# -----------------------------------------
# 15. ORDERED RESULTS
# -----------------------------------------

print("\n6. ORDERED RESULTS")
print("-" * 75)

ranked_students = []

for student in STUDENTS:
    student_records = [
        record for record in unique_records
        if record["student"] == student
    ]

    valid_scores = [
        record["score"] for record in student_records
        if record["score"] is not None
    ]

    if valid_scores:
        average = sum(valid_scores) / len(valid_scores)
        ranked_students.append((student, average))

ranked_students.sort(key=lambda item: (-item[1], item[0]))

for rank, (student, average) in enumerate(ranked_students, start=1):
    print(f"{rank}. {student} - Average: {average:.2f}")

print("\n" + "=" * 75)
print("                 END OF REPORT")
print("=" * 75)
