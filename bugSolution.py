def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average of an empty list is: {result}")

#Improved Solution
def calculate_average_improved(numbers):
    if not numbers:
        return 0 #Return 0 for empty list to avoid ZeroDivisionError
    return sum(numbers) / len(numbers)

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average_improved(my_numbers)
print(f"The improved average is: {result}")

my_empty_list = []
result = calculate_average_improved(my_empty_list)
print(f"The improved average of an empty list is: {result}") 