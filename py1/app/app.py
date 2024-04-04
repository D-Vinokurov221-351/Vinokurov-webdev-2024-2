import random
from flask import Flask, render_template
from faker import Faker
from flask import request
from flask import make_response
from flask import redirect, url_for, request, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

fake = Faker()

app = Flask(__name__)
application = app
app.secret_key = 'Secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = {'user': {'password': 'qwerty'}}
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

images_ids = ['7d4e9175-95ea-4c5f-8be5-92a6b708bb3c',
              '2d2ab7df-cdbc-48a8-a936-35bba702def5',
              '6e12f3de-d5fd-4ebb-855b-8cbc485278b7',
              'afc2cfe7-5cac-4b80-9b9a-d5c65ef0c728',
              'cab5b7f2-774e-4884-a200-0c0180fa777f']

def generate_comments(replies=True):
    comments = []
    for i in range(random.randint(1, 3)):
        comment = { 'author': fake.name(), 'text': fake.text() }
        if replies:
            comment['replies'] = generate_comments(replies=False)
        comments.append(comment)
    return comments

def generate_post(i):
    return {
        'title': 'Заголовок поста',
        'text': fake.paragraph(nb_sentences=100),
        'author': fake.name(),
        'date': fake.date_time_between(start_date='-2y', end_date='now'),
        'image_id': f'{images_ids[i]}.jpg',
        'comments': generate_comments()
    }

posts_list = sorted([generate_post(i) for i in range(5)], key=lambda p: p['date'], reverse=True)

@app.route('/')
def index1lb():
    return render_template('index1lb.html')

@app.route('/2lb')
def index2lb():
    return render_template('index2lb.html')

@app.route('/Home')
def indexHome():
    return render_template('indexHome.html')

@app.route('/visits')
def visits():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return 'Number of visits: {}'.format(session['visits'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = True if 'remember' in request.form else False

        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user, remember=remember)
            return redirect(url_for('secret'))
        else:
            return 'Invalid username or password'

    return render_template('login.html')

@app.route('/secret')
#@login_required
def secret():
    return render_template('secret.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('indexHome'))

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

@app.route('/url')
def url():
    return render_template('url.html', title="Параметры URL", )

@app.route('/posts')
def posts():
    return render_template('posts.html', title='Посты', posts=posts_list)

@app.route('/posts/<int:index>')
def post(index):
    p = posts_list[index]
    return render_template('post.html', title=p['title'], post=p)

@app.route('/about')
def about():
    return render_template('about.html', title='Об авторе')

@app.route('/forms', methods=['GET', 'POST'])
def forms():
    # if request.method == "POST"
    return render_template('forms.html', title="Параметры формы")

@app.route('/headers')
def headers():
    return render_template('headers.html', title="Заголовки")


@app.route('/cookies')
def cookies():
    resp = make_response(render_template('cookies.html', title="Куки"))
    if 'user' in request.cookies:
        resp.delete_cookie('user')
    else:
        resp.set_cookie('user', 'admin')
    return resp

@app.route("/phoneNumber", methods=["POST", "GET"])
def phoneNumber():
    if request.method == 'POST':
        phone = request.form["phone"]

        phoneNumbers = re.findall("\d{1}", phone)
        if not phoneNumbers:
            phoneNumbers.append("")

        error = ""
        if not all([symbol in [" ", "(", ")", "-", ".", "+", *list(map(str, list(range(10))))] for symbol in phone]):
            error = "Недопустимый ввод. В номере телефона встречаются недопустимые символы."
        elif phoneNumbers[0] in ["7", "8"] and len(phoneNumbers) != 11:
            error = "Недопустимый ввод. Неверное количество цифр."
        elif phoneNumbers[0] not in ["7", "8"] and len(phoneNumbers) != 10:
            error = "Недопустимый ввод. Неверное количество цифр."

        if error:
            return render_template("phoneNumber.html", title="Проверка номера телефона", phone=error)

        if len(phoneNumbers) == 10:
            phoneNumbers.insert(0, "8")

        return render_template("phoneNumber.html", title="Проверка номера телефона", phone="8-{1}{2}{3}-{4}{5}{6}-{7}{8}-{9}{10}".format(*phoneNumbers))
    else:
        return render_template("phoneNumber.html", title="Проверка номера телефона")
