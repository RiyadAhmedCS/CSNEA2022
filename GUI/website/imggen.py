import os
os.environ["TF_CCP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

generator = tf.keras.models.load_model('model_Generator')

def generateImage(generator, name = "image"):
    print("Generating")
    latent_dim = 128

    opt_gen = keras.optimizers.Adam(1e-4)
    opt_disc = keras.optimizers.Adam(1e-4)
    loss_fn = keras.losses.BinaryCrossentropy()

    random_latent_vectors = tf.random.normal(shape=(128, latent_dim))
    fake = generator(random_latent_vectors)

    img = keras.preprocessing.image.array_to_img(fake[0])
    img.save("website\\static\\" + str(name) + ".png")


