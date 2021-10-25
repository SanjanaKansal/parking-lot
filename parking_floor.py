class ParkingFloor:
	def __init__(self, parking_spots):
		self.parking_spots = parking_spots		

	def get_floor_status(self):
		for row in self.parking_spots:
			for spot in row:
				print(int(spot.is_available)),
			print("\n")

	def get_available_spot_type_map(self):
		spot_type_map = {}
		for i in range(len(self.parking_spots)):
			for j in range(len(self.parking_spots[0])):
				spot = self.parking_spots[i][j]
				if spot.is_available:
					if spot_type_map.get(spot.spot_type):
						spot_type_map[spot.spot_type].append((i, j))
					else:
						spot_type_map[spot.spot_type] = [(i,j)]
		return spot_type_map