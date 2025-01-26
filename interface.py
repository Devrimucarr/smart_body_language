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

        # Example feedback logic (you can replace this with real logic)
        focus_level = 80  # Replace this with your actual focus detection logic
        if focus_level > 70:
            feedback_text = "Great focus!"
        else:
            feedback_text = "Please focus more!"

        # Update feedback label
        self.feedback_label.config(text=f"Feedback: {feedback_text}")

    # Schedule the next frame update
    self.root.after(10, self.update_frame)
