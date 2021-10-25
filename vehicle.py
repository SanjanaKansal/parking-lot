class Vehicle:
	def __init__(self, plate_no, type):
		self.plate_no = plate_no
		self.type = type

	def __str__(self):
		return "Plate no: {}, Type : {}".format(self.plate_no, self.type)