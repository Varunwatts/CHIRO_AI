import face_recognition
import cv2

def is_user_present():
    # Load known face
    known_image = face_recognition.load_image_file("my_face.png")
    known_encoding = face_recognition.face_encodings(known_image)[0]

    video_capture = cv2.VideoCapture(0)
    result = False

    for _ in range(5):  # Try 5 frames
        ret, frame = video_capture.read()
        if not ret:
            continue

        # Convert BGR to RGB and ensure uint8 format
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb_frame = rgb_frame.astype('uint8')

        # Detect faces
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Compare each detected face to the known face
        for face_encoding in face_encodings:
            match = face_recognition.compare_faces([known_encoding], face_encoding)
            if match[0]:
                result = True
                break

        if result:
            break

    video_capture.release()
    return result
