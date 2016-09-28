perceptron.py

# set up threshold algorithm
# create data set of True (1) and False (-1)
# do algorithm for And, Or, [X_OR] separately

# add in weight bias when summation

# where to put weights initially?
# where do we generate weights so that we can put them back into the algorithm? 

#do you average the outputs to get the final one?


T = 1
F = -1
bias = 1

data = [[T,T], [T,F], [F,T], [F,F]]

weights = list(random.randrange(-1, 1)) #how do you decide range?, also separate lists for separate algorithms?


#simple perceptron
def perceptron():
	data_input1 = T
	data_input2 = F
	weights = list(random.randrange(-1, 1))

	product1 = data_input1 * weights[].random #select one randomly?
	product2 = data_input2 * weights[].random

	summation = product1 + product2 + bias

	if summation > 0: # if summation is a positive number
		output = 1
	elif summation < 0: # if summation is a negative number
		output = -1

	#check to see if output is what was expected >> is this outside of function? 
	if output = expected_output:
		print "correct answer"
	elif output != expected_output:
		print "incorrect answer"
		redo algorithm

		# for i in data_input: #go through each item in the list and multiply it by a random weight

		# 	product[k] = i * weights[j]






def add_perceptron(data, weight): #processor 
	# weights = list(random.randrange(-1, 1)) #how do you decide range?
	products = []
	expected_output = T
	new_weight = [] #a new list?

	for i in data: # each epoch of training
		products.append(product) = i * weights[i]


	for item in products: #summation
		summation = product[n] + product[n+1] + bias #how to not count multiples



	#threhold algorithm; calculate output
	if summation > 0:
		output = T
	elif summation < 0:
		output = F

	#check errors
	error = expected_output - output

	weight_change = error * data[i]

	new_weight.append(old_weight + weight_change)

	return new_weight


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


