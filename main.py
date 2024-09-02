#Импорт
from flask import Flask, render_template,request, redirect
import codecs


app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def russian():
    return render_template('russia.html')

@app.route('/eng')
def eng():
    return render_template('english.html')

@app.route('/cz')
def czech():
    return render_template('czech.html')

@app.route('/subrus', methods=['GET','POST'])
def submit_russian():
    email = request.form['email']
    comment = request.form['comment']
    with codecs.open('forms.text', 'a', 'utf-8') as f:
            f.write(email+'\n')
            f.write(comment+'\n')
            f.write("-------------"+'\n')
    return render_template('subrussian.html',
                           email=email,
                           comment=comment
                           )

@app.route('/suben', methods=['GET','POST'])
def submit_english():
    email = request.form['email']
    comment = request.form['comment']
    with codecs.open('forms.text', 'a', 'utf-8') as f:
            f.write(email+'\n')
            f.write(comment+'\n')
            f.write("-------------"+'\n')
    return render_template('subeng.html',
                           email=email,
                           comment=comment
                           )

@app.route('/subczechrep', methods=['GET','POST'])
def submit_czech():
    email = request.form['email']
    comment = request.form['comment']
    with codecs.open('forms.text', 'a', 'utf-8') as f:
            f.write(email+'\n')
            f.write(comment+'\n')
            f.write("-------------"+'\n')
    return render_template('subcz.html',
                           email=email,
                           comment=comment
                           )

if __name__ == "__main__":
    app.run(debug=True)