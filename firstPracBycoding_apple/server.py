from flask import Flask, request,redirect
import random 

app = Flask(__name__)

#변수 만들기
nextId = 4
topics = [
    {'id':1,'title':'html','body':'htmlis...'},
    {'id':2,'title':'css','body':'css is...'},
    {'id':3,'title':'javascript','body':'javascript is...'}  
]

#함수 만들기
# 템플릿으로 만들어도 된다.
def template(contents,content,id=None):
    ContextUI = ''  
    if id !=None:
        ContextUI = f'''
            
            <li><a href="/update/{id}">update</a></li>
            <li><form action="/delete/{id}"  method="POST"><input type="submit" value="delete"></form></li>
        '''
    return f'''<!dotype html>
    <html>
        <body>
            <h1><a  href="/">WEB</a></h1>
            <h2><a  href="/first">first</a></h2>
            
            
            <ol>
                {contents}           
            </ol>
                {content}
            <ul>
                <li><a href="/create/">create</a></li>
                {ContextUI}
            </ul>
        </body>
    </html>
    '''
    
def getContents():
    liTags=''
    for topic in topics:
        liTags  = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags
###################################
#처음 flask 사용시 이용법
# @app.route('/')
# def index():
#     return 'radom: <strong>'+str(random.random())+'</strong>'
@app.route('/')
def index():# 기본 주소로 들어갈 경우
     #return 문 더 줄이기  getcontents 함수를 만들었다.  
    return template(getContents(),'<h2>Welcome</h2>Hello, WEB <h2><a  href="/first">first</a></h2>')
    # liTags=''
    # for topic in topics:
    #     # liTags  = liTags+'<li>'+topic['title']+'</li>' ### 요 내용이 아래의 문장으로
    #     liTags  = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    #위 코드를 getcontents 함수로 만들기 
    
    # return f'''<!dotype html>
    # <html>
    #     <body>
    #         <h1><a  href="/">WEB</a></h1>
    #         <ol>
    #             {liTags}           
    #         </ol>
    #         <h2>welcome</h2>
    #         Hello,Web
    #     </body>
    # </html>
    # '''
    #위의 리턴과 html구문이 상단의 template 함수가 만들어지면 아래 코드로 return
    # return template(liTags,'<h2>Welcome</h2>Hello,WEB')

    #바로 위 코드에 {liTags}가 만들어져서 li태그는 생략됨
    # <li> <a  href="/read/1/">html</a></li>
    # <li> <a  href="/read/2/">css</a></li>
    # <li> <a  href="/read/3/">javascript</a></li> 
    
   

@app.route('/readtest/1/') 
def  read():#readtest/1/로 들어갈 경우
        return 'Read 1'
# @app.route('/readtest/2/') 
# def first():
#     directory = os.path.dirname(os.path.abspath(__file__))  # 현재 파일의 디렉터리 경로
#     filename = 'first.html'
#     return send_from_directory(directory, filename)
#html파일을 로딩하려면 jina템플릿이 잇어야된다.

###################################
#읽기
# @app.route ('/read/<id>/') 
# def readId(id):
#     return str(id)

#아이디 값이 들어갈 경우
#1처럼 가변적으로 바뀐는 변수를 만드는 게 router
# Flask web framework - 6. 읽기
@app.route ('/read/<int:id>/') #꺽쇠 <> 는 주소의 파라미터에 이름을 받아준다. 
def readId(id):#<id>는 여기 파라미터 값으로 자리에 들어오는 값이  꺽쇠 이름의 파라미터로 들어온다.
    # print(id) 하면 값이 스트링으로 나온다. 아이디 값을 int로 컴퍼팅해줘도 되고 혹은 상단 route 부분에 int:id로 넣어줘도 된다.
    # liTags =''
    # for topic in topics:
    #     liTags = liTags +f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    #getContents 함수로 대채
    
    #topics 조회하기 
    title=''
    body=''
    for topic in topics:
         if id == topic['id']:
             title = topic['title']
             body = topic['body']
             break
        #print(title, body)
    return template(getContents(),f'<h2>{title}</h2>{body}',id)
    # return f'''<!doctype html>
    #     <html>
    #         <body>
    #             <h1><a href="/">WEB</a></h1>
    #                 <ol>
    #                     {liTags}
    #                 </ol>
    #                 <h2>{title}</h2>
    #                 {body}
    #         </body>
    #     </html>
    #     '''    
 
      
###################################
# 수정 form만들기#request, redirect import하기
@app.route('/create/', methods=['GET','POST'])
def  create():#create주소로 들어갈 경우
    #request.method# 상단에 request import 하기
    #print('request.method===',request.method)
    if request.method == 'GET':
        content  ='''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea placeholder="body" name="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(),content)
    elif request.method == 'POST':
        global nextId #전역변수 가져오기
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id':nextId,'title':title,'body':body}
        topics.append(newTopic)
        url ='/read/'+str(nextId)+'/'
        nextId += 1
        # return title+','+body
        return redirect(url)
###################################
#수정
@app.route('/update/<int:id>/', methods=['GET','POST'])
def  update(id):#create주소로 들어갈 경우
    if request.method == 'GET':
        title=''
        body=''
        for topic in topics:
            if id == topic['id']:
                title = topic['title']
                body = topic['body']
                break
        content  =f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" name="title" placeholder="title" value="{title}"></p>
                <p><textarea placeholder="body" name="body">{body}</textarea></p>
                <p><input type="submit" value="update"></p>
            </form>
        '''
        return template(getContents(),content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        for topic in topics:#검색하기
            if id == topic['id']:
                topic['title'] = title
                topic['body'] = body 
                break
        url ='/read/'+str(id)+'/'
        return redirect(url)
###################################
#삭제
@app.route('/delete/<int:id>/', methods=['POST'])
def  delete(id):
    for topic in topics:
        if id ==topic['id']:
            topics.remove(topic)
            break
    return redirect('/')

app.run(port=5001, debug=True)