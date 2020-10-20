# module4_crop
"""
Image crop
"""

import argparse
from pathlib import Path

from PIL import Image

print('Running module4_crop.py')


def crp_p(input_image, output_folder, p_w, p_h):
    """

    :param input_image:
    :param output_folder:
    :param p_w:
    :param p_h:
    :return:
    """

    assert 0 < p_w <= 1, 'Percentage value must be a non-zero positive float in (0, 1]'
    assert 0 < p_h <= 1, 'Percentage value must be a non-zero positive float in (0, 1]'

    img_path = Path(input_image)
    img = Image.open(img_path)

    # Resize image
    width, height = int(img.width * p_w), int(img.height * p_h)
    if width == 0 or height == 0:
        raise ValueError('The percentage value is too small')

    left = int((img.width - width) / 2)
    right = left + width
    top = int((img.height - height) / 2)
    bottom = top + height

    img = img.crop((left, top, right, bottom))

    img.save(Path(output_folder).joinpath(f'cropped_p_{img_path.name}'))
    print('Cropped the input image')


def crp_px(input_image, output_folder, px_w, px_h):
    """

    :param input_image:
    :param output_folder:
    :param px_w:
    :param px_h:
    :return:
    """

    img_path = Path(input_image)
    img = Image.open(img_path)

    assert 0 < px_w <= img.width, f'Cropped img width must be a non-zero positive int < {img.width}'
    assert 0 < px_h <= img.height, f'Cropped img height must be a non-zero positive int < {img.height}'

    # Resize image
    p_w = px_w / img.width
    p_h = px_h / img.height

    width, height = int(img.width * p_w), int(img.height * p_h)
    if width == 0 or height == 0:
        raise ValueError('The percentage value is too small')

    left = int((img.width - width) / 2)
    right = left + width
    top = int((img.height - height) / 2)
    bottom = top + height

    img = img.crop((left, top, right, bottom))

    img.save(Path(output_folder).joinpath(f'cropped_px_{img_path.name}'))
    print('Cropped the input image')


if __name__ == '__main__':
    print('Running module4_crop')
    parser = argparse.ArgumentParser(description=__doc__)

    # These are positional arguments (must not specify the keyword arguments)
    parser.add_argument('input_image', type=str, help='input image path')
    parser.add_argument('output_folder', type=str, help='output folder path')

    parser.add_argument('-w', type=str, help='resize width percentage')
    parser.add_argument('-hi', type=str, help='resize height percentage')
    parser.add_argument('-wx', type=str, help='target image width in pixels')
    parser.add_argument('-hx', type=str, help='target image height in pixels')

    args = parser.parse_args()

    print(args.input_image)
    print(args.output_folder)

    if args.w and args.hi and not args.wx and not args.hx:
        crp_p(rf'{args.input_image}', rf'{args.output_folder}', float(args.w), float(args.hi))
    elif not args.w and not args.hi and args.wx and args.hx:
        crp_px(rf'{args.input_image}', rf'{args.output_folder}', float(args.wx), float(args.hx))
    else:
        print('Invalid / Missing command line arguments. Must specify either `w` & `hi` or `wx` & `hx`')

    print('Job completed')
