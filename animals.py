class Animal(object):
	def __init__(self, animal_name, animal_type, fur, age):
		self.animal_name = animal_name
		self.animal_type = animal_type
		self.fur = fur
		self.age = age
	def print_animal_name(self):
		print self.animal_name
	def print_animal_type(self):
		print self.animal_type
	def has_fur(self):
		if self.fur == True:
			print "it has fur"
		else:
			print "no fur"
	def print_age(self):
		print "the pet is:", self.age


pet_list = [
	Animal("rupert", "dog", True,  3),
	Animal("splash", "fish", False, 1),
	Animal("batman", "cat", True, 10)
]

for i in pet_list:
	i.print_animal_name()
	i.print_animal_type()
	i.has_fur()
	i.print_age()
	