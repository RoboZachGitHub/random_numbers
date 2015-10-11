# plot random numbers based on different generators

import matplotlib.pyplot as plt



#linear congruent random number generator
def rand_lin_con(length_of_random_sequence):
	sqnc = []
	# r1 is supplied rando seed
	r1 = 10
	# a and c are supplied constants
	a = 57; c = 1;
	# m is the number from which to get the modulus
	m = 256

	for i in range(length_of_random_sequence):
		r2 = (a*r1 + c)%m
		sqnc.append(r2)
		r1 = r2

	return sqnc


sequence = rand_lin_con(300)




# plot pairs to reveal pattern
x_points = []
y_points = []
for i in range(0,len(sequence),2):
	x_points.append(sequence[i])
	y_points.append(sequence[i+1])

# make plot
plt.plot(x_points, y_points, marker='.', linestyle='None')
plt.show()





# plot sequence number vs random number
y_points2 = sequence
x_points2 = []
for i in range(0,len(sequence)):
	x_points2.append(i)

# make plot
plt.plot(x_points2, y_points2, marker='+')
plt.show()



