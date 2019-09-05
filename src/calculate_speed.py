
class CalculateSpeed:

    def __init__(self, SuperElevation, SideFrictionFactor, CurvatureRadius):
        self.elevation = SuperElevation     #Percent
        self.friction = SideFrictionFactor    #no unit
        self.curvature = CurvatureRadius       #ft

    def calculate_speed(self):
        return 15*(0.01*self.elevation+self.friction)*self.curvature
        # V^2 = 15*(0.01*super elevation + side friction factor)* radius of curvature
        # Advisory speed (MPH)
# Main Function
if __name__ == '__main__':
    system1 = CalculateSpeed(1,1,1)
    new_speed = system1.calculate_speed()
    print("Truck speed should be: " + str(new_speed))