import tkinter as tk

def initialize_main_window():
    print("Initializing main window...")
    root = tk.Tk()
    
    # Set title
    root.title("Man Hours Logger")
    print(f"Window title set to: 'Man Hours Logger'")
    
    # Set geometry
    root.geometry("400x300")
    print(f"Window size set to: 400x300")

    return root
