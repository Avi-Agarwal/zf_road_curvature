
class CalculateSpeed:

    def __init__(self, curvature, weight, length):
        self.curvature = curvature
        self.weight = weight
        self.length = length

    def calculate_speed(self):
        return 10

# Main Function
if __name__ == '__main__':
    system1 = CalculateSpeed(1,1,1)
    new_speed = system1.calculate_speed()
    print("Truck speed should be: " + str(new_speed))