import sqlite3
#from logger_setup import get_logger

#logger = get_logger(__name__)

def new_schema():
    """Create the tables related to the project if they do not exist
    
    """
    # OPEN DB
    db_path = '/home/elkin/Documents/Python/utilities/bills/terminal/bills.db'
    #logger.info('This function was called')
    with sqlite3.connect(db_path) as con:
        # Create a Cursor
        cur = con.cursor()
        # Enable foreign key support (SQLite has foreign key constraints disabled by default)
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(""" CREATE TABLE IF NOT EXISTS people(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50),
                    UNIQUE (name, last_name)
                    )""")


        cur.execute("""CREATE TABLE IF NOT EXISTS places(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50) NOT NULL UNIQUE
                    )""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS events(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50) NOT NULL UNIQUE
                    )""")

        cur.execute("""CREATE TABLE IF NOT EXISTS bills(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    total DOUBLE NOT NULL,
                    place_id INT NOT NULL,
                    event_id INT NOT NULL,
                    date DATE,
                    UNIQUE(place_id, event_id)
                    FOREIGN KEY (place_id) REFERENCES places(id)
                        ON DELETE CASCADE                    
                        ON UPDATE CASCADE
                    FOREIGN KEY (event_id) REFERENCES events(id)
                        ON DELETE CASCADE                    
                        ON UPDATE CASCADE
                    )""")
        
        cur.execute(""" CREATE TABLE IF NOT EXISTS people_bills(
                    person_id INT NOT NULL,
                    bill_id INT NOT NULL,
                    share DECIMAL(10,2) DEFAULT 0,
                    payed DECIMAL (10,2) DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (person_id) REFERENCES people(id)
                        ON DELETE CASCADE                      -- Delete relationship if the person is deleted
                        ON UPDATE CASCADE,                     -- Update relationship if person_id changes
                    FOREIGN KEY (bill_id) REFERENCES bills(id)
                        ON DELETE CASCADE                      -- Delete relationship if the bill is deleted
                        ON UPDATE CASCADE                      -- Update relationship if bill_id changes
                    PRIMARY KEY(person_id, bill_id)
                    )""")
