
from tensorflow.keras.utils import img_to_array, load_img
import numpy as np
from factory import Factory

def classify(imgname: str, model_name: str) -> (str, int):
    factory = Factory()
    
    img_path = f"uploads/{imgname}" 
    img = load_img(img_path, target_size=(48, 48))

    
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0


    loaded_model = factory.create(model_name)
    predictions = loaded_model.predict(img_array)
    class_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']  

    predicted_class = class_labels[np.argmax(predictions)]
    confidence = np.max(predictions)
    return (predicted_class, confidence)
