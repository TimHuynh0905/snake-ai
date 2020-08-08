import numpy as np
import keras 
from keras.models import Sequential
from keras.layers import Dense

import getTrainData

class neuralNetwork:
    def __init__(self):
        train_X, train_y = getTrainData.newTrainingData()
        print(np.array(train_X).shape)
        print(np.array(train_y).shape)
        self.in_dim = np.array(train_X).shape[1]
        self.out_dim = np.array(train_y).shape[1]
        self.train_X = np.array(train_X).reshape(-1,self.in_dim)
        self.train_y = np.array(train_y).reshape(-1,self.out_dim)

        self.model = Sequential()
        self.model.add(Dense(units=5, input_dim=self.in_dim))
        self.model.add(Dense(units=25, activation="relu"))
        self.model.add(Dense(units=10, activation="relu"))
        self.model.add(Dense(units=self.out_dim, activation="softmax"))
    
    def train(self):
        self.model.compile(optimizer="adam", loss="mean_squared_error", metrics=["accuracy"])
        self.model.fit(x=self.train_X, y=self.train_y, batch_size=300, epochs=10)
        self.model.save_weights("snake_ai.h5")


if __name__ == "__main__":
    nn = neuralNetwork()
    nn.train()
    snake_ai_json = nn.model.to_json()
    with open('snake_ai.json', 'w') as json_file: json_file.write(snake_ai_json)