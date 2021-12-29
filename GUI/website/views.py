import os
import tensorflow as tf
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from random import randint

from . import db
from . import imggen
from . import capgen

os.environ["TF_CCP_MIN_LOG_LEVEL"] = "3"
generator = tf.keras.models.load_model('model_Generator')

tokenizer = AutoTokenizer.from_pretrained("./gpt2-trained")
model = AutoModelForCausalLM.from_pretrained("./gpt2-trained")
gpt2_finetune = pipeline('text-generation', model=model, tokenizer=tokenizer)


views = Blueprint('views', __name__)
caption = ""

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    f = open("website\\static\\quote.txt", "r")
    if request.method == 'POST':
        if request.form.get('ImageGenButton') == 'Generate Image':
            print("working")
            imggen.generateImage(generator, "test")
            return redirect(url_for('views.home'))
        if request.form.get('CaptionGenButton') == 'Generate Caption':
            print("working caption")
            f = open("website\\static\\quote.txt", "w")
            caption = capgen.generatequote(gpt2_finetune)
            f.write(caption)
            return redirect(url_for('views.home'))
        if request.form.get('BothGenButton') == 'Generate Both':
            print("working both")
            imggen.generateImage(generator, "test")
            f = open("website\\static\\quote.txt", "w")
            caption = capgen.generatequote(gpt2_finetune)
            f.write(caption)
            return redirect(url_for('views.home'))

    return render_template("home.html", user=current_user, quote=f.readlines()[0])
    #return redirect(url_for('views.home'))

