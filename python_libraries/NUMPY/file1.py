import numpy as np

a = np.array([1,2,3])#normal array
a2 = np.array([[1,23,4], [45, 66, 78], [45, 77, 6]])
a_changed =np.array(a[:], dtype = 'int16')#changes a 'int32'-> 'int16'
#............get dimension............#

print("\nmy array is a {} dimensional array.\n".format(a.ndim))#print dimension

#............get shape...............#
#* its sensitive to inhomogeneous arrays, it will bring a value error
print("the array has a shape of {} rows to column respectively \n".format(a2.shape))

#...........get type ...........#

print("my array is of \t{}\t data type\n".format(a.dtype))

#............... get size ..........#
print("The size of my array'a' is {}bytes\n".format(a.itemsize))
print("\t * on changing to 'int16' the size reduced to {}bytes".format(a_changed.itemsize))

#............. get total size ..................#
print("total size is a.size(number of elements) {} * a.itemsize(memory it occupies) {}".format(a.size, a.itemsize))
size = a.size * a.itemsize
print("thus size is {}bytes".format(size))#we can use a.nbytes instead of size

