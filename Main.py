import sys
from Generator import Generator
from Generator import Cryptography_Class

if __name__ == "__main__":

    # Create instance of all imported classes
    generator_class = Generator()
    crypto_class = Cryptography_Class()

    # Accept Terminal commands
    arguments = sys.argv

    if len(arguments) != 2:

        # Print message and stop program
        # mode -> gp (generate password), vp (view passwords)
        # file -> Text file to write in or read from
        print("Usuage: psswd_gen <mode> [file]")
        exit(0)

    # Execute password_request() with the following arguments
    if (arguments[1] == "gp") or (arguments[1] == "Generate Password"):

        # Show password generating options
        generator_class.password_request()

        # Ask user if password should be saved to an OTP file
        save_file = input("Save a password to file? Y/n")
        
        if save_file == "Y" or save_file == "y":
            crypto_class.menu_options()
