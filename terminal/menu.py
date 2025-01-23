import querys
import os
from datetime import datetime

def add_person():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("List of people in the APP:")
        people = querys.look_people(name='%')

        if people: 
            for i, person in enumerate(people):
                print(f'{i} {" ".join(map(str, person))}')

        print("\n1. Add a person")
        print("2. Delete a person")
        print("\nPress q to exit")

        inp = input("\nEnter an option: ")

        match inp:
            case '1':
                name = input("Name of the person: ")
                last_name = input("Last Name of the person: ")
                if name and last_name: querys.add_people(name=name, last_name=last_name)
            case '2':
                id = input("Number of the person: ")
                if id : 
                    name = people[int(id)][0]
                    last_name = people[int(id)][1]
                    querys.del_people(name=name, last_name=last_name)
            case 'q':
                break      

def add_place():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("List of places in the APP:")
        places = querys.look_place(name='%')

        if places: 
            for i, place in enumerate(places):
                print(f'{i} {" ".join(map(str, place))}')

        print("\n1. Add a place")
        print("2. Delete a place")
        print("\nPress q to exit")

        inp = input("\nEnter an option: ")

        match inp:
            case '1':
                name = input("Name of the place: ")
                if name : querys.add_place(name=name)
            case '2':
                id = input("Number of the place: ")
                if id : 
                    name = places[int(id)][0]
                    querys.del_place(name=name)
            case 'q':
                break

def add_event():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("List of events in the APP:")
        events = querys.look_event(name='%')

        if events: 
            for i, event in enumerate(events):
                print(f'{i} {" ".join(map(str, event))}')

        print("\n1. Add an event")
        print("2. Delete an event")
        print("\nPress q to exit")

        inp = input("\nEnter an option: ")

        match inp:
            case '1':
                name = input("Name of the event: ")
                if name : querys.add_event(name=name)
            case '2':
                id = input("Name of the event: ")
                if id : 
                    name = events[int(id)][0]
                    querys.del_event(name=name)
            case 'q':
                break

def add_bill():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("List of bill in the APP:")
        bills = querys.look_bill(place='%', event='%')

        if bills: 
            for i, bill in enumerate(bills):
                print(f'{i} {" ".join(map(str, bill))}')


        print("\n1. Add a bill")
        print("2. Delete a bill")
        print("\nPress q to exit")

        inp = input("\nEnter an option: ")

        match inp:
            case '1':
                total = input("Total amount of the bill: ")
                place = input("Name of the place: ")
                event = input("Name of the event: ")
                try:
                    date = datetime.strptime(input("Date of the bill (d-m-y): "), "%d-%m-%y").date()
                except Exception as e:
                    print(f'The error is: {e}')
                    date = None
                if total and place and event: 
                    querys.add_bill(total=total, place=place, event=event, date=date)
            case '2':
                id = input("Number of the event: ")
                if id : 
                    place = bills[int(id)][0]
                    date = bills[int(id)][1]
                    event = bills[int(id)][2]
                    querys.del_bill(place=place, event=event, date=date)
            case 'q':
                break

def add_per_bill():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("List of bill in the APP:")
        bills = querys.look_bill(place='%', event='%')

        if bills: 
            for i, bill in enumerate(bills):
                print(f'{i} {" ".join(map(str, bill))}')

        print("List of people in the APP:")
        people = querys.look_people(name='%')

        if people: 
            for i, person in enumerate(people):
                print(f'{i} {" ".join(map(str, person))}')


        print("\n1. Add a person to bill")
        print("2. Delete a person from bill")
        print("\nPress q to exit")

        inp = input("\nEnter an option: ")

        match inp:
            case '1':
                bill = input("Number of the bill: ")
                person = input("Number of the person: ")
                if bill and person: 
                    querys.add_people_bills(name=people[0], last_name=people[1],
                                            place=bill[0], date=bill[1], event=bill[2])
            case '2':
                id = input("Number of the event: ")
                if id : 
                    place = bills[int(id)][0]
                    date = bills[int(id)][1]
                    event = bills[int(id)][2]
                    querys.del_bill(place=place, event=event, date=date)
            case 'q':
                break

def values():
    print("This are the values to each one")