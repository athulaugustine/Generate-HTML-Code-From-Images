from flask import Flask,render_template,request
import box_2 as b
import webbrowser
app=Flask(__name__,static_url_path='/static', static_folder='/static')

@app.route("/")
def index():
	return render_template("index.html")
@app.route("/datahook",methods=['POST'])
def reply():
	print " you pressed a button"
	print "opening"
	value=request.form['fileName']
	print "you passed in "+value
	b.box_extraction(value, "./")
	webbrowser.open('file:///Users/arunmani/Documents/Box%20Detection%20/html/index.html')
	return render_template("jack.html")
if __name__=='__main__':
	app.run()
else:
	print "error"