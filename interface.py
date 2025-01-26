import tkinter as tk
from PIL import Image, ImageTk
import cv2

class RealTimeInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Body Language Analysis")

        # Set up video capture
        self.cap = cv2.VideoCapture(0)

        # Create a label to display video frames
        self.video_label = tk.Label(self.root)
        self.video_label.pack()

        # Create a label to display feedback
        self.feedback_label = tk.Label(self.root, text="Feedback: None", font=("Arial", 14))
        self.feedback_label.pack()

        # Start updating frames
        self.update_frame()

    def update_frame(self):
        # Capture frame from the camera
        ret, frame = self.cap.read()
        if ret:
            # Convert the frame to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert the frame to a format compatible with Tkinter
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            # Update the video label
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

            # Example feedback logic (replace with real logic)
            focus_level = 80  # Replace this with actual focus detection logic
            if focus_level > 70:
                feedback_text = "Great focus!"
            else:
                feedback_text = "Please focus more!"

            # Update feedback label
            self.feedback_label.config(text=f"Feedback: {feedback_text}")

        # Schedule the next frame update
        self.root.after(10, self.update_frame)

    def __del__(self):
        # Release the video capture when the application closes
        if self.cap.isOpened():
            self.cap.release()

# This class is now ready to be used in your main.py file
