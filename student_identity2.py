student_info = (
"BORON",
2,
"SEVENTEEN"
)

print("=== STUDENT IDENTITY ===")
print(f"Student Name: {student_info[0]}")
print(f"Seed Number: {student_info[1]}")
print(f"Favorite Artist: {student_info[2]}")

print("\nStudent Information (Tuple):")
print(student_info)

# Student Identity
LAST_NAME = "Boron" 
STUDENT_ID = "TUPM-26-4312"
FAVORITE_ARTIST = "Seventeen"
SEED_NUM = 2

from student_identity import LAST_NAME, SEED_NUM , FAVORITE_ARTIST

TEST_SOURCES = [
f"{LAST_NAME}_T1",
f"{LAST_NAME}_T2",
f"{LAST_NAME}_T3",
f"{LAST_NAME}_T4",
f"{LAST_NAME}_T5"
]

MEASUREMENT_CATEGORIES = [
"TEMPERATURE",
"VOLTAGE",
"CURRENT",
"PRESSURE",
"SPEED"
]

system_config = {
"student": LAST_NAME,
"seed_number": SEED_NUM,
"favorite_artist": FAVORITE_ARTIST,
"test_sources": TEST_SOURCES,
"measurement_categories": MEASUREMENT_CATEGORIES
}


if __name__ == "__main__":
    print(f"=== ENGINEERING TEST DATA CONFIGURATION ===")

for key, value in system_config.items():
    print(f"{key}: {value}")