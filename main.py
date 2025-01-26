import tkinter as tk
from interface import RealTimeInterface
from agents.gesture_analyzer import GestureAnalyzer
from agents.expression_tracker import ExpressionTracker
from agents.focus_meter import FocusMeter
from agents.feedback_provider import FeedbackProvider

def main():
    # Initialize agents
    gesture_analyzer = GestureAnalyzer()
    expression_tracker = ExpressionTracker()
    focus_meter = FocusMeter()
    feedback_provider = FeedbackProvider()

    # Start the Tkinter interface
    root = tk.Tk()
    app = RealTimeInterface(root)

    # Optional: Integrate agents with the interface
    # app.gesture_analyzer = gesture_analyzer
    # app.expression_tracker = expression_tracker
    # app.focus_meter = focus_meter
    # app.feedback_provider = feedback_provider

    # Run the main loop for the interface
    root.mainloop()

if __name__ == "__main__":
    main()
