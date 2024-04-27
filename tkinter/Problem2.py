class Stock:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Student:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet


class StockManagementApp:
    def __init__(self):
        self.stock_list = [
            Stock("apple", 10, 1),
            Stock("orange", 5, 2),
            Stock("pear", 7, 3)
        ]
        self.students_list = [
            Student("alice", 10),
            Student("bob", 20),
            Student("charlie", 5)
        ]
        self.already_ate_list = []

    def add_stock(self):
        food_name = input("Enter Food Name: ")
        quantity = int(input("Enter Stock Quantity: "))
        price = int(input("Enter Price: "))
        self.stock_list.append(Stock(food_name, quantity, price))
        print(f"{food_name} added to stock. Quantity: {quantity}, Price: {price}")

    def check_stock(self):
        print("Current Stock:")
        for stock in self.stock_list:
            print(
                f"{stock.name} ==> Quantity: {stock.quantity} ==> Price: {stock.price}")

    def update_stock(self):
        food_name = input("What food was eaten? ")
        student_name = input("Who ate the food? ")
        amount = int(input("How many did they eat? "))

        food_found = False
        student_found = False

        for stock in self.stock_list:
            if stock.name == food_name:
                food_found = True
                break
        if not food_found:
            print("Food not found in stock.")
            return

        for student in self.students_list:
            if student.name == student_name:
                student_found = True
                if student.wallet < amount * self.get_price(food_name):
                    print("Not enough credit for", student_name)
                    return
                break
        if not student_found:
            print("No student with the name", student_name, "found")
            return

        if student_name in self.already_ate_list:
            print(student_name, "was refused and sent out the queue")
        else:
            if stock.quantity >= int(amount):
                print(student_name, "ate", food_name)
                stock.quantity -= int(amount)
                self.already_ate_list.append(student_name)
                for s in self.students_list:
                    if student.name == student_name:
                        student.wallet -= amount * stock.price
                        break
            else:
                print(student_name, "did not eat because it's out of stock")
        if not food_found:
            print("Food not found in stock.")

    def already_ate(self):
        print("Already Ate:")
        for student in self.already_ate_list:
            print(student)

    def add_student(self):
        student_name = input("Enter Student Name: ")
        wallet_balance = int(input("Enter Wallet Balance: "))
        self.students_list.append(Student(student_name, wallet_balance))
        print(
            f"Student {student_name} added with Wallet Balance: {wallet_balance}")

    def view_students(self):
        print("Current Students:")
        for student in self.students_list:
            print(f"{student.name} ==> Wallet Balance: {student.wallet}")

    def get_price(self, food):
        for stock in self.stock_list:
            if stock.name == food:
                return stock.price
        return None

    def quit_app(self):
        print("Goodbye!")

    def run(self):
        while True:
            print("\nSelect an option:")
            print("1. Add Stock")
            print("2. Check Stock")
            print("3. Add Student")
            print("4. View Students")
            print("5. Update Stock")
            print("6. Already Ate")
            print("7. Quit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_stock()
            elif choice == '2':
                self.check_stock()
            elif choice == '3':
                self.add_student()
            elif choice == '4':
                self.view_students()
            elif choice == '5':
                self.update_stock()
            elif choice == '6':
                self.already_ate()
            elif choice == '7':
                self.quit_app()
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = StockManagementApp()
    app.run()
