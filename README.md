# CRM API Automation (Pytest + Python)

##  Project Overview

This project automates REST APIs of a CRM system using **Python, Pytest, and Requests**.
It includes authentication, API validation, and pagination testing with reusable framework design.

---

##  Tech Stack

* Python
* Pytest
* Requests
* JSON

---

##  Features

### Authentication

* Send OTP API
* Verify OTP API
* Extract Access Token
* Use Bearer Token for authorized APIs

---

### Category API

* Create Category
* Get Categories
* Pagination validation

---

### Material API

* Create Material
* Get Materials
* Search functionality
* Pagination validation

---

### Supplier API

* Create Supplier
* Get Suppliers
* Pagination validation

---

##  Key Concepts

* Token-based Authentication (Bearer Token)
* Pytest Fixtures (`auth_api`, `auth_token`)
* Dynamic Data (random values)
* Query Parameters (`page`, `limit`, `search`)
* Response Validation (status code, JSON body)
* Pagination Testing

---

##  Project Structure

crm_api_automation/
│── api/
│── tests/
│── conftest.py
│── requirements.txt
│── README.md

---

##  How to Run

### 1. Clone Repo

git clone https://github.com/MeetShrimal19/crm-api-automation.git
cd crm-api-automation

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Run Tests

pytest -v -s

---

##  Sample Assertions

assert response.status_code in [200, 201]
assert body["success"] is True
assert "results" in body

---

##  Future Improvements

* CI/CD (GitHub Actions / Jenkins)
* Reporting (Allure)
* Negative Test Cases
* Data-driven testing

---

## 👨‍💻 Author

Meet Shrimal
QA Automation Engineer
