import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
import numpy as np
import tensorflow as tf 
from tensorflow import keras
# import util.version_checker
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader

class SaveLoad:

    train_images : object = None
    train_labels : object = None
    test_images : object = None
    test_lables : object = None

    def __init__(self):
        # util.version_checker.env_info()
        print(f'baseurl #### {baseurl}')
        self.reader = FileReader() 
        

    def hook(self):
        self.get_data()
        # self.create_model()
        # self.train_model()
        # self.save_model()
        self.load_model()

    def get_data(self):
        # (self.train_images, self.train_labels), (self.test_images, self.test_lables) \
        #     = tf.keras.datasets.mnist.load_data()
        # self.train_labels = self.train_labels[:1000]
        # self.test_lables = self.test_lables[:1000]
        # self.train_images = self.train_images[:1000].reshape(-1, 28 * 28) / 255.0
        # self.test_images = self.test_images[:1000].reshape(-1, 28 * 28) / 255.0

    def create_model(self):
        self.model = tf.keras.models.Sequential([
            keras.layers.Dense(512, activation='relu', input_shape=(784,)),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(10, activation='softmax')
        ])
        self.model.compile(optimizer = 'adam',
        loss='sparse_categorical_crossentropy', metrics = ['accuracy'])

    def train_model(self):
        checkpoint_path = 'training_1/cp.ckpt'
        cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                        save_weights_only = True,
                                                        verbose = 1 )
        self.model.fit(self.train_images, self.train_labels, epochs = 10,
        validation_data = (self.test_images, self.test_lables),
        callbacks=[cp_callback]) # 훈련단계에서 콜백전달
        self.model.load_weights(checkpoint_path) # 가중치 추가
        loss, acc = self.model.evaluate(self.test_images, self.test_lables, verbose = 2)
        # verbose 는 학습 진행상황 보여주는 여부 옵션
        '''
        verbose: Integer. 0, 1, or 2. 
        Verbosity mode. 
        0 = silent, 
        1 = progress bar, 
        2 = one line per epoch.
        '''
        print('복원된 모델의 정확도 : {:5.2f}%'.format(100 * acc))
        # 파일 이름에 에포크 번호를 포함시킵니다. 
        checkpoint_path = os.path.join(baseurl,"training_2/cp-{epoch: 04d}.ckpt")
        checkpoint_dir = os.path.dirname(checkpoint_path)
        cp_callback = tf.keras.callbacks.ModelCheckpoint(
            checkpoint_path, verbose = 1, save_weights_only = True,
            # 5번째 에포크마다 가중치를 저장합니다.
            period = 5
        )
        self.model.save_weights(checkpoint_path.format(epoch=0))
        self.model.fit(self.train_images, self.train_labels, epochs = 50, callbacks=[cp_callback],
        validation_data = (self.test_images, self.train_labels), verbose = 0)

    def save_model(self):
        # 전체 모델을 HDF5 파일로 저장합니다.
        self.model.save(os.path.join(baseurl,'saved_model/my_model.h5'))
        print('===============================')

    def load_model(self):
        self.new_model = keras.models.load_model(os.path.join(baseurl,'saved_model/my_model.h5'))
        self.new_model.summary()
        loss, acc = self.new_model.evaluate(self.test_images, self.test_lables, verbose = 2)

    def debug_model(self):
        print(f'모델 정보 : {self.model.summary()}')

if __name__ == '__main__':
    api = SaveLoad()
    api.hook()
    