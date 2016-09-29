import random
import numpy as np
import matplotlib.pyplot as plt


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

expected_output = [T, T, T, F]

weights = []

#seed random weights between -1 and 1 to start (floats)
for i in range(3):
	weights.append(random.uniform(-1,1))

learning_constant = .1

errors_list = []


for i in range(100): #run the perceptron an x number of times
	for j in range(len(data_input)): #for each index in data_input
			
		#ask the perceptron to guess the outputs
		summation = (data_input[j][0] * weights[0]) + (data_input[j][1] * weights[1]) + (bias * weights[2])

		#threhold algorithm; calculate output

		if summation > 0: # if summation is a positive number
			guess = T
		elif summation < 0: # if summation is a negative number
			guess = F

		output_value = expected_output[j]
		error = output_value - guess


		#define change in weight
		delta_weight0 = error * data_input[j][0]
		delta_weight1 = error * data_input[j][1]
		delta_bias_weight = error * bias


		#create new weights to seed the next pair of inputs and bias
		weights[0] = weights[0] + delta_weight0 * learning_constant
		weights[1] = weights[1] + delta_weight1 * learning_constant
		weights[2] = weights[2] + delta_bias_weight * learning_constant

		errors_list.append(error)

print errors_list

def plotErrors(thing,label): #borrowed from Eve
    plt.xlabel('Iteration')
    plt.ylabel(label)
    plt.plot(thing)
    plt.show()


plotErrors(errors_list, 'errors')
