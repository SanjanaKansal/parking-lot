import parking_floor
import parking_spot
import ticket
import vehicle
import utils


def get_ticket(vehicle):
	spot_type_map = parking_floor.get_available_spot_type_map()
	spot_type  = utils.get_spot_type_for_vehicle(vehicle)
	if spot_type == 0 or not spot_type_map.get(spot_type):
		return "Pardon, we don't have any spot for the vehicle."
	spot_row, spot_col = spot_type_map[spot_type][0]
	spot = parking_spots[spot_row][spot_col]
	spot.book_spot(vehicle)
	return ticket.Ticket(spot)


def accept_ticket(ticket):
	ticket.spot.vacate_spot()
	return utils.get_charges(ticket)


if __name__ == "__main__":
	parking_spots = [
		[
			parking_spot.TwoWheelerParkingSpot(i, j) if i < 3 else parking_spot.CompactParkingSpot(i, j) for i in
			range(5)
		]
		for j in range(5)
	]
	parking_floor = parking_floor.ParkingFloor(parking_spots)
	parking_floor.get_floor_status()

	my_scooter = vehicle.Vehicle('FK127', "two_wheeler")
	ticket = get_ticket(my_scooter)
	print(ticket)

	parking_floor.get_floor_status()

	charges = accept_ticket(ticket)
	print(charges)

	parking_floor.get_floor_status()



