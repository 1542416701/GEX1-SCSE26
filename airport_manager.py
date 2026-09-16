######################## IMPORTANT ########################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################


# Airport metadata (immutable, uses tuple)
airport_info = ("OUL", 1, "14-09-2026")

# Allowed gates (O(1) membership test, uses set)
allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}

# Restricted destinations (uses set)
restricted_destinations = {"Moscow", "Pyongyang"}

# Flight database (key = normalized flight number, uses dict)
# Each flight stores a passenger list (uses list)
flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": ["Alice Wong", "David Kim", "Fatima Ali"],
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": ["Chen Wei", "George Smith"],
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": ["Hana Lee", "Maria Garcia", "Noah Wilson"],
    },
}


## Logic to find if a flight exists
def find_flight(flights, flight_number):
    """Return normalized flight key if the flight exists, otherwise None."""
    if not isinstance(flight_number, str):
        return None
    normalized = flight_number.strip().upper()
    if normalized in flights:
        return normalized
    return None


## Logic to find if a passenger exists
def passenger_exists(passengers, passenger_name):
    """Return True if the passenger is in the list (case-insensitive)."""
    if not isinstance(passenger_name, str) or not passenger_name.strip():
        return False
    name_lower = passenger_name.strip().lower()
    for p in passengers:
        if p.lower() == name_lower:
            return True
    return False


## Logic to check in a passenger
def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    """Check in a passenger.

    Returns one of: OK, FLIGHT_NOT_FOUND, EMPTY_NAME, DUPLICATE, FULL, RESTRICTED
    """
    flight = find_flight(flights, flight_number)
    if flight is None:
        return "FLIGHT_NOT_FOUND"

    if not isinstance(passenger_name, str) or not passenger_name.strip():
        return "EMPTY_NAME"

    name = passenger_name.strip().title()

    # Restricted destinations cannot accept new passengers
    if flights[flight]["destination"] in restricted_destinations:
        return "RESTRICTED"

    # Duplicate passenger (case-insensitive)
    if passenger_exists(flights[flight]["passengers"], name):
        return "DUPLICATE"

    # Flight at capacity
    if len(flights[flight]["passengers"]) >= flights[flight]["capacity"]:
        return "FULL"

    flights[flight]["passengers"].append(name)
    return "OK"


## Logic to remove a passenger from a flight
def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    """Remove a passenger from a flight.

    Returns one of: OK, FLIGHT_NOT_FOUND, PASSENGER_NOT_FOUND
    """
    flight = find_flight(flights, flight_number)
    if flight is None:
        return "FLIGHT_NOT_FOUND"

    if not isinstance(passenger_name, str) or not passenger_name.strip():
        return "PASSENGER_NOT_FOUND"

    name_lower = passenger_name.strip().lower()
    for i, p in enumerate(flights[flight]["passengers"]):
        if p.lower() == name_lower:
            flights[flight]["passengers"].pop(i)
            return "OK"

    return "PASSENGER_NOT_FOUND"


# Logic to change the gate of a flight
def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    """Change the departure gate of a flight.

    Returns one of: OK, FLIGHT_NOT_FOUND, INVALID_GATE
    """
    flight = find_flight(flights, flight_number)
    if flight is None:
        return "FLIGHT_NOT_FOUND"

    if not isinstance(new_gate, str) or new_gate.strip().upper() not in allowed_gates:
        return "INVALID_GATE"

    flights[flight]["gate"] = new_gate.strip().upper()
    return "OK"


# Logic to get the status of a flight
def flight_status(flight):
    """Return the availability status of a flight.

    Returns one of: AVAILABLE, ALMOST FULL, FULL
    - FULL: 100% capacity
    - ALMOST FULL: >= 75% capacity
    - AVAILABLE: < 75% capacity
    """
    count = len(flight["passengers"])
    capacity = flight["capacity"]
    percentage = count / capacity * 100

    if percentage >= 100:
        return "FULL"
    if percentage >= 75:
        return "ALMOST FULL"
    return "AVAILABLE"


# Logic to get the sorted manifest of a flight
def sorted_manifest(
    flights,
    flight_number
):
    """Return a sorted copy of passenger names for a flight, or None if not found."""
    flight = find_flight(flights, flight_number)
    if flight is None:
        return None
    return sorted(flights[flight]["passengers"])


# Logic to get the total number of passengers across all flights
def total_passengers(flights):
    """Return the total number of passengers across all flights."""
    total = 0
    for flight in flights.values():
        total += len(flight["passengers"])
    return total


# Logic to check if any flight is full
def any_full_flight(flights):
    """Return True if at least one flight is full."""
    for flight in flights.values():
        if len(flight["passengers"]) >= flight["capacity"]:
            return True
    return False


# Logic to check if all flights have at least one passenger
def all_flights_have_passengers(flights):
    """Return True if every flight has at least one passenger."""
    if not flights:
        return False
    for flight in flights.values():
        if len(flight["passengers"]) == 0:
            return False
    return True
