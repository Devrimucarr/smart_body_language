import mediapipe as mp

class GestureAnalyzer:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()

    def analyze_gesture(self, frame):
        results = self.pose.process(frame)
        if results.pose_landmarks:
            print("Gesture detected!")
            return results.pose_landmarks
        return None
