
from flask import Flask,render_template,request
import requests as req
app = Flask(__name__)
#golabl var
pname,msg = '',""

@app.route("/api")
def api():
  msg = request.args.get('msg')
  name = request.args.get('name')
  url = "https://api.affiliateplus.xyz/api/chatbot?message="+msg+"&name="+name+"&user=1"

  reply = req.get(url).json()
  if reply['error'] == 'true':
    return "Opps! server error"
  if reply['message'] == "":
    return "I'm busy right now"
  return reply['message']

@app.route("/",methods =["GET", "POST"])
def home():
  global pname
  global msg
  if request.method == "POST":
       your_name = request.form.get("uname")
       pname = request.form.get("pname") 

       data = {
       "uname":your_name,
       "pname":pname
       }

       return render_template('chat.html',data=data)
  return render_template("home.html")

@app.route("/about")
def about():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)