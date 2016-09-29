import random
import numpy as np


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


#seed random weights to start
weights = 0.9 * np.random.random(3)+0.01

learning_constant = .01

errors_list = []


for i in range(50): #run the perceptron an x number of times
	for j in range(len(data_input)): #for each index in data_input
			
		#ask the perceptron to guess the outputs
		summation = (data_input[j][0] * weights[0]) + (data_input[j][1] * weights[1]) + (bias * weights[2])

		#threhold algorithm; calculate output > is this ok? only dealing with ints...will it ever get closer then?
		# if summation > 0: # if summation is a positive number
		# 	guess = T
		# elif summation < 0: # if summation is a negative number
		# 	guess = F

		# output_value = expected_output[j]
		# error = output_value - guess

		#if not doing threshold algorithm:
		output_value = expected_output[j]
		error = output_value - summation


		#define change in weight
		delta_weight0 = error * data_input[j][0]
		delta_weight1 = error * data_input[j][1]
		delta_bias_weight = error * bias


		#create new weights to seed the next pair of inputs and bias
		weights[0] = weights[0] + delta_weight0 * learning_constant
		weights[1] = weights[1] + delta_weight1 * learning_constant
		weights[2] = weights[2] + delta_bias_weight * learning_constant

		errors_list.append(error)


def plotThing(num,thing,label):
    # plt.subplot(num)
    plt.xlabel('Iteration')
    plt.ylabel(label)
    plt.plot(thing)
    plt.show()



# plotThing(211,errorsWithBias,'error with bias')
plotThing(212,errors_list, 'errors')
