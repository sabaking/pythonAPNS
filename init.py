#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as db
import string
from apnsclient import *

db = db.connect(host="myhost", user="user", passwd="psswd", db="base", charset='utf8')

c = db.cursor()
c.execute(""" SELECT  s.* FROM `push`.`push_subscribers` s where device_type = 'apns'   and last_time > unix_timestamp() - 90*24*60*60
  and disable = 'N'  
  or   device_id = '32hex device id ' 
  order by last_time """)

result = c.fetchall()

session = Session()
con = session.get_connection("push_production", cert_file="production_full.pem")
kwargs = { "aps" : {'sound':'default' , 'badge':1 , 'alert': 'test' , 'type':0 , 'id':'6074161'}}

for row in result: 
		  print row[2]
		  message = Message(row[2],payload=kwargs)
		  srv = APNs(con)
		  res = srv.send(message)
