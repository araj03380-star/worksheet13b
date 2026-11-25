# Python Library Projects

A beginner-friendly project for System and AI Essentials Worksheet 13b.

## Libraries
- **pyfiglet** creates large ASCII-art text.
- **Pillow** creates and edits images.
- **qrcode** (homework) generates QR codes.

## Requirements
- Python 3
- Packages listed in `requirements.txt`

Install them:

```bash
python3 -m pip install -r requirements.txt
```

## Run the projects

```bash
python3 first.py
python3 second.py
python3 combined.py
python3 homework.py
```

## Outputs
- `first.py`: prints ASCII-art banners for ARYAN and PYTHON.
- `second.py`: creates `my_second_image.png` (600 × 400, light blue).
- `combined.py`: creates `python_banner.png` (1200 × 500, dark blue, with ASCII-art text).
- `homework.py`: creates `my_qrcode.png`.

## Limitations
- The text and styling are currently set in the source code.
- There is no graphical user interface.
- The banner's appearance depends on the fonts available on the computer.
- The QR code contains a fixed sample message.
