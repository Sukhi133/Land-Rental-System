import datetime
import read
import write

# Dictionary to hold customer transactions
customer_transactions = {}

def display_land_features(features):
    print('\n')
    print('-------------------------------------------------------------------------------------------------')
    print('|' + ' Kitta No. '.center(15) + '|' + ' Location '.center(15) + '|' + ' Direction '.center(15) + '|' + ' Anna '.center(15) + '|' + ' Price '.center(15) + '|' + ' Status '.center(15) + '|')
    print('-------------------------------------------------------------------------------------------------')
    for land_info in features:
        print('|' + str(land_info["kitta"]).center(15) + '|' + str(land_info["location"]).center(15) + '|' + str(land_info["direction"]).center(15) + '|' + str(land_info["anna"]).center(15) + '|' + str(land_info["price"]).center(15) + '|' + str(land_info["status"]).center(15) + '|')
    print('-------------------------------------------------------------------------------------------------')
    print('\n')

def display_available_land(features):
    print('\n')
    print('-------------------------------------------------------------------------------------------------')
    print('|' + ' Kitta No. '.center(15) + '|' + ' Location '.center(15) + '|' + ' Direction '.center(15) + '|' + ' Anna '.center(15) + '|' + ' Price '.center(15) + '|' + ' Status '.center(15) + '|')
    print('-------------------------------------------------------------------------------------------------')
    for land_info in features:
        if land_info['status'] == "Available":
            print('|' + str(land_info["kitta"]).center(15) + '|' + str(land_info["location"]).center(15) + '|' + str(land_info["direction"]).center(15) + '|' + str(land_info["anna"]).center(15) + '|' + str(land_info["price"]).center(15) + '|' + str(land_info["status"]).center(15) + '|')
    print('-------------------------------------------------------------------------------------------------')
    print('\n')

def display_not_available(features):
    print('\n')
    print('-------------------------------------------------------------------------------------------------')
    print('|' + ' Kitta No. '.center(15) + '|' + ' Location '.center(15) + '|' + ' Direction '.center(15) + '|' + ' Anna '.center(15) + '|' + ' Price '.center(15) + '|' + ' Status '.center(15) + '|')
    print('-------------------------------------------------------------------------------------------------')
    for land_info in features:
        if land_info['status'] == "Not Available":
            print('|' + str(land_info["kitta"]).center(15) + '|' + str(land_info["location"]).center(15) + '|' + str(land_info["direction"]).center(15) + '|' + str(land_info["anna"]).center(15) + '|' + str(land_info["price"]).center(15) + '|' + str(land_info["status"]).center(15) + '|')
    print('-------------------------------------------------------------------------------------------------')
    print('\n')

def get_current_time():
    return datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

def rent_land(features, transaction):
    name = input("\tEnter your name: ")
    address = input("\tEnter your address: ")
    email = input("\tEnter your e-mail: ")
    num = input("\tEnter your number: ")

    if num not in customer_transactions:
        customer_transactions[num] = {
            'name': name,
            'address': address,
            'phone': num,
            'email': email,
            'transactions': []
        }

    while True:
        rent_kitta = input("\n\tEnter the kitta number you want to rent (or enter 'e' to exit): ")
        if rent_kitta.lower() == 'e':
            print("\n\t\t\t\t\t\t\t\t\t***Thank you for using our system***")
            break
        
        property_found = False
        for property_info in features:
            if property_info['kitta'] == rent_kitta and property_info['status'] == 'Available':
                property_info['status'] = 'Not Available'
                property_found = True
                
                try:
                    rent_duration = int(input("\tFor how many months would you like to rent the land: "))
                    transaction_details = {
                        'kitta': rent_kitta,
                        'location': property_info['location'],
                        'anna': property_info['anna'],
                        'duration': rent_duration,
                        'price': int(property_info['price']),
                        'transaction_time': get_current_time()
                    }
                    customer_transactions[num]['transactions'].append(transaction_details)
                    print("\n\t\t\t\t\t\t\t\t\t***Land rented successfully***")
                    
                    total_amount = rent_duration * int(property_info['price'])
                    
                    try:
                        write.generate_invoice(name, address, email, num, rent_kitta, property_info['price'], rent_duration, get_current_time(), total_amount)
                        write.update_land_file("land.txt", features)
                        print("\n\t\t\t\t\t\t\t\t\t***Property status updated successfully.***")
                    except Exception as e:
                        print("\t\t\t\t\t\t\t***Error: Cannot update Property File or Generate Invoice***", e)
                except ValueError:
                    print("\t\t\t\t\t\t\t***Error: Invalid input for duration. Please enter a valid number.***")
        
        if not property_found:
            print("\t\t\t\t\t\t\t***Error: Invalid kitta number. Land may not be available for rent.***")

def return_land(features, transaction):
    name = input("\tEnter your name: ")
    address = input("\tEnter your address: ")
    email = input("\tEnter your e-mail: ")
    num = input("\tEnter your number: ")
    
    if num not in customer_transactions:
        print("\t\t\t\t\t\t\t***Error: No transactions found for this number.***")
        return

    while True:
        return_kitta = input("\n\tEnter the kitta number you want to return (or enter 'e' to exit): ")
        if return_kitta.lower() == 'e':
            print("\n\t\t\t\t\t\t\t\t\t***Thank you for using our system***")
            break
        
        transaction_found = False
        for property_info in features:
            if property_info['kitta'] == return_kitta and property_info['status'] == 'Not Available':
                property_info['status'] = 'Available'
                transaction_found = True
