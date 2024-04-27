import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog


class StockManagementApp:
    def __init__(self):
        self.stock = {"apple": 10, "orange": 5, "pear": 7}
        self.already_ate_list = []

        self.root = tk.Tk()
        self.root.title("Stock Management App")
        self.root.geometry("600x400")  # Set the window size

        self.heading_label = tk.Label(
            self.root, text="Stock Management", font=("Helvetica", 18),
        )
        self.heading_label.pack(pady=10)

        self.menu_label = tk.Label(
            self.root, text="Select an option:", font=("Helvetica", 14),
        )
        self.menu_label.pack(pady=10)

        self.add_stock_button = tk.Button(
            self.root, text="1. Add Stock", command=self.add_stock, font=("Helvetica", 16),
            bg="lightblue",  # button background color
            fg="white",  # button text color
            width=15,  # button width
            height=2,  # button height
            borderwidth=1,  # button border
            anchor=tk.W,  # align text to the left of the button instead of center
        )
        self.add_stock_button.pack(pady=5)

        self.check_stock_button = tk.Button(
            self.root, text="2. Check Stock", command=self.check_stock, font=("Helvetica", 16),
            bg="lightblue",  # button background color
            fg="white",  # button text color
            width=15,  # button width
            height=2,  # button height
            borderwidth=1,  # button border
            anchor=tk.W,  # align text to the left of the button instead of center
        )
        self.check_stock_button.pack(pady=5)

        self.update_stock_button = tk.Button(
            self.root, text="3. Update Stock",
            command=self.update_stock,
            font=("Helvetica", 16),
            bg="lightblue",  # button background color
            fg="white",  # button text color
            width=15,  # button width
            height=2,  # button height
            borderwidth=1,  # button border
            anchor=tk.W,  # align text to the left of the button instead of center
        )
        self.update_stock_button.pack(pady=5)

        self.already_ate_button = tk.Button(
            self.root, text="4. Already Ate",
            command=self.already_ate,
            font=("Helvetica", 16),
            bg="lightblue",  # button background color
            fg="white",  # button text color
            width=15,  # button width
            height=2,  # button height
            borderwidth=1,  # button border
            anchor=tk.W,  # align text to the left of the button instead of center
        )
        self.already_ate_button.pack(pady=10)

        self.quit_button = tk.Button(
            self.root, text="5. Quit", command=self.quit_app, font=("Helvetica", 16),
            bg="lightblue",  # button background color
            fg="white",  # button text color
            width=15,  # button width
            height=2,  # button height
            borderwidth=1,  # button border
            anchor=tk.W,  # align text to the left of the button instead of center
        )
        self.quit_button.pack(pady=5)

    def add_stock(self):
        food_name = tk.simpledialog.askstring("Add Stock", "Enter Food Name:")
        if food_name:
            quantity = tk.simpledialog.askinteger(
                "Add Stock", f"Enter Stock Quantity for {food_name}:")
            if quantity is not None:
                self.stock[food_name] = quantity
                messagebox.showinfo(
                    "Add Stock", f"{food_name} added to stock. Quantity: {quantity}",
                )

    def check_stock(self):
        messagebox.showinfo(
            "Current Stock", "\n".join(
                ["{}: {}".format(key, value) for key, value in self.stock.items()]),
        )

    def update_stock(self):
        food = tk.simpledialog.askstring(
            "Update Stock", "What food was eaten?",
        )
        person = tk.simpledialog.askstring("Update Stock", "Who ate the food?")
        amount = tk.simpledialog.askinteger(
            "Update Stock", "How many did they eat?")

        if food and person:  # Ensure both food and person are not None or empty
            if food in self.stock:
                if person in self.already_ate_list:
                    messagebox.showinfo(
                        "Update Stock", "{} was refused and sent out the queue".format(person))
                else:
                    if self.stock[food] > 0:
                        messagebox.showinfo(
                            "Update Stock", "{} ate {}".format(person, food))
                        self.stock[food] -= 1
                        self.already_ate_list.append(person)
                    else:
                        messagebox.showinfo(
                            "Update Stock", "{} did not eat because it's out of stock".format(person))
            else:
                messagebox.showinfo("Update Stock", "Food not found in stock.")
        else:
            messagebox.showinfo(
                "Update Stock", "Invalid input. Both food and person are required.")

    def already_ate(self):
        messagebox.showinfo(
            "Already Ate", "\n".join(self.already_ate_list),
        )

    def quit_app(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = StockManagementApp()
    app.run()
