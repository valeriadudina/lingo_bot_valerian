import mysql.connector

class MySQL():
  def __init__(self):
    self.mydb = mysql.connector.connect(
      host="sql7.freemysqlhosting.net",
      user="sql7618986",
      password="RI6V8GxBAu",
      database="sql7618986",
      auth_plugin='mysql_native_password'
    )

    self.mycursor = self.mydb.cursor()

  def search_user(self, tg_nikname):

    sql = "SELECT id FROM sql7618986.users where tg_nikname = %s "
    val = (tg_nikname,)
    self.mycursor.execute(sql, val)
    myresult = self.mycursor.fetchall()
    print(myresult)
    if myresult !=[]:
      return myresult[0][0]
    else:
      return 0
  def get_user_by_id(self, user_id):
    sql = "SELECT * FROM sql7618986.users where id = %s "
    val = (user_id,)
    self.mycursor.execute(sql, val)
    myresult = self.mycursor.fetchall()
    print(myresult)
    if myresult != []:
      return myresult[0][0], myresult[0][1], myresult[0][2]
    else:
      return 0
  def insert_user(self, name, tg_nikname):

    sql = "INSERT INTO `sql7618986`.`users` (name, tg_nikname) VALUES (%s, %s)"
    val = (name, tg_nikname)
    self.mycursor.execute(sql, val)

    self.mydb.commit()

    print(self.mycursor.rowcount, "record inserted.")
    return self.mycursor.rowcount-1, name, tg_nikname
  def insert_word(self, user, new_words):

    sql = "INSERT INTO `sql7618986`.`vocabulary` (user_id, word, translate) VALUES (%s, %s, %s)"
    val = (user.user_id,new_words.word, new_words.translate)
    self.mycursor.execute(sql, val)

    self.mydb.commit()

    print(self.mycursor.rowcount, "word inserted.")

  def get_random_word(self, user_id):
    sql = "SELECT * FROM sql7618986.vocabulary where user_id=%s ORDER BY RAND() LIMIT 1 ; "
    val = (user_id,)
    self.mycursor.execute(sql, val)
    myresult = self.mycursor.fetchall()
    print(myresult)
    if myresult != []:
      return  myresult[0][1], myresult[0][2]
    else:
      return 0

  def get_trhee_extra_words(self, user_id, word):

     sql = "SELECT * FROM sql7618986.vocabulary where user_id=%s and word not like %s ORDER BY RAND() LIMIT 3 ; "
     val = (user_id,word,)
     self.mycursor.execute(sql, val)
     myresult = self.mycursor.fetchall()
     print(myresult)
     if myresult != []:
       return myresult
     else:
       return 0