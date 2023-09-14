# main.py
from watcher import Watcher

server_name = 'CHRISTIAN-LT\SQLEXPRESS01'
db_name = 'TestDBJSON'
table_name = 'TestTABLEJSON'

w = Watcher(db_name, table_name, server_name)
w.run()
