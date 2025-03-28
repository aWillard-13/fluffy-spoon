
"""
stand-alone GUI example
"""


# Libraries
import tkinter as tk  # Unified tkinter import
from tkintermapview import TkinterMapView

class TkinterDesigner:
    def __init__(self):
        # Configure main window
        self.main_window = tk.Tk()
        self.main_window.title("App Title")
        self.main_window.geometry("700x600")
        self.main_window.configure(bg="#1E1E1E")
        self.main_window.eval("tk::PlaceWindow . center")  # Center window

        # Layout configuration using `grid`
        self.main_window.rowconfigure(0, weight=1)
        self.main_window.rowconfigure(1, weight=1)
        self.main_window.columnconfigure(0, weight=1)
        self.main_window.columnconfigure(1, weight=1)

        # Layout configuration using `grid` (alternative) - on the RIGHT side
        # Add labels
        self.label_result = tk.Label(self.main_window, text="Result:", fg="cyan", bg="#1E1E1E")
        self.label_result.grid(row=1, column=1, padx=1, pady=1)

        self.label_next_bus = tk.Label(self.main_window, text="Next Bus Info:", fg="yellow", bg="#1E1E1E")
        self.label_next_bus.grid(row=0, column=1, padx=1, pady=1)

        # Add map view
        self.map = TkinterMapView(self.main_window)
        self.map.set_position(41.6, -72.7)
        self.map.set_zoom(10)
        self.map.grid(row=0, column=0, rowspan=2, sticky="nsew")


        """
        # Layout configuration using `grid` (alternative) - on the LEFT side
                # Add labels
        self.label_result = tk.Label(self.main_window, text="Result:", fg="cyan", bg="#1E1E1E")
        self.label_result.grid(row=1, column=0, padx=5, pady=5)

        self.label_next_bus = tk.Label(self.main_window, text="Next Bus Info:", fg="yellow", bg="#1E1E1E")
        self.label_next_bus.grid(row=0, column=0, padx=5, pady=5)

        # Add map view
        self.map = TkinterMapView(self.main_window)
        self.map.grid(row=0, column=1, rowspan=2, sticky="nsew")
        """




if __name__ == "__main__":
    app = TkinterDesigner()
    tk.mainloop()
