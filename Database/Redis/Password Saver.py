# Python's version used: 3.8.2 64 bit
# Need on Manjaro to install the package:
# sudo pacman -S xclip
# pip install xerox
# pip install redis
# Redis' server need to be active
import redis
import xerox

# Creating connection
client = redis.StrictRedis(host="127.0.0.1", port=6379, db=0)
print("\n")

# Starting the while loop
while True:
    try:
        # Choosing the action to do
        x = input('''Type 1 to add a password.
Type 2 to retrieve a password.
Type 3 to delete a password.
Type 4 to delete all passwords.
Type 5 to exit.
You can press CTRL+C to exit the program directly in any moment.
Your choice: ''')
        # Converting the input in int
        x = int(x)
        print("\n")

        if x == 1:
            # Saving a key-password couple
            key = input("Insert the Name of the Password: ")
            if key == "":
                print("You can't insert an empty Name!")
                input("Press any key to continue: ")
                print("\n")
            else:
                value = input("Insert the Password: ")
                if value == "":
                    print("You can't insert an empty Password!")
                    input("Press any key to continue: ")
                    print("\n")
                else:
                    client.set(key, value)
                    print("Password saved!")
                    input("Press any key to continue: ")
                    print("\n")

        elif x == 2:
            # Printing all the keys in the database
            print("Saved Passwords:")
            for key in client.scan_iter():
                # Converting the bytes in string
                key1 = key.decode("utf-8")
                print(key1)
            print("\n")
            key2 = input("Type which password you wanna retrieve: ")
            # Converting the text written in bytes for Redis
            key3 = bytes(key2, 'utf-8')
            # Checking if the password is in the database
            if key3 in client.scan_iter():
                # Copying the value to the clipboard
                password = client.get(key2)
                # Converting the bytes in string
                password = password.decode("utf-8")
                # Copying the password to the clipboard
                xerox.copy(password)
                print("Password copied to the clipboard!")
                input("Press any key to continue: ")
                print("\n")
            else:
                print("No password associated to this name!")
                input("Press any key to continue: ")
                print("\n")
                pass

        elif x == 3:
            # Printing all the keys in the database
            print("Saved Passwords:")
            for key in client.scan_iter():
                # Converting the bytes in string
                key1 = key.decode("utf-8")
                print(key1)
            print("\n")
            key2 = input("Type which password you wanna delete: ")
            # Converting the text written in bytes for Redis
            key3 = bytes(key2, 'utf-8')
            # Checking if the password is in the database
            if key3 in client.scan_iter():
                client.delete(key3)
                print("Password correctly deleted from the database!")
                input("Press any key to continue: ")
                print("\n")
            else:
                print("No password associated to this name!")
                input("Press any key to continue: ")
                print("\n")
                pass

        elif x == 4:
            y = input('''Do you really wanna delete all passwords?
Type "yes" if yes or any other key to return to the menu: ''')
            if y == "yes":
                # Delete all passwords in the database
                client.flushdb()
                print("All passwords correctly deleted from the database!")
                input("Press any key to continue: ")
                print("\n")
            else:
                print("\n")
                pass

        elif x == 5:
            print("Bye Bye!\n")
            # Exit the program
            break

        else:
            print("Wrong input!")
            input("Press any key to continue: ")
            print("\n")

    # When a wrong input is typed
    except (ValueError):
        print("\n")
        print("Wrong input!")
        input("Press any key to continue: ")
        print("\n")

    # When CTRL+C is typed
    except (KeyboardInterrupt):
        print("\n")
        print("Bye Bye!\n")
        break
