# 🚀 Internet Speed Monitor & Alert Bot

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white)
![Automation](https://img.shields.io/badge/Type-Browser_Automation-orange)
![Security](https://img.shields.io/badge/Credentials-Environment_Variables-blue)
![Email Alerts](https://img.shields.io/badge/Alerts-SMTP_TLS-red)
![Status](https://img.shields.io/badge/Status-Stable-success)

### A Python automation project that measures real-time internet speed using Selenium and automatically sends an email alert if the results fall below the promised ISP contract threshold.

## 📌 Project Overview

Internet providers often promise specific download and upload speeds. This tool:

1. Launches a Chrome browser using Selenium

2. Navigates to Speedtest.net

3. Executes a speed test

4. Extracts the live download and upload results

5. Compares results to predefined thresholds

6. Sends an automated email alert if performance is below expectations

## 🛠 Tech Stack

- Python 3

- Selenium WebDriver

- WebDriverWait & Expected Conditions

- SMTP (Gmail TLS)

- python-dotenv

- ChromeDriver

## Coding Highlights
- ✅ Explicit Waits (No Hardcoded Sleeps)
 
    Uses WebDriverWait instead of time.sleep() to handle dynamic loading reliably.


- ✅ Secure Credentials

    Sensitive data is stored in a .env file and never hardcoded.


- ✅ Dynamic Content Handling

    Waits specifically for result elements (download-speed and upload-speed) before extraction.


- ✅ Graceful Error Handling

    SMTP wrapped in try/except block to prevent crashes.

## ⚠️ Legacy Feature (Disabled)

The original version attempted to automate posting complaints directly to X (Twitter) using Selenium.

Due to modern anti-bot protections and login flow instability, this feature was intentionally removed and replaced with a reliable SMTP-based email alert system.

This design decision improves:

- Ethical automation

- Greater stability

- More reliable and maintainable code

## 📂 Project Structure
    internet-speed-bot/
    │
    ├── main.py
    ├── .env.example
    ├── requirements.txt
    ├── .gitignore
    └── README.md

## 🧾 Setup Instructions

1. Copy `.env.example` and rename it to `.env`.


2. Open `.env` and add your credentials:


    EMAIL_ADDRESS="your_email@gmail.com"
    EMAIL_PASSWORD="your_app_password"
    ISP_EMAIL="isp@example.com"
    PROMISED_DOWN=100
    PROMISED_UP=50

3. Save the file and run the script.

⚠️ Use a Gmail App Password (not your real password).

## ▶️ How to Run

    git clone https://github.com/fernandogrh/internet-speed-monitor-bot.git
    cd internet-speed-monitor-bot
    pip install -r requirements.txt
    python main.py

## 📊 Example Output
    Download Speed: 128.45 Mbps
    Upload Speed: 8.23 Mbps
    🚨 Internet Speed Alert Sent


## 👨‍💻 Author
Built by **Fernando Ramirez**