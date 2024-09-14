from random import randint
from flask import Flask, session, redirect, url_for, request, render_template
import os
from main_db_controll import db

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def index():
   max_quiz = 3
   session['quiz'] = randint(1, max_quiz)

   session['last_question'] = 0
   return render_template('main.html')
# f'''<a href="/test">Тест №{session['quiz']}</a>'''



def test():
   if request.method == 'POST':
      # print(request.form.get('first_name'))
      file = request.files['file']
      if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
      obj = request.form.to_dict()
      print(obj)
      db.add_data(obj, file.filename)
      info = db.get_data()
      print(info)
      return render_template('answer.html', array=info)
   # obj['first_name'][0]
   # request.form.get('first_name')
   return 'Получил не POST запрос'

def result():
   return "that's all folks!"



# Створюємо об'єкт веб-програми:
app = Flask(__name__)  
app.add_url_rule('/', 'index', index)   # створює правило для URL '/'
app.add_url_rule('/test', 'test', test, methods=['POST']) # створює правило для URL '/test'
app.add_url_rule('/result', 'result', result) # створює правило для URL '/test'
app.config['SECRET_KEY'] = 'secret_key'

if __name__ == '__main__':
   # Запускаємо веб-сервер:
   app.run(debug=True)
