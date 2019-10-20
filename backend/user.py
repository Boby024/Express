from backend.FlaskandDBConnect import *

@app.route('/allUsers', methods=['GET'])
def allUsers():
  try:
    cur = mysql.connection.cursor()
    response=cur.execute('''SELECT * FROM users''')
    result = cur.fetchall()
    cur.close()
  except (MySQL.Error, MySQL.Warning) as err :
    print("something went wrong {}".format(err))
    pass
  return jsonify(result)


@app.route('/api/register', methods=['POST'])
def addUser():
  data = request.get_json()
  username = data['username']
  passwd = data['passwd']
  email = data['email']
  try:
    cur = mysql.connection.cursor()
    response= cur.execute(""" SELECT * FROM  users WHERE username = %s and passwd= %s and email= %s """,( username,passwd,email) )

    if response >0:
      result = {'message': 'register fail/already exits'}
    else:
      cur.execute(""" INSERT INTO users (username,passwd,email) VALUES (%s, %s, %s)""",( username,passwd,email) )
      mysql.connection.commit()
      cur.close()
      result = {'message': 'register done', 'email': username}

  except (MySQL.Error, MySQL.Warning) as err:
    print("something went wrong {}".format(err))
    pass
  return jsonify(result)





