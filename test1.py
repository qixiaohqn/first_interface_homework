from bytedmysql import connect
from evtest import test
from evtest.env import Env


@test.story("查询db")
@test.runtime(Env.BOE, data=[{}])
def test_query_db(title, env, params, expected, other):
    # 打开数据库连接
    db = connect(db="data_build", db_psm="toutiao.mysql.data_build_write")
    # 使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()
    cursor.execute("select * from product limit 5")
    # 获取所有记录列表
    result = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    print(result)
