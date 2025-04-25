# UI Automation Test Suite - Practice Automation Testing

This project automates several UI test cases for the website [https://practice.automationtesting.in](https://practice.automationtesting.in) using **Selenium WebDriver** with **Python**.

---

## 🧪 Test Cases Automated

### ✅ Positive Test Cases
1. **User Registration / Login**
   - Registers a new user using email and password.
   - If the user already exists, the script logs in with those credentials.

2. **Add Product to Cart**
   - Adds a product to the shopping cart from the Shop page.

3. **Remove Product from Cart**
   - Removes the product from the cart and verifies if the cart is empty.

4. **Add Another Product & Checkout**
   - Adds another product to the cart.
   - Proceeds to checkout and fills in billing information.
   - Places the order successfully.

---

 ## How to Run the Tests
Simply execute the test script with Python:
python test_ui_automation.py


📌 Notes
Make sure Chrome is installed and updated on your machine.

A valid email address is required for registration (update in the script as needed).

The script handles login automatically if the email is already registered.



