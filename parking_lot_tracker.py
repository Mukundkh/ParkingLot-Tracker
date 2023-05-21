class ParkingLot:
    def __init__(self):
        self.spots = {}  # In-memory storage to store the parked vehicles

        # Initialize parking spots on levels A and B
        self.spots['A'] = [False] * 20  # False indicates an empty spot
        self.spots['B'] = [False] * 20

    def assign_parking_space(self, vehicle_number):
        for level in ['A', 'B']:
            # Check if there is an empty spot in the level
            if False in self.spots[level]:
                spot_number = self.spots[level].index(False) + 1
                self.spots[level][spot_number - 1] = vehicle_number
                return {"level": level, "spot": spot_number}

        return None  # No available parking spots

    def retrieve_parking_spot(self, vehicle_number):
        for level in ['A', 'B']:
            if vehicle_number in self.spots[level]:
                spot_number = self.spots[level].index(vehicle_number) + 1
                return {"level": level, "spot": spot_number}

        return None  # Vehicle not found in the parking lot


# Example usage of the ParkingLot class

# Create an instance of the ParkingLot
parking_lot = ParkingLot()

# Assign a parking spot to a new vehicle
assigned_spot = parking_lot.assign_parking_space("ABC123")
if assigned_spot:
    print("Assigned spot:", assigned_spot)
else:
    print("No available parking spots.")

# Retrieve the parking spot of a particular vehicle
vehicle_spot = parking_lot.retrieve_parking_spot("ABC123")
if vehicle_spot:
    print("Vehicle spot:", vehicle_spot)
else:
    print("Vehicle not found in the parking lot.")
