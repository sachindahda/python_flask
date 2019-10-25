import os
import secrets
from PIL import Image
from flask import    request,render_template, url_for,flash,redirect,abort
from flaskblog.forms import RegistrationForm, LoginForm ,UpdateAccountForm,PostForm,RequestResetForm,ResetPasswordForm
from flaskblog.models import User,Post
from flaskblog import app,db,bcrypt,mail
from flask_login import login_user,current_user,logout_user,login_required
from flask_mail import Message

