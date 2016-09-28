import random

# set up threshold algorithm
# create data set of True (1) and False (-1)
# do algorithm for And, Or, [X_OR] separately

# add in weight bias when summation

# where to put weights initially?
# where do we generate weights so that we can put them back into the algorithm? 

#do you average the outputs to get the final one?

#use a while loop to go through until correct answer is reached? 
#> yes, but why is summation 0 and still producing 1 or -1? and when I try weights, super long list...
#because it was 8, so fixed > NO, not if it goes into the while

#do we need a bias if we're assigning either a 1 or -1?



T = 1
F = -1
bias = 1
expected_output = T

#input and weights should be 2 lists

data_input = [T, T]
# data_input = [[T,T], [T,F], [F,T], [F,F]]


summation = 0

weights = []


def activate(summation):

	

	for i in range(0,2):
		weights.append(random.uniform(-1, 1)) #how do you decide range?, also separate lists for separate algorithms?
	
	for i in data_input: #go through each item in the list and multiply it by a random weight
		summation += i * weights[i] #does that make sense in python?

	if summation > 0: # if summation is a positive number
		return 1
	elif summation < 0: # if summation is a negative number
		return -1


output = activate(summation)
	
def learning(output): #need to know what the weights are?
	if output == expected_output: 
		print str(weights) + str(output) + " correct answer" #works


	elif output != expected_output: #BROKEN
		print str(weights) + str(output) + " going to try again"

		while output != expected_output:
			print str(weights) + str(output) + " going to try again"
			output = activate(summation) #repeat function
			
			# print output 

			if output == expected_output: #check to see if answer is correct
				# ouput = expected_output
				print str(weights) + str(output) + " correct answer"
				break #why you no break?
#why returns didn't work?
	


perceptron = learning(output)





	#check errors
	# error = output_expected - output

	# weight_change = error * data[i]

	# new_weight.append(old_weight + weight_change)

	# return new_weight






