perceptron.py

# set up threshold algorithm
# create data set of True (1) and False (-1)
# do algorithm for And, Or, [X_OR] separately

# add in weight bias when summation

# where do we generate weights so that we can put them back into the algorithm? 

T = 1
F = -1
bias = 1

data = [[T,T], [T,F], [F,T], [F,F]]

weights = list(random.randrange(-1, 1)) #how do you decide range?



def add_perceptron(data, weight): #processor 
	# weights = list(random.randrange(-1, 1)) #how do you decide range?
	products = []

	expected_output = True
	new_weight = [] #a new list?

	for i in data: # each epoch of training
		products.append(product) = i * weights[i]


	for item in products: #summation
		summation = product[n] + product[n+1] + bias #how to not count multiples



	#threhold algorithm; calculate output
	if summation > 0:
		output = True
	elif summation < 0:
		output = False

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


