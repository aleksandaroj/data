

def square_numbers(nums):
    for i in nums:
        yield (i*i)
        
my_nums = square_numbers([1, 2, 3, 4, 5])

for x in my_nums:
    print(x)
    
    
# List comprehension

my_nums = [x*x for x in [1, 2, 3, 4, 5]]

print(my_nums)

# Generator object

my_nums = (x*x for x in [1, 2, 3, 4, 5])

print(my_nums)