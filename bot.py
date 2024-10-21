import time
from datetime import datetime, timedelta
from enum import Enum
from curl_cffi import requests

class ApplicationType(Enum):
    INDIVIDUAL = 1  # Bireysel
    FAMILY = 2      # Aile

class AppointmentTypeId(Enum):
    STANDARD = 16    # Standart
    VIP = 18         # Vip
    EEA_AB_SPOUSE = 2339  # EEA AB Eşi

# Define your Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = "xxxxxxxxxxxxxxxxxxxx"  # Replace with your bot's token
CHAT_ID = "xxxxxxxxxxx"  # Replace with your chat ID

def get_appointment_hour_quota_info(nationality_number, dealer_id, date, application_type, appointment_type, only_available=True):
    url = "https://api.kosmosvize.com.tr/api/AppointmentLayouts/GetAppointmentHourQoutaInfo"
    
    query_params = {
        'nationalityNumber': nationality_number,
        'dealerId': dealer_id,
        'date': date,
        'appointmentTypeId': appointment_type.value,
        'onlyAvailable': str(only_available).lower(),
        'applicationType': application_type.value
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://basvuru.kosmosvize.com.tr',
        'priority': 'u=1, i',
        'referer': 'https://basvuru.kosmosvize.com.tr/',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers, params=query_params)
    return response.json()  # Return JSON directly

# Function to send message to Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=data)  # Use json parameter for sending JSON data

# Example usage
nationality_number = "xxxxxxxxxxx"
dealer_id = 1
application_type = ApplicationType.FAMILY
appointment_type = AppointmentTypeId.STANDARD

while True:
    # Iterate through the next 30 days
    for i in range(30):
        date = (datetime.now() + timedelta(days=i)).strftime("%Y/%m/%d")
        result = get_appointment_hour_quota_info(nationality_number, dealer_id, date, application_type, appointment_type)

        if result and isinstance(result, list) and len(result) > 0:  # Check if result is a non-empty JSON array
            message = f"Available appointments on {date}: {result}"
            send_telegram_message(message)

    # Wait for 10 minutes before checking again
    time.sleep(600)  # 600 seconds = 10 minutes
