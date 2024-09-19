# Custom orm
"""
    - A few methods to allow us manage a table`s lifecycle
    - Methods to manage a rows lifecycle

    -> A class can be referenced to a whole db table
    -> attributes of the class are columns in the table
    -> the class instance is associated with a table row
"""

from db import conn, cursor

class Meeting:
    # constant classs attribute
    TABLE_NAME = 'meetings'

    def __init__(self, venue, members, host, time):
        self.id = None
        self.venue = venue
        self.members = members
        self.host = host
        self.time = time

    # returns a printable text of the class instance
    def __repr__(self) -> str:
        return f"<Meeting {self.id} -> Venue:{self.venue}, Host:{self.host}, Time:{self.time}, Members:{self.members}>"

    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (venue, host, time, members)
            VALUES (?, ?, ?, ?)
        """

        cursor.execute(sql, (self.venue, self.host, self.time, self.members))
        conn.commit()

        print(f"Meeting created")

    def update(self):
        sql = f"""
            UPDATE {self.TABLE_NAME}
            SET venue = ?, host = ?, time = ?, members = ?
            WHERE id = ?
        """

        cursor.execute(sql, (self.venue, self.host, self.time, self.members, self.id))
        conn.commit()
        print(f"Meeting {self.id} updated")

    def to_dict(self):
        return {
            "id": self.id,
            "venue": self.venue,
            "host": self.host,
            "members": self.members,
            "time": self.time
        }

    @classmethod
    def find_one(cls, id):
        sql = f"""
            SELECT * FROM {cls.TABLE_NAME}
            WHERE id = ?
        """

        row = cursor.execute(sql, (id,)).fetchone()

        if row == None:
            return None

        return cls.row_to_instance(row)

    @classmethod
    def find_all(cls):
        rows = cursor.execute(f"SELECT * FROM {cls.TABLE_NAME}").fetchall()

        return [cls.row_to_instance(row) for row in  rows]

    @classmethod
    def row_to_instance(cls, row):
        meeting = cls(row[1], row[4], row[2], row[3])
        meeting.id = row[0]

        return meeting

    # modifier functions
    @classmethod
    def create_table(cls):
        # sql logic to create meetings table
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                venue TEXT NOT NULL,
                host TEXT NOT NULL,
                time TEXT NOT NULL,
                members STRING NOT NULL
            )
        """

        cursor.execute(sql)
        conn.commit()
        print("Meetings table created")

    @classmethod
    def alter_table(cls, column, datatype = None):
        drop_sql = f"ALTER TABLE {cls.TABLE_NAME} DROP COLUMN {column}"
        add_sql = f"ALTER TABLE {cls.TABLE_NAME} ADD COLUMN {column} {datatype}"


    @classmethod
    def drop_table(cls):
        sql = f"""DROP TABLE IF EXISTS {cls.TABLE_NAME}"""

        cursor.execute(sql)
        conn.commit()
        print("Meetings table dropped")

# Meeting.drop_table()

Meeting.create_table()
# Meeting.alter_table("members", "STRING")


# python_catchup = Meeting("Room 302", "Jane, John", "Andrew", "9-10am")

# python_catchup.save()

# meeting = Meeting.find_one(1)

# meeting.members = "Eddah, George"

# meeting.update()

# print(meeting.members)

# print(Meeting.find_all())
