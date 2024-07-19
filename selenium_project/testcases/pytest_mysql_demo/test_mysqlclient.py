import platform
import mysql.connector
import sys
import pytest

'''mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456"
)
print(platform.architecture())
print(sys.maxsize>=2**32)
'''

connection=mysql.connector.connect(
    host="localhost",
    database='test_db',
    user="root",
    passwd="123456"
)

cursor = connection.cursor()

# 定义 SQL 查询语句
query = "SELECT * FROM users"

# 执行查询
cursor.execute(query)

# 获取查询结果
results = cursor.fetchall()

# 打印结果

list_0=[]
for row in results:
    tuple_0=(row[1],row[2])
    list_0.append(tuple_0)

@pytest.mark.parametrize("name,email",list_0)
def test_mysqlclient(name,email):
    print(name,email)

if __name__ == '__main__':
    pytest.main(['-sv', './testcases/pytest_mysql_demo/test_mysqlclient.py'])

# 关闭 cursor 和连接
cursor.close()
connection.close()


