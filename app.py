from flask import Flask,request
import requests as req
app = Flask(__name__)

@app.route("/")
def home():

  return "<h1>HI Page</h1>"

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
  if msg=="debug":
  	return url
  return reply['message']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)