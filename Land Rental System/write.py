# Importing the operation module
import operation

# Dictionary to store customer invoice data
customer_invoices = {}

# Function to create a box to display text inside
def display_box(text):
    print("-" * 45)
    print("|" + text.center(43) + "|")
    print("-" * 45)

# Function to generate an invoice for a rental transaction and store it in a text file
def generate_invoice(name, address, email, num, kitta, price_per_month, duration, transaction_time, total):
    try:
        transaction_details = {
            'name': name,
            'address': address,
            'email': email,
            'num': num,
            'transactions': [
                {
                    'kitta': kitta,
                    'duration': duration,
                    'transaction_time': transaction_time,
                    'price_per_month': price_per_month,
                    'total': total
                }
            ],
            'total_amount': total
        }
        if num in customer_invoices:
            customer_invoices[num]['transactions'].append(transaction_details['transactions'][0])
            customer_invoices[num]['total_amount'] += total
        else:
            customer_invoices[num] = transaction_details

        with open("invoice.txt", "a") as file:
            for phone_num, invoice_data in customer_invoices.items():
                file.write("INVOICE GENERATED\n")
                file.write("-" * 45 + "\n")
                file.write("Name: " + invoice_data['name'] + "\n")
                file.write("Address: " + invoice_data['address'] + "\n")
                file.write("Phone: " + invoice_data['num'] + "\n")

                transaction_index = 1
                for transaction in invoice_data['transactions']:
                    file.write("Transaction " + str(transaction_index) + ":\n")
                    file.write("Kitta no: " + transaction['kitta'] + "\n")
                    file.write("Duration: " + str(transaction['duration']) + "\n")
                    file.write("Transaction time: " + transaction['transaction_time'] + "\n")
                    file.write("Price per month: " + str(transaction['price_per_month']) + "\n")
                    file.write("Total Amount: " + str(transaction['total']) + "\n")
                    file.write("-" * 45 + "\n")
                    transaction_index += 1

                file.write("Total Amount for all transactions: " + str(invoice_data['total_amount']) + "\n")
                file.write("-" * 45 + "\n")

        print("\n\t\t\t\t\t\t\t\t\t***Invoice generated successfully.***")
    except Exception as e:
        print("\t\t\t\t\t\t\t***Error: Cannot Generate Invoice***", e)


# Function to update the LandRentalSystem file
def update_land_file(file, properties):
    try:
        # Open the file in write mode to overwrite the existing content
        with open(file, 'w') as f:
            for property_info in properties:
                # Create a line from the property_info dictionary
                line = ','.join([
                    property_info['kitta'],
                    property_info['location'],
                    property_info['direction'],
                    property_info['anna'],
                    property_info['price'],
                    property_info['status'],
                ])
                # Write the line to the file
                f.write(line + '\n')
        
        print("\n\t\t\t\t\t\t\t\t\t***Property File updated successfully.***")
    
    except Exception as e:
        # Print error message if an exception occurs
        print("\t\t\t\t\t\t\t***Error: Cannot Update Property File***", e)




