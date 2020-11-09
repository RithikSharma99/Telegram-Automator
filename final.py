from telethon import TelegramClient  # pip install telethon
import asyncio
import time
import random
import tkinter as tk
from tkinter import filedialog as fd


# Get you API_ID and HASH from -> https://my.telegram.org
API_ID = "YOUR API WITHOUT QUOTES"
API_HASH = "YOUR API HASH"
client = TelegramClient("Automator", API_ID, API_HASH)


async def main():
    # print(client.get_me().stringify()) # Info of your account and session
    print("\n" + "#" * 15 + " WELCOME TO TELEGRAM AUTOMATOR " + "#" * 15)
    print("Kindly enter you phone number with country code if prompted.")
    time.sleep(1)

    print("\nStarting Session...")
    user_names = []
    messages = (
        "Hello There!",
        "Hi. What's Up?",
        "Greetings of the day :)"
    )
    MESSAGE = random.choice(messages)
    ATTACHMENTS = []
    while True:
        print("\n" + "*" * 70)
        print("\n1. Add Username")
        print("2. Enter/Update Message")
        print("3. Send Message")
        print("4. Quit")

        try:
            user_choice = int(input("\nChoose: "))
        except ValueError:
            print("Invalid Option!")
            continue

        if user_choice == 1:
            user_cnt = 0
            while True:
                user_name = input("\nEnter a valid Username: ")
                if user_name not in user_names:
                    user_names.append(user_name)
                    user_cnt += 1
                    print("User Added!")

                else:
                    print("\nUser already present!")

                choice = input("\nAdd more? [y/n]: ")
                if choice.lower() == "n":
                    print(f"\n{user_cnt} User(s) Added!")
                    break

                elif choice.lower() != "y":
                    print("\nInvalid Option!")

        elif user_choice == 2:
            new_msg = input("\nEnter a message to send: ")
            MESSAGE = new_msg
            print('Message Added!\n')
            file_choice = input(
                "Would you like to send any attachments? [y/n]: ")
            if file_choice.lower() == "y":
                count = 0
                while True:
                    tk.Tk().withdraw()  # Prevent root window from opening
                    attachment = fd.askopenfile("r").name
                    ATTACHMENTS.append(attachment)
                    count += 1
                    print("Attachment Added!")
                    choice = input("\nAdd more? [y/n]: ")
                    if choice.lower() == "n":
                        print(f"\n{count} Attachments Added!")
                        break
            else:
                print("No attachments attached...")

        elif user_choice == 3:
            print("\nSending Now...\n")
            if user_names:
                for name in user_names:
                    time.sleep(0.5)
                    try:
                        await client.send_message(name, MESSAGE)
                        if ATTACHMENTS:
                            for file in ATTACHMENTS:
                                await client.send_file(name, file)
                        print(f"Message successfully sent to {name}")
                    except:
                        print(
                            f"Bad Request! Could not send message to {name}.")
            else:
                print("No user names found! First add some...")

        elif user_choice == 4:
            print("\nExiting...")
            break

        else:
            print("Invalid Option!")

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
