import MySQLdb

def connection():
	conn = MySQLdb.connect(host="localhost",
		                    user= "root",
		                    passwd="!@aA12345",
		                    db="pythonprogramming")

	c = conn.cursor()

	return c, conn