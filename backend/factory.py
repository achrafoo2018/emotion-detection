from keras.models import load_model

class Factory:
    def create(self, type: str):
        filename = 'models/'
        if type == 'resnet':
            filename += 'ResNet.keras'
        elif type == 'googlenet':
            filename += 'GoogleNet.keras'
        elif filename == 'VGG16':
            filename += 'VGG16.keras'
            
        model = load_model(filename)
        return model