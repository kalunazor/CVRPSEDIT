# Import the required libraries
import cv2
from keras.models import load_model
import numpy as np
import random


class CameraRPS:
    def __init__(self):
        pass
        #Initialize the user score and the computer score.
    
    def get_computer_choice(self):
        pass
        get_user_choice = input("get_user_choice 'R' for rock, 'P' for paper, 'S' for scissors\n")
        get_user_choice = get_user_choice.upper()

        get_computer_choice = random.choice(['R', 'P', 'S'])

        if get_user_choice == get_computer_choice:
            return (0, get_user_choice, get_computer_choice)

        if get_winner(get_user_choice, get_computer_choice):
            return (1, get_user_choice, get_computer_choice)

        return (-1, get_user_choice, get_computer_choice)

    def get_prediction(self):
        pass
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction[0][0])
            print(prediction[0][1])
            print(prediction[0][2])
            print(prediction[0][3])
            if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    def get_winner(self):
        pass
        if (user_choice == 'R' and computer_choice == 'S') or (user_choice == 'S' and computer_choice == 'P') or (user_choice == 'P' and computer_choice == 'R'):
            return True
        return False

def play_game():
    game = CameraRPS()
    game.get_computer_choice()
    game.get_prediction()
    
