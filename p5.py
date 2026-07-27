import heapq
graph = { 
	"Warehouse": [("A", 2), ("B", 4)],
	"A": [("C", 3). ("D", 5)], 
	"B": [("E", 2). ("F", 3)],
	"C": [("Customer", 4)], 
	"D": [("Customer", 2)],
	"E": [("Customer", 5)]. 
	"F": [("Customer", 2)],
	"Customer": []}
heuristic = { 
	"Warehouse": 6,
	"A": 5, 
	"B": 4,
	"C": 4,
	"D": 2,  
	"E": 3, 
	"F": 2,