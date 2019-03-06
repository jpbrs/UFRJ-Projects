# -*- coding: utf-8 -*-
import sqlite3 as sql

class DataBase:
    def __init__(self, name="siga"):
        self.name = name
        self.db = "{}.db".format(name)

    def __repr__(self):
        return "DB[{}]".format(self.name)

    def __call__(self, cmd):
        with sql.connect(self.db) as con:
            cur = con.cursor()
            cur.execute(cmd)
            out = cur.fetchall()
            con.commit()
        return out
