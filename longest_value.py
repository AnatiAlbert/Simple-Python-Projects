def longest_value(d: dict):
    longest = max(d.values(), key=len)
    return longest

fruits = {"fruit": "apple", "color": "green"}
print(longest_value(fruits))
