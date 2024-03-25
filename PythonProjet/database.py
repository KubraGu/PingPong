#database.py
import sys
sys.path.append('/usr/lib/python3/dist-packages') 

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['PingPong']