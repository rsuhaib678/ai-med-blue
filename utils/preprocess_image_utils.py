import numpy as np

# Preprocessing Functions
def preprocess_image(image):
    """Preprocess images for input into models."""
    if image.mode != "RGB":
        image = image.convert("RGB")
    img = image.resize((128, 128))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array