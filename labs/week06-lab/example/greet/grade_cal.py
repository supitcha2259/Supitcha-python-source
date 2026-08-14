# Example 1: Grade calculator
def calculate_grade(score):
    """Converts numerical score to letter grade"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("Grade Calculator:")
test_scores = [95, 87, 73, 68, 45]
for score in test_scores:
    grade = calculate_grade(score)
    print(f"Score {score} = Grade {grade}")
print()