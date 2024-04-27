import tkinter as tk
from tkinter import messagebox


class DirectionsGameApp:
    # initialise the necessary variables
    current_location = "Hobart"
    next_direction = "N"
    destination = "Melbourne"

    def __init__(self):
        self.points = 0  # initialise points
        self.root = tk.Tk()  # create the window
        self.root.geometry("600x400")  # set the window size
        self.root.title("Around Australia Game")  # set the window title

        # Heading label initialisation
        self.header_label = tk.Label(
            self.root, text="Welcome to the Around Australia game.", font=("Helvetica", 20),
        )
        # Place the heading label in the window
        self.header_label.pack(pady=10)

        # Points label initialisation
        self.points_label = tk.Label(
            self.root, text=f"Points: {self.points}", font=("Helvetica", 18, "bold", "italic", "underline"),
        )
        # Place the points label in the window
        self.points_label.pack(pady=5)

        # Current location label initialisation
        self.current_location_label = tk.Label(
            self.root, text=f"You are currently in {self.current_location}.", font=("Helvetica", 16),
        )
        # Place the current location label in the window
        self.current_location_label.pack(pady=5)

        # Destination label initialisation
        self.destination_label = tk.Label(
            self.root, text=f"Your destination is {self.destination}.", font=("Helvetica", 16),
        )
        # Place the destination label in the window
        self.destination_label.pack(pady=5)

        # Select direction label initialisation
        self.select_direction_label = tk.Label(
            self.root, text="What direction do you want to travel?", font=("Helvetica", 16),
        )
        # Place the select direction label in the window
        self.select_direction_label.pack(pady=20)

        # create a frame to hold the buttons for the directions
        self.direction_buttons_frame = tk.Frame(self.root)
        # add the frame to the window
        self.direction_buttons_frame.pack()

        # list of directions
        directions = ["N", "S", "W", "E"]

        # create a button for each direction by looping through the list
        for direction in directions:
            button = tk.Button(
                self.direction_buttons_frame,  # parent widget
                text=direction,  # button text
                # Lambda function is a function that is defined inline
                command=lambda dir=direction: self.process_direction(
                    dir),  # button command
                width=4,  # button width
                height=2,  # button height
                font=("Helvetica", 16),  # button font
                bg="lightblue",  # button background color
                fg="white",  # button text color
                borderwidth=0,  # button border
            )
            button.pack(side=tk.LEFT, padx=10, pady=10)

    def process_direction(self, direction):
        # check if the direction is correct
        self.check_destination(direction)

    def check_destination(self, direction):
        # if the direction is wrong
        if direction != self.next_direction:

            # show a message and update points
            self.show_message(
                f"Sorry, wrong direction!", self.update_points(-1)
            )
        # if the direction is correct
        else:
            # update points
            self.update_points(3)
            # and go to the next destination
            self.next_destination()

    def next_destination(self):
        # set the next destination based on the current location
        if self.current_location == "Hobart":
            self.melbourne()
        elif self.current_location == "Melbourne":
            self.adelaide()
        elif self.current_location == "Adelaide":
            self.darwin()
        elif self.current_location == "Darwin":
            self.act()

    def melbourne(self):
        # update the location and the next destination
        self.update_location("Melbourne", "W", "Adelaide")

    def adelaide(self):
        # update the location and the next destination
        self.update_location("Adelaide", "S", "Darwin")

    def darwin(self):
        # update the location and the next destination
        self.update_location("Darwin", "E", "ACT")

    def act(self):
        # update the location and the next destination
        self.update_location("ACT", None, "ACT")

    def update_location(self, location, next_direction, next_destination):
        # if the next direction is None, it means the game is over
        if next_direction is None:
            # show a message and end the game
            self.show_message(
                f"Congratulations! You have reached {location}.", self.end)
        # otherwise update the location and the next destination
        else:
            self.current_location = location
            self.next_direction = next_direction
            self.destination = next_destination
            self.update_labels()

    def update_labels(self):
        """Update the labels with the current location and destination.

        This method is called every time the location is updated.
        """

        # update the labels with the current location
        self.current_location_label.config(
            text=f"You are currently in {self.current_location}.")

        # update the labels with the destination
        self.destination_label.config(
            text=f"Your destination is {self.destination}.")

    def show_message(self, message, next_function):
        messagebox.showinfo("Game Info", message)
        next_function()

    def update_points(self, points):
        """Update the points.

        Args:
            points (int): The points to add to the current points.

        """

        # update the points
        self.points += points

        # update the points label
        self.points_label.config(text=f"Points: {self.points}")

    def end(self):
        """End the game.

        This method is called when the game is over.
        """
        response = messagebox.askquestion(
            "Play Again", "Do you want to play again?")
        if response == 'yes':
            self.reset()
        else:
            self.root.destroy()

    def reset(self):
        """Reset the game.

        This method is called when the user wants to play again.
        """
        self.current_location = "Hobart"
        self.next_direction = "N"
        self.destination = "Melbourne"
        self.update_labels()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = DirectionsGameApp()
    app.run()
