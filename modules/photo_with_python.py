import datetime
import cv2


def photo_with_python():
    t = datetime.datetime.now()
#     Taking a video from the webcam 
    camera = cv2.VideoCapture(0)
#     Taking first 20 frames of the video
    for i in range(20):
        return_value, image = camera.read()
#     Using 20th frame as the picture and now saving the image as the time in seconds,minute,hour,day and month of the year
# Giving the camera around 20 frames to adjust to the surroundings for better picture quality
    cv2.imwrite(f"{t.second,t.minute,t.hour,t.day,t.month}.png",image)
#     As soon as the image is saved we will stop recording
    del camera

    
# Calling the photo_with_python function
if __name__ == "__main__":
    photo_with_python()

# We need to give some special keyword to this function like click a picture or open camera so the when that's called this function is called






#if __name__ == "__main__":
  #  photo_with_python()
