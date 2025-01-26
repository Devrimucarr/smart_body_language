class FeedbackProvider:
    def provide_feedback(self, focus_level):
        if focus_level > 70:
            return "Great focus!"
        elif focus_level > 40:
            return "You could improve your focus."
        else:
            return "Try to concentrate better."
