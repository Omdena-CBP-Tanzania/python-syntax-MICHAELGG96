def format_string(name, age):
    """
    name= "Michael"
    age= 28
    result= f"My name is {name} and i am {age} years old"
    print(result)

def conditional_check(number):
    """
    number = int(input("enter a number:"))
    if number > 10:
        print("greater")
    elif number < 10:
        print("lesser")
    else:
        print("equal")
    
def loop_sum(n):
    #initialize the sum to 0
    total = 0
    #use a loop to add all numbers from 1 to n
    for i in range(1,n + 1):
        total += i #Add each number to the total

    return total #Return the total sum
# Call the function with n=5
result = loop_sum(5)
print(f"The sum of numbers from 1 to 5 is: {result}")

def list_operations(numbers):
    if not numbers: #check if the list empty
        return "The list is empty. No operations can be performed."
    
    # perform operations on the list
    total = sum(numbers) #calculate the sum of all numbers
    maximum = max(numbers) #find the largest number
    minimum = min(numbers) #find the smallest number
    average = total/len(numbers) #calculate the average

    #return the results as a dictionary
    return {
        "Sum":total,
        "Maximum":maximum,
        "Minimum":minimum,
        "Average":average,
    }

#Input list of numbers
numbers = [10,20,30,40,50]

#call the function
result = list_operations(numbers)

#print the result
print(result) 

def perform_operations(numbers):
    """
        Perform operations on a list of numbers.
    
    Args:
        numbers (list): List of numbers
    

    Returns:
        tuple: (sum, max, min)
    """
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    total_sum = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total_sum, maximum, minimum
#Example
numbers_list = [5, 10, -3, 7, 2]
result = perform_operations(numbers_list)
print("Results:", result)
def perform_operations(numbers):
    """
    Perform operations on a list of numbers.

    Args:
        numbers (list): List of numbers.

    Returns:
        tuple: (sum, max, min)
    """
    if not numbers:
        return (0, None, None)
    total_sum = sum(numbers)
    max_value = max(numbers)
    min_value = min(numbers)

    return (total_sum, max_value, min_value)
#Example
numbers = [10, 20, 30, 40, 50]
result = perform_operations(numbers)
print(f"Sum: {result[0]}, Max: {result[1]}, Min: {result[2]}")

def dict_operations(students_dict):
    """


Find students with scores above 80.

    Args:
        students_dict (dict): Dictionary of student names and scores.

    Returns:
        list: Names of students with scores > 80.
    """
    return [name for name, score in students_dict.items() if score > 80]
#Example
students = {
    "Alice": 85,
    "Bob": 75,
    "Charlie": 90,
    "David": 60,
    "Eve": 95
}
result = dict_operations(students)
print(f"Students with scores above 80: {result}")

def set_operations(list1, list2):
    """
    Perform set operations on two lists.

    Args:
        list1 (list): First list of elements.
        list2 (list): Second list of elements.

    Returns:
        dict: A dictionary containing the following set operations:
            - union: All unique elements from both lists.
            - intersection: Elements common to both lists.
            - difference: Elements in list1 but not in list2.
            - symmetric_difference: Elements in either list1 or list2 but not both.
    """
    set1 = set(list1)
    set2 = set(list2)

    return {
        "union": set1 | set2,
        "intersection": set1 & set2,
        "difference": set1 - set2,
        "symmetric_difference": set1 ^ set2
    }

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = set_operations(list1, list2)

print(f"Union: {result['union']}")
print(f"Intersection: {result['intersection']}")
print(f"Difference: {result['difference']}")
print(f"Symmetric Difference: {result['symmetric_difference']}")
    
def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        dict: Results of arithmetic operations including:
            - addition
            - subtraction
            - multiplication
            - division (if b != 0)
            - modulo (if b != 0)
    """
    results = {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
    }

    # Handle division and modulo only if b is not zero
    if b != 0:
        results["division"] = a / b
        results["modulo"] = a % b
    else:
        results["division"] = "undefined (division by zero)"
        results["modulo"] = "undefined (modulo by zero)"

    return results

#Example
a = 10
b = 5

result = arithmetic_ops(a, b)
print(f"Addition: {result['addition']}")
print(f"Subtraction: {result['subtraction']}")
print(f"Multiplication: {result['multiplication']}")
print(f"Division: {result['division']}")
print(f"Modulo: {result['modulo']}")

def logical_ops(x, y):
    """
    Perform logical operations.

    Args:
        x (bool): First boolean.
        y (bool): Second boolean.

    Returns:
        dict: Results of logical operations including:
            - AND
            - OR
            - NOT x
            - NOT y
     
        
        #Example
        - XOR
    """
    return {
        "AND": x and y,
        "OR": x or y,
        "NOT_x": not x,
        "NOT_y": not y,
        "XOR": x ^ y  # XOR: True if only one of x or y is True
    }

#Example
x = True
y = False

result = logical_ops(x, y)
print(f"AND: {result['AND']}")
print(f"OR: {result['OR']}")
print(f"NOT x: {result['NOT_x']}")
print(f"NOT y: {result['NOT_y']}")
print(f"XOR: {result['XOR']}")

def bitwise_ops(a, b):
    """
    Perform bitwise operations.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        dict: Results of bitwise operations including:
            - AND
            - OR
            - XOR
            - NOT a
            - NOT b
            - Left Shift a by 1
            - Right Shift b by 1
    """
    return {
        "AND": a & b,
        "OR": a | b,
        "XOR": a ^ b,
        "NOT_a": ~a,
        "NOT_b": ~b,
        "Left_Shift_a": a << 1,
        "Right_Shift_b": b >> 1,
    }

a = 10  # Binary: 1010
b = 5   # Binary: 0101

result = bitwise_ops(a, b)

print(f"AND: {result['AND']}")                  # 0 (0000)
print(f"OR: {result['OR']}")                    # 15 (1111)
print(f"XOR: {result['XOR']}")                  # 15 (1111)
print(f"NOT a: {result['NOT_a']}")              # -11 (Two's complement of 10)
print(f"NOT b: {result['NOT_b']}")              # -6 (Two's complement of 5)
print(f"Left Shift a: {result['Left_Shift_a']}") # 20 (Binary: 10100)
print(f"Right Shift b: {result['Right_Shift_b']}") # 2 (Binary: 0010)
