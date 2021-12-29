import os
os.environ["TF_CCP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

generator = tf.keras.models.load_model('model_Generator')

from PIL import Image
from PIL import ImageFilter

def generateImage(generator, name = "image"):
    print("Generating")
    latent_dim = 128

    opt_gen = keras.optimizers.Adam(1e-4)
    opt_disc = keras.optimizers.Adam(1e-4)
    loss_fn = keras.losses.BinaryCrossentropy()

    for i in range(0,4):

        random_latent_vectors = tf.random.normal(shape=(128, latent_dim))
        fake = generator(random_latent_vectors)

        img = keras.preprocessing.image.array_to_img(fake[0])
        img.save("website\\static\\" + str(name) + str(i) + ".png")

    image0 = Image.open("website\\static\\" + str(name) + "0.png")
    image1 = Image.open("website\\static\\" + str(name) + "1.png")
    image2 = Image.open("website\\static\\" + str(name) + "2.png")
    image3 = Image.open("website\\static\\" + str(name) + "3.png")

    new_image = Image.new('RGB',(128, 128), (250,250,250))
    new_image.paste(image0,(0,0))
    new_image.paste(image1,(64,0))
    new_image.paste(image2,(0,64))
    new_image.paste(image3,(64,64))
    new_image = new_image.filter(ImageFilter.GaussianBlur(radius=2))
    new_image.save("website\\static\\" + str(name) +  ".png","PNG")


