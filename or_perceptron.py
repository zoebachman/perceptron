import random

# set up threshold algorithm
# create data set of True (1) and False (-1)
# do algorithm for And, Or, [X_OR] separately

# add in weight bias when summation

# where to put weights initially?
# where do we generate weights so that we can put them back into the algorithm? 

#do you average the outputs to get the final one?

#use a while loop to go through until correct answer is reached?


T = 1
F = -1
bias = 1
expected_output = T

#input and weights should be 2 lists

data_input = [T, T]
# data_input = [[T,T], [T,F], [F,T], [F,F]]


summation = 0

weights = []

def or_perceptron(data, weight): # processor
	# weights = list(random.randrange(-1, 1)) #how do you decide range?
	products = []
	output_expected = False

	new_weight = [] #a new list?

	for i in data: # each epoch of training
		products.append(product) = i * weights[i]


	for item in products: #summation
		summation = product[n] + product[n+1] + bias #how to not count multiples

	#threhold algorithm
	if summation > 0:
		output = True
	elif summation < 0:
		output = False

	#check errors
	error = output_expected - output

	weight_change = error * data[i]

	new_weight.append(old_weight + weight_change)

	return new_weight
