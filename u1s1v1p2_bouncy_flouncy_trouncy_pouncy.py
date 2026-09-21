def final_value_after_operations(operations):
    tigger = 1
    for op in operations:
        if op in ["bouncy", "flouncy"]:
            tigger = tigger + 1
        if op in ["trouncy", "pouncy"]:
            tigger = tigger - 1
    print(tigger)

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)

# Example Output:
# 2
# 4