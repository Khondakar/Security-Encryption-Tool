# Generate encryption keys, create encrypt and decrypt files using keys
# Author : Khondakar
# Date : 03/Sep/2020
import encrypt
import os
import sys
import glob
from tkinter import filedialog

# Define variable as dictionary to pair up key and value use for encryption
encrypt_key_value_dict = {}


# Define function to create encryption keys
def encryption_key():
    try:
        print("Please enter the encryption key file name to save in a directory : ")
        input("Press <ENTER> to continue...")

        # User will prompt to select folder for saving the key file
        key_file_name = filedialog.asksaveasfilename(initialdir="/", title="Save File As",
                                                     filetypes=(("key files", "*.key"), ("all files", "*.*")))

        # Trim only key file name from the whole path
        key_file_name = key_file_name.split('/')[-1]    # e.g.: MyKeyFile.key

        # Exception handle: check condition for user invalid inputs
        if key_file_name == '':  # if user not provide any key file name
            print("Operation cancelled by the user!")
        else:
            # Call make_key function and add (.key) extension with key file
            if os.path.splitext(key_file_name)[1]:
                encrypt.make_key(key_file_name)
                print("Key File is successfully overwritten!")
            else:
                key_file_name = (os.path.splitext(key_file_name)[0])    # Check key file name with extension
                encrypt.make_key(key_file_name + '.key')
                print("\n:: ENCRYPTION KEY ::")
                print("Encryption key file is successfully created: " + key_file_name + '.key')
    except FileNotFoundError:
        print("Operation cancelled by the user!")


# Define function to encrypt files using existing keys
def encrypt_file_use_existing_key():
    try:
        # Select the main plain file to encrypt
        print("\nStep 1: Please select your Main File (Plain Text) that you want to encrypt : ")
        input("Press <ENTER> to continue...")
        try:
            main_file = filedialog.askopenfile(initialdir="/", title="Select Plain Text File To Encrypt")
            print("The selected main plain file is: " + main_file.name)

            # Select location to save the encrypted file
            print("\nStep 2: Please give a name of encrypted file and select directory to save it : ")
            input("Press <ENTER> to continue...")
            encrypt_file = filedialog.asksaveasfile(initialdir="/", title="Save Encrypted File",
                                                    filetypes=(("encrypt files", "*.enc"), ("all files", "*.*")))

            x = encrypt_file.name
        except AttributeError:
            print("Operation cancelled by the user!")
        else:
            # Trim data from the path value
            encrypt_file = x.split('/')[-1] + ".enc"
            os.remove(x)  # Exception handle: remove file without .enc extension
            print("You have saved encrypted file as: " + encrypt_file)

            # Select a key file for encryption
            print("\nStep 3: Please select the Key File for encryption : ")
            input("Press <ENTER> to continue...")
            key_file = filedialog.askopenfile(initialdir="/", title="Select Key File")
            print("The key file you have selected to encrypt is: " + key_file.name)
            try:
                # Encryption process
                encrypt.encrypt_file(main_file.name, encrypt_file, key_file.name)

                # Update key & value with encrypted file names and their keys paired up
                if encrypt_key_value_dict.keys():
                    encrypt_key_value_dict[key_file.name].append(encrypt_file)
                else:
                    encrypt_key_value_dict[key_file.name] = [encrypt_file]

                print("\nEncryption completed successfully and '" + encrypt_file + "' file is created.")
                input("Press <ENTER> to continue...")
            except AttributeError:
                print("Operation cancelled by the user!!")
    except FileNotFoundError:
        print("Exception: File Not Found!")


# Define function decrypt files using existing keys
def decrypt_file_use_existing_key():
    try:
        # Select encrypted file
        print("\nStep 1: Please select your encrypted file to decrypt : ")
        input("Press <ENTER> to continue...")
        try:
            encrypt_file = filedialog.askopenfile(initialdir="/", title="Select Encrypted File")
            print("The encrypted file you have selected is: " + encrypt_file.name)

            # Select a location to save the decrypted file
            print("\nStep 2: Please select directory to save your decrypted file : ")
            input("Press <ENTER> to continue...")
            decrypt_file = filedialog.asksaveasfile(initialdir="/", title="Save Decrypted File",
                                                    filetypes=(("decrypt files", "*.dec"), ("all files", "*.*")))

            x = decrypt_file.name
        except AttributeError:
            print("Operation cancelled by the user!")
        else:
            # Trim data from the path value
            decrypt_file = x.split('/')[-1] + ".dec"
            os.remove(x)  # Exception handle: remove file without .dec extension
            print("You have saved the decrypted file as: " + decrypt_file)

            # Select a key file for decryption
            print("\nStep 3: Please select the Key File for decryption : ")
            input("Press <ENTER> to continue...")
            key_file = filedialog.askopenfile(initialdir="/", title="Select Key File")
            print("The key file you have selected to decrypt is: " + key_file.name)

            # Decryption process
            encrypt.decrypt_file(encrypt_file.name, decrypt_file, key_file.name)

            print("\nDecryption completed successfully and the decrypted '" + decrypt_file + "' file has created!")
            input("Press <ENTER> to continue...")
    except FileNotFoundError:
        print("Exception: File Not Found!")


# Function to check files exist or not and display files name
def check_files_exist_count():
    try:
        decrypt_file_count = 0
        key_file_count = 0
        encrypt_file_count = 0

        # Check and count of decrypted (.dec) files
        WorkingPath = os.path.dirname(os.path.abspath(__file__))
        for file in glob.glob(os.path.join(WorkingPath, '*.dec')):
            decrypt_file_count += 1
        print("\n[1] Number of decrypted(.dec) files being created = " + str(decrypt_file_count))
        print("    The files are: " + str(glob.glob("*.dec")))
        path = str(glob.glob("*.dec"))
        print("    All files created under this path : " + os.path.dirname(os.path.abspath(path)))

        # Check and count of encrypted (.enc) files
        WorkingPath = os.path.dirname(os.path.abspath(__file__))
        for file in glob.glob(os.path.join(WorkingPath, '*.enc')):
            encrypt_file_count += 1
        print("\n[2] Number of encrypted(.enc) files being created = " + str(encrypt_file_count))
        print("   The files are: " + str(glob.glob("*.enc")))
        path = str(glob.glob("*.enc"))
        print("   All files created under this path : " + os.path.dirname(os.path.abspath(path)))

        # Check and count of .key files being generated
        WorkingPath = os.path.dirname(os.path.abspath(__file__))
        for file in glob.glob(os.path.join(WorkingPath, '*.key')):
            key_file_count += 1
        print("\n[3] Number of (.key) file being created = " + str(key_file_count))
        print("   The files are: " + str(glob.glob("*.key")))
        path = str(glob.glob("*.key"))
        print("   All files created under this path : " + os.path.dirname(os.path.abspath(path)))
    except FileNotFoundError:
        print("Exception: File not found!")


# Define main menu function
def main_menu():
    # Check list 1: Using infinite while Loop to keep user in the main menu
    selection = 0
    while selection <= 4:
        # Check list 2: Menu with exit option [4]
        print("""
        :: CREATE ENCRYPTION KEYS, ENCRYPT & DECRYPT FILES USING KEYS ::
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        MAIN MENU:
        [1] Create encryption keys.
        [2] Encrypt files using existing keys.
        [3] Decrypt files using existing keys.
        [4] Exit.
                """)
        # Exception handing by calling try/exception build-in function
        try:
            selection = int(input("What would you like to do? Please select option 1 to 4 -> "))
            if selection == 1:
                encryption_key()  # call encryption_key function
            elif selection == 2:
                # Exception handle: if user select wrong key file
                try:
                    encrypt_file_use_existing_key()  # call encrypt_file_use_existing_key function
                except Exception as err:
                    print("Invalid key file used!! Contact IT support team and try again.")
            elif selection == 3:
                # Exception handle: if user select wrong key file
                try:
                    decrypt_file_use_existing_key()  # call decrypt_file_use_existing_key function
                except Exception as err:
                    print("Invalid key file used!! Contact IT support team and try again.")
            elif selection == 4:
                print("\nSUMMARIES REPORT:")
                print("~~~~~~~~~~~~~~~~~")
                print("The following files are created under the current directory:")
                check_files_exist_count()  # Call the files count function
                # Check list 12: Display encrypted file names and their keys names are paired
                print("\n[4] List of key file being used to encrypt file: ", "\n", encrypt_key_value_dict)
                print("\nThank you for using this program! Goodbye.")
                sys.exit()
            else:
                print("\nNot a Valid Choice! Try again from option 1 to 4.")
                selection = 0
        except ValueError:  # try/exception part end here
            print("\nInvalid user input! Please provide valid input!")
            print("Please select valid option from the menu 1 to 4.")


# Main function
if __name__ == '__main__':
    main_menu()  # call main menu function
