import numpy as np



def summation_tenD(number_samples):
	total_summation = float(0.0)

	for i in range(number_samples):
		x_list_tenD = np.random.random_sample(10)
		summation = float(0.0)
		for x in x_list_tenD:
			summation += x
	
		integrand_sample = summation*summation
		total_summation += integrand_sample

	integral_eval =	total_summation/float(number_samples)
	return integral_eval





N = 100000 #number of MC samples
integral_tenD = summation_tenD(N)

print integral_tenD

#integral_summation = float(0.0)
#for i in range(0,N):
	# b is upper integrand range a i lower integrand range
#	a = 0
#	b = 1
#	x_i = random.uniform(a,b)
#	summation += func(x_i)

#MC_integral = summation/float(N)
#analytic_integral = float(int_x_sqr(0,1))




#print "MC Integral is: %f" % MC_integral
#print "Analytical Integral is: %f" % analytic_integral

