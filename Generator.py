import random

class Generator(object):

    def __init__(self):

        # Lists for password composition
        self.numeric_list = "1234567890"
        self.alpha_list = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        self.special_characters_list = "~!@#$%^&*()_+|}{;?><,./`"
        self.full_keyboard_list = "1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz~!@#$%^&*()_+|}{;?><,./`"

    def randomPinGenerator(self, pin_quantity, pin_length):

        # OBJECTIVE: Generates a random pin with set length

        # Execute for-loop based on pin_quantity
        for i in range(pin_quantity):

            # Create empty string
            pin_suggestion = ""

            # Execute for-loop based on pin_length
            for _ in range(pin_length):
                pin_suggestion += random.choice(self.numeric_list)

            # Print suggestion
            print("{} - {}".format(i+1, pin_suggestion))

    def randomAlphaGenerator(self, alpha_quantity, alpha_length):

        # OBJECTIVE: Generates a random password with set length

        # Execute for-loop based on pin_quantity
        for i in range(alpha_quantity):

            # Create empty string
            alpha_suggestion = ""

            # Execute for-loop based on pin_length
            for _ in range(alpha_length):
                alpha_suggestion += random.choice(self.alpha_list)

            # Print suggestion
            print("{} - {}".format(i+1, alpha_suggestion))

    def randomMixGenerator(self, mix_quantity, mix_length):

        # OBJECTIVE: Generates a random password with a set length from all lists

        # Execute for-loop based on pin_quantity
        for i in range(mix_quantity):

            # Create empty string
            mix_suggestion = ""

            # Execute for-loop based on pin_length
            for _ in range(mix_length):
                mix_suggestion += random.choice(self.full_keyboard_list)

            # Print suggestion
            print("{} - {}".format(i+1, mix_suggestion))

    def passwordRequest(self):

        # OBJECTIVE: Handle user's action and calls any function N times

        # Ask for quantity of recommendations and password's quantity
        password_type = input("Which kind of password? (Pin/Alpha/Mix) ")

        if not (password_type in ["Pin", "Alpha", "Mix"]):
            print("{} is an invalid request!".format(password_type))
            return None
        
        password_quantity = input("How many suggestions? ")
        password_quantity = int(password_quantity)

        password_length = input("How many characters? ")
        password_length = int(password_length)

        # If function is available, execute it
        if password_type == "Pin":
            self.randomPinGenerator(password_quantity, password_length)
        elif password_type == "Alpha":
            self.randomAlphaGenerator(password_quantity, password_length)
        elif password_type == "Mix":
            self.randomMixGenerator(password_quantity, password_length)
