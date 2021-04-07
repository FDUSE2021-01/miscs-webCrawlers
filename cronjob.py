#!/bin/python3

import sqlite3

if __name__ == '__main__':
    with sqlite3.connect() as myConnection:
        import history.daily
        history.daily(myConnection)
