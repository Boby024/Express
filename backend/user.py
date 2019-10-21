from backend.FlaskandDBConnect import *
from backend.helper import prepareforJSON, encodePASSWD

@app.route('/api/allUsers', methods=['GET'])
def allUsers():
  try:
    cur = mysql.connection.cursor()
    response=cur.execute('''SELECT * FROM users''')
    result = cur.fetchall()
    cur.close()
  except (MySQL.Error, MySQL.Warning) as err :
    print("something went wrong {}".format(err))
    pass
  modeller=["id","username","passwd","email"]
  return jsonify(prepareforJSON(result,modeller)) #jsonify(result)


@app.route('/api/register', methods=['POST'])
def addUser():
  data = request.get_json()
  username = data['username']
  psd = data['passwd']
  passwd= encodePASSWD(psd)
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


@app.route('/api/login', methods=['POST'])
def login():
  data= request.get_json()
  username= data['username']
  ps = data['passwd']
  passwd = encodePASSWD(ps)
  try:
    cur = mysql.connection.cursor()
    response= cur.execute(""" SELECT * FROM  users WHERE username = %s and passwd= %s""",( username,passwd) )
    rs= cur.fetchall()
    cur.close()

    if response > 0 :
      modeller = ["id", "username", "passwd", "email"]
      userData = prepareforJSON(rs,modeller)
      user= userData[0]
      user['login']= 'login done'
      user.pop('id')
      user.pop('email')
      user.pop('passwd')
      result = user
    else:
      result = {'login' : 'login fail'}

  except (MySQL.Error, MySQL.Warning) as err:
    print("something went wrong {}".format(err))
    pass
  return jsonify(result)



