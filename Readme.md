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

Run the full test suite and generate an HTML report:
```bash
pytest -s -v --html=report.html
```
