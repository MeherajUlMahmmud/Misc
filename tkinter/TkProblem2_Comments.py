import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog


class Stock:
    """Class to represent a stock item

    Attributes:
        name (str): Name of the stock item
        quantity (int): Quantity of the stock item
        price (int): Price of the stock item

    Purpose:
        To represent a stock item in the stock list
    """

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Student:
    """Class to represent a student

    Attributes:
        name (str): Name of the student
        wallet (int): Wallet balance of the student

    Purpose:
        To represent a student in the students list
    """

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet


class StockManagementApp:
    def __init__(self):
        # Initialize stock list with some initial items
        self.stock_list = [
            Stock("apple", 10, 1),
            Stock("orange", 5, 2),
            Stock("pear", 7, 3)
        ]
        # Initialize students list with some initial students
        self.students_list = [
            Student("alice", 10),
            Student("bob", 20),
            Student("charlie", 5)
        ]
        # List to keep track of already ate items
        self.already_ate_list = []

        # Initialize the main Tkinter window
        self.root = tk.Tk()
        self.root.title("Stock Management App")
        # Set the window size,
        # self.root.geometry("400x600")  # this line is not used because we want the window to resize automatically based on the widgets inside

        # Heading label initialization
        self.heading_label = tk.Label(
            self.root, text="Stock Management", font=("Helvetica", 18),
        )
        # Place the heading label on the grid
        self.heading_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Menu label initialization
        self.menu_label = tk.Label(
            self.root, text="Select an option:", font=("Helvetica", 14),
        )
        # Place the menu label on the grid
        self.menu_label.grid(row=1, column=0, columnspan=3, pady=10)

        # Create buttons and place them on the grid
        self.create_button("Add Stock", self.add_stock, 2, 0)
        self.create_button("Check Stock", self.check_stock, 2, 1)
        self.create_button("Add Student", self.add_student, 3, 0)
        self.create_button("View Students", self.view_students, 3, 1)
        self.create_button("Update Stock", self.update_stock, 4, 0)
        self.create_button("Already Ate", self.already_ate, 4, 1)
        self.create_button("Quit", self.quit_app, 5, 0, 1, 3)

    def create_button(self, text, command, row, column, rowspan=1, columnspan=1):
        button = tk.Button(
            self.root, text=text, command=command, font=("Helvetica", 16),
            bg="lightblue",  # button background color
            fg="white",  # button text color
            width=15,  # button width
            height=2,  # button height
            borderwidth=1,  # button border
            anchor=tk.W,  # align text to the left of the button instead of center
        )
        button.grid(
            row=row, column=column,  # Position of the button on the grid
            rowspan=rowspan, columnspan=columnspan,
            padx=10, pady=5,  # Padding around the button
        )  # Place the button on the grid

    def add_stock(self):
        food_name = tk.simpledialog.askstring(
            "Add Stock", "Enter Food Name:",
        )

        if food_name:
            quantity = tk.simpledialog.askinteger(
                "Add Stock", f"Enter Stock Quantity for {food_name}:",
            )

            price = tk.simpledialog.askinteger(
                "Add Stock", f"Enter Price for {food_name}:",
            )

            if quantity is not None and price is not None:
                self.stock_list.append(Stock(food_name, quantity, price))

                messagebox.showinfo(
                    "Add Stock", f"{food_name} added to stock. Quantity: {quantity}, Price: {price}",
                )

    def check_stock(self):
        messagebox.showinfo(
            "Current Stock", "\n".join(
                ["{}: Quantity: {}, Price: {}".format(stock.name, stock.quantity, stock.price) for stock in self.stock_list]),
        )

    def update_stock(self):
        food_options = [stock.name for stock in self.stock_list]
        food = tk.simpledialog.askstring(
            "Update Stock", "What did they eat?",
            initialvalue=food_options[0],
            parent=self.root,
        )
        student = tk.simpledialog.askstring(
            "Update Stock", "Who ate the food?")
        amount = tk.simpledialog.askinteger(
            "Update Stock", "How many did they eat?")

        if food and student:
            student_found = False
            for s in self.students_list:
                if s.name == student:
                    student_found = True
                    if s.wallet < amount * self.get_price(food):
                        messagebox.showinfo(
                            "Update Stock", "Not enough credit for {}".format(student))
                        return
                    break
            if not student_found:
                messagebox.showinfo(
                    "Update Stock", "No student with the name {} found".format(student))
                return

            food_found = False
            for stock in self.stock_list:
                if stock.name == food:
                    food_found = True
                    if student in self.already_ate_list:
                        messagebox.showinfo(
                            "Update Stock", "{} was refused and sent out the queue".format(student))
                    else:
                        if stock.quantity >= int(amount):
                            messagebox.showinfo(
                                "Update Stock", "{} ate {}".format(student, food))
                            stock.quantity -= int(amount)
                            self.already_ate_list.append({
                                "food": food,
                                "student": student,
                                "amount": amount,
                            })
                            for s in self.students_list:
                                if s.name == student:
                                    s.wallet -= amount * stock.price
                                    break
                        else:
                            messagebox.showinfo(
                                "Update Stock", "{} did not eat because it's out of stock".format(student))
                    break
            if not food_found:
                messagebox.showinfo("Update Stock", "Food not found in stock.")
        else:
            messagebox.showinfo(
                "Update Stock", "Invalid input. Both food and student are required.")

    def already_ate(self):
        messagebox.showinfo(
            "Already Ate", "\n".join(
                ["{} ate {} {}".format(
                    item["student"], item["amount"], item["food"])
                    for item in self.already_ate_list])
            + "\n",
        )

    def add_student(self):
        student_name = tk.simpledialog.askstring(
            "Add Student", "Enter Student Name:")

        if student_name:
            wallet_balance = tk.simpledialog.askinteger(
                "Add Student", f"Enter Wallet Balance for {student_name}:")

            if wallet_balance is not None:
                self.students_list.append(
                    Student(student_name, wallet_balance))
                messagebox.showinfo(
                    "Add Student", f"Student {student_name} added with Wallet Balance: {wallet_balance}",
                )

    def view_students(self):
        messagebox.showinfo(
            "Current Students", "\n".join(
                ["{}: Wallet Balance: {}".format(student.name, student.wallet) for student in self.students_list]),
        )

    def get_price(self, food):
        # loop through the stock list to find the food item
        for stock in self.stock_list:
            # if the food item is found
            if stock.name == food:
                # return the price of the food item
                return stock.price
        # if the food item is not found return None
        return None

    def quit_app(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = StockManagementApp()
    app.run()
