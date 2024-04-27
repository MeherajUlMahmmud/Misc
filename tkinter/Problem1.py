class DirectionsGameApp:
    current_location = "Hobart"
    next_direction = "N"
    destination = "Melbourne"
    points = 0

    def __init__(self):
        print("Welcome to the Around Australia game.")
        print("Points: 0")
        print()
        self.display_location()

    def process_direction(self, direction):
        self.check_destination(direction)

    def check_destination(self, direction):
        if direction != self.next_direction:
            print()
            print("Sorry, wrong direction!")
            self.update_points(-1)
            self.display_location()
        else:
            print()
            print("Correct direction!")
            self.update_points(3)
            self.next_destination()

    def next_destination(self):
        if self.current_location == "Hobart":
            self.melbourne()
        elif self.current_location == "Melbourne":
            self.adelaide()
        elif self.current_location == "Adelaide":
            self.darwin()
        elif self.current_location == "Darwin":
            self.act()

    def melbourne(self):
        self.update_location("Melbourne", "W", "Adelaide")

    def adelaide(self):
        self.update_location("Adelaide", "S", "Darwin")

    def darwin(self):
        self.update_location("Darwin", "E", "ACT")

    def act(self):
        self.update_location("ACT", None, "ACT")

    def update_location(self, location, next_direction, next_destination):
        if next_direction is None:
            print(f"Congratulations! You have reached {location}.")
            self.end()
        else:
            self.current_location = location
            self.next_direction = next_direction
            self.destination = next_destination
            self.display_location()

    def display_location(self):
        print(f"You are currently in {self.current_location}.")
        print(f"Your destination is {self.destination}.")
        self.select_direction()

    def select_direction(self):
        direction = input(
            "What direction do you want to travel? (N/S/W/E): ").upper()
        self.process_direction(direction)

    def update_points(self, points):
        self.points += points
        print(f"Points: {self.points}")
        print()

    def end(self):
        response = input("Do you want to play again? (yes/no): ").lower()
        if response == 'yes':
            self.reset()
        else:
            print("Goodbye!")

    def reset(self):
        self.current_location = "Hobart"
        self.next_direction = "N"
        self.destination = "Melbourne"
        self.points = 0
        self.display_location()


if __name__ == "__main__":
    app = DirectionsGameApp()
