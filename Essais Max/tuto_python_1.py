class mammifere:
	def __init__(self):
		self.age = 0

	def vieillir(self):
		self.age += 1
		return self.age

mouton = mammifere()
print mouton.age
print mouton.vieillir()

i = 0
while i < 27:
	print mouton.vieillir()
	i += 1
	print "mouton est vivant"
print mouton.age

a = [1, 2, 3]
for c in a:
	print c