import sys
# Checking the size of genertor expression


l = [x for x in range(100000)]
print(type(l))
print("List size of 10000 elements: ", sys.getsizeof(l))


gl = (x for x in range(10000))
print(type(gl))
print("Generator size of 10000 elements: ", sys.getsizeof(gl))
