import random 

memory = ["TIP","Visualisation","See","Go","Link"]

subject_of_study =["Maths","Programming","sciences"]

memory_select = random.choice(memory)
study_point = random.choice(subject_of_study)

print(f"What area of class {study_point} are you doing, i bet {memory_select} could be a good choice")