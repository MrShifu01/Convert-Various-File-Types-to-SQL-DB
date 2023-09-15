# main.py
from watcher import Watcher

server_name = 'CHRISTIAN-LT\SQLEXPRESS01'
db_name = 'TestDatabase'
table_name = 'TestTableJSONTest3'

w = Watcher(db_name, table_name, server_name)
w.run()
