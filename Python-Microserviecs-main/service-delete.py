from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

@app.route('/delete', methods=['DELETE'])
def delete():
    # Get the user's login information from the request
    user = request.form.get('username')
  

    _user = us.find_username(user)

    if _user:
        us.user_name_remove(user)
        return jsonify({'message': 'delete successfully.'}), 200
    else:
        return jsonify({'message': 'Cannot delete user.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1