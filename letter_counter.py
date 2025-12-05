from collections import Counter

name = "Haiqa Noor"
clean_name = name.replace(" ", "")
letter_count = Counter(clean_name)

print("Letter frequencies")
for letter , count in letter_count.items():
    print(f"{letter}: {count}")

unique_letters = [letter for letter , count in letter_count.items()if count == 1]

print("\nUnique letters: ", unique_letters)
