# Inventory Management using Intelligent Agent
# Demonstrating Hill Climbing and Best First Search

inventory = {
    "Laptop": {"stock": 50, "demand": 60},      
    # Difference = 10
    "Mobile": {"stock": 20, "demand": 25},      
    # Difference = 5
    "Headphone": {"stock": 70, "demand": 40},   
    # Difference = 30
    "Keyboard": {"stock": 10, "demand": 50}     
    # Difference = 40
}

print("===== INVENTORY STATUS =====")

for product, data in inventory.items():
    difference = abs(data["demand"] - data["stock"])
    print(product, "Difference =", difference)


# ---------------------------------
# Hill Climbing
# ---------------------------------

def hill_climbing(inventory):

    products = list(inventory.keys())

    current_product = products[0]

    current_score = abs(
        inventory[current_product]["demand"] -
        inventory[current_product]["stock"]
    )

    print("\nHill Climbing Path:")
    print(current_product, "=", current_score)

    for i in range(1, len(products)):

        next_product = products[i]

        next_score = abs(
            inventory[next_product]["demand"] -
            inventory[next_product]["stock"]
        )

        if next_score > current_score:

            current_product = next_product
            current_score = next_score

            print("Moved to", current_product, "=", current_score)

        else:

            print("Stopped because",
                  next_score,
                  "<",
                  current_score)

            break

    return current_product, current_score


# ---------------------------------
# Best First Search
# ---------------------------------

def best_first_search(inventory):

    priority_list = []

    for product, data in inventory.items():

        priority = abs(data["demand"] - data["stock"])

        priority_list.append((priority, product))

    priority_list.sort(reverse=True)

    return priority_list


# Run Hill Climbing

hill_product, hill_value = hill_climbing(inventory)

print("\n===== HILL CLIMBING RESULT =====")
print("Selected Product:", hill_product)
print("Difference:", hill_value)


# Run Best First Search

result = best_first_search(inventory)

print("\n===== BEST FIRST SEARCH RESULT =====")

for priority, product in result:
    print(product, "Priority =", priority, "\nChannaveerayya \n 2403031460094")
