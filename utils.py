import parking_spot
import constants

def get_spot_type_for_vehicle(vehicle):
	if vehicle.type == "two_wheeler":
		return parking_spot.TwoWheelerParkingSpot.spot_type

	elif vehicle.type == "compact":
		return parking_spot.CompactParkingSpot.spot_type

	elif vehicle.type == "medium":
		return parking_spot.MediumParkingSpot.spot_type

	elif vehicle.type == "huge":
		return parking_spot.HugeParkingSpot.spot_type

	else:
		return 0


def get_charges(ticket):
	return (
       ticket.spot.out_time - ticket.in_time
	) * constants.SPOT_TYPE_CHARGE_PER_HOUR_MAP[ticket.spot.spot_type] / 3600 