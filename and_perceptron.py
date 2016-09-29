import random
import numpy as np

# set up threshold algorithm
#do you average the outputs to get the final one?

# The Procedure:

# Provide the Perceptron with inputs for which there are known outputs.
# Ask the Perceptron to guess the outputs.
# Compute the error.
# Adjust all weights according to error.
# Return to Step 1 and repeat.


T = 1
F = -1
bias = 1


data_input = [[T,T], [T,F], [F,T], [F,F]]
guess = []
expected_output = [T, F, F, F]


weights_list = []
error_list = []

# new_weights = []
learning_constant = .01
# summation = 0 #got this from NoC

first_time = True

for i in range(1): #run the perceptron an x number of times
	for j in range(len(data_input)): #for each index in data_input (so 4 times)
		
		#seed random weights to start
		if first_time == True:
			weights = 0.9 * np.random.random(3)+0.01
			first_time = False


		print weights[0]
		#ask the perceptron to guess the outputs
		summation = (data_input[j][0] * weights[0]) + (data_input[j][1] * weights[1]) + (bias * weights[2])

		#threhold algorithm; calculate output > is this ok? only dealing with ints...will it ever get closer then?
		if summation > 0: # if summation is a positive number
			guess = T
		elif summation < 0: # if summation is a negative number
			guess = F

		output_value = expected_output[j]

		#if not doing threshold algorithm:
		# error = output_value - summation

		#compute the error
		error = output_value - guess

		
		error_list.append(error) #should be 4, and I want this in a list to refer back to 

		weights_list.append(weights[0])
		weights_list.append(weights[1]) 
		weights_list.append(weights[2])
		

	# print error_list #4 overall errors
	# print weights_list	

	#reset the weights - but, before we try next thing in the list?
	#shouldn't this happen with each iteration in range rather than each time through the input?
	#so, does it work to have the first loop run and thennnn do another loop? 

	#define change in weight, referencing error_list
	
	for j in range(len(data_input)):
		delta_weight0 = error_list[i] * data_input[j][0]
		delta_weight1 = error_list[i] * data_input[j][1]
		delta_bias_weight = error_list[i] * bias


		#create new weights to seed next round
		weights[0] = weights_list[0] + delta_weight0 * learning_constant
		weights[1] = weights_list[1] + delta_weight1 * learning_constant
		weights[2] = weights_list[2] + delta_bias_weight * learning_constant

		#how do I seed the new weights into the next round?

		print "check to see if this changed" str(weights[0])



	# for i in weights: #for each item in weights
		# new_weights[i] +=  learning_constant * error #append a new weight plus a learning constant, taking into account the error?


	


	#check errors
	# error = expected_output - output

	# weight_change = error * data[i]

	# new_weight.append(old_weight + weight_change)

	# return new_weight



#thinking of end goal of weight?
