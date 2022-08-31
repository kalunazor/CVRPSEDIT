# Import the required libraries
import cv2
from keras.models import load_model
import numpy as np
import random


class CameraRPS:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors', 'nothing']
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        #Initialize the user score and the computer score.
    
    def get_computer_choice(self):
        comp_choice = random.choice(self.choices[0:3])
        return comp_choice
          
    def get_prediction(self):
        prediction = self.model.predict(self.data)
        print(prediction)
        max_index = np.argmax(prediction[0])
        user_choice = self.choices[max_index]
        print(user_choice)
        
        # Press q to close the window
        return user_choice

    def get_winner(self):
        self.get_computer_choice()
        self.get_prediction()
        
        # Pass user_choice and comp_choice as parameters to the get_winner method
        user_choice = self

def play_game():
    game = CameraRPS()
    game.model
    game.cap

    while True: 
        image = game.data
        print(image.shape)
        ret, frame = game.cap.read()
        game.get_prediction()

        # TODO: THE IMAGE IS EMPTY, HOW DO I FIX THIS?
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        game.data[0] = normalized_image
        cv2.imshow('frame', frame)
        game.get_computer_choice()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # After the loop release the cap object
        game.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

play_game()
