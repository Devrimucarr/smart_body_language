import cv2
from agents.gesture_analyzer import GestureAnalyzer
from agents.expression_tracker import ExpressionTracker
from agents.focus_meter import FocusMeter
from agents.feedback_provider import FeedbackProvider

gesture_analyzer = GestureAnalyzer()
expression_tracker = ExpressionTracker()
focus_meter = FocusMeter()
feedback_provider = FeedbackProvider()

cap = cv2.VideoCapture(0)  # Kamerayı başlat

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gesture_data = gesture_analyzer.analyze_gesture(frame)
    expression_data = expression_tracker.analyze_expression(frame)
    focus_level = focus_meter.calculate_focus(gesture_data, expression_data)
    feedback = feedback_provider.provide_feedback(focus_level)

    cv2.putText(frame, feedback, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Smart Body Language", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
