from flask import Flask,request
from flask import jsonify



app = Flask(__name__) 
app.json.sort_keys=False

from datetime import datetime, timezone
def get_today():
    dt=datetime.now()
    today=dt.strftime('%A')
    return today

"""def get_time():
    t=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    return t"""

user={
      'slack_name':'Maureen_Mwenswa',
      'track':'backend',
        'current_day':get_today(),
        'utc_time':datetime.utcnow.strftime("%Y-%m-%dT%H:%m:%SZ"),
        'github_file_url':'https://github.com/kurves/hng-backend-task/blob/main/app.py',
        'github_repo_url':'https://github.com/kurves/hng-backend-task',
        'status_code':200

}
@app.route('/api',methods=['GET'])
def apis():
    request
    slack_name=request.args.get("slack_name")
    track=request.args.get("track")

    return jsonify(
       user

    )


if __name__== '__main__':
    app.run()    