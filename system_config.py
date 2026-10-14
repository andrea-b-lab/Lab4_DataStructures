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