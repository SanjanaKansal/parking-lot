import time

class ParkingSpot:
	is_available = True
	vehicle = None
	def __init__(self, row, col):
		self.row = row
		self.col = col

	def book_spot(self, vehicle):
		self.vehicle = vehicle
		self.is_available = False

	def vacate_spot(self):
		if self.vehicle:
			self.is_available = True
			self.vehicle = None
			self.out_time = time.time()


class TwoWheelerParkingSpot(ParkingSpot):
	spot_type = 1

class CompactParkingSpot(ParkingSpot):
	spot_type = 2

class MediumParkingSpot(ParkingSpot):
	spot_type = 3

class HugeParkingSpot(ParkingSpot):
	spot_type = 4