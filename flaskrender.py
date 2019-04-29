from flask import Flask, request, render_template
from GNBsem1 import gnbsem1
from GNBsem2 import gnbsem2
from GNBsub1 import gnbsub1
from GNBsub2 import gnbsub2
from GNBsub3 import gnbsub3
from GNBsub4 import gnbsub4
from GNBsub5 import gnbsub5
from GNBsub6 import gnbsub6
from GNBsub7 import gnbsub7
from GNBsub8 import gnbsub8
from GNBsub9 import gnbsub9
from GNBsub10 import gnbsub10
from GNBsub11 import gnbsub11
from GNBsub12 import gnbsub12

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('index.html')


@app.route('/x')
def my_form_sem():
    return render_template('semop.html')


@app.route('/x/a')
def my_form_a():
    return render_template('inputse1.html')


@app.route('/x/b')
def my_form_b():
    return render_template('inputse2.html')


@app.route('/y')
def my_form_sub():
    return render_template('inputsub.html')


@app.route('/x/getsem1', methods=['POST'])
def my_sem1_result_post():
    text1 = int(request.form['user_Gender'])
    text2 = int(request.form['user_Income'])
    text3 = int(request.form['HS_percent'])
    text4 = int(request.form['HS_Stream'])
    text5 = int(request.form['PCM_percent'])
    text6 = int(request.form['entrance_markp'])
    text7 = int(request.form['user_Quota'])
    text8 = int(request.form['user_Dist'])
    text9 = int(request.form['user_s1c1i'])
    text10 =int(request.form['user_s1c1a'])
    text11 = int(request.form['user_s1c2i'])
    text12 = int(request.form['user_s1c2a'])
    text13 = int(request.form['user_s1c3i'])
    text14 = int(request.form['user_s1c3a'])
    text15 = int(request.form['user_s1c4i'])
    text16 = int(request.form['user_s1c4a'])
    text17 = int(request.form['user_s1c5i'])
    text18 = int(request.form['user_s1c5a'])
    text19 = int(request.form['user_s1c6i'])
    text20 = int(request.form['user_s1c6a'])


    x = [[text1, text2, text3, text4, text5, text6, text7, text8, text9, text10,
          text11, text12, text13, text14, text15, text16, text17, text18, text19, text20]]
    a = gnbsem1(x)
    return render_template('resultsem.html', output=a)


@app.route('/x/getsem2', methods=['POST'])
def my_sem2_result_post():
    text1 = int(request.form['user_Gender'])
    text2 = int(request.form['user_Income'])
    text3 = int(request.form['HS_percent'])
    text4 = int(request.form['HS_Stream'])
    text5 = int(request.form['PCM_percent'])
    text6 = int(request.form['entrance_markp'])
    text7 = int(request.form['user_Quota'])
    text8 = int(request.form['user_Dist'])
    text9 = int(request.form['user_s2c1i'])
    text10 = int(request.form['user_s2c1a'])
    text11 = int(request.form['user_s2c2i'])
    text12 = int(request.form['user_s2c2a'])
    text13 = int(request.form['user_s2c3i'])
    text14 = int(request.form['user_s2c3a'])
    text15 = int(request.form['user_s2c4i'])
    text16 = int(request.form['user_s2c4a'])
    text17 = int(request.form['user_s2c5i'])
    text18 = int(request.form['user_s2c5a'])
    text19 = int(request.form['user_s2c6i'])
    text20 = int(request.form['user_s2c6a'])

    x = [[text1, text2, text3, text4, text5, text6, text7, text8, text9, text10,
          text11, text12, text13, text14, text15, text16, text17, text18, text19,text20]]
    a = gnbsem2(x)
    return render_template('resultsem.html', output=a)


@app.route('/getsub', methods=['POST'])
def my_sub1_result_post():
    text1 = int(request.form['user_Gender'])
    text2 = int(request.form['user_Income'])
    text3 = int(request.form['HS_percent'])
    text4 = int(request.form['HS_Stream'])
    text5 = int(request.form['PCM_percent'])
    text6 = int(request.form['entrance_markp'])
    text7 = int(request.form['user_Quota'])
    text8 = int(request.form['user_Dist'])
    text9 = int(request.form['internal'])
    text10= int(request.form['attendence'])
    sub = request.form['sub']
    x = [[text1, text2, text3, text4, text5, text6, text7, text8, text9,text10]]
    if sub == '1':
               out = gnbsub1(x)
    elif sub == '2':
             out = gnbsub2(x)
    elif sub == '3':
             out = gnbsub3(x)
    elif sub == '4':
             out = gnbsub4(x)
    elif sub == '5':
             out = gnbsub5(x)
    elif sub == '6':
             out = gnbsub6(x)
    elif sub == '7':
             out = gnbsub7(x)
    elif sub == '8':
             out = gnbsub8(x)
    elif sub == '9':
             out = gnbsub9(x)
    elif sub == '10':
             out = gnbsub10(x)
    elif sub == '11':
             out = gnbsub11(x)
    elif sub == '12':
             out = gnbsub12(x)
    if out=='Bad':
        info="You need to work hard"
    else:
        info="continue your hardwork"
   
    return render_template('resultsub.html',output=out,info=info)


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=8080)
