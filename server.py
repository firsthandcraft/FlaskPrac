from flask import Flask
import random 

app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'radom: <strong>'+str(random.random())+'</strong>'

topics = [
    {'id':1,'title':'html','body':'htmlis...'},
    {'id':2,'title':'css','body':'css is...'},
    {'id':3,'title':'javascript','body':'javascript is...'}
]

@app.route('/')
def index():
    liTags=''
    for topic in topics:
        # liTags  = liTags+'<li>'+topic['title']+'</li>'
        liTags  = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return f'''<!dotype html>
    <html>
        <body>
            <h1><a  href="/">WEB</a></h1>
            <ol>
                {liTags}           
            </ol>
            <h2>welcome</h2>
            Hello,Web
        </body>
    </html>
    '''
    #<li> <a  href="/read/1/">html</a></li>
    #<li> <a  href="/read/2/">css</a></li>
    #<li> <a  href="/read/3/">javascript</a></li>

@app.route('/create/')
def  create():
        return 'Create'


@app.route('/readtest/1/') 
def  read():
        return 'Read 1'

#1처럼 가변적으로 바뀐는 변수를 만드는 게 router
@app.route ('/read/<id>/') #꺽쇠 <> 는 주소의 파라미터에 이름을 받아준다. 
def readId(id):
    print(id)
    return str(id)

    
app.run(port=5001, debug=True)