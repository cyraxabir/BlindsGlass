# BlindsGlass
Recognize Faces in order to help blind people
The Blind's Glass is a sunglass for blind People.
The glass has a raspberry motherboard and camera attached.
Pi will first encode the images from target directory and extract person name from the image filename at startup.
Then it will capture frame from camera and match with the encoded faces.
If match it will translate persons name through espeak so that blind person can listen to the headphone.
else face found but not matched, espeak will say "unknown person".

#Install
python face recognition library: (https://github.com/ageitgey/face_recognition)
dlib : (https://github.com/davisking/dlib), check latest version : (https://github.com/davisking/dlib/releases)
