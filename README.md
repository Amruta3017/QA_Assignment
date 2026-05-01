# QA Automation Assignment – End-to-End Testing

## Project Overview

This project demonstrates an end-to-end automation framework for testing the login and dashboard functionality of the SauceDemo application.

The framework is built using **Python + Selenium + Pytest** following **Page Object Model (POM)** design to ensure scalability, maintainability, and reusability.

---

## Objectives Covered

* Automate login functionality (valid & invalid scenarios)
* Validate dashboard elements after login
* Handle edge cases (empty input, special characters, etc.)
* Implement reusable automation framework
* Capture screenshots on test failure

---

## Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)

---

## Project Structure

```
qa-automation-assignment/
│
├── tests/
│   ├── test_login.py
│   ├── test_add_to_cart.py
│   ├── test_logout.py
│   └── conftest.py
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── logout_page.py
│
├── utils/
│   ├── driver_factory.py
│   ├── waits.py
│   └── screenshot.py
│
├── config/
│   └── config.py
│
├── screenshots/
├── TEST_CASES.md
├── requirements.txt  
└── README.md
```

---

## Setup Instructions

<<<<<<< HEAD
### Clone Repository
=======
###  Clone Repository
>>>>>>> 06041a2 (Update framework)

```bash
git clone https://github.com/Amruta3017/QA_Assignment.git
cd QA_Assignment
<<<<<<< HEAD
```
```

# Create Virtual Environment
=======
```

### Create Virtual Environment
>>>>>>> 06041a2 (Update framework)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install selenium pytest
```

---

<<<<<<< HEAD
##  How to Run Tests
=======
## How to Run Tests
>>>>>>> 06041a2 (Update framework)

Run all tests:

```bash
pytest
```

Run specific test file:

```bash
pytest tests/test_login.py
```

Run single test:

```bash
pytest tests/test_login.py::test_valid_login
```
Run the complete test suite using the following command:

```bash
pytest -v -s tests/ --html=reports/report_01may2026.html --self-contained-html
```

### Command Purpose

- `-v` → Enables verbose mode for detailed test execution logs  
- `-s` → Displays print statements in the console  
- `tests/` → Specifies the test directory  
- `--html=...` → Generates an HTML execution report  
- `--self-contained-html` → Creates a standalone report file for easy sharing  

### Output

- Executes all test cases inside the `tests/` folder  
- Displays execution details in the terminal  
- Generates a professional HTML report inside the `reports/` directory  

This helps in debugging, result analysis, and sharing execution outcomes with stakeholders.
---

## Test Scenarios Covered

### Login Tests

* Valid login
* Invalid login
* Empty username
* Empty password
* Empty username & password
* Special characters input
* Very long input values

# Cart Test

* Add item to cart and verify cart count

# Logout Test

* Verify user can logout successfully

# Dashboard Validation

* Verify URL after login
* Validate page title ("Products")
* Check UI elements (cart, menu, buttons)
* Verify product listing section

---

# Screenshot Handling

* Screenshots are captured on test failure using a reusable utility function
* Stored in:

```
screenshots/
```

---

# Framework Features

* Page Object Model (POM) design
* Reusable utility functions
* Explicit waits for better stability
* Pytest fixtures for driver setup and teardown
* Clean and maintainable structure

---

## Test Case Document

Detailed test cases are available in:

```
TEST_CASES.md
```

---

## Key Highlights

* Covers **positive, negative, edge, and security scenarios**
* Implements a **scalable automation framework**
* Follows **industry best practices**
* Easy to extend for additional test scenarios

---

# Author

**Amruta Mali**
