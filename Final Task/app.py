from flask import Flask, render_template, request, redirect, session, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DATABASE = 'tasks.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    if 'db' in g:
        g.db.close()

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect('/login')
    db = get_db()
    tasks = db.execute('SELECT * FROM tasks WHERE user_id = ?', (session['user_id'],)).fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/login', methods=['GET', 'POST'])
def login():
    db = get_db()
    if request.method == 'POST':
        username = request.form['username']
        user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        if user:
            session['user_id'] = user['id']
            return redirect('/')
        db.execute('INSERT INTO users (username) VALUES (?)', (username,))
        db.commit()
        session['user_id'] = db.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone()['id']
        return redirect('/')
    return render_template('login.html')

@app.route('/add', methods=['POST'])
def add():
    if 'user_id' in session:
        task = request.form['task']
        db = get_db()
        db.execute('INSERT INTO tasks (user_id, task) VALUES (?, ?)', (session['user_id'], task))
        db.commit()
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    db = get_db()
    db.execute('DELETE FROM tasks WHERE id = ? AND user_id = ?', (task_id, session['user_id']))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
