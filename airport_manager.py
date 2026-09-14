######################## IMPORTANT ########################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################


airport_info = None
allowed_gates = None
restricted_destinations = None
flights = None


## Logic to find if a flight exists
def find_flight(flights, flight_number):
    pass


## Logic to find if a passenger exists
def passenger_exists(passengers, passenger_name):
    pass


## Logic to check in a passenger
def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    pass


## Logic to remove a passenger from a flight
def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    pass


# Logic to change the gate of a flight
def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    pass


# Logic to get the status of a flight
def flight_status(flight):
    pass



# Logic to get the sorted manifest of a flight
def sorted_manifest(
    flights,
    flight_number
):
    pass


# Logic to get the total number of passengers across all flights
def total_passengers(flights):
    pass


# Logic to check if any flight is full
def any_full_flight(flights):
    pass



# Logic to check if all flights have at least one passenger
def all_flights_have_passengers(flights):
    pass