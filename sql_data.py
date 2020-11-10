import sqlite3


class Database:
    def __init__(self):
        # Create or Connect to macro database
        self.connection = sqlite3.connect('database/macro.db')
        # Create cursor
        self.cursor = self.connection.cursor()
        # Create table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS target (
            Protein real,
            Carbs real,
            Fats,
            sqltime TEXT DEFAULT (strftime('%Y-%m-%d','now', 'localtime'))        
        )""")
        # Commit changes
        self.connection.commit()

        # Create or connect to existing daily database
        self.daily_connection = sqlite3.connect('database/daily.db')
        # Create cursor
        self.daily_cursor = self.daily_connection.cursor()
        # Create Table
        self.daily_cursor.execute("""CREATE TABLE IF NOT EXISTS day (
            Meal text,
            Protein real,
            Carbs real,
            Fats real,
            Total_Weight int,
            sqltime TEXT DEFAULT (strftime('%Y-%m-%d','now', 'localtime'))
        )""")
        # Commit changes
        self.daily_connection.commit()

        # Create or connect to existing meals database
        self.meals_connection = sqlite3.connect('database/meals.db')
        print("Connected to SQLite")
        # Create Cursor
        self.meals_cursor = self.meals_connection.cursor()
        # Create table
        self.meals_cursor.execute("""CREATE TABLE IF NOT EXISTS meal (
            Food text,
            Protein int,
            Carbs int,
            Fats int,
            Total_Weight int
        )""")
        # Commit Changes
        self.meals_connection.commit()
        # Close Connection (optional, will close anyway)
        self.meals_connection.close()


def item_list():
    conn = sqlite3.connect('database/meals.db')
    c = conn.cursor()
    items = c.execute("SELECT Food FROM meal")
    food_list = [it[0] for it in items.fetchall()]
    return food_list


if __name__ == "__main__":
    d = Database()