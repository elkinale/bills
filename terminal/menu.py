import querys
from logger_setup import get_logger
import os
from datetime import datetime
import inspect
import sqlite3
import pandas as pd

logger = get_logger(__name__)
db_path = '/home/elkin/Documents/Python/utilities/bills/terminal/bills.db'
con = sqlite3.connect(db_path)
cur = con.cursor()

def add_person():
    while True:
        try:
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
        except Exception as e:
            logger.info(f"The error in {inspect.currentframe().f_code.co_name} is: {e}")      

def add_place():
    while True:
        try:
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
        except Exception as e:
            logger.info(f"The error in {inspect.currentframe().f_code.co_name} is: {e}")      

def add_event():
    while True:
        try:
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
        except Exception as e:
            logger.info(f"The error in {inspect.currentframe().f_code.co_name} is: {e}")      

def add_bill():
    while True:
        try:
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
        except Exception as e:
            logger.info(f"The error in {inspect.currentframe().f_code.co_name} is: {e}")      

def add_per_bill():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("List of events in the APP:")
            events = querys.look_event(name='%')
            if events:
                for i, event in enumerate(events):
                    print(f'{i} {" ".join(map(str, event))}')

            event_inp = input("\nSelect the event you want to intercat with or press \'q\' to exit: ")

            match event_inp:
                case 'q':
                    break
                case event_inp if int(event_inp) < len(events):
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear') 
                        print("List of bill in the event:")
                        bills = querys.look_bill(event=events[int(event_inp)][0])

                        if bills: 
                            for i, bill in enumerate(bills):
                                print(f'{i} {" ".join(map(str, bill))}')


                        print("\n1. Add a person to bill")
                        print("2. Delete a person from bill")
                        print("\nPress q to exit")

                        inp = input("\nEnter an option: ")
                        if inp == 'q': break

                        bill = int(input("Number of the bill: "))

                        print("\nList of people in the bill: ")
                        people_bill = querys.look_bill_people(place=bills[bill][0], event=bills[bill][2])
                        for i, person in enumerate(people_bill):
                            print(f'{i} {" ".join(map(str, person))}')

                        match inp:
                            case '1':
                                if bill!='':
                                    print("List of people in the APP:")
                                    people = querys.look_people(name='%')

                                    if people: 
                                        for i, person in enumerate(people):
                                            print(f'{i} {" ".join(map(str, person))}')
                                    
                                    person = int(input("Number of the person: "))
                                    pay = int(input("Enter the amount payed: "))
                                    if person!='': 
                                        querys.add_people_bills(name=people[person][0], last_name=people[person][1],
                                                                place=bills[bill][0], date=bills[bill][1], 
                                                                event=bills[bill][2],
                                                                payed=pay)
                                        querys.update_person_bills(place=bills[bill][0], date=bills[bill][1], 
                                                            event=bills[bill][2])
                            case '2':
                                person = input("Number of the person: ")
                                if person!='' : 
                                    querys.del_people_bills(name=people_bill[int(person)][0], last_name=people_bill[int(person)][1],
                                                            place=bills[bill][0], date=bills[bill][1], 
                                                            event=bills[bill][2])
                                    querys.update_person_bills(place=bills[bill][0], date=bills[bill][1], 
                                                            event=bills[bill][2])
                            case _:
                                os.system('cls' if os.name == 'nt' else 'clear') 
                case _:
                   os.system('cls' if os.name == 'nt' else 'clear') 
        except Exception as e:
            logger.info(f"The error in {inspect.currentframe().f_code.co_name} is: {e}")      

def values():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')

            print("List of events in the APP:")
            events = querys.look_event(name='%')
            if events:
                for i, event in enumerate(events):
                    print(f'{i} {" ".join(map(str, event))}')

            event_inp = input("Select the event you want to see the account\n or press \'q\' to exit: ")

            match event_inp:
                case 'q':
                    break
                case event_inp if int(event_inp) < len(events):
                    cur.execute("""
                                SELECT p.name, p.last_name, b.id, 
                                ROUND(SUM(pb.payed) - SUM(pb.share), 0)
                                FROM people_bills pb
                                JOIN bills b ON b.id = pb. bill_id
                                JOIN people p ON p.id = pb.person_id
                                JOIN events e ON e.id = b.event_id
                                WHERE e.name = ?
                                GROUP BY p.name, p.last_name, b.id
                                """,
                                (events[int(event_inp)][0],)
                    )       
                    bills = cur.fetchall()
                    b_df = pd.DataFrame(bills, columns=['Name', 'Last_Name', 'Bill id', 'Total'])
                    total_df = b_df.groupby(['Name', 'Last_Name']).agg({'Total':'sum'}).reset_index()
                    total_df['Full Name'] = total_df['Name'] + ' ' + total_df['Last_Name']
                    total_df.drop(['Name', 'Last_Name'], inplace=True, axis=1)
                    total_df.sort_values(by='Total', ascending=False, inplace=True)

                    balanced_pos = total_df[total_df['Total'] >= 0].reset_index(drop=True)
                    balanced_neg = total_df[total_df['Total'] < 0].reset_index(drop=True)
                    balanced_neg['Creditor'], balanced_neg['Amount'] = "", 0.0

                    
                    max_pos_id = balanced_pos.shape[0]
                    max_neg_id = balanced_neg.shape[0]
                    id_pos, id_neg = 0, 0
                    total = 1
                    while total != 0:

                        pos_val = balanced_pos.at[id_pos, 'Total']
                        neg_val = balanced_neg.at[id_neg, 'Total']

                        total = pos_val + neg_val
                        if total > 0:
                            balanced_neg.at[id_neg, 'Amount'] = neg_val*-1
                            balanced_neg.at[id_neg, 'Creditor'] = balanced_pos.at[id_pos, 'Full Name']
                            balanced_pos.at[id_pos, 'Total'] = total
                            if max_neg_id == id_neg: continue
                            id_neg += 1
                        else:
                            balanced_neg.at[id_neg, 'Amount'] = pos_val
                            balanced_neg.at[id_neg, 'Creditor'] = balanced_pos.at[id_pos, 'Full Name']
                            balanced_neg.at[id_neg, 'Total'] = total
                            if max_pos_id == id_pos: continue
                            id_pos +=1

                    balanced_neg['Amount'] = balanced_neg['Amount'].apply(
                                            lambda x: f'${x:,.0f}'.replace(".", ",").replace(",", "."))
                    
                    print(balanced_neg[['Full Name', 'Creditor', 'Amount']])
                    input('Press any key to Continue')
                case _:
                   os.system('cls' if os.name == 'nt' else 'clear') 
        except Exception as e:
            logger.info(f"The error in {inspect.currentframe().f_code.co_name} is: {e}") 