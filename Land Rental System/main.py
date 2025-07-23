import operation
import read
import write

def mainDisplay():
    system = {}

    print("\t" * 8 + "TECHNO PROPERTY NEPAL")
    print("\n")
    print("\t" * 6 + "Kalanki, Kathmandu | Contact no: +9761294137")
    print("\n")
    print("\t" * 5 + "~~~ Hello! Welcome to Techno Property Nepal ~~~")
    print("____________________________________________________________________________________________________________________________________________________")
    print(".-------------------------------------------------------.")
    print("| Here are some of the options available in our system  |")
    print(".-------------------------------------------------------.")

    file = 'land.txt'
    features = read.read(file)  # Reading the land data from the file

    operation.display_land_features(features)  # Displaying the land data

    # Displaying options for users
    while True:
        print("Press 1 to rent land.")
        print("Press 2 to return land.")
        print("Press 3 to exit.")

        try:
            choose = int(input("Enter the value: "))
            if choose == 1:
                # Displaying available properties and renting function
                operation.display_available_land(features)
                transaction = []  # Define transaction as an empty list
                operation.rent_land(features, transaction)
            elif choose == 2:
                # Displaying unavailable properties and return function
                operation.display_not_available(features)
                transaction = []  # Define transaction as an empty list
                operation.return_land(features, transaction)
            elif choose == 3:
                # Exiting the system
                print("Exiting from the system.....")
                break
            else:
                # Error handling for invalid option
                print("Error!!! Please choose a valid choice")
        except ValueError:
            # Handling error for invalid input (non-integer)
            print("Error!! Invalid input entered. Please enter a valid choice")

# Run this code block only if the script is executed directly by the Python interpreter
if __name__ == "__main__":
    mainDisplay()
