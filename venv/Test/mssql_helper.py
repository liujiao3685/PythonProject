import pymssql

# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称

server = "127.0.0.1"
user = "sa"
password = "1234"
database = "Python"
conn = pymssql.connect(server, user, password, database)
cursor = conn.cursor()


# 新建表
def CreateTable():
    sql = """
    IF OBJECT_ID('persons', 'U') IS NOT NULL DROP TABLE persons
    CREATE TABLE persons (id INT NOT NULL identity(1,1),name VARCHAR(100),age int,PRIMARY KEY(id))
    """
    cursor.execute(sql)
    conn.commit()


# 批量插入数据
def InsertData():
    sql = "INSERT INTO persons(name,age) VALUES (%s, %d)"
    data = [
        ('zhangsan', 15),
        ('lisi', 16),
        ('wangwu T.', 17)]
    cursor.executemany(sql, data)
    # 如果没有指定autocommit属性为True的话就需要调用commit()方法
    conn.commit()


# 删除操作
def DeleteData():
    sql = "delete persons where id=5"
    cursor.execute(sql)
    conn.commit()


# 查询操作
def SelectTable():
    sql = "SELECT * FROM persons"
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        print("ID=%d, Name=%s" % (row[0], row[1]))
        row = cursor.fetchone()
    # 也可以使用for循环来迭代查询结果
    # for row in cursor:
    #     print("ID=%d, Name=%s" % (row[0], row[1]))


# 修改操作
def UpdateData():
    sql = "update [persons] set name ='Python1' where id<3"
    cursor.execute(sql)
    conn.commit()


# 关闭连接
def Close():
    conn.close()


def main():
    CreateTable()
    InsertData()
    DeleteData()
    UpdateData()
    SelectTable()
    conn.close()


if __name__ == '__main__':
    main()


class MSSQL:
    def __init__(self, host, user, pwd, db):  # 类的构造函数，初始化数据库连接ip或者域名，以及用户名，密码，要连接的数据库名称
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):  # 得到数据库连接信息函数， 返回: conn.cursor()
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset='utf8')
        cur = self.conn.cursor()  # 将数据库连接信息，赋值给cur。
        if not cur:
            return (NameError, "连接数据库失败")
        else:
            return cur

    # 执行查询语句,返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    def ExecQuery(self, sql):  # 执行Sql语句函数，返回结果
        cur = self.__GetConnect()  # 获得数据库连接信息
        cur.execute(sql)  # 执行Sql语句
        resList = cur.fetchall()  # 获得所有的查询结果
        # 查询完毕后必须关闭连接
        self.conn.close()  # 返回查询结果
        return resList

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

    def CreateTable(self):
        cur = self.__GetConnect()
        CreateTable()
