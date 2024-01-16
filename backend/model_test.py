
from tensorflow.keras.utils import img_to_array, load_img
import numpy as np
from factory import Factory

def classify(imgname: str, model_name: str) -> (str, int):
    factory = Factory()
    
    img_path = f"uploads/{imgname}"     
    
    # Load the image in grayscale mode (this will result in one channel)
    img = load_img(img_path, color_mode="grayscale", target_size=(48, 48))
    
    # Convert the image to a numpy array
    img_array = img_to_array(img)
    
    # Reshape the image to add a batch dimension, since Keras expects this shape (batch_size, height, width, channels)
    img_array = img_array.reshape((1, 48, 48, 1))
    
    # Normalize the image
    img_array = img_array.astype('float32')
    img_array = img_array / 255.0


    loaded_model = factory.create(model_name)
    predictions = loaded_model.predict(img_array)
    class_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']  

    predicted_class = class_labels[np.argmax(predictions)]
    confidence = np.max(predictions)
    return (predicted_class, confidence)
