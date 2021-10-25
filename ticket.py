import time

class Ticket:
	spot = None
	def __init__(self, spot):
		if spot.vehicle:
			self.spot = spot
			self.in_time = time.time()

	def __str__(self):
		return "Spot:{}{}, In Time:{}".format([self.spot.row],[self.spot.col], self.in_time)

		