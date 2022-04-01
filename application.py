from flask import Flask, render_template, redirect, url_for, request, json
from flask_socketio import SocketIO, join_room, leave_room
import robot_developer as rd
import robot_customer as rc
import os
import sys

application = Flask(__name__)
socketio = SocketIO(application)
# print(start_year, file=sys.stderr)



#Generate random url for files in static to avoid cache problems 
@application.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(application.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
    
    

#
  
 # ----Chat -----
 
 
 
 
 
 
 # --- Chat ---
  
  
  
  
  
  
  
# --------------------------- ROUTES -------------------------------------------------

#---------------- Index.html -------------
@application.route("/")
def home():
	return render_template("index.html")
@application.route("/help/")
def help():
 return render_template("help.html")	
#--------------------------------------------
 
# --------------------robot_developer.html----------------------------------
@application.route("/robot_developer/",methods=["POST","GET"])
def robot_developer():
 selected =[]
 if request.method=="POST":
  for i in range (1,11):
   if(request.form["stock"+str(i)] != "" ):
    selected.append(request.form["stock"+str(i)])
  num_portfolios = int(request.form["num_portfolios"])
  
  start_year = str(request.form["start_year"])
  end_year = str(request.form["end_year"])
  if(num_portfolios < 50000 and num_portfolios > 3):
   output =  rd.start(selected,start_year,end_year,num_portfolios)
  else:
   return render_template("robot_developer.html")
  return render_template("complete.html")
 else:
  return render_template("robot_developer.html")  
#-----------------------------------------------------------------------------------  

# ------------------------------------------robot_customer.html----------------
@application.route("/robot_customer/",methods=["POST","GET"])
def robot_customer():
 if request.method=="POST":

  output =  rc.start(['QQQ','LQD','IEI','SPY'],'2000-01-01','2020-01-01')
  return render_template("complete.html")
 else:
  return render_template("robot_customer.html")	
#-------------------------------------------------------------------------------------    

 
# ------------------------------------------chat.html----------------
@application.route('/chat')
def chat():
    username = request.args.get('username')
    room = request.args.get('room')

    if username and room:
        return render_template('chat.html', username=username, room=room)
    else:
        return redirect(url_for('home'))     
#-----------------------------------------------------------------------------------------     

# ------------------------------------------chat_log.html-----------------------------   
@application.route('/chat_log')
def chat_log():
        return render_template('chat_log.html')
    
#-----------------------------------------------------------------------------------------    
# ----------------------------- ROUTES -------------------------------------------------
 
 
# ----------------------------- SOCKET IO  --------------------------------------------------------
@socketio.on('send_message')
def handle_send_message_event(data):
    application.logger.info("{} has sent message to the room {}: {}".format(data['username'],
                                                                    data['room'],
                                                                    data['message']))
    socketio.emit('receive_message', data, room=data['room'])


@socketio.on('join_room')
def handle_join_room_event(data):
    application.logger.info("{} has joined the room {}".format(data['username'], data['room']))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])


@socketio.on('leave_room')
def handle_leave_room_event(data):
    application.logger.info("{} has left the room {}".format(data['username'], data['room']))
    leave_room(data['room'])
    socketio.emit('leave_room_announcement', data, room=data['room'])
#----------------------------------------------------------------------------------------------------------    
 
 
 
 
 
 
 
 
 
 
 
 
 
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.debug = True
    application.run()

