from backend.FlaskandDBConnect import *
from backend.user import allUsers, addUser


allUsers
addUser


if __name__ == '__main__':
    app.run(port=5001, debug=True)
