from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

#---------------------------
#drop database flaskmysql
#create database flaskmysql
#---------------------------

#----------usuario----------
#--------------------------
class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(15), nullable=False)
    nombres = db.Column(db.String(30), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(300), nullable=True)
    cellphone = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    isadmin = db.Column(db.Boolean, default=False)
    avatar = db.Column(db.String(500), nullable=True)
    estado = db.Column(db.String(1), nullable=True)
    createdat = db.Column(db.String(11), nullable=True) 

    def onGetSetPassword(self, password):
        self.password = generate_password_hash(password)

    def onGetCheckPassword(self, password):
        return check_password_hash(self.password, password)

    def __init__(self, cedula, nombres, apellidos, username, email, password, cellphone, phone, isadmin, avatar, estado, createdat):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.username = username
        self.email = email
        self.password = password
        self.cellphone = cellphone
        self.phone = phone
        self.isadmin = isadmin
        self.avatar = avatar
        self.estado = estado
        self.createdat = createdat

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','cedula', 'nombres', 'apellidos', 'username', 'email', 'password', 'cellphone', 'phone', 'isadmin', 'avatar', 'estado', 'createdat')

userSchema = UserSchema()
usersSchema = UserSchema(many=True)



#-----------------------------
#----------Categoria----------
#-----------------------------.

class Categoria(db.Model):
    __tablename__='categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    image = db.Column(db.String(300), nullable=False)
    detalle = db.Column(db.String(500), nullable=False)
    estado = db.Column(db.String(1), nullable=True)
    createdat = db.Column(db.String(11), nullable=True) 

    def __init__(self, nombre, image, detalle, estado, createdat):
        self.nombre = nombre
        self.image = image
        self.detalle = detalle
        self.estado = estado
        self.createdat = createdat

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'image', 'detalle' , 'estado', 'createdat')

categoriaSchema = CategoriaSchema()
categoriaSchema = CategoriaSchema(many=True)

#---------------------------
#------------ Caso----------
#--------------------------

class Caso(db.Model):
    __tablename__='casos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    image = db.Column(db.String(300), nullable=False)
    detalle = db.Column(db.String(500), nullable=False)
    estado = db.Column(db.String(1), nullable=True)
    createdat = db.Column(db.String(11), nullable=True) 
    categoriaid = db.Column(db.Integer, db.ForeignKey('categorias.id',ondelete='CASCADE'), nullable=False)
    categoria = db.relationship('Categoria',backref=db.backref('casos',lazy=True))

    def __init__(self, nombre, image, detalle, estado, createdat, categoriaid):
        self.nombre = nombre
        self.image = image
        self.detalle = detalle
        self.estado = estado
        self.createdat = createdat
        self.categoriaid = categoriaid

class CasoSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'image', 'detalle' , 'estado', 'createdat', 'categoriaid')

casoSchema = CasoSchema()
casoSchema = CasoSchema(many=True)


#-----------------------------
#----------usercaso----------
#-----------------------------.

class Usercaso(db.Model):
    __tablename__='usercasos'

    id = db.Column(db.Integer, primary_key=True)
    avance = db.Column(db.String(3), nullable=False)
    estado = db.Column(db.String(1), nullable=True)
    createdat = db.Column(db.String(11), nullable=True) 
    userid = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'), nullable=False)
    user = db.relationship('User',backref=db.backref('usercasos',lazy=True))
    casoid = db.Column(db.Integer, db.ForeignKey('casos.id',ondelete='CASCADE'), nullable=False)
    caso = db.relationship('Caso',backref=db.backref('usercasos',lazy=True))

    def __init__(self, avance, estado, createdat, userid, casoid):
        self.avance = avance
        self.estado = estado
        self.createdat = createdat
        self.userid = userid
        self.casoid = casoid

class UsercasoSchema(ma.Schema):
    class Meta:
        fields = ('id','avance', 'estado', 'createdat', 'userid', 'casoid')

usercasoSchema = UsercasoSchema()
usercasoSchema = UsercasoSchema(many=True)

class Formulario(db.Model):
    __tablename__='formulario'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(250), nullable=False)
    detalle = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    estado = db.Column(db.String(1), nullable=True)
    createdat = db.Column(db.String(11), nullable=True) 
    userid = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'), nullable=False)
    user = db.relationship('User',backref=db.backref('formulario',lazy=True))

    def __init__(self, nombre, image, detalle, url, estado, createdat, userid):
        self.nombre = nombre
        self.image = image
        self.detalle = detalle
        self.url = url
        self.estado = estado
        self.createdat = createdat
        self.userid = userid

class FormularioSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','image','detalle','url', 'estado', 'createdat', 'userid')

formularioSchema = FormularioSchema()
formularioSchema = FormularioSchema(many=True)