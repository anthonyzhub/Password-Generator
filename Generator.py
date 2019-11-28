import secrets
import string
import os

class Cryptography_Class(object):

    def __init__(self):

        # full_keyboard_list[] is only implemented because this class only focuses on encrypting the message
        self.full_keyboard_list = "1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz~!@#$%^&*()_+|}{;?><,./`'"

    def generate_one_time_pad_sheets(self, num_of_sheets, sheets_length):

        # OBJECTIVE: Generate OTP sheets to be used as references later on

        print("Generating OTP sheets...")

        # Create new files
        for sheet in range(num_of_sheets):
            with open("OTP-SHEET__" + str(sheet) + ".txt", "w") as sheet:

                # Write random numbers to file
                for _ in range(sheets_length):
                    sheet.write(str(secrets.randbelow(82)) + "\n")

        print("OTP sheets have been generated!")

    def load_one_time_pad_sheet(self, otp_sheet):

        # OBJECTIVE: Open a one time pad sheet for reading

        print("Loading OTP sheet...")

        # Open OTP sheet
        with open("OTP-SHEET__" + otp_sheet + ".txt", "r") as otp_to_read:

            # 'splitlines() breaks each line up into a single
            # item in the list and removes '\n' character
            message = otp_to_read.read().splitlines()

        # If "message" is not NULL, return it
        if message is not None:
            print("Loaded OTP sheet!")
            return message
        else:
            print("UNLOADED OTP sheet")

    def read_users_file(self, filename):

        # OBJECTIVE: Opens any file that the user chooses

        print("Reading {} file...".format(filename))

        # Open file with read-only
        with open(filename, 'r') as f:
            contents = f.read()

        print("Finished reading.\n*whisphers* About time! {} was too long! *whisphers*\n Oh wait, is this thing on?".format(filename))

        return contents

    def write_users_file(self, filename, data):

        # OBJECTIVE: Create a file and write user's content to it

        print("Writing file as {}".format(filename))

        # Open file with write-only
        with open(filename, 'w') as f:
            f.write(data)

        # Print location of recently written file
        print("{} written at {}".format(filename, os.getcwd()))
        print("Finished writing. \n*Cracks binary knockles*")

    def encrypt_file(self, plain_text, otp_sheet):

        # OBJECTIVE: Encrypt any plain message with an OTP sheet

        # Create empty string variable for further use
        current_cipher_text = ""

        print("Encrypting {}...".format(plain_text))

        # enumerate() returns a character from plaintext and its position
        for position, character in enumerate(plain_text):

            # If character isn't in list, add it to current_cipher_text
            if character not in self.full_keyboard_list:
                current_cipher_text += character
            else:
                # Get position of the character with sheet
                # Break down:
                # 1. self.full_keyboard_list.index(character) -> gets position of the character inside list
                # 2. int(otp_sheet[position]) -> otp_sheet[position] returns character at index
                # 3. Steps #1 and #2 are added, so result is the outcome of shifting from a previous character
                # 4. %81 -> self.full_keyboard_list has a totaly of 81 elements. A modulu is needed if the message is greater
                # than 81 characters, so some characters will be reused

                encrypted_character_result = (self.full_keyboard_list.index(character) + int(otp_sheet[position])) % 81

                # Change number to letter
                current_cipher_text += self.full_keyboard_list[encrypted_character_result]

        if current_cipher_text is not None:
            print("Encryption is complete!")
            return current_cipher_text
        else:
            print("INCOMPLETE encryption")

    def decrypt_file(self, cipher_text, otp_sheet):

        # OBJECTIVE: Decrypt any ciphertext with an OTP sheet

        # Create empty string for further use
        plaintext = ""

        print("Decrypting {}".format(cipher_text))

        # enumerate() returns a character from plaintext and its position
        for position, character in enumerate(cipher_text):

            # Same logic as above
            if character not in self.full_keyboard_list:
                plaintext += character
            else:
                decrypted = (self.full_keyboard_list.index(character) - int(otp_sheet[position])) % 81
                plaintext += self.full_keyboard_list[decrypted]

        if plaintext is not None:
            print("Successful decryption!")
            return plaintext
        else:
            print("UNSUCCESSFUL decryption")

    def decrypt_password_file(self):
        
        # OBJECTIVE: Decrypt encrypted password file and save it as another file

        # Send password file to decrypt_file()
        otp_for_decrypting = input("Which One-Time-Pad (OTP) should be used? (enter # only) ")
        unencrypted_content = self.decrypt_file("password_file_encrypted.txt", otp_for_decrypting)

        # Send unencrypted_content to write_users_file()
        self.write_users_file("Unencrypted_Password_file.txt", unencrypted_content)

    def write_password_file(self, new_account_credentials):
        
        # OBJECTIVE: Write to password file and encrypt it later on
        pass

    def menu_options(self):

        # OBJECTIVE: Main interface for user to encrypt/decrypt files

        pass



class Generator(object):

    def __init__(self):

        # Lists for password composition
        self.numeric_list = "1234567890"
        self.alpha_list = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        self.special_characters_list = "~!@#$%^&*()_+|}{;?><,./`'"
        self.full_keyboard_list = "1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz~!@#$%^&*()_+|}{;?><,./`'"

    def random_pin_generator(self, pin_quantity, pin_length):

        # OBJECTIVE: Generates a random pin with set length

        # Execute for-loop based on pin_quantity
        for i in range(pin_quantity):

            # Create empty string
            pin_suggestion = ""

            # Execute for-loop based on pin_length
            for _ in range(pin_length):
                # pin_suggestion += random.choice(self.numeric_list)
                pin_suggestion += secrets.choice(self.numeric_list)

            # Print suggestion
            print("{} - {}".format(i+1, pin_suggestion))

    def random_alpha_generator(self, alpha_quantity, alpha_length):

        # OBJECTIVE: Generates a random alpha password with set length

        # Execute for-loop based on pin_quantity
        for i in range(alpha_quantity):

            # Create empty string
            alpha_suggestion = ""

            # Execute for-loop based on pin_length
            for _ in range(alpha_length):
                # alpha_suggestion += random.choice(self.alpha_list)
                alpha_suggestion += secrets.choice(self.alpha_list)

            # Print suggestion
            print("{} - {}".format(i+1, alpha_suggestion))

    def random_mix_generator(self, mix_quantity, mix_length):

        # OBJECTIVE: Generates a random password with a set length from all lists

        # Execute for-loop based on pin_quantity
        for i in range(mix_quantity):

            # Create empty string
            mix_suggestion = ""

            # Execute for-loop based on pin_length
            for _ in range(mix_length):
                # mix_suggestion += random.choice(self.full_keyboard_list)
                mix_suggestion += secrets.choice(self.full_keyboard_list)

            # Print suggestion
            print("{} - {}".format(i+1, mix_suggestion))

    def password_request(self):

        # OBJECTIVE: Handle user's action and calls any function N times

        # Ask for quantity of recommendations and password's quantity
        password_type = input("Password type? (Pin/Alpha/Mix) ")

        # If user's selection is not available, then don't continue
        if  password_type not in ["Pin", "Alpha", "Mix"]:
            print("{} is an invalid request!".format(password_type))
            return None
        
        password_quantity = input("How many suggestions? ")
        password_quantity = int(password_quantity)

        password_length = input("How many characters? ")
        password_length = int(password_length)

        # If function is available, execute it
        if password_type == "Pin":
            self.random_pin_generator(password_quantity, password_length)
        elif password_type == "Alpha":
            self.random_alpha_generator(password_quantity, password_length)
        elif password_type == "Mix":
            self.random_mix_generator(password_quantity, password_length)
