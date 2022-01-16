import pymysql 

username = "root"
host="localhost"
password=""
dbname = "data_db"

def connect():
    db = pymysql.connect(user=username,host=host,password=password,db=dbname)
    return db

def insert_task(name,description,deadline):
    try:
        db = connect()
        cs = db.cursor()
        sql = "insert into data (data_name,data_description,data_deadline) values (%s,%s,%s)"
        values = (name,description,deadline)
        cs.execute(sql,values)
        db.commit()
        return True
    except:
        return False
    finally:
        db.close()
        
        
def get_tasks():
    
    try:
        db = connect()
        cs = db.cursor()
        sql = "select * from data"
        cs.execute(sql)
        tasks = cs.fetchall()
        return tasks
    except:
        return False
    finally:
        db.close()
        
        
def get_task(id):
    
    try:
        db = connect()
        cs = db.cursor()
        sql = "select * from data where data_id=%s"
        value = (id,)
        cs.execute(sql,value)
        task = cs.fetchone()
        return task
    except Exception as e:
        print(e)
        return False
    finally:
        db.close()      
        
def update_task(id,name,description,deadline):
    try:
        db = connect()
        cs = db.cursor()
        sql = "update task set data_name=%s, data_description=%s, data_deadline=%s where data_id=%s"
        values = (name,description,deadline,id)
        cs.execute(sql,values)
        db.commit()
        return True
    except:
        return False
    finally:
        db.close()   

 
def delete_task(id):
    try:
        db = connect()
        cs = db.cursor()
        sql = "delete from task where data_id=%s"
        value = (id,)
        cs.execute(sql,value)
        db.commit()
        return True
    except:
        return False
    finally:
        db.close()
  
    