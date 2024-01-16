from keras.models import load_model

class Factory:
    def create(self, type: str):
        filename = 'models/'
        if type == 'resnet':
            filename += 'ResNet.h5'
        elif type == 'googlenet':
            filename += 'GoogleNet.h5'
        elif filename == 'VGG16':
            filename += 'VGG16.h5'
        elif type == 'custom':
            filename += 'Custom.h5'
            
        model = load_model(filename)
        return model