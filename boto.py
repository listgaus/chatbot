"""This is the template server side for ChatBot"""

from bottle import route, run, template, static_file, request
from json import dumps

CURSES = ['fuck', 'bitch', 'cunt', 'whore', 'shit']
SCARYS = ['kill', 'shoot', 'stab', 'yell', 'thief', 'hit']

@route('/', method='GET')
def index():
    return template('chatbot.html')


@route('/chat', method='POST')
def chat():
    user_message = request.POST.get('msg')
    interpret_respond, name_is = interpret(user_message)
    return dumps({'animation': name_is, 'msg': interpret_respond})

def curse_reply():
        return 'Who taught you those words? boto will never accept such low level, mofo!', 'no'

def sad():
    return 'it makes me sad youre leaving', 'sad'

def interpret(user_input):
    user_input = user_input.lower()

    for curse in CURSES:
        if user_input.find(curse) != -1:
            return curse_reply()

    if user_input == 'hello':
        return 'Hi, what is your name?', 'excited'

    if user_input.startswith('my name is'):
        start = user_input.find('is') + 3
        name = user_input[start:]
        return 'Nice to meet you {}, what can i do for you today?'.format(name.title()), 'dog'

    if user_input.count('bye') == 1:
        return 'Good day, byebye', 'takeoff'

    if user_input.count('rich' or 'money') == 1:
        return 'haha, money aint a thing', 'money'

    if user_input.count('do') == 1:
        return 'Sir yes sir', 'ok'

    if user_input.count('dance') or user_input.count('song') == 1:
        return 'I love dancing to songs', 'dancing'

    for scary in SCARYS:
        if user_input.find(scary) != -1:
            return 'Wow thats scary', 'afraid'

    if user_input.count('leaving'):
        return sad()
    else:
        animation = 'confused'
        return user_input, animation


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
