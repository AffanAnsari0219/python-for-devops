"""days = set()
days = {"sunday", "sunday", "staturday", "monday"}

print(days)  # Output: {'sunday', 'staturday', 'monday'}
print("Length of days set is :", len(days))  # Output: 3
days.add("friday")
print("Days after adding friday :", days)
days.remove("monday")
print("Days after removing monday :", days)"""

num = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(num)) #list
num_set = set(num)
print("List :", num)

print(type(num_set)) #set
print("Set :", num_set)
