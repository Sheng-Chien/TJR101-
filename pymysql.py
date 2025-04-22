import pymysql 


conn = pymysql.connect(host=host, 
                       port=3306, 
                       user=root, 
                       passwd=abc912321, 
                       db=db, charset=charset) 
print(Successfully connected!)