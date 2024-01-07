import os
import time
import requests
from colorama import Fore

print("ExCL x AltKn1ght\nScript : AutoPOST Discord\nSpecial Credits for Bang Pateng")
Delay = int(input("Input the Sending message delay : "))

os.system('cls' if os.name == 'nt' else 'clear')

with open("APChannel.txt", "r") as f:
    Channel = f.readline().strip()
    
with open("APMessage.txt", "r") as f:
    Text = f.read()

with open("APAccount.txt", "r") as f:
    Authorization = f.readline().strip() 

while True:
    payload = {
        'content': Text
    }
    headers = {
        'Authorization': Authorization
    }

    r = requests.post(f"https://discord.com/api/v9/channels/{Channel}/messages", data=payload, headers=headers)
    print(Fore.WHITE + "Send message : " + payload['content'])

    response = requests.get(f'https://discord.com/api/v9/channels/{Channel}/messages', headers=headers)
    if response.status_code == 200:
        messages = response.json()
    else:
        print(f'Fail to send a message on channel : {response.status_code}')

    time.sleep(Delay)
