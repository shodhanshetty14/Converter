import WeightnHeight as mass
import temperature_conv as temp


while True:
    print("1. Weight and Height conversion: \n2. Temperature conversion: ")
    choice = input("Enter your Choice: ")
    if choice == '1':
        print("1. Kg to Lbs: \n2. Lbs to Kg: \n3. Cm to ft: \n4. ft to Cm: \n5. Mile to Km: \n6. Km to Mile: ")
        ch1 = input("Enter your Choice: ")
        if ch1 == '1':
            data = float(input("Enter the data in 'Kg': "))
            ans = mass.kg_to_lbs(data)
            print(f"{data}Kg is {ans}Lbs ")
        elif ch1 == '2':
            data = float(input("Enter the data in 'Lbs': "))
            ans = mass.lbs_to_kg(data)
            print(f"{data}Lbs is {ans}Kg ")
        elif ch1 == '3':
            data = float(input("Enter the data in 'Cm': "))
            ans = mass.cm_to_ft(data)
            print(f"{data}CM is {ans}ft ")
        elif ch1 == '4':
            data = float(input("Enter the data in 'ft': "))
            ans = mass.ft_to_cm(data)
            print(f"{data}ft is {ans}Cm ")
        elif ch1 == '5':
            data = float(input("Enter the data in 'Mile': "))
            ans = mass.mile_to_km(data)
            print(f"{data}mile is {ans}Km ")
        elif ch1 == '6':
            data = float(input("Enter the data in 'Km': "))
            ans = mass.km_to_mile(data)
            print(f"{data}Km is {ans}mile ")
        else:
            print("Invalid Choice!!")
            print("")
    elif choice == '2':
        print("1. Celsius to Fahrenheit: \n2. Fahrenheit to Celsius: ")
        print("3. Celsius to Kelvin: \n4. Kelvin to Celsius: ")
        ch2 = input("Enter your Choice: ")
        if ch2 == '1':
            data = float(input("Enter Temperature in Celsius: "))
            ans = temp.celsius_to_fahrenheit(data)
            print(f"{data}C is {ans}F")
        elif ch2 == '2':
            data = float(input("Enter Temperature in Fahrenheit: "))
            ans = temp.fahrenheit_to_celsius(data)
            print(f"{data}F is {ans}C")
        elif ch2 == '3':
            data = float(input("Enter Temperature in Celsius: "))
            ans = temp.celsius_to_kelvin(data)
            print(f"{data}C is {ans}K")
        elif ch2 == '4':
            data = float(input("Enter Temperature in Kelvin: "))
            ans = temp.kelvin_to_celsius(data)
            print(f"{data}K is {ans}C")
        else:
            print('INVALID Choice!!')
    else:
        print('INVALID Choice: ')
        quit()
