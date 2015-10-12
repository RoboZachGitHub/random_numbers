# plot random numbers based on different generators

import matplotlib.pyplot as plt



#linear congruent random number generator
def rand_lin_con(length_of_random_sequence):
	sqnc = []
	# r1 is supplied rando seed
	r1 = 10
	# a and c are supplied constants
	a = 9999; c = 32;
	# m is the number from which to get the modulus
	m = 112233

	for i in range(length_of_random_sequence):
		r2 = (a*r1 + c)%m
		sqnc.append(r2)
		r1 = r2

	return sqnc



def name_figure():
	fig_title = raw_input("Type figure title withou extension, will be saves as *.pdf: ")
	return fig_title

sequence = rand_lin_con(300)




# plot pairs to reveal pattern
x_points = []
y_points = []
for i in range(0,len(sequence),2):
	x_points.append(sequence[i])
	y_points.append(sequence[i+1])

# make plot
plt.plot(x_points, y_points, marker='.', linestyle='None')
fig_title = name_figure()
plt.savefig(fig_title)
plt.show()





# plot sequence number vs random number
y_points2 = sequence
x_points2 = []
for i in range(0,len(sequence)):
	x_points2.append(i)

# make plot
plt.plot(x_points2, y_points2, marker='+')
fig_title = name_figure()
plt.savefig(fig_title)
plt.show()



