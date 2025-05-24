import tkinter as tk
from PIL import Image, ImageTk

def setup_gui():
    root = tk.Tk()
    root.title("CHIRO AI Assistant")
    root.geometry("400x500")
    root.configure(bg="white")

    # Load and display the Baymax-like image
    image = Image.open("assets/baymax.png")  # Ensure this file exists
    image = image.resize((300, 300), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(root, image=photo, bg="white")
    image_label.image = photo
    image_label.pack(pady=20)

    # Status label
    status_label = tk.Label(root, text="CHIRO is Listening...", font=("Helvetica", 16), bg="white")
    status_label.pack(pady=20)

    root.mainloop()
