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

    # Bind agents to the interface
    app.set_agents(
        gesture_analyzer,
        expression_tracker,
        focus_meter,
        feedback_provider
    )

    # Run the main loop for the interface
    root.mainloop()

if __name__ == "__main__":
    main()
