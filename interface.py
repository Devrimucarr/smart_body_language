import tkinter as tk
from PIL import Image, ImageTk
import cv2

class RealTimeInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Body Language Analysis")

        # Başlangıçta Agent referansları None
        self.gesture_analyzer = None
        self.expression_tracker = None
        self.focus_meter = None
        self.feedback_provider = None

        # Set up video capture
        self.cap = cv2.VideoCapture(0)  # Kamerayı aç (genelde 0)
        
        # Create a label to display video frames
        self.video_label = tk.Label(self.root)
        self.video_label.pack()

        # Create a label to display feedback text
        self.feedback_label = tk.Label(
            self.root,
            text="Feedback: None",
            font=("Arial", 14),
            fg="blue"
        )
        self.feedback_label.pack()

        # Create an exit button
        self.exit_button = tk.Button(
            self.root,
            text="Exit",
            command=self.close_application,
            font=("Arial", 12),
            fg="red"
        )
        self.exit_button.pack(pady=10)

        # Start updating frames
        self.update_frame()

    def set_agents(self, gesture_analyzer, expression_tracker, focus_meter, feedback_provider):
        """
        This method receives the 4 agents from main.py
        and stores them for usage in the interface.
        """
        self.gesture_analyzer = gesture_analyzer
        self.expression_tracker = expression_tracker
        self.focus_meter = focus_meter
        self.feedback_provider = feedback_provider

    def update_frame(self):
        """
        Capture video frames from the camera, process them,
        and display on the Tkinter label.
        Also, call the agents to analyze gestures/expressions,
        compute focus, and show feedback.
        """
        ret, frame = self.cap.read()
        if ret:
            # Convert the frame to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # 1. Gesture analysis
            gesture_data = None
            if self.gesture_analyzer is not None:
                gesture_data = self.gesture_analyzer.analyze_gesture(frame)

            # 2. Expression analysis
            expression_data = None
            if self.expression_tracker is not None:
                expression_data = self.expression_tracker.analyze_expression(frame)

            # 3. Calculate focus
            focus_level = None
            if self.focus_meter is not None:
                focus_level = self.focus_meter.calculate_focus(
                    gesture_data,
                    expression_data
                )

            # 4. Provide feedback
            if focus_level is not None and self.feedback_provider is not None:
                feedback_text = self.feedback_provider.provide_feedback(focus_level)
                self.feedback_label.config(text=f"Feedback: {feedback_text}")

            # Convert frame to ImageTk format for Tkinter
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            # Update the label with the new frame
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        # Schedule the next frame update
        self.video_label.after(10, self.update_frame)

    def close_application(self):
        """
        Safely release the camera and close the Tkinter window.
        """
        if self.cap.isOpened():
            self.cap.release()
        self.root.destroy()

    def __del__(self):
        """
        Destructor to ensure resources are freed if the interface object is deleted.
        """
        if self.cap.isOpened():
            self.cap.release()
