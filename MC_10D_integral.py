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


