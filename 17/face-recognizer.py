
import os
import cv2
import imutils
import face_recognition
import face_recognition_models 
import mediapipe as mp

# Load the known faces
known_face_encodings= []
known_face_names = []

for filename in os.listdir ('known_faces'):
    path = os.path.join ('known_faces', filename)
    image = face_recognition.load_image_file (path)
    encodings = face_recognition.face_encodings (image)
    if encodings:
        known_face_encodings.append(encodings[0])
        name = os.path.splitext(filename)[0]
        known_face_names.append(name)

# MediaPipe face detection setup
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture ('../videos/IMG_1322.mov')

with mp_face_detection.FaceDetection (min_detection_confidence=0.6) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break

        # BGR to RGB conversion
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Reduce size of the image to speed up processing or if it's too large
        print(frame.shape)
        img = imutils.resize (rgb_frame, width = min(800, frame.shape[1]))
        print(img.shape)

        # Extract the face locations and encodings (AI)
        face_locations = face_recognition.face_locations (img)
        face_encodings = face_recognition.face_encodings (img, face_locations)
        
        # Loop over each face found in the frame
        for (top, right, bottom, left), face_encoding in zip (face_locations, face_encodings):
            matches = face_recognition.compare_faces (known_face_encodings, face_encoding)
            name = "Unknown"
            
            # Use the shortest distance for best match
            face_distances = face_recognition.face_distance (known_face_encodings, face_encoding)
            
            if len (face_distances) > 0:
                best_match_index = face_distances.argmin()
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
            
            cv2.rectangle (img, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText (img, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
        cv2.imshow("Face Recognition", img)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
