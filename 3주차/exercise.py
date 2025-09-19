import random

scores = dict()
for i in range(11, 51):
    scores['S' + str(i)] = random.randrange(50, 101)

max_score = max(scores.values())
for student, score in scores.items():
    if score == max_score:
        print(student, score)
        break