def read(file):
    estate = []
    try:
        with open(file, 'r') as file:
            for line in file:
                if line[-1] == '\n':  # Removing newline characters
                    line = line[:-1]
                estate_info = line.split(',')
                if len(estate_info) >= 6:
                    kitta = str(estate_info[0])
                    location = estate_info[1]
                    direction = estate_info[2]
                    anna = estate_info[3]
                    price = estate_info[4]
                    status = estate_info[5]
                    estate_INFO = {
                        'kitta': kitta,
                        'location': location,
                        'direction': direction,
                        'anna': anna,
                        'price': price,
                        'status': status
                    }
                    estate.append(estate_INFO)
                else:
                    print("\t\t\t\t\t\t\t***Error: Invalid Data Format***")
    except FileNotFoundError:
        print(f"\t\t\t\t\t\t\t***Error: File '{file}' not found***")
    except Exception as e:
        print(f"\t\t\t\t\t\t\t***Error: An unexpected error occurred - {e}***")   
    
    return estate
