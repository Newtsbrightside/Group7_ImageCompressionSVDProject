import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
from PIL import Image
import numpy as np

# === 1. Load image ===
img_path = "week8/test.jpg"  # ← Replace with your image file
img = np.array(Image.open(img_path))

fig, ax = plt.subplots()
ax.imshow(img)
ax.set_title("Drag to select a region (press Enter to confirm)")

# === 2. Global variables to store selection ===
coords = []  # [x1, y1, x2, y2]

def onselect(eclick, erelease):
    """Record the coordinates of the selected area."""
    global coords
    x1, y1 = int(eclick.xdata), int(eclick.ydata)
    x2, y2 = int(erelease.xdata), int(erelease.ydata)
    coords = [min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)]
    print(f"Selected region: {coords}")

# === 3. Create rectangle selector ===
rect_selector = RectangleSelector(
    ax, onselect,
    useblit=True,
    button=[1],  # left mouse button
    minspanx=5, minspany=5,
    spancoords='pixels',
    interactive=True
)

def on_key(event):
    """When 'Enter' is pressed, crop and show the region."""
    if event.key == "enter" and coords:
        x1, y1, x2, y2 = coords
        region = img[y1:y2, x1:x2]
        print("\nPixel values of the selected region (RGB):")
        print(region)
        
        plt.figure()
        plt.imshow(region)
        plt.title("Selected Region")
        plt.show()

# === 4. Connect keyboard event ===
plt.connect("key_press_event", on_key)
plt.show()