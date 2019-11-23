import random

class Generator:

    def __init__(self):
        self.numeric_list = "1234567890"
        self.alpha_list = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        self.special_characters_list = "~!@#$%^&*()_+|}{;?><,./`"
        self.full_keyboard_list = "1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz~!@#$%^&*()_+|}{;?><,./`"

    def randomPinGenerator(self, pin_length):

        # OBJECTIVE: Generates a random pin with set length

        # Create empty string
        pin_suggestion = ""

        # Execute loop based on pin_length times
        for i in range(pin_length):

            # Add randomly selected digit to string
            pin_suggestion += random.choice(self.numeric_list)

        # Return suggestion
        return pin_suggestion

    def randomAlphaGenerator(self, password_length):

        # OBJECTIVE: Generates a random password with set length

        # Create an empty string
        alpha_suggestion = ""

        # Execute loop based on password_length times
        for i in range(password_length):

            # Add randomly selected digit to string
            alpha_suggestion += random.choice(self.alpha_list)

        # Return suggestion
        return alpha_suggestion

    def randomMixGenerator(self, password_length):

        # OBJECTIVE: Generates a random password with a set length from all lists

        # Create an empty string
        mix_password_suggestion = ""

        # Execute loop password_length times
        for i in range(password_length):

            # Select a random character, then add it to string
            mix_password_suggestion += random.choice(self.full_keyboard_list)

        return mix_password_suggestion

    def passwordRequest(self, generator_selected, suggested_quantity, suggested_length):

        # OBJECTIVE: Handle user's action and calls any function N times

        if generator_selected == "Mix":
            for i in range(suggested_quantity):
                print(f'{i}. {self.randomMixGenerator(suggested_length)}')

        elif generator_selected == "Alpha":
            for i in range(suggested_quantity):
                print(f'{i}. {self.randomAlphaGenerator(suggested_length)}')

        elif generator_selected == "Pin":
            for i in range(suggested_quantity):
                print(f'{i}. {self.randomPinGenerator(suggested_length)}')

        else:
            print(f'Invalid request')