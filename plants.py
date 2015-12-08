class Plant(object):
	def __init__(self, plant_type, is_flowering, color):
		self.plant_type = plant_type
		self.is_flowering = is_flowering
		self.color = color
	def print_plant_type(self):
		print self.plant_type
	def set_is_flowering(self, flowering):
		self.is_flowering = flowering
		print self.is_flowering
	def print_color(self):
		print self.color

flower_list = [
	Plant("rose", True, "red"), 
	Plant("tulip", False, "white"), 
	Plant("daisy", True, "white")
]

for i in flower_list:
	i.print_plant_type()
	i.set_is_flowering(False)
	i.print_color()
