courses = [
	{"name":"Python basics","level":1,"rating":9},
	{"name":"Data Structures","level":1,"rating":7},
	{"name":"OOP in python","level":2,"rating":8},
	{"name":"statistics","level":2,"rating":6},
	{"name":"Machine learning","level":3,"rating":10},
	{"name":"deep learning","level":3,"rating":8}	
]
current_level = 1
goal_level = 3
print("----------means analylis----------")
while(current_level < goal_level):
	difference = goal_level - current_level
	print("\nCurrent level = ", current_level,"\nGoal level = ", goal_level,"\nDifference = ",difference)
	next_level = current_level+1
	for course in courses:
		if course["level"] == next_level:
			print("Recommended courses :", course["name"])
		current_level = next_level
print("\n Global Reached!")
print("----------HEURISTIC SEARCH----------")
sorted_courses = sorted(courses, key=lambda x: x["rating"], reverse=True)
for course in sorted_courses:
	print("Course: ", course["name"], ", Rating: ", course["rating"])
print("Channaveerayya \n2403031460094")