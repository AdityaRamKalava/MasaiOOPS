class Device:
    def __init__(self, device_id, model):
        self.device_id = device_id
        self.model = model

    def show_info(self):
        print(f"Device ID: {self.device_id}, Model: {self.model}")

class Flyer:
    def fly(self):
        print("Drone is flying")

class Drone(Device, Flyer):
    def __init__(self, device_id, model):
        # Initialize the Device part of the Drone
        super().__init__(device_id, model)

    def capture_image(self):
        print("Image captured by the drone.")


# Create a Drone object
drone1 = Drone("DR123", "X-200")

# Use all the functionalities from Device, Flyer, and Drone
drone1.show_info()        
drone1.fly()              
drone1.capture_image()   