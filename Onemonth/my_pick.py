import random 

memory = ["TIP","Visualisation","See Link Go"]

subject_of_study =["Maths","Programming","sciences"]

memory_select = random.choice(memory)
study_point = random.choice(subject_of_study)

print(f"You are studying {study_point}, i bet memory technique {memory_select} could be a good choice.")imo