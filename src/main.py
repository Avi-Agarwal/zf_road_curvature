from calculate_speed import *

# Main Function
if __name__ == '__main__':
    # Find system variables for now us temp variables
    superelevation = float(input('Enter superelevation (percent): '))
    friction_factor = float(input('Enter friction factor: '))
    curvature_radius = int(input('Enter radius of curvature (ft): '))

    # Create system
    system1 = CalculatdeSpeed(superelevation, friction_factor, curvature_radius)
    # Super Elevation(Percent), Side Friction Factor, Radius of Curvature (ft)
    # Super Elevation:      the amount by which the outer edge of a curve on a road or railroad is banked above the inner edge.
    # Side Friction Factor: represents the friction between the tires and pavement surface. This friction results in a lateral -
    # acceleration that acts upon a vehicle, and which occupants within the vehicle can feel. Like superelevation,-
    # side friction factor is limited for design speeds.

    # Calculate speed
    advisory_speed = system1.calculate_speed()
    # advisory_speed is in mph


    print('Truck speed should be: ' + str(advisory_speed) + ' mph')
# # Main Function
# if __name__ == '__main__':
# #
# #
#     # Find system variables for now us temp variables
#
#     # Create system
#     system1 = CalculateSpeed(1, 1, 1)
#     #Super Elevation(Percent), Side Friction Factor, Radius of Curvature (ft)
#         #Super Elevation: the amount by which the outer edge of a curve on a road or railroad is banked above the inner edge.
#         #Side Friction Factor: represents the friction between the tires and pavement surface. This friction results in a lateral acceleration that acts upon a vehicle, and which occupants within the vehicle can feel. Like superelevation, side friction factor is limited for design speeds.
#
#
#     # Calculate speed
#     new_speed = system1.calculate_speed()
#     #new speed is advisory speed, mph
#
#     print("Truck speed should be: " + str(new_speed))
#     this is nothig
