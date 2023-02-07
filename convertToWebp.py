from pathlib import Path
from PIL import Image


def convert_to_webp(source):
    """Convert image to webp.

    Args:
        source (pathlib.Path): Path to source image

    Returns:
        pathlib.Path: path to new image
    """
    destination = source.with_suffix(".webp")

    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination


def main():
    paths = Path("C:/Users/mario.sanchez/desktop").glob("*.*")  #Paths to all documents. Change it to the directory where your images are placed.
    for path in paths:
        if path.suffix == ".png" or path.suffix == ".jpg" or path.suffix == ".jpeg":    #Add an or for each image format you want to convert. Usually used of png and jpg/jpeg
            webp_path = convert_to_webp(path)
            print(webp_path)
main()