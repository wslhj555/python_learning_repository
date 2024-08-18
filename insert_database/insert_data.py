import mysql.connector

mydb=mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="123456",
  database="test_db"
)

mycursor=mydb.cursor()

# 第一步：创建表格
create_table_sql = """
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
)
"""
#mycursor.execute(create_table_sql)

# 第二步：插入一万条数据
insert_sql = "INSERT INTO products (name, price) VALUES (%s, %s)"

# 生成一万条数据
data = []
for i in range(10001, 20001):
    name = f"Product_{i}"
    price = i * 10  # 假设价格是产品ID的10倍
    data.append((name, price))

# 批量插入数据
mycursor.executemany(insert_sql, data)

# 提交事务
mydb.commit()


mycursor.close()
mydb.close()