from calculate_speed import *

# Main Function
if __name__ == '__main__':

    # Find system variables for now us temp variables

    # Create system
    system1 = CalculateSpeed(1, 1, 1)

    # Calculate speed
    new_speed = system1.calculate_speed()


    print("Truck speed should be: " + str(new_speed))