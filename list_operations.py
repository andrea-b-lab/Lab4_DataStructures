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