from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return HOME_HTML

HOME_HTML = """
    <html><body>
         <h2>Program to find prime numbers less than equal to a given number</h2>
         
         <form action="/greet">
             Enter a number  <input type='text' name='n'><br>
             <input type='submit' value='Continue'>
         </form>
     </body></html>"""

@app.route('/greet')
def greet():
    n = request.args.get('n', '')
    n=n.strip()
    n=int(n)
    def p(x):
        l=list()
        if x<=1:
            pass
        else:
            for i in range(2,x+1):
                f=1
                for j in range(2,(int(i**0.5)+1)):
                    if (i%j)==0:
                        f=0
                        break
                if(f==1):
                    l.append(i)
        return l
    res=p(n)

    return GREET_HTML.format(n, p(n))

GREET_HTML = """
    <html><body>
         <h2>Prime numbers till {0} are:</h2>
         {1}
    </body></html>
     """

if __name__ == "__main__":
    app.run(host="localhost", debug=True)