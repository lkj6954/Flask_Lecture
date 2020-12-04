import pymongo

MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))

def conn_mongodb():
    try:
        MONGO_CONN.admin.command('ismaster')
        # blog_session_db와 blog_ab는 어디서 튀어나온거..?
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    except: # 연결 에러 떴을 경우 다시 연결
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    return blog_ab