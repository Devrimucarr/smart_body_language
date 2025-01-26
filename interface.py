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

        # Create an exit button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.close_application, font=("Arial", 12))
        self.exit_button.pack(pady=10)

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

            # Example dynamic feedback logic
            focus_level = self.calculate_focus(frame)  # Replace this with actual logic
            if focus_level > 70:
                feedback_text = "Great focus!"
            elif focus_level > 40:
                feedback_text = "You could improve your focus."
            else:
                feedback_text = "Please focus more!"

            # Update feedback label
            self.feedback_label.config(text=f"Feedback: {feedback_text}")

        # Schedule the next frame update
        self.root.after(10, self.update_frame)

    def calculate_focus(self, frame):
        # Placeholder logic for focus calculation
        # Replace this with your actual focus detection logic
        return 80  # Example fixed value for demonstration

    def close_application(self):
        # Release the video capture and close the application
        if self.cap.isOpened():
            self.cap.release()
        self.root.destroy()

    def __del__(self):
        # Ensure the video capture is released when the object is deleted
        if self.cap.isOpened():
            self.cap.release()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = RealTimeInterface(root)
    root.mainloop()
