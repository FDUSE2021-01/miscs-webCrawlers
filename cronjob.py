#!/bin/python3

import sqlite3

if __name__ == '__main__':
    myConnection = sqlite3.connect()
    import history.daily
    history.daily()
