import requests
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def calculate():
    d=fun()
    return render_template("index.html",d=d)


li=[]

def fun():
    if request.method == 'POST':
            if request.form.get('1') == '1':
                li.append("1")
            elif  request.form.get('2') == '2':
                li.append("2")
            elif  request.form.get('3') == '3':
                li.append("3")
            elif  request.form.get('4') == '4':
                li.append("4")
            elif  request.form.get('5') == '5':
                li.append("5")
            elif  request.form.get('6') == '6':
                li.append("6")
            elif  request.form.get('7') == '7':
                li.append("7")
            elif  request.form.get('8') == '8':
                li.append("8")
                
            elif  request.form.get('9') == '9':
                li.append("9")
            elif  request.form.get('0') == '0':
                li.append("0")
            elif  request.form.get('c') == 'c':
                li.clear()
            
            elif  request.form.get('⌫') == '⌫':
                if len(li)==0:
                     li.append("invalid")
                li.pop()

            elif  request.form.get('+') == '+':
                li.append("+")
            elif  request.form.get('-') == '-':
                li.append("-")
            elif  request.form.get('×') == '×':
                li.append("*")
            elif  request.form.get('÷') == '÷':
                li.append("/")
            elif  request.form.get('.') == '.':
                li.append(".")    
            elif  request.form.get('=') == '=':
                try:
                    b="".join(li)
                    k=eval(b)
                    k=str(k)
                    li.clear()
                    li.append(k)
                except:
                    li.clear()
                    li.append("invalid")
            else:
                # pass # unknown
                return render_template("gg.html")
    elif request.method == 'GET':
            # return render_template("index.html")
        print("No Post Back Call")
    return "".join(li)
if __name__=='__main':
    app.run(debug=True)
