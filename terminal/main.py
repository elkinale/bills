from schema import new_schema
import os
import menu

# Create the schema of DB if not exist already
new_schema()

while True:
    print("Menu")
    print("1. Add person")
    print("2. Add place")
    print("3. Add event")
    print("4. Add bill")
    print("5. Add person to bill")
    print("6. See the values to pay")
    print("\n\n\n")
    print("press q to exit")

    inp = input("\nEnter an option: ")
    
    match inp:
        case 'q':
            break
        case '1':
            menu.add_person()
        case '2':
            menu.add_place()
        case '3':
            menu.add_event()
        case '4':
            menu.add_bill()
        case '5':
            menu.add_per_bill()
        case '6':
            menu.values()
        case _:
            os.system('cls' if os.name =='nt' else 'clear' )