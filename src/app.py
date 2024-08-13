from flask import Flask, render_template, request, jsonify,redirect, url_for, flash
import mysql.connector
from config import config
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.middleware.proxy_fix import ProxyFix

# Models
from models.ModelUser import ModelUser

# Entities
from models.entities.User import User

# External code
from py_scripts.Votes import Votes
from py_scripts.Wallet import Wallet
from py_scripts.Enrollments import Enrollments



app = Flask(__name__)
app.config.from_object(config['development'])

db = MySQL(app)
login_manager_app = LoginManager(app)

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user:
        if current_user.is_authenticated:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))
    if request.method=='POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña incorrecta")
        else:
            flash("Usuario no encontrado")
        
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/register', methods=['GET','POST'])
def register():
    
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        fullname = request.form['fullname']
        email = request.form['email']
        mobile_number = request.form['mobile_number']
        drepa_coins = 50
        
        
        try:
            mobile_number=int(mobile_number)
        except Exception as ex:
            print(ex)
            flash('Ingrese un numero de telefono valido')
        
        
        if ModelUser.check_existing_username(db, username):
            flash('El nombre de usuario que elegiste')
            flash('no está disponible')
            return redirect('/register')
        
        elif username.isdigit():
            flash('El usuario no puede ser solo numeros')
            
        elif " " in username:
            flash("El nombre de usuario")
            flash("no puede contener espacios")
            return redirect(url_for('register'))
        
        elif len(username) > 10 or len(username) < 3:
            flash('El nombre de usuario debe tener')
            flash('entre 3 y 10 caracteres')
            
        
        elif len(password) < 6:
            flash("Ingrese una contraseña")
            flash("de al menos 6 caracteres")
            return redirect(url_for('register'))
        
        else:
            hashed_password = User.create_hashed_password(password)
            ModelUser.create_new_user(db, username, hashed_password, fullname, email, mobile_number, drepa_coins)
            return redirect(url_for('succesfull_register'))
        
        
        
        
    return render_template('register.html')
        
            
@app.route('/verify_mobile_number', methods=['GET','POST'])
def verify_mobile_number():
    return render_template('auth/verify_mobile_number.html')
            

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/wallet')
@login_required
def wallet():
    username = current_user.username
    drepa_coins_tuple = Wallet.check_drepa_coins(db, username)
    drepa_coins = drepa_coins_tuple[0]
    return render_template('wallet.html', drepa_coins=drepa_coins)


@app.route('/votaciones',  methods=['GET','POST'])
@login_required
def votaciones():
    song_checkboxes = {
    "cancion1": False,
    "cancion2": False,
    "cancion3": False,
    "cancion4": False,
    "cancion5": False,
    "cancion6": False,
    "cancion7": False,
    "cancion8": False,
    "cancion9": False,
    "cancion10": False,
    "cancion11": False,
    "cancion12": False,
    "cancion13": False,
    "cancion14": False,
    "cancion15": False,
    "cancion16": False,
    "cancion17": False,
    "cancion18": False,
    "cancion19": False,
    "cancion20": False,
    "cancion21": False,
    "cancion22": False,
    "cancion23": False,
    "cancion24": False,
    "cancion25": False,
    "cancion26": False,
    "cancion27": False,
    "cancion28": False,
    "cancion29": False,
    "cancion30": False,
    "cancion31": False,
    "cancion32": False,
    "cancion33": False,
    "cancion34": False,
    "cancion35": False,
    "cancion36": False,
    "cancion37": False,
    "cancion38": False,
    "cancion39": False,
    "cancion40": False,
}
    username = current_user.username
    form_button = "Votar"
    user_voted = Votes.check_user_vote(db,username)
    if user_voted == True:
        form_button = "Actualizar voto"
        voted_songs = Votes.fetch_user_votes(db,username)
        for song in voted_songs:
            song_checkboxes[song] = True
        
        if request.method == 'POST':
            voted_songs_post = [song for song, vote in request.form.items() if vote == 'on']

            deselected_songs = [song for song in voted_songs if song not in voted_songs_post]

            for song in deselected_songs:
                Votes.delete_user_vote(db, song, username)

            for song in voted_songs_post:
                if song not in voted_songs:
                    Votes.add_song_vote(db, song, username)
            return redirect(url_for('resultado_votaciones'))
            
            
    else:
        if request.method=='POST':
            voted_songs = request.form.to_dict()
            for song, vote in voted_songs.items():
                if vote == 'on':
                    Votes.add_song_vote(db,song,username)
            return redirect(url_for('resultado_votaciones'))
                
        
        
    return render_template('votaciones.html', form_button=form_button, song_checkboxes=song_checkboxes)

@app.route('/resultado_votaciones',methods=['GET'])
@login_required
def resultado_votaciones():
    return render_template('resultado_votaciones.html')

@app.route('/dl4kas3ksdLasdk3Fdl4%$3dlfsdlskgf$5kl34l5SgDFgsd4',methods=['GET'])
@login_required
def exchange_drepacoins():
    return "Prueba"


@app.route('/lista_de_canciones')
@login_required
def lista_de_canciones():
    return render_template('lista_de_canciones.html')

@app.route('/enrollments', methods=['GET'])
@login_required
def enrollments():
    return render_template('enrollments.html')


@app.route('/enrollment_data', methods=['GET'])
def enrollment_data():
    available_instruments = Enrollments.filter_instruments(db)
    available_songs = Enrollments.filter_songs(db,available_instruments)
    
    return jsonify({'available_instruments': available_instruments, 'available_songs': available_songs})

@app.route('/enrollment_form', methods=['GET', 'POST'])
def enrollment_form():
    username = current_user.username
    song = request.form.get('song')
    instrument = request.form.get('instrument')
    
    enrollment = Enrollments.enroll_user(db, song, instrument, username)
    
    if enrollment != "succes":
        print("error en la inscripcion")
    
    return render_template('enrollments.html')



@app.route('/tabla')
@login_required
def tabla():
    return render_template('tabla.html')


@app.route('/mis_datos')
@login_required
def mis_datos():
    return render_template('mis_datos.html')

@app.route('/update_mis_datos')
@login_required
def update_mis_datos():
    return render_template('mis_datos.html')

@app.route('/succesfull_register')
def succesfull_register():
    return render_template('succesfull_register.html')


@app.route('/fetch_votes', methods=['GET'])
def fetch_votes():
    votes_results = Votes.votes_counter(db)
    return votes_results

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>"


app.register_error_handler(401, status_401)
app.register_error_handler(404, status_404)


if __name__=='__main__':
    app.run(host="0.0.0.0")