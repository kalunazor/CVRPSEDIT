# Import the required libraries
import cv2
from keras.models import load_model
import numpy as np
import random
import time

class CameraRPS:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors', 'nothing']
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        #Initialize the user score and the computer score, set at initial values of 0. 
        self.user_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        comp_choice = random.choice(self.choices[0:3])
        return comp_choice
        
    def get_prediction(self):
        stop_time = time.time() + 2
        while stop_time > time.time(): 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            max_index = np.argmax(prediction[0])
            user_choice = self.choices[max_index]
            print(user_choice)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Press q to close the window
        return user_choice
    #increase user score by one whenever user wins
    #increase computer score by one whenever computer wins
    def get_winner(self):
        computer_choice = self.get_computer_choice()
        user_choice = self.get_prediction()
        if user_choice == 'nothing':
            print('You have made an invalid choice')
        elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
            print('You won')
            self.user_wins += 1
        else:
            print('Whoops, you Lost!')
            self.computer_wins += 1

def play_game():
    game = CameraRPS()
    while game.user_wins < 3 and game.computer_wins < 3:
        game.get_winner()
        if game.user_wins == 3:
            print("User Won!")
            break
        elif game.computer_wins == 3:
            print("You Lost!")
            break

        # After the loop release the cap object
    game.cap.release()
        # Destroy all the windows
    cv2.destroyAllWindows()

play_game()
