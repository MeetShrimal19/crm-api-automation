# CRM API Automation

This is an API test automation framework for the CRM backend.

## Requirements
- Python 3.x

## Setup & Installation

1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up the environment variables:
   Create a `.env` file in the root directory based on the following template:
   ```env
   BASE_URL=https://dev-api.profitmanager.in
   EMAIL=your-registered-email@example.com
   OTP=123456
   ```

## Running Tests

Run the full test suite and automatically generate Allure report data:
```bash
python -m pytest
```

*(Note: The framework is configured to save test results in an `allure-results` folder automatically.)*

### Viewing the Allure HTML Report
To view the graphical dashboard, you must have the Allure command-line tool installed on your system (`npm install -g allure-commandline` or `scoop install allure`).

Once the tests finish, serve the report in your browser by running:
```bash
allure serve allure-results
```
