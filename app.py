#_*_ coding:utf-8 _*_
import MySQLdb
from xml.dom import minidom
try:
	conn = MySQLdb.connect(host='192.168.1.141',user='root',passwd='',db='jianai',charset='utf8')
	cur = conn.cursor()
except MySQLdb.Error,e:
	print e.args

def get(sql):
	cur.execute(sql)
	rs = cur.fetchone()
	if rs is None:
		return rs
	return rs[0]

def getAll(sql):
	cur.execute(sql)
	rs = cur.fetchall()
	for v in rs:
		print v[0],v[1],v[2],v[3]

def sql(sql):
	try:
		cur.execute(sql)
	except MySQLdb.Error,e:
		print e.args
	else:
		conn.commit()
	#cur.close()
	#conn.close()

def get_xmlnode(node,name):
    return node.getElementsByTagName(name) if node else []
def get_attrvalue(node, attrname):
     return node.getAttribute(attrname) if node else ''

def main():
	doc = minidom.parse('Citys.xml')
	root = doc.documentElement
	for node in get_xmlnode(root,'Province'):
		province = get_attrvalue(node,'pname')
		pid = get("select id from ja_city where name='%s'" % province)
		if pid:
			for city in get_xmlnode(node,'City'):
				cityname = get_attrvalue(city,'cname')
				cid = get("select id from ja_city where name='%s'" % cityname)
				if cid:
					for location in get_xmlnode(city,'County'):
						locationname = get_attrvalue(location,'name')
						sid = get("select id from ja_city where name='%s'" % locationname)
						if sid is None:
							sql("insert into ja_city (pid,cid,name) value (%s,%s,'%s')" % (pid,cid,locationname))
				else:
					sql("insert into ja_city (pid,cid,name) value (%s,0,'%s')" % (pid,cityname))
		else:
			sql("insert into ja_city (pid,cid,name) value (0,0,'%s')" % province)


#main()
#getAll("select * from ja_city where name ='%s'" % '罗田县')
#print sql('delete from ja_city where id = 1')