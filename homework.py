#Question 1
def hello_name(user_name):
    """Display a hello username message"""
    print(f"Hello_ {user_name.title()}!")

hello_name('kaseykalka')

#Question 2
def first_odds():
    current_number = 0
    while current_number < 100:
        current_number += 1 
        if current_number % 2 == 0:
            continue

print(first_odds())

#Question 3
numbers = [1, 2, 3, 55, 6, 23, 7, 13]
def max_num_in_list(a_list):
    """Returns the max number of a given list"""
    max_num = max(a_list)
    return max_num

print(max_num_in_list(numbers))

#Question 4
def is_leap_year(a_year):
    """Checks to see if the passed value is a leap year or not"""
    if a_year % 4 == 0:
        return True
    else:
        return False
    
print(is_leap_year(2024))

#Question 5
consecutive_numbers = [1, 2, 4, 3, 5]
nonconsecutive_numbers = [1, 3, 5, 7, 9]
def is_consecutive(a_list):
    """Checks to see if all numbers in a list are consecutive"""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

print(is_consecutive(nonconsecutive_numbers))