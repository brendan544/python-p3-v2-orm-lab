from __init__ import CURSOR, CONN
from department import Department
from employee import Employee


class Review:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, year, summary, employee_id, id=None):
        self.id = id
        self.year = year
        self.summary = summary
        self.employee_id = employee_id
 def create(cls, year, summary, employee_id):
        review = cls(year, summary, employee_id)
        # Simulate saving to a database and assigning an ID
        review.id = 1  # Example ID; replace with actual DB logic
        return review

    def save(self):
        # Logic to save the review to a database
        pass

    @classmethod
    def get_all(cls):
        # Logic to get all reviews from the database
        return []

    @classmethod
    def get_all_for_employee(cls, employee_id):
        # Logic to get all reviews for a specific employee
        return []

    @classmethod
    def instance_from_db(cls, db_row):
        return cls(db_row['year'], db_row['summary'], db_row['employee_id'])

    @classmethod
    def find_by_id(cls, review_id):
        # Logic to find a review by ID in the database
        return None  # Simulate not found for now

    def update(self):
        # Logic to update this review in the database
        pass

    def delete(self):
        # Logic to delete this review from the database
        pass
    def __repr__(self):
        return (
            f"<Review {self.id}: {self.year}, {self.summary}, "
            + f"Employee: {self.employee_id}>"
        )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Review instances """
        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            year INT,
            summary TEXT,
            employee_id INTEGER,
            FOREIGN KEY (employee_id) REFERENCES employee(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Review  instances """
        sql = """
            DROP TABLE IF EXISTS reviews;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the year, summary, and employee id values of the current Review object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        pass

    @classmethod
    def create(cls, year, summary, employee_id):
        """ Initialize a new Review instance and save the object to the database. Return the new instance. """
        pass
   
    @classmethod
    def instance_from_db(cls, row):
        """Return an Review instance having the attribute values from the table row."""
        # Check the dictionary for  existing instance using the row's primary key
        pass
   

    @classmethod
    def find_by_id(cls, id):
        """Return a Review instance having the attribute values from the table row."""
        pass

    def update(self):
        """Update the table row corresponding to the current Review instance."""
        pass

    def delete(self):
        """Delete the table row corresponding to the current Review instance,
        delete the dictionary entry, and reassign id attribute"""
        pass

    @classmethod
    def get_all(cls):
        """Return a list containing one Review instance per table row"""
        pass

