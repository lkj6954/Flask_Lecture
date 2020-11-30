import pymongo

MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST)) # .MongoClient 로 접속

def conn_mongodb():
    try:
        MONGO_CONN.admin.command('ismaster') # 이 명령이 안된다는건 연결이 끊겼다는 것
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    except:
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        blog_ab = MONGO_CONN.blog_session_db.blog_ab

    return blog_ab
