# Worksheet 13b — Suggested Written Answers

Use these as a guide. Replace any run results, error messages, attempt counts, and Git commit hashes with what you actually observe on your Mac.

## Page 2 — Where did your first library land?
Run `python3 -m pip show pyfiglet` and copy the actual `Location:` value from Terminal.

## Page 3 — Pick two
**My two:** pyfiglet and Pillow.

**Why those two?** I chose pyfiglet because it creates attractive ASCII-text banners, and Pillow because it can create and edit images. They can also be combined in one project.

**Repository name:** `python-library-projects`  
**URL:** Paste the URL of the GitHub repository you create.

## Page 4–5 — v0.1: pyfiglet
**What is it for?** Pyfiglet converts normal text into large ASCII-art banners.

**Docs:** https://pypi.org/project/pyfiglet/

**Quickstart code used:**
```python
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('HELLO'))
```

**Smallest test:** Run `python3 first.py`. Expected result: large ASCII-art banners for ARYAN and PYTHON.

**Before asking:** I want to display my name and the word PYTHON as large ASCII-art banners.

**Prompt used:** Write a beginner-friendly Python program using pyfiglet to print ASCII-art banners for ARYAN and PYTHON. Explain each line.

**Line explained:** `fig.renderText("ARYAN")` converts the supplied text into ASCII-art characters.

**Break it:** Temporarily call `fig.renderText()` without a text argument.  
**Expected error category:** TypeError, because the required text argument is missing. Record the actual first error line shown by your Python version.

**Check:** Read the printed banner and confirm that the words are legible.

**Commit message:** `Add pyfiglet banner project`  
**Short hash:** Copy the real value from `git rev-parse --short HEAD`.

## Page 5–6 — v0.2: Pillow
**What is it for?** Pillow is a Python imaging library used to create, open, edit, and save images.

**Docs:** https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

**Smallest test:** Run `python3 second.py`. Expected result: a 600 × 400 light-blue PNG image named `my_second_image.png`.

**Before asking:** I want to create a light-blue image with a width of 600 pixels and height of 400 pixels, then save it as a PNG.

**Prompt used:** Write a simple Python program using Pillow to create a 600 × 400 light-blue image and save it as `my_second_image.png`. Explain each line.

**Line explained:** `Image.new("RGB", (600, 400), "lightblue")` creates a new RGB image with the specified dimensions and background colour.

**Break it:** Try opening a file that does not exist with `Image.open("missing_image.png")`.  
**Expected error category:** FileNotFoundError. Record the actual first error line.

**Check:** Open `my_second_image.png` and verify its dimensions and colour.

**Commit message:** `Add Pillow image creation project`  
**Short hash:** Copy the real value from `git rev-parse --short HEAD`.

## Page 7–8 — v0.3: combine the libraries
**What will it do?** The program will generate ASCII-art text using pyfiglet and draw it onto an image using Pillow.

**Predicted output:** A 1200 × 500 PNG with a dark-blue background and white ASCII-art text reading PYTHON PROJECT.

**Prompt used:** Create a beginner-friendly Python program using pyfiglet to generate the words PYTHON PROJECT as ASCII art, then use Pillow to place that text on a 1200 × 500 dark-blue image in white. Save it as `python_banner.png` and explain the code.

**Back-and-forth count:** Fill in the actual number of attempts you needed.

**What changed about my asking?** I made the prompt more specific by stating the exact text, image dimensions, background colour, text colour, and output filename.

**Something AI got wrong:** Do not invent an error. If an AI suggestion fails, record the exact incorrect function/import/argument and explain how you checked it against the official documentation. If the suggestion in your actual interaction was correct, ask for a deliberate review and test one questionable line before completing this field.

**Does it match the prediction?** If the script runs and the saved image has the predicted dimensions, background, and text, answer Yes. Otherwise describe the difference.

**Commit message:** `Combine pyfiglet and Pillow`  
**Short hash:** Copy the real value from `git rev-parse --short HEAD`.

## Page 8 — README
The repository's `README.md` is included in this project folder and covers what it does, the libraries, installation, run commands, output, and limitations.

## Page 9 — Before you go
| Source | How fast? | How reliable? |
|---|---|---|
| Help flag | Very fast | Reliable for command options |
| Manual | Moderate | Reliable |
| Official docs | Moderate | Very reliable |
| AI | Very fast | Useful, but can be confidently wrong |

**Which was fastest? Which was most reliable? Were they the same?**  
AI was the fastest because it responds immediately. The official documentation was the most reliable because it describes the library's supported behaviour. They were not the same.

**Five steps:**
1. What is this for?
2. Find the shape.
3. Run the smallest thing that works.
4. Change exactly one thing.
5. Break it on purpose.

## Page 9 — Homework: qrcode
**What is it for?** The qrcode library generates QR-code images from text or links.

**Install:** `python3 -m pip install "qrcode[pil]"`  
**Run:** `python3 homework.py`  
**Expected output:** `my_qrcode.png`, containing the sample message in the script.

**Four-line learning log:**
- What it is for: qrcode creates QR-code images from text or links.
- Command that worked: `python3 homework.py`
- What broke: A missing package can cause an import error.
- What I'd try next: Generate QR codes for website links and other messages.

**Fourth commit message:** `Add QR code homework project`  
**Short hash:** Copy the real value from `git rev-parse --short HEAD`.

## Important
The instructor section on page 10 is for your teacher. Leave it blank.
