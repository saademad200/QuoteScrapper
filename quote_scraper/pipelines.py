import sqlite3
import logging

class SQLitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('quotes.db')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                author TEXT,
                tags TEXT
            )
        ''')
        self.conn.commit()
        logging.info("Database connection opened and table created.")

    def close_spider(self, spider):
        try:
            self.conn.commit()
            logging.info("Data committed to database.")
        finally:
            self.conn.close()
            logging.info("Database connection closed.")

    def process_item(self, item, spider):
        try:
            self.c.execute('''
                INSERT INTO quotes (text, author, tags) VALUES (?, ?, ?)
            ''', (
                item['title'],
                item['author'],
                ','.join(item['tags'])
            ))
            self.conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error while inserting item: {e}")
        return item
