"""
@Author: Chandan Sharma.
@GitHub: https://github.com/devchandansh/
"""

"""
Here, bubble sort algorith is implemented by taking user inputs.
It sorted in Ascending Order of the given Input. 
"""


print("How many numbers you want to add.?")
size = input()
unsorted_data = []
print("")
print("Enter the Numbers::")
for n in range(0, int(size)):
	num = input()
	unsorted_data.append(num)

print("--------------------------")
print("You have Entered: ", unsorted_data)

# For Sorting as Ascending Order
for i in range(len(unsorted_data)-1):
	for j in range(len(unsorted_data)-1):
		# Sorted Data for ascending order 
		if unsorted_data[j] > unsorted_data[j+1]:
			unsorted_data[j+1], unsorted_data[j] = unsorted_data[j], unsorted_data[j+1]


print("New Sorted Data (ascending order): ", unsorted_data)
print("--------------------------")


