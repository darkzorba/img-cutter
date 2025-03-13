from settings import DEFAULT_SIZES
from PIL import Image
import os

from PIL import Image
import os

def centralize_and_crop(img_path, width_size=300, height_size=300, show=True):
    img = Image.open(img_path)
    width, height = img.size

    # get img name
    img_name = os.path.splitext(os.path.basename(img_path))[0]

    target_ratio = width_size / height_size
    original_ratio = width / height

    if original_ratio > target_ratio:
        new_height = height_size
        new_width = int(new_height * original_ratio)
    else:
        new_width = width_size
        new_height = int(new_width / original_ratio)

    img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    center_x = new_width // 2
    center_y = new_height // 2

    left = center_x - width_size // 2
    top = center_y - height_size // 2
    right = left + width_size
    bottom = top + height_size

    new_img = img_resized.crop((left, top, right, bottom))

    if show:
        new_img.show()

    os.makedirs(f"media/{img_name}",exist_ok=True)
    new_img.save(f"media/{img_name}/{img_name}_{width_size}x{height_size}.png")

    return new_img



def main(img_path):
    ls_imgs=[]
    for size in DEFAULT_SIZES:
        img = centralize_and_crop(img_path, size[0],size[1],show=False)
        ls_imgs.append(img)
    return ls_imgs

