# Write function called convert_add
def convert_add(nums):
# Takes list of strings as an argument

# converts list to integers and sums list
    int_nums =[]
    for n in nums:
        int_nums.append(int(n))
    print(sum(int_nums))
convert_add(nums = ["1", "3", "5"])
