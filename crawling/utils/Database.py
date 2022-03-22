import pymysql
import pymysql.cursors
import logging

import sys
[sys.path.append(i) for i in ['.', '..']]
from crawling.config.DatabaseConfig import *

class Database:
    def __init__(self):
        self.conn = None
    def connect(self):
        if self.conn != None:
            return
        self.conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            db=DB_NAME,
            charset='utf8'
        )
    # def cursor(self):
        # return self.conn.cursor()
    def close(self):
        if self.conn is None:
            return
        if not self.conn.open:
            self.conn = None
            return
        self.conn.close()
        self.conn = None
    def execute(self, sql):
        last_row_id = -1
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
            self.conn.commit()
            last_row_id = cursor.lastrowid
        except Exception as ex:
            logging.error(ex)
        finally:
            return last_row_id
    def select_one(self, sql):
        result = None
        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        except Exception as ex:
            logging.error(ex)
        finally:
            return result
    def select_all(self, sql):
        result = None
        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
        except Exception as ex:
            logging.error(ex)
        finally:
            return result