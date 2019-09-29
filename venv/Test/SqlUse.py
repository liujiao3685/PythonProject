import mssql_helper

server = "127.0.0.1"
user = "sa"
password = "1234"
database = "Python"

mssql = ""


def main():
    global mssql
    mssql = mssql_helper.MSSQL(server, user, password, database)

def create():
    mssql.CreateTable()

def test():
    rows = mssql.ExecQuery("SELECT * FROM persons")
    print(rows)


if __name__ == '__main__':
    main()
    create()
    test()
