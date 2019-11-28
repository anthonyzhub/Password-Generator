from Generator import Generator

if __name__ == "__main__":

    # Create instance of Generator class
    generator_class = Generator()

    while True:

        # Print options to user
        print("0. Exit")
        print("1. Generate Password")
        print("2. View Saved Passwords")

        # Ask for selection
        option_selected = input("Enter Option: ")

        # Check if user wants to terminate program
        if option_selected == "0":
            exit(1)
        elif option_selected == "1":
            generator_class.password_request()
