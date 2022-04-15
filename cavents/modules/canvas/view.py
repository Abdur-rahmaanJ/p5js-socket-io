from shopyo.api.module import ModuleHelp

from flask_socketio import SocketIO, join_room, leave_room, emit
# from flask import render_template
# from flask import url_for
# from flask import redirect
# from flask import flash
# from flask import request

# from shopyo.api.html import notify_success
# from shopyo.api.forms import flash_errors

from init import socketio

mhelp = ModuleHelp(__file__, __name__)
globals()[mhelp.blueprint_str] = mhelp.blueprint
module_blueprint = globals()[mhelp.blueprint_str]


@module_blueprint.route("/")
def index():
    return mhelp.render('index.html')


# @socketio.on('join')
# def join(message):
#     join_room(room)
#     # emit('status', {'msg':  session.get('username') + ' has entered the room.'}, room=room)


@socketio.on('mouse')# , namespace='/chat')
def mouse(data, methods=['GET', 'POST']):
    # print(data)
    emit('mouse', data, broadcast=True)





# If "dashboard": "/dashboard" is set in info.json
#
# @module_blueprint.route("/dashboard", methods=["GET"])
# def dashboard():

#     context = mhelp.context()

#     context.update({

#         })
#     return mhelp.render('dashboard.html', **context)
