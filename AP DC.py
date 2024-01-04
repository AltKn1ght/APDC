import os, time, request
from colorama import Fore

print("ExCL x AltKn1ght\nScript : AutoPOST Discord\nCredits for Youtube : Bang Pateng")
Channel = int(input("Input the ID channel for posting your messages : "))
Delay = int(input("Input the Sending message delay : "))

os.system('cls' if os.name == 'nt' else 'clear')
with open("APMessage.txt", "r") as f:
    Text = f.readlines()
with open("APAccount.txt", "r") as f:
    Authorization = f.readlines().strip()

while True:
    Channel = Channel.strip()
    payload = {
        'Content' : Text
    }
    headers = {
        'Authorization' : Authorization
    }
    r = request.post(f"https://discord.com/api/v9/channels/{Channel}/messages", data=payload, headers=headers)
    print(fore.WHITE + "Send message : " + payload['content'])
    response = request.get(f'https://discord.com/api/v9/channels/{Channel}/messages', headers=headers)
    if response.status_code == 200:
        messages = response.json()
        else:
            print(f'Fail to send a message on channel :'{response.status_code})
            print(f'Gagal Mengirimkan pesan di channel : '{response.status_code})
    time.sleep(Delay)