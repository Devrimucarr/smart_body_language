import mediapipe as mp

class ExpressionTracker:
    def __init__(self):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh()

    def analyze_expression(self, frame):
        results = self.face_mesh.process(frame)
        if results.multi_face_landmarks:
            print("Facial expression detected!")
            return results.multi_face_landmarks
        return None
