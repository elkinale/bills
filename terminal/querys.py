import sqlite3
from logger_setup import get_logger

db_path = '/home/elkin/Documents/Python/utilities/bills/terminal/bills.db'
logger = get_logger(__name__)

con = sqlite3.connect(db_path)
cur = con.cursor()

def add_people(name, last_name):
    try:
        cur.execute("INSERT INTO people (name, last_name) VALUES(?,?)",
                    (name, last_name))
        con.commit()
    except Exception as e:
        logger.warning(f'The error is: {e}')

def add_place(name):
    try:
        cur.execute("INSERT INTO places (name) VALUES(?)",
                    (name,)
                    )
        con.commit()
    except Exception as e:
        logger.warning(f'The error is: {e}')

def add_event(name):
    try:
        cur.execute("INSERT INTO events (name) VALUES(?)",
                    (name,)
                    )
        con.commit()
    except Exception as e:
        logger.warning(f'The error is: {e}')

def add_bill(total, place, event, date=None):
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
    cur.execute("""
                DELETE FROM people 
                WHERE name=? AND last_name=?
                """,
                (name, last_name))
    con.commit()

def del_place(name):
    cur.execute("""
                DELETE FROM places
                WHERE name=?
                """,
                (name,)
                )
    con.commit()

def del_event(name):
    cur.execute("""
                DELETE FROM events
                WHERE name=?
                """,
                (name,)
                )
    con.commit()

def del_bill(place=None, date=None, event=None):

    cur.execute("""
                DELETE FROM bills
                WHERE place_id = (SELECT id FROM places WHERE name = ?)
                AND event_id = (SELECT id FROM events WHERE name = ?)
                """,
                (place, event)
                )
    con.commit()

def del_people_bills(name=None, last_name=None, place=None, date=None, event=None):
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
    res = cur.execute("""
                    SELECT b.total, pl.name, b.date, e.name, pb.share, pb.payed
                    FROM people p
                    JOIN people_bills pb ON pb.person_id = p.id
                    JOIN bills b ON pb.bill_id = b.id
                    JOIN places pl ON b.place_id = pl.id
                    JOIN events e ON b.event_id = e.id
                    WHERE p.name = ?
                    """,
                    (name, )
                    )
    
    return res.fetchall()
    