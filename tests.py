from data.db import SQLite

dd = {
    'number' : 1,
    'date': '11.12.2023'
}


data = SQLite()

data.insert(params=dd)