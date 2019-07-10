import face_recognition
import picamera
import numpy as np
import os

camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

face_locations = []
face_encodings = []
face_names = []

known_person=[]
known_image=[]
known_face_encoding=[]

# Load the sample pictures 
print("Loading known face image(s)")
#Loop to add images from target folder
for file in os.listdir("friends"):
    try:
        #Extracting person name from the image filename
        known_person.append(file.replace(".jpg", ""))
        file=os.path.join("friends/", file)
        known_image = face_recognition.load_image_file(file)
        known_face_encoding.append(face_recognition.face_encodings(known_image)[0])
    except Exception as e:
        pass



while True:
    print("Capturing frame.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")

    # Find all the faces and face encodings in the current frame 
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)

    # Loop over each face found in the frame to see if it's someone pi know.
    for face_encoding in face_encodings:

        match = face_recognition.compare_faces(known_face_encoding, face_encoding)
        matches=np.where(match)[0] #Checking which image is matched
        if len(matches)>0:
          name = str(known_person[matches[0]])
          #text to speech
          os.system("espeak  'Hello {}' -ven+f5 -k5 -s150".format(name))
        else:
          name = ""
          #speaker voice= us, female, speed=normal
          os.system("espeak 'Unknown person' -ven-us+f4 -s170") 
        print("I see {}!".format(name))



