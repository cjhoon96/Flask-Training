from flask import Flask, render_template, request
app = Flask(__name__)

#http://localhost/m_search/ --->> 대응컨트롤러(search_member_con)
@app.route('/m_search/')
def search_page() -> 'html':
    print("searchpage")
    return render_template("return.html")

#http://localhost/m_del/    --->> 대응컨트롤러(del_member_con)
@app.route('/m_del/')
def del_page() -> 'html':
    print("del_page")
    return("del_page")



@app.route('/')     # post 로 전송된 것들을 받음
def homepage_controller() -> 'html':
    print("Homepage")
    return render_template("m_reg.html")
  

#http://localhost/m_reg/ 라고 접속하면 이곳을 처리하게 됨
@app.route('/m_reg/', methods=['Post'])
def add_member_controller() -> 'html':
    name = request.form['m_name']
    addr = request.form['m_addr']
    tel = request.form['m_tel']
    print("from m_reg.html")    #cmd 창에 결과가 찍힘
    return render_template("return.html")      #브라우저에 결과가 찍힘

app.run(debug=True)             #app.run 은 실제로 이 앱을 작동 시킨다. debug True: 오류 메세지를 뜨게 함 False: 오류 메세지가 뜨지 않음
