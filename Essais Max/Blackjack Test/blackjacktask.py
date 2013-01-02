from scipy import clip, asarray

from pybrain.rl.environments.task import Task 
from numpy import *

class BlackjackTask(Task) :
	def __init__(self, environment) :
		self.env = environment
		self.lastreward = 0

	def performAction(self, action) : 
		self.env.performAction(action)

	def getObservation(self) :
		sensors = self.env.getSensors()