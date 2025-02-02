import sqlite3
from logger_setup import get_logger

db_path = '/home/elkin/Documents/Python/utilities/bills/terminal/bills.db'
logger = get_logger(__name__)

con = sqlite3.connect(db_path)
cur = con.cursor()

def add_people(name, last_name):
    """Add new people to the database

    Args:
        name (string): Person name
        last_name (string): Person last name
    """
    try:
        cur.execute("INSERT INTO people (name, last_name) VALUES(?,?)",
                    (name, last_name))
        con.commit()
    except Exception as e:
        logger.warning(f'The error is: {e}')

def add_place(name):
    """Add new places to the data base

    Args:
        name (string): Place name
    """
    try:
        cur.execute("INSERT INTO places (name) VALUES(?)",
                    (name,)
                    )
        con.commit()
    except Exception as e:
        logger.warning(f'The error is: {e}')

def add_event(name):
    """Add an event to the data base

    Args:
        name (string): Event name
    """
    try:
        cur.execute("INSERT INTO events (name) VALUES(?)",
                    (name,)
                    )
        con.commit()
    except Exception as e:
        logger.warning(f'The error is: {e}')

def add_bill(total, place, event, date=None):
    """Add new bills to the data base with a relaciont with an event and a place

    Args:
        total (double): Amount of money of the bill
        place (string): Name of the place the bill refers to
        event (string): Name of the event the bill refers to
        date (date, optional): Date of the bill
    """
    place_id = look_place(id=True, name=place)
    event_id = look_event(id=True, name=event)

    try:
        if place_id and event_id:
            #print(f' The values are val : {total}, place : {place_id}, event : {event_id}, date : {date}')
            cur.execute("""
                        INSERT INTO bills (total, place_id, event_id,date) VALUES(?,?,?,?)
                        """,
                        (total, place_id[0], event_id[0], date)
                        )
            con.commit()
    except Exception as e:
        logger.warning(f'The error is: {e}')

def add_people_bills(name=None, last_name=None, place=None, date=None, event=None, payed=None):
    """Add relation of persons to an specific bill

    Args:
        name (string, optional): Person name. Defaults to None.
        last_name (string, optional): Person last name. Defaults to None.
        place (string, optional): Place name. Defaults to None.
        date (date, optional): Date of the bill. Defaults to None.
        event (string, optional): Event name. Defaults to None.
        payed (double, optional): Amount payed by the person. Defaults to None.
    """
    people_id = look_people(id=True, name=name, last_name=last_name)
    bill_id = look_bill(id=True, place=place, date=date, event=event)

    if people_id and bill_id:
        try:
            cur.execute("INSERT INTO people_bills (person_id, bill_id, payed) VALUES (?,?, ?)",
                        (people_id[0], bill_id[0], payed))
            con.commit()
        except Exception as e:
            logger.warning(f'The error is: {e}')

def del_people(name, last_name):
    """Delete people from the database

    Args:
        name (string): Person name
        last_name (string): Person last name
    """
    cur.execute("""
                DELETE FROM people 
                WHERE name=? AND last_name=?
                """,
                (name, last_name))
    con.commit()

def del_place(name):
    """Delete a place from the data base

    Args:
        name (string): Place name
    """
    cur.execute("""
                DELETE FROM places
                WHERE name=?
                """,
                (name,)
                )
    con.commit()

def del_event(name):
    """Delete an event from the data base

    Args:
        name (string): Event name
    """
    cur.execute("""
                DELETE FROM events
                WHERE name=?
                """,
                (name,)
                )
    con.commit()

def del_bill(place=None, date=None, event=None):
    """Delete a bill from the data base with a relation with an event and a place

    Args:
        place (string, optional): Name of the place the bill refers to. Default to None
        date (date, optional): Date of the bill. Default to None
        event (string, optional): Name of the event the bill refers to. Default to None
    """
    cur.execute("""
                DELETE FROM bills
                WHERE place_id = (SELECT id FROM places WHERE name = ?)
                AND event_id = (SELECT id FROM events WHERE name = ?)
                """,
                (place, event)
                )
    con.commit()

def del_people_bills(name=None, last_name=None, place=None, date=None, event=None):
    """Delete a relation of a person to an specific bill

    Args:
        name (string, optional): Person name. Defaults to None.
        last_name (string, optional): Person last name. Defaults to None.
        place (string, optional): Place name. Defaults to None.
        date (date, optional): Date of the bill. Defaults to None.
        event (string, optional): Event name. Defaults to None.
    """
    cur.execute("""
                DELETE FROM people_bills 
                WHERE person_id = (SELECT id FROM people WHERE name=? AND last_name=? )
                AND bill_id = (SELECT b.id FROM bills b 
                JOIN places pl ON pl.id = b.place_id
                JOIN events e ON e.id = b.event_id
                WHERE pl.name=? AND b.date=? AND e.name=?)
                """,
                (name, last_name, place, date, event)
                )
    con.commit()

def look_people(id=False, name=None, last_name=None):
    """Search for people related to the name or last name desired, or get the id 
    of one person

    Args:
        id (bool, optional): Get the id of the query. Default to False
        name (string): Person name. Default to None
        last_name (string): Person last name. Default to None
    """
    if id:
        res = cur.execute("""
                        SELECT id
                        FROM people 
                        WHERE name = ? AND last_name = ?
                        """,
                        (name, last_name)
                        )
        return res.fetchone()
    else:
        res = cur.execute("""
                        SELECT name, last_name
                        FROM people 
                        WHERE name LIKE ? OR last_name LIKE ?
                        """,
                        (name, last_name)
                        )
        return res.fetchall()
    
def look_place(id=False, name=None):
    """Search for a place according to the name desired or get the id of a place

    Args:
        id (bool, optional): Get the id of the query. Default to False
        name (string): Place name. Default to None
    """
    if id:
        res = cur.execute("""
                        SELECT id
                        FROM places
                        WHERE name = ?
                        """,
                        (name, )
                        )
        return res.fetchone()
    else:
        res = cur.execute("""
                        SELECT name
                        FROM places
                        WHERE name LIKE ?
                        """,
                        (name, )
                        )
        return res.fetchall()
    
def look_event(id=False, name=None):
    """Search for an event according to the name desired or get the id of an event

    Args:
        id (bool, optional): Get the id of the query. Default to False
        name (string): Event name. Default to None
    """
    if id:
        res = cur.execute("""
                        SELECT id
                        FROM events
                        WHERE name = ?
                        """,
                        (name, )
                        )
        return res.fetchone()
    else:
        res = cur.execute("""
                        SELECT name
                        FROM events
                        WHERE name LIKE ?
                        """,
                        (name, )
                        )
        return res.fetchall()

def look_bill(id=False, place=None, date=None, event=None):
    """Look a bill from the data base with a relation with an event and a place or
    get the id of a bill

    Args:
        id (bool, optional): Get the id of the query. Default to False
        place (string, optional): Name of the place the bill refers to. Default to None
        date (date, optional): Date of the bill. Default to None
        event (string, optional): Name of the event the bill refers to. Default to None
    """
    if id:
        res = cur.execute("""
                        SELECT b.id
                        FROM bills b
                        JOIN places pl ON pl.id = b.place_id
                        JOIN events e ON e.id = b.event_id
                        WHERE pl.name=? AND b.date=? AND e.name=?
                        """,
                        (place, date, event)
                        )
        return res.fetchone()
    else:
        res = cur.execute("""
                        SELECT pl.name, b.date, e.name, b.total
                        FROM bills b
                        JOIN places pl ON pl.id = b.place_id
                        JOIN events e ON e.id = b.event_id
                        WHERE pl.name LIKE ? OR b.date LIKE ? OR e.name LIKE ?
                        """,
                        (place, date, event)
                        )
        return res.fetchall()

def look_bill_people(place=None, event=None, date=None):
    """Look for the people to an specific bill acording to place and event name

    Args:
        place (string, optional): Name of the place the bill refers to. Default to None
        event (string, optional): Name of the event the bill refers to. Default to None
    """
    res = cur.execute("""
                    SELECT p.name, p.last_name
                    FROM people_bills pb
                    JOIN people p ON pb.person_id = p.id
                    JOIN bills b ON pb.bill_id = b.id
                    JOIN places pl ON b.place_id = pl.id
                    JOIN events e ON e.id = b.event_id
                    WHERE pl.name = ? AND e.name = ?;
                    """,
                    (place, event)
                    )
    
    return res.fetchall()

def look_person_bills(name=None, last_name=None):
    """Look for bills related a person according to the name and last name

    Args:
        name (string, optional): Name of the person. Default to None
        last name (string, optional): Last name of the person. Default to None
    """
    res = cur.execute("""
                    SELECT b.total, pl.name, b.date, e.name, pb.share, pb.payed
                    FROM people p
                    JOIN people_bills pb ON pb.person_id = p.id
                    JOIN bills b ON pb.bill_id = b.id
                    JOIN places pl ON b.place_id = pl.id
                    JOIN events e ON b.event_id = e.id
                    WHERE p.name = ? AND p.last_name=?
                    """,
                    (name, last_name)
                    )
    
    return res.fetchall()

def update_person_bills(place=None, date=None, event=None):
    """Update the ahsre item of the people related to an specific bill

    Args:
        place (string, optional): Name of the place. Default to None
        date (date, optional): Date of the bill. Default to None
        event (string, optional): Name of the event. Default to None
    """
    cur.execute(""" 
                UPDATE people_bills
                SET share = (
                    SELECT b.total / COUNT(pb.person_id)
                    FROM bills b
                    JOIN people_bills pb ON pb.bill_id = b.id
                    JOIN places pl ON pl.id = b.place_id
                    JOIN events e ON e.id = b.event_id
                    WHERE b.id = pb.bill_id
                    AND pl.name = ? AND b.date = ?   -- Replace with the specific place
                    AND e.name = ?      -- Replace with the specific event
                )
                WHERE bill_id = (SELECT b.id FROM bills b 
                JOIN events e ON e.id = b.event_id
                JOIN places pl ON pl.id = b.place_id
                WHERE pl.name = ? AND b.date = ? and e.name = ? )
                """,
                (place, date, event, place, date, event))
    con.commit()