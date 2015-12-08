class Food(object):
	def __init__(self, name, recipe, weight, color, size):
		self.name = name
		self.recipe = recipe
		self.weight = weight
		self.color = color
		self.size = size
	def print_name(self):
		print self.name
	def print_recipe(self):
		print self.recipe
	def print_weight(self):
		print self.weight
	def print_color(self):
		print self.color
	def print_size(self):
		print self.size


food_list = [
	Food("apple", "Cut into 4 \nput peanut butter on it", "300g", "red", "20cm"),
	Food("banana_bread", "Cut banana \nadd flour \nbake", "50g", "yellow", "40cm"),
	Food("cookie", "mix butter and chocolate \nbake", "25g", "brown", "10cm")
]

for i in food_list:
	i.print_name()
	i.print_recipe()
	i.print_weight()
	i.print_color()
	i.print_size()



