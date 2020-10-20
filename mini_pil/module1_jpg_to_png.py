# module1_jpg_to_png
"""
Converts jpeg image to pil image
"""

import argparse
from pathlib import Path

from PIL import Image

print('Running module1_jpg_to_png.py')


def j2p(input_image, output_folder):
    img_path = Path(input_image)
    img = Image.open(img_path)
    img.save(Path(output_folder).joinpath(f'{img_path.stem}.png'))
    print('Converted the jpeg image to png image')


if __name__ == '__main__':
    print('Running module1_jpg_to_png')
    parser = argparse.ArgumentParser(description=__doc__)

    # These are positional arguments (must not specify the keyword arguments)
    parser.add_argument('input_image', type=str, help='input image path')
    parser.add_argument('output_folder', type=str, help='output folder path')
    args = parser.parse_args()

    print(args.input_image)
    print(args.output_folder)

    j2p(rf'{args.input_image}', rf'{args.output_folder}')
    print('Job completed')
