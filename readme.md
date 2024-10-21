# Appointment Availability Checker

This Python script checks appointment availability on the Kosmos Visa system for the next 30 days and sends a notification to a specified Telegram chat when appointments are available. The script runs in a loop and checks for new appointments every 10 minutes.

## Features
- Fetches appointment quota information for a specified nationality, dealer, and appointment type.
- Sends Telegram notifications when new appointments are available.
- Configurable for different application types and appointment types.

## Prerequisites

To run this script, you need the following:

1. **Python 3.x** installed on your machine.
2. Install the required libraries using `pip`:
    ```bash
    pip install curl_cffi
    ```

## How to Use

1. **Clone or Download the Repository**  
   Clone the repository or download the script to your local machine.

2. **Set Your Configuration**  
   Modify the following in the script with your own values:
   - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token. Create a bot using [BotFather](https://core.telegram.org/bots#botfather) if you don't have one.
   - `CHAT_ID`: The chat ID where you want to receive notifications. You can find this by messaging your bot and inspecting the response.
   - `nationality_number`: Set the nationality number for the applicant.
   - `dealer_id`: Set the dealer ID for your case.
   - `application_type`: Choose between `INDIVIDUAL` or `FAMILY` for the application type.
   - `appointment_type`: Choose between `STANDARD`, `VIP`, or `EEA_AB_SPOUSE` for the appointment type.

3. **Run the Script**  
   Run the script using Python:
   ```bash
   python bot.py
