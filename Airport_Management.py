import heapq
from typing import List

class Airplane:
    def __init__(self, flight_number: str, emergency: int, fuel: int, time: int):
        # Initialize the airplane with flight number, emergency level, fuel level, and time
        self.flight_number = flight_number
        self.emergency = emergency
        self.fuel = fuel
        self.time = time

    def calculate_priority(self) -> float:
        # Calculate the priority of the airplane based on emergency, fuel, and time
        return self.emergency * 100 + 10 / (self.fuel + 1) + 1 / self.time

    def __repr__(self):
        # Return a string representation of the airplane with its details and priority
        return (f"Flight: {self.flight_number}, Emergency: {self.emergency}, "
                f"Fuel: {self.fuel}, Time: {self.time}, Priority: {self.calculate_priority():.2f}")


class AirportPriorityManager:
    def __init__(self):
        # Initialize an empty heap to manage airplane priorities
        self.heap = []

    def add_airplane(self, airplane: Airplane):
        # Add an airplane to the heap with its priority (negative for max-heap behavior)
        priority = -airplane.calculate_priority()
        heapq.heappush(self.heap, (priority, airplane.flight_number, airplane))

    def process_airplanes_with_details(self) -> List[Airplane]:
        # Process and return a list of airplanes sorted by priority
        result = []
        while self.heap:
            # Pop the airplane with the highest priority from the heap
            _, _, airplane = heapq.heappop(self.heap)
            result.append(airplane)
        return result


# Example usage
if __name__ == "__main__":
    # Initial data
    initial_data = [
        {"flight_number": "GN-MH-001", "emergency": 1, "fuel": 20, "time": 30},
        {"flight_number": "GN-TH-002", "emergency": 0, "fuel": 50, "time": 60},
        {"flight_number": "GN-ES-003", "emergency": 0, "fuel": 15, "time": 45},
        {"flight_number": "GN-SH-004", "emergency": 1, "fuel": 10, "time": 20},
    ]

    # Create the manager and add initial data
    manager = AirportPriorityManager()
    for data in initial_data:
        airplane = Airplane(
            flight_number=data["flight_number"],
            emergency=data["emergency"],
            fuel=data["fuel"],
            time=data["time"]
        )
        manager.add_airplane(airplane)

    # Process airplanes and print details
    print("Processing airplanes with details:")
    processed_airplanes = manager.process_airplanes_with_details()
    for airplane in processed_airplanes:
        print(airplane)



