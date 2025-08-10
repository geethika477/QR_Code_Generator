# QR Code Generator (Python + Tkinter)

A simple yet powerful **QR Code Generator** built with Python, Tkinter, Pillow, and the `qrcode` library.  
Generate custom QR codes from any text or URL, choose your own colors, preview them instantly, and save them as PNG files.  
**Works 100% offline after setup.**

---

# Features
- Generate QR Codes from text or URLs.
- Custom Colors — set QR foreground and background colors.
- Instant Preview — see the QR code before saving.
- Save as PNG — store your QR codes locally.
- Desktop Application — works offline, no internet required.
- Privacy-Friendly — your data stays on your device.

---

# Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
```

### 2. Install dependencies
```bash
pip install qrcode[pil] pillow
```

---

# Usage

Run the script:
```bash
python qr_code_generator.py
```

1. Enter your text or URL in the input field.  
2. Choose the QR box size.  
3. Pick your desired colors for the QR and background.  
4. Click **Generate QR Code** to preview.  
5. Click **Save QR Code** to save as a PNG file.

---

# Project Structure
```
qr-code-generator/
│-- qr_code_generator.py   # Main application file
│-- README.md               # Project documentation
```

---

# How It Works
- Uses the [`qrcode`](https://pypi.org/project/qrcode/) library to generate QR code data.
- Uses **Pillow (PIL)** for image manipulation and display.
- Uses **Tkinter** to create the desktop GUI, including:
  - Input box for text/URL
  - Spinbox for QR size
  - Color pickers for customization
  - Image preview panel
  - Save dialog for exporting

---

# Example Uses
- Event tickets with QR codes.
- Restaurant digital menus.
- Wi-Fi password sharing.
- Personal portfolio or resume links.
- Business flyers and marketing materials.

---

# License
This project is open for learning and personal use.

---

# Acknowledgments
- [qrcode](https://github.com/lincolnloop/python-qrcode) for QR code generation.
- [Pillow](https://python-pillow.org/) for image processing.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.
