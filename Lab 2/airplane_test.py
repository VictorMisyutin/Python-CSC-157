#**************************************************************************
# * Name: Victor Misyutin                                           CSC 157
# * Date: 14-6-2023                                                 LAB 2   
# *************************************************************************
# * Problem Statement and Specifications: ask the user for details about   
# *     another airplane. Then create a new airplane with the details that
# *     the user entered. Then print the details, distance, and height difference
# *     of both airplanes. Then move both of the planes and print the data again.
# * Input:  
# *     Callsign, distance, direction, and alititude
# *
# * Output: 
# *     Callsign(plane 1 and 2), distance from watch tower (plane 1 and 2),
# *     bearing (plane 1 and 2), altitude (plane 1 and 2), distance between 
# *     plane 1 and 2, height difference between plane 1 and 2. All of that for both
# *     the new and old positions.
# *************************************************************************
from airplane import *

# create default airplane
p1 = Airplane()
# ask for inputs
callSign = input("Enter the details of the second airplane (call-sign, distance, bearing and altitude):\n")
distance = float(input())
bearing = int(input())
altitude = int(input())

callSign = callSign.upper()
# create second plane
p2 = Airplane(callSign, distance, bearing, altitude)
# calculate distance and height difference
distance= p1.distTo(p2)
heightDifference= p2.altitude-p1.altitude if p1.altitude < p2.altitude else p1.altitude-p2.altitude
# output initial positions and info
print("\nInitial Positions:")
print(f"\"Airplane 1\": {p1.callSign} - {p1.distance} miles away at bearing {p1.direction:03d}\u00b0, altitude {p1.altitude} feet")
print(f"\"Airplane 2\": {p2.callSign} - {p2.distance} miles away at bearing {p2.direction:03d}\u00b0, altitude {p2.altitude} feet")
print(f"The distance between the planes is {distance} miles")
print(f"The difference in height between the planes is {heightDifference} feet")
# add altitude to first airplane
p1.gainAlt()
p1.gainAlt()
p1.gainAlt()
p1.gainAlt()
# bring airplane 2 altitude down
p2.loseAlt()
p2.loseAlt()
# move both airplanes
p1.move(10.5, 50)
p2.move(8, 125)
# recalculate distance
distance= p1.distTo(p2)
# format distance
distance= "{:.2f}".format(distance)
# recalculate height difference
heightDifference= p2.altitude-p1.altitude if p1.altitude < p2.altitude else p1.altitude-p2.altitude
# format distance 
p1.distance = "{:.2f}".format(p1.distance)
p2.distance = "{:.2f}".format(p2.distance)
# output new positions and info
print("\nNew Positions:")
print(f"\"Airplane 1\": {p1.callSign} - {p1.distance} miles away at bearing {p1.direction:03d}\u00b0, altitude {p1.altitude} feet")
print(f"\"Airplane 2\": {p2.callSign} - {p2.distance} miles away at bearing {p2.direction:03d}\u00b0, altitude {p2.altitude} feet")
print(f"The distance between the planes is {distance} miles")
print(f"The difference in height between the planes is {heightDifference} feet")