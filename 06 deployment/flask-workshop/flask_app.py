from flask import Flask, render_template, request, send_file, abort, flash, redirect, url_for
import os, os.path
import matplotlib.pyplot as plt
import sqlite3 

upload_path = 'uploads'
images_path = 'images'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aksjdfq345rjk5643k5l67kmsdfgl;vk;js'

# -------------------------------------------------------------------------

def genplot(x, y, type='bar', filename='plot.jpg'):
    plt.bar(x, y)
    plt.xlabel('Months')
    plt.ylabel('Sales')
    #plt.show()
    plt.savefig(os.path.join(images_path, filename))
    return True

def get_db_connection():
    conn = sqlite3.connect("database.db")
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    conn.close()

    if post is None:
        abort(404)

    return post

# -------------------------------------------------------------------------

# 127.0.0.1:5000/
@app.route('/')
def index():
    return ('''
            <h1 style="color:#F05647">Welcome to Flask Experiments!</h1>
            <button>Click Me!</button>
            ''')

# 127.0.0.1:5000/calc
@app.route('/calc')
def calc():
    return render_template('calculator.html')

# 127.0.0.1:5000/upload
@app.route('/upload')
def uploadresume():
    return render_template('resume.html')

@app.route('/process', methods=["GET", "POST"])
def process():
    print(request.form)
    print(request.files['cert'])
    file = request.files['cert']
    print(file.filename)
    file.save(os.path.join(upload_path, file.filename))
    #return('<h1>Thank you! {} </h1>'.format(request.form.get('fname')))
    return render_template('summary.html', username=request.form.get('fname'), result=request.form)

# 127.0.0.1/download
@app.route('/download')
def download():
    return send_file(r"images\pinkfloyd.jpg")

# 127.0.0.1/getplot
@app.route('/getplot')
def getplot():
    genplot([0, 1, 2, 3, 4, 5], [10, 34, 45, 23, 45, 98])
    return send_file(r"images\plot.jpg")

# 127.0.0.1/pic
@app.route('/pic')
def getpic():
    return render_template('pic.html')

# 127.0.0.1/blogs
@app.route('/blogs')
def blogs():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    #print(posts)
    conn.close()
    return render_template('blogs.html', posts=posts)

# 127.0.0.1/create
@app.route('/create', methods=["GET", "POST"])
def create():
    print(request.method)
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash("Title required")
        elif not content:
            flash("Content required")
        else: 
            conn = get_db_connection()
            conn.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('blogs'))

    return render_template('create.html')
    
# 127.0.0.1/1/edit
@app.route('/<int:id>/edit', methods=["GET", "POST"])
def edit(id):
    post = get_post(id) 
    if request.method == "POST": 
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash("Title required")
        elif not content:
            flash("Content required")
        else: 
            conn = get_db_connection()
            conn.execute("UPDATE posts SET title = ?, content = ? WHERE id = ?", (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('blogs'))

    return render_template('edit.html', post=post)


if __name__ == "__main__":
    app.run(debug=True)