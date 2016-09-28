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


def activate(summation):
	weights = []

	for i in range(0,8):
		weights.append(random.uniform(-1, 1)) #how do you decide range?, also separate lists for separate algorithms?
	
	for i in data_input: #go through each item in the list and multiply it by a random weight
		summation += i * weights[i] #does that make sense in python?

	if summation > 0: # if summation is a positive number
		return 1
	elif summation < 0: # if summation is a negative number
		return -1


output = activate(summation)
	
def learning(output):
	if output == expected_output: 
		print str(output) + " correct answer"


	elif output != expected_output:
		print str(output) + " going to try again"

		while output != expected_output:
			print str(output) + " going to try again"
			output = activate(summation) #repeat function
			
			# print output 

			if output == expected_output: #check to see if answer is correct
				# ouput = expected_output
				print str(output) + " correct answer"
				break #why you no break?
#why returns didn't work?
	


perceptron = learning(output)







# def add_perceptron(data, weight): #processor 
# 	# weights = list(random.randrange(-1, 1)) #how do you decide range?
# 	products = []
# 	expected_output = T
# 	new_weight = [] #a new list?

# 	for i in data: # each epoch of training
# 		products.append(product) = i * weights[i]


# 	for item in products: #summation
# 		summation = product[n] + product[n+1] + bias #how to not count multiples



# 	#threhold algorithm; calculate output
# 	if summation > 0:
# 		output = T
# 	elif summation < 0:
# 		output = F

# 	#check errors
# 	error = expected_output - output

# 	weight_change = error * data[i]

# 	new_weight.append(old_weight + weight_change)

# 	return new_weight


# def or_perceptron(data, weight): # processor
# 	# weights = list(random.randrange(-1, 1)) #how do you decide range?
# 	products = []
# 	output_expected = False

# 	new_weight = [] #a new list?

# 	for i in data: # each epoch of training
# 		products.append(product) = i * weights[i]


# 	for item in products: #summation
# 		summation = product[n] + product[n+1] + bias #how to not count multiples

# 	#threhold algorithm
# 	if summation > 0:
# 		output = True
# 	elif summation < 0:
# 		output = False

# 	#check errors
# 	error = output_expected - output

# 	weight_change = error * data[i]

# 	new_weight.append(old_weight + weight_change)

# 	return new_weight


