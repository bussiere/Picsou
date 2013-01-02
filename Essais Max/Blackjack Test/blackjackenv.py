from pybrain.rl.environments.environment import Environment 
from scipy import zeros

Class BlackjackEnv(Environment)
	# the number of action values the environment accepts
	indim = 2

	# the number of senson values the environment produces
	outdim = 21

	def getSensors(self)
		hand_value = int(raw_input("Enter hand value")) - 1
		return[float(hand_value),]

	def performAction(self, action) :
		print "Action performed: ", action

	def reset(self) :



