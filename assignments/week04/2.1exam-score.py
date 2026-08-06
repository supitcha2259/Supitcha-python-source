scores = []

#input score
for i in range(1,6):
    score = int(input(f"Enter score of student {i}: "))
    scores.append(score)

print()

for i in range(len(scores)):
    score = scores[i]
    if score >= 50:
        result = "Pass"
    else:
        result = "Not Pass"
    print(f"Student {i + 1}: {score} -> {result}")