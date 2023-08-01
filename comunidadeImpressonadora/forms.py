from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeImpressonadora.models import Usuario
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed


class FormCriarConta(FlaskForm):
    username = StringField("Nome do Usuário", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6,20)])
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_submit_confirmacao = SubmitField("Criar Conta")


    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("email já cadastrado- cadastre com outro email ou faça login para continuar!...")


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6,20)])
    lembrar_dados = BooleanField("Lembrar Dados de Acesso")
    botao_submit_login = SubmitField("Fazer Login")


class FormEditarPerfil(FlaskForm):
    username = StringField("Nome do Usuário", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    foto_perfil = FileField("Atualizar Foto de Perfil", validators=[FileAllowed(["jpg", "png"])])
    curso_excel = BooleanField("excel_impressionador")
    curso_vba = BooleanField("vba_impressionador")
    curso_python = BooleanField("python_impressionador")
    curso_powerbi = BooleanField("powerbi_impressionador")
    curso_ppt = BooleanField("ppt_impressionador")
    curso_sql = BooleanField("sql_impressionador")
    botao_confirmar_edicao = SubmitField("Confirmar Edição")


    def validate_email(self, email):
        # verificar se a pessoa mudou de email
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError("Já existe um usuário cadastrado com esse email. cadastre outro email!...")


class FormCriarPost(FlaskForm):
    titulo = StringField("Título do Post", validators=[DataRequired(), Length(2,140)])
    corpo= TextAreaField("Escreva Seu Post Aqui", validators=[DataRequired()])
    botao_submit = SubmitField("Criar Post")


