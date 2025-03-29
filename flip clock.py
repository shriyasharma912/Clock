import tkinter as tk
from time import strftime

class FlipClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Flip Clock")
        self.geometry("400x200")
        self.configure(bg="black")

        self.font = ('Arial', 60, 'bold')

        # Create a frame to hold the flip clock labels
        self.time_display = tk.Label(self, font=self.font, bg="black", fg="white")
        self.time_display.pack(expand=True)

        # Call the update_time function to update the time every second
        self.update_time()

    def update_time(self):
        # Get the current time as a string in "HH:MM:SS" format
        current_time = strftime('%H:%M:%S')
        
        # Set the current time to the label
        self.time_display.config(text=current_time)

        # Call update_time every 1000 milliseconds (1 second)
        self.after(1000, self.update_time)


# Create and run the flip clock application
if __name__ == "__main__":
    app = FlipClock()
    app.mainloop()
