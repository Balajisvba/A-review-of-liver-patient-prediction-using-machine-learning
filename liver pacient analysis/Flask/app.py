from flask import Flask, request, render_template
import pickle
import sklearn3



app=Flask(__name__)

model=pickle.load(open('liver_pridict1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/predect')
def predect():
    return render_template('predect.html')

@app.route('/prec', methods=['post'])
def pred():
    age= request.form['age']
    gender = request.form['gender']
    tb = request.form['tb']
    db = request.form['db']
    ap = request.form['ap']
    aa1 = request.form['aa']
    aa2 = request.form['aspa']
    tp = request.form['tp']
    a = request.form['albumin']
    agr = request.form['agr']
    variables = [[int(age), int(gender),float(tb),float(db),int(ap),int(aa1),int(aa2),float(tp),float(a),float(agr)]]
    print(variables)
    prediction = model.predict(variables)[0]
    if (prediction == 1):
        return render_template('submit.html', prediction='you have a liver desease problem')
    else:
        return render_template('submit.html', prediction='you do not have liver desease problem' )




if __name__=='__main__':
    app.run(debug=True)