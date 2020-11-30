import pymysql

MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='dave',
    passwd='funcoding',
    db='blog_db',
    charset='utf8')

def conn_mysqldb():
    if not MYSQL_CONN.open:             # 연결이 끊어지면 false 출력
        MYSQL_CONN.ping(reconnect=True) # 다시 재접속
    return MYSQL_CONN
