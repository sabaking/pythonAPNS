#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as db
import string
from apnsclient import *
db = db.connect(host="db2.gazeta.ru", user="unrest", passwd="satyr1con", db="unrest", charset='utf8')
c = db.cursor()

#c.execute('''SELECT * FROM `news`.`articles`
#			where article_stripe in (1732, 1728, 4658, 21273, 4524, 4548, 1883, 3147, 3848, 58837, 58845, 58841, 21317, 21321, 926, 4612, 4206)
#			and article_publish_time > 0 and article_deleted = 0
#			and article_content like  '%%<%%breaking%%>on<%%/breaking%%>%%'
#			and article_publish_time > unix_timestamp() - 48*60*60 order by article_publish_time desc
#			limit 1''')
#result = c.fetchall()
#for row in result: 
#				 id = str(row[0])
#				 article_name = row[1].decode('utf8')

#print article_name
#exit;

c.execute(""" SELECT  s.* FROM `push`.`push_subscribers` s where device_type = 'apns'   and last_time > unix_timestamp() - 90*24*60*60
  and disable = 'N'  
  or   device_id = 'c988ddfac4568955381d9090f42f45833115431de10b76835d79a4b219161e86' 
  order by last_time """)
result = c.fetchall()
session = Session()
con = session.get_connection("push_production", cert_file="gazeta_production_full.pem")
article_name = "ПАСЕ лишила Россию права голоса до конца 2014 года"
uu = article_name.decode('utf-8')
kwargs = { "aps" : {'sound':'default' , 'badge':1 , 'alert':uu , 'type':0 , 'id':'6074161'}}

for row in result: 
				  print "Device"
				  print row[2]
				  message = Message(row[2],payload=kwargs)
				  srv = APNs(con)
				  res = srv.send(message)
