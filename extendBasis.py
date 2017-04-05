import numpy as np
dim = int(raw_input("Enter the number of dimensions :"))
matrix = []
print "Enter the matrix : "
for i in range(dim):
	vector = list(map(int,raw_input().split()))
	matrix.append(vector)

print
print "Starting the extension -------------------"
print

def extend(matrix,n):
	orthonorm = gramSchmidt(matrix,n)
	ext_matrix = []
	for vector in orthonorm:
		x = vector.tolist()
		x.append(0)
		ext_matrix.append(x)
	zeros = np.zeros(n)
	y = zeros.tolist()
	y.append(1)
	ext_matrix.append(y)
	return ext_matrix

def gramSchmidt(matrix,n):
	orthonorm = []
	for vector in matrix:
		b = vector
		zeros = np.zeros(n)
		for v in orthonorm:
			zeros += np.dot(b,v)/np.dot(v,v)*v
		orthonorm.append((b-zeros)/np.dot(b-zeros,b-zeros)**0.5)
	return np.array(orthonorm)

for i in range(dim,10):
	print i+1
	print "--------------------------------------"
	new_matrix = extend(matrix, i)
	print np.array(new_matrix)
	print "--------------------------------------"
	matrix = new_matrix