import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser
from PIL import Image, ImageTk

# Global variables
qr_image = None
preview_label = None

# Function to generate QR Code (plain text)
def generate_qr():
    global qr_image, preview_label

    data = entry.get()
    box_size = int(size_var.get())

    if not data.strip():
        messagebox.showwarning("Input Error", "Please enter some text or a link.")
        return

# Create QR code object
    qr = qrcode.QRCode(
        version=1,
        box_size=box_size,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

# Generate image with chosen colors
    img = qr.make_image(fill_color=fill_color.get(), back_color=bg_color.get())

# Show preview in GUI
    qr_image = ImageTk.PhotoImage(img.resize((200, 200)))
    preview_label.config(image=qr_image)
    preview_label.image = qr_image

# Function to save QR Code as image
def save_qr():
    if qr_image is None:
        messagebox.showwarning("No QR Code", "Please generate a QR code first.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
    if file_path:
        data = entry.get()
        box_size = int(size_var.get())

        qr = qrcode.QRCode(
            version=1,
            box_size=box_size,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color.get(), back_color=bg_color.get())
        img.save(file_path)
        messagebox.showinfo("Success", f"QR Code saved at:\n{file_path}")

# Color chooser for QR foreground
def choose_fill_color():
    color = colorchooser.askcolor(title="Choose QR Color")
    if color[1]:
        fill_color.set(color[1])

# Color chooser for QR background
def choose_bg_color():
    color = colorchooser.askcolor(title="Choose Background Color")
    if color[1]:
        bg_color.set(color[1])

# GUI setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("450x520")
root.resizable(True, True)

tk.Label(root, text="Enter Your Text or URL:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=45, font=("Arial", 12))
entry.pack(pady=5)

# QR Size Option
tk.Label(root, text="QR Code Size (Box):", font=("Arial", 10)).pack()
size_var = tk.StringVar(value="10")
tk.Spinbox(root, from_=5, to=20, textvariable=size_var, font=("Arial", 10)).pack()

# Colors
fill_color = tk.StringVar(value="black")
bg_color = tk.StringVar(value="white")

tk.Button(root, text="Choose QR Color", command=choose_fill_color).pack(pady=5)
tk.Button(root, text="Choose Background Color", command=choose_bg_color).pack(pady=5)

# Action Buttons
tk.Button(root, text="Generate QR Code", font=("Arial", 12), command=generate_qr).pack(pady=10)
tk.Button(root, text="Save QR Code", font=("Arial", 12), command=save_qr).pack(pady=5)

# Preview
tk.Label(root, text="QR Code Preview:", font=("Arial", 12)).pack(pady=10)
preview_label = tk.Label(root)
preview_label.pack()

root.mainloop()
