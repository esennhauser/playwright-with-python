

## Scope

The automation covers the following scenarios:

### 1. Customer Login

Validates that a customer can successfully authenticate and access the products page.

### 2. Add a product

Validates that a customer can add a product to the cart and verifies is present.

---

## Tech Stack

* Python
* Behave
* Playwright
* Allure
* python-dotenv
* Docker

## Project Structure

```text
.
├── driver/
│   └── driver.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── appointments_page.py
│   └── book_appointment_page.py
├── tests/
│   └── features/
│       ├── environment.py
│       ├── login.feature
│       ├── reschedule_appointment.feature
│       ├── book_appointment.feature
│       └── steps/
│           ├── login_steps.py
│           ├── reschedule_appointment_steps.py
│           └── book_appointment_steps.py
├── behave.ini
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.txt
```

## Design

The project follows the **Page Object Model (POM)** pattern.

Page-specific locators and interactions are encapsulated inside page classes, while Behave step definitions describe the business behavior.

Example:

```text
Feature
   ↓
Step Definition
   ↓
Page Object
   ↓
Playwright
   ↓
Application
```

This keeps test scenarios readable and reduces duplication.

---

# Setup

## Prerequisites

For local execution:

* Python 3.x
* Playwright
* Allure CLI

For Docker execution:

* Docker

## 1. Clone the repository

```bash
git clone <repository-url>
cd playwright-with-python
```

## 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Install Playwright browsers

```bash
playwright install
```

## Environment Variables

Create a `.env` file or use `.env.example` in the project root:

```env
EMAIL=your_email
PASSWORD=your_password
URL=https://www.saucedemo.com/
```

Credentials are loaded using `python-dotenv`.

The `.env` file is excluded from version control.

---

# Running the Tests

## Local execution

Run all scenarios:

```bash
behave tests/features
```

Run a specific feature:

```bash
behave tests/features/login.feature
```

Run a specific test suite:

```bash
behave tests/features --tags=smoke
```

---

# Allure Reports

The framework is configured to generate Allure results automatically. Once you have this folder on your repository:

```text
allure-results/
```

To generate the HTML report, run:

```bash
allure generate allure-results -o allure-report --clean
```


To open:

```bash
allure open allure-report
```

The report contains screenshots associated with each executed step, which makes UI failures easier to investigate.


Latest Allure Report:

https://esennhauser.github.io/playwright-with-python/


---

# Docker

The project can also be executed inside Docker to provide a consistent test environment.

Build image:

```bash
docker build -t saucedemo-tests .
```

Run tests and persist Allure results locally:

```bash
docker run --rm \
  --env-file .env \
  -v "$(pwd)/allure-results:/app/allure-results" \
  saucedemo-tests
```

Generate Allure report

```bash
allure generate allure-results -o allure-report --clean
```

Open report

```bash
allure open allure-report
```

The Docker image contains the Python dependencies and Playwright browser required to execute the test suite.

---
Live demo