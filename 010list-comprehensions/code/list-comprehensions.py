# Let's learn about list comprehensions! 
# You are given three integers x, y, and z representing the
#  dimensions of a cuboid along with an integer . 
# Print a list of all possible coordinates given by (i,j,k)
#  on a 3D grid where the sum of i+j+k is not equal to n
# Here, 0<i<x; 0<j<y; 0<k<z. Please use list comprehensions
#  rather than multiple loops, as a learning exercise.

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
n = int(input("n: "))

lst = [x, y, z]

xs = [i for i in range(x+1) if x >= 0]
print(xs)

ys = [i for i in range(y+1) if y >= 0]
print(ys)

zs = [i for i in range(z+1) if z >= 0]
print(zs)

perm = [[i, j, k]   for i in xs
                    for j in ys
                    for k in zs]
                
#print(perm)

dont_sum_to_n = [i for i in perm 
                    if i[0] + i[1] + i[2] != n]

print(dont_sum_to_n)