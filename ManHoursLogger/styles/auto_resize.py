from PIL import Image, ImageTk

def resize_image(image_path, new_width):
    original_image = Image.open(image_path)
    original_width, original_height = original_image.size
    new_height = int((new_width / original_width) * original_height)
    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)
