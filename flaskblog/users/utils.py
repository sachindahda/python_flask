import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskblog import mail
from flask import current_app


def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _,f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex+f_ext
    print(picture_fn)
    picture_path=os.path.join(current_app.root_path,'static/profile_pics/'+picture_fn)
    print(picture_path)
    output_size=(125,125)
    i =Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token=user.get_reset_token()
    msg=Message('Password Reset Request',sender='sachin1324982@yopmail.com',recipients=[
        user.email
    ])
    msg.body=f''' To Reset Your Password, visit the following link:
{url_for('users.reset_token',token=token,_external=True)}

If you did not make this request, ignore this.
 '''
    mail.send(msg)

