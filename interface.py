import tkinter as tk
from tkinter import Label
import cv2
from PIL import Image, ImageTk

class RealTimeInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Body Language Analysis")
        self.root.geometry("800x600")  # Window size: 800x600

        # OpenCV kamera başlatma
        self.cap = cv2.VideoCapture(0)  # Kamerayı başlatıyoruz

        # Video display label
        self.video_label = Label(self.root)
        self.video_label.grid(row=0, column=1, pady=20, padx=20)

        # Feedback display label
        self.feedback_label = Label(self.root, text="Feedback: Initializing...", font=("Arial", 16), fg="green")
        self.feedback_label.grid(row=0, column=0, pady=20, padx=20)

        # Exit button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.close_program)
        self.exit_button.grid(row=1, column=0, pady=20, padx=20)

        # Update video feed
        self.update_frame()

    def update_frame(self):
        # Capture frame from camera
        ret, frame = self.cap.read()
        if ret:
            # Convert OpenCV image to PIL format
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

            # Example feedback (you can replace this with your project's logic)
            self.feedback_label.config(text="Feedback: Great focus!")

        # Schedule the next frame update
        self.root.after(10, self.update_frame)

    def close_program(self):
        self.cap.release()  # Kamerayı serbest bırak
        self.root.destroy()

# Start the Tkinter interface
if __name__ == "__main__":
    root = tk.Tk()
    app = RealTimeInterface(root)
    root.mainloop()
