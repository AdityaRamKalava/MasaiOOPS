# Base class
class Appliance:
    def status(self):
        print("Appliance is operating normally.")

# Subclasses
class Fan(Appliance):
    def status(self):
        print("Fan is running at medium speed.")

class Light(Appliance):
    def status(self):
        print("Light is set to warm white.")

class Ac(Appliance):
    def status(self):
        print("Air Conditioner is cooling at 22°C.")

# Create list of appliances
devices = [Fan(), Light(), Ac()]

# Demonstrate polymorphism
for device in devices:
    device.status()