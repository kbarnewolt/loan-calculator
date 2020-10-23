from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mnthlyPmt', methods=['POST'])
def mnthlyPmt():
    if request.method == 'POST':
        form = request.form
        loanAmt = float(form['loanAmt'])
        lengthOfLoan= float(form['lengthOfLoan'])
        intRate= float(form['intRate'])

        mySum = loanAmt + lengthOfLoan + intRate

        print("******************")
        print(loanAmt)
        print(lengthOfLoan)
        print(intRate)
        print (mySum)
        #return render_template('index.html', display=calc, pageTitle='My Calculator')
        
    return render_template('monthlyPayment.html')

if __name__ == '__main__':
    app.run(debug=True)