from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json

import os
os.environ["TF_CCP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf
from . import imggen

generator = tf.keras.models.load_model('model_Generator')


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        if request.form.get('ImageGenButton') == 'Generate Image':
            print("working")
            imggen.generateImage(generator, "test")
            request.method = "PUT"
            return redirect(url_for('views.home'))

    return render_template("home.html", user=current_user)
    #return redirect(url_for('views.home'))

