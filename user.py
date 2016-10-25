#! python3

import sqlite3

class User:

  def __init__(self, username, password):
    self.username = username
    self.password = password

  def signup(self):
      conn = sqlite3.connect( 'interview_app.db' )
      conn.row_factory= sqlite3.Row

      username = self.username
      password = self.password

      try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM User ORDER BY ID DESC LIMIT 1;")

        row = cur.fetchone()

        if row == None:
          conn.execute("INSERT into User (id,username,password) VALUES (?,?,?);", (1, username, password))
        else:
          increment = int(row["id"])
          conn.execute("INSERT into User (id,username,password) VALUES (?,?,?);", (increment + 1, username, password))
        conn.commit()
        conn.close()
      except:
        raise