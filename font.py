import tkinter as tk
from tkinter import font

class FontApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Font Selector")

        self.label = tk.Label(root, text="Sample Text", font=("Arial", 12))
        self.label.pack(pady=20)

        self.font_family_var = tk.StringVar()
        self.font_family_var.set("Arial")

        self.font_size_var = tk.IntVar()
        self.font_size_var.set(12)

        self.create_widgets()

    def create_widgets(self):
        # Font Family Selection
        family_frame = tk.Frame(self.root)
        family_frame.pack()

        tk.Label(family_frame, text="Select Font Family: ").pack(side=tk.LEFT)

        fonts = font.families()
        self.font_family_menu = tk.OptionMenu(family_frame, self.font_family_var, *fonts)
        self.font_family_menu.pack(side=tk.LEFT)

        # Font Size Selection
        size_frame = tk.Frame(self.root)
        size_frame.pack()

        tk.Label(size_frame, text="Select Font Size: ").pack(side=tk.LEFT)

        self.font_size_entry = tk.Entry(size_frame, textvariable=self.font_size_var, width=5)
        self.font_size_entry.pack(side=tk.LEFT)

        # Apply Button
        apply_button = tk.Button(self.root, text="Apply", command=self.apply_font)
        apply_button.pack(pady=10)

    def apply_font(self):
        new_family = self.font_family_var.get()
        new_size = self.font_size_var.get()
        self.label.config(font=(new_family, new_size))

if __name__ == "__main__":
    root = tk.Tk()
    app = FontApp(root)
    root.mainloop()
