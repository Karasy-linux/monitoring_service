import config
import requests
import sys
import time


def send_telegram(text,max_matries=3):
    
    token = config.BOT_TOKEN
    chat_id = config.CHAT_ID
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id, 
        "text": text
    }
    for i in range(max_matries):
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("Message sent!")
                return True
            else:
                print(f"Telegram error: {response.text}")
        except Exception as e:
            print(f"network error: {e}/n please wait 5 sec")
            time.sleep(20)

if __name__ == "__main__":
    # if you want write on konsole: python3 send_tg.py
    message = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Test message"
    send_telegram(message)