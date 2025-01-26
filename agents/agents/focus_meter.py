class FocusMeter:
    def __init__(self):
        self.focus_level = 0

    def calculate_focus(self, gesture_data, expression_data):
        if gesture_data and expression_data:
            self.focus_level += 10
        else:
            self.focus_level -= 5
        self.focus_level = max(0, min(self.focus_level, 100))
        return self.focus_level
