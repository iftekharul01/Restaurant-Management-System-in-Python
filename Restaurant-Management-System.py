from abc import ABC, abstractmethod

class MenuItem:
    def __init__(self, data, foodname, quantity, price):
        self.data = data
        self.foodname = foodname
        self.quantity = quantity
        self.price = price

    def __str__(self):
        if self.quantity == 0:
            return f"{self.data}\t{self.foodname}\t{self.price:.2f}"
        else:
            return f"{self.data}\t{self.foodname}\t{self.quantity}\t{self.price:.2f}"

class AbstractMenu(ABC):
    @abstractmethod
    def add_item(self, data, foodname, price):
        pass

    @abstractmethod
    def delete_item(self, data):
        pass

    @abstractmethod
    def check_item(self, data):
        pass

    @abstractmethod
    def display(self):
        pass

class Menu(AbstractMenu):
    def __init__(self):
        self.items = []

    def add_item(self, data, foodname, price):
        new_item = MenuItem(data, foodname, 0, price)
        self.items.append(new_item)

    def delete_item(self, data):
        for item in self.items:
            if item.data == data:
                self.items.remove(item)
                return True
        return False

    def check_item(self, data):
        for item in self.items:
            if item.data == data:
                return True
        return False

    def get_item(self, data):
        for item in self.items:
            if item.data == data:
                return item
        return None

    def display(self):
        for item in self.items:
            print(item)

class TotalSales(Menu):
    def calculate_total_sale(self):
        total_sale = sum((item.price * item.quantity) for item in self.items)
        return total_sale

    def display(self):
        super().display()  # Call the display method from the Menu class
        total_sale = self.calculate_total_sale()
        print(f"\n\t\t\t\t\t\t\t\tTotal Sale: {total_sale:.2f}")

class RestaurantManagementSystem:
    def __init__(self):
        self.menu = Menu()
        self.total_sales = TotalSales()
        self.__pass = "1234"
        self.customer_orders = []

        # Add predefined items to the total sales
        self.predefine_sales()

    def get_pas(self):
        return self.__pass

    def set_pas(self, pas):
        pass

    def predefine_sales(self):
        predefined_items = [
            (1, "Rice", 10, 10),
            (2, "Fish Curry", 5, 60),
            (4, "Grill Chicken", 3, 120)
        ]
        for data, foodname, quantity, price in predefined_items:
            self.total_sales.add_item(data, foodname, price)
            added_item = self.total_sales.get_item(data)
            added_item.quantity = quantity

    def admin_menu(self):
        print("\n\t\t\t\t\t\t\t1. View total sales")
        print("\t\t\t\t\t\t\t2. Add new items in the order menu")
        print("\t\t\t\t\t\t\t3. Delete items from the order menu")
        print("\t\t\t\t\t\t\t4. Display order menu")
        print("\t\t\t\t\t\t\t5. Back To Main Menu")
        choice = input("\n\t\t\t\t\t\t\t   Enter Your Choice ---> ")
        return choice

    def customer_menu(self):
        print("\n\t\t\t\t\t\t\t1. Place your order")
        print("\t\t\t\t\t\t\t2. View your ordered items")
        print("\t\t\t\t\t\t\t3. Delete an item from order")
        print("\t\t\t\t\t\t\t4. Display final bill")
        print("\t\t\t\t\t\t\t5. Back To Main Menu \n\n")
        choice = input("\n\t\t\t\t\t\t\t   Enter Your Choice ---> ")
        return choice

    def add_item_to_menu(self):
        try:
            num = int(input("\n\t\t\t\t\t\t\tEnter serial no. of the food item: "))
            if not self.menu.check_item(num):
                name = input("\t\t\t\t\t\t\tEnter food item name: ")
                price = float(input("\t\t\t\t\t\t\tEnter price: "))
                self.menu.add_item(num, name, price)
                print("\n\t\t\t\t\tNew food item added to the list!!\n\n")
            else:
                print("\n\t\t\t\t\t\tFood item with given serial number already exists!!\n\n")
        except ValueError:
            print("\n\t\t\t\t\t\tError: Please enter a valid integer for the serial number.")
        except Exception as e:
            print("\n\t\t\t\t\t\tError:", str(e))

    def delete_item_from_menu(self):
        try:
            num = int(input("\n\t\t\t\t\tEnter serial no. of the food item which is to be deleted: "))
            if self.menu.delete_item(num):
                print("\n\t\t\t\t\t\t### Updated list of food items menu ###")
                self.menu.display()
            else:
                print("\n\t\t\t\t\t\tFood item with given serial number doesn't exist!\n\n")
        except ValueError:
            print("\n\t\t\t\t\tError: Please enter a valid integer for the serial number.")
        except Exception as e:
            print("\n\t\t\t\t\tError:", str(e))

    def display_order_menu(self):
        print("\n\t\t\t\t\t\t\t   ### Order menu ###")
        self.menu.display()

    def display(self):
        self.total_sales.display()

    def main_menu(self):
        print("\n                                 **************************************************************************")
        print("                                                     WELCOME TO RESTAURANT MANAGEMENT SYSTEM")
        print("                                 **************************************************************************\n\n\n")
        print("\t\t\t\t\t\t\t1. ADMIN SECTION")
        print("\t\t\t\t\t\t\t2. CUSTOMER SECTION")
        print("\t\t\t\t\t\t\t3. Exit\n\n")
        choice = input("\t\t\t\t\t\t\tEnter Your Choice ---> ")
        return choice

    def run(self):
        while True:
            choice = self.main_menu()
            if choice == '3':
                print("\n\n\n\n\n\n\t\t\t\t\t\t\t************Thank you!!************\n\n")
                break
            elif choice == '1':
                id = input("\t\t\t\t\t\t\tEnter UserId: ")
                pas = input("\t\t\t\t\t\t\tEnter Password: ")
                if id == 'admin' and pas == self.get_pas():
                    self.admin_section()
                else:
                    print("Wrong Id or Password")
            elif choice == '2':
                self.customer_section()
            else:
                print("\n\t\t\t\t\t\tWrong Input !! Please choose a valid option\n")

    def admin_section(self):
        print("\n\t\t\t\t\t   ----------------------------------------------\n")
        print("\t\t\t\t\t\t\t    ADMIN SECTION\n")
        print("\n\t\t\t\t\t   ----------------------------------------------\n")
        while True:
            opt = self.admin_menu()
            if opt == '5':
                break
            elif opt == '1':
                print("\n")
                self.display()
            elif opt == '2':
                self.display_order_menu()
                self.add_item_to_menu()
            elif opt == '3':
                self.display_order_menu()
                self.delete_item_from_menu()
            elif opt == '4':
                self.display_order_menu()
            else:
                print("\n\t\t\t\t\t\tWrong Input !! Please choose a valid option\n")

    def customer_section(self):
        print("\n\t\t\t\t\t   ----------------------------------------------\n")
        print("\t\t\t\t\t\t\t    CUSTOMER SECTION\n")
        print("\n\t\t\t\t\t   ----------------------------------------------\n")
        while True:
            opt = self.customer_menu()
            if opt == '5':
                self.customer_orders = []  # Reset customer orders
                break
            elif opt == '1':
                self.display_order_menu()
                self.place_order()
            elif opt == '2':
                self.view_ordered_items()
            elif opt == '3':
                self.view_ordered_items()
                self.delete_ordered_item()
            elif opt == '4':
                self.display_final_bill()
            else:
                print("\n\t\t\t\t\t\tWrong Input !! Please choose a valid option\n")

    def place_order(self):
        try:
            num = int(input("\n\t\t\t\t\tEnter serial no. of the food item: "))
            item = self.menu.get_item(num)
            if item:
                quantity = int(input("\t\t\t\t\tEnter quantity: "))
                ordered_item = MenuItem(item.data, item.foodname, quantity, item.price)
                self.customer_orders.append(ordered_item)
                self.total_sales.add_item(item.data, item.foodname, item.price)  # Add to total sales
                added_item = self.total_sales.get_item(item.data)
                added_item.quantity += quantity
                print("\n\t\t\t\t\tOrder placed successfully!\n")
            else:
                print("\n\t\t\t\t\tFood item with given serial number doesn't exist!\n")
        except ValueError:
            print("\n\t\t\t\t\tError: Please enter a valid integer for the serial number and quantity.")
        except Exception as e:
            print("\n\t\t\t\t\tError:", str(e))

    def view_ordered_items(self):
        if not self.customer_orders:
            print("\n\t\t\t\t\tNo items ordered yet!\n")
        else:
            print("\n\t\t\t\t\t### Ordered items ###")
            for item in self.customer_orders:
                print(item)

    def delete_ordered_item(self):
        if not self.customer_orders:
            self.customer_section()
        else:
            try:
                num = int(input("\n\t\t\t\t\tEnter serial no. of the food item to delete from order: "))
                for item in self.customer_orders:
                    if item.data == num:
                        self.customer_orders.remove(item)
                        print("\n\t\t\t\t\tItem removed from order!\n")
                        return
                print("\n\t\t\t\t\tItem not found in your order!\n")
            except ValueError:
                print("\n\t\t\t\t\tError: Please enter a valid integer for the serial number.")
            except Exception as e:
                print("\n\t\t\t\t\tError:", str(e))

    def display_final_bill(self):
        if not self.customer_orders:
            print("\n\t\t\t\t\tNo items ordered yet!\n")
        else:
            print("\n\t\t\t\t\t### Final Bill ###")
            total = 0
            for item in self.customer_orders:
                print(item)
                total += item.price * item.quantity
            print(f"\n\t\t\t\t\tTotal Bill: {total:.2f}\n")

# Initialize the restaurant management system
rms = RestaurantManagementSystem()
rms.menu.add_item(1, "Rice", 10)
rms.menu.add_item(2, "Fish Curry", 60)
rms.menu.add_item(3, "Chicken Masala", 80)
rms.menu.add_item(4, "Grill Chicken", 120)
rms.run()
