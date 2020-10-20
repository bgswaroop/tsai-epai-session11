# module3_image_resize
"""
Image resize
"""

import argparse
from pathlib import Path

from PIL import Image

print('Running module3_image_resize.py')


def res_p(input_image, output_folder, p):
    """

    :param input_image:
    :param output_folder:
    :param p:
    :return:
    """

    assert p > 0, 'Percentage value must be a non-zero positive float'

    img_path = Path(input_image)
    img = Image.open(img_path)

    # Resize image
    width, height = int(img.width * p), int(img.height * p)
    if width == 0 or height == 0:
        raise ValueError('The percentage value is too small')
    img = img.resize((width, height))

    img.save(Path(output_folder).joinpath(f'{img_path.name}'))
    print('Resized the input image')


def res_w(input_image, output_folder, w):
    """

    :param input_image:
    :param output_folder:
    :param w:
    :return:
    """

    assert w > 0, 'Pixels value must be a non-zero positive integer'

    img_path = Path(input_image)
    img = Image.open(img_path)

    # Resize image
    p = w / img.width
    width, height = int(img.width * p), int(img.height * p)
    if width == 0 or height == 0:
        raise ValueError('The width value is too small')
    img = img.resize((width, height))

    img.save(Path(output_folder).joinpath(f'{img_path.name}'))
    print('Resized the input image')


def res_h(input_image, output_folder, h):
    """

    :param input_image:
    :param output_folder:
    :param h:
    :return:
    """

    assert h > 0, 'Pixels value must be a non-zero positive integer'

    img_path = Path(input_image)
    img = Image.open(img_path)

    # Resize image
    p = h / img.height
    width, height = int(img.width * p), int(img.height * p)
    if width == 0 or height == 0:
        raise ValueError('The height value is too small')
    img = img.resize((width, height))

    img.save(Path(output_folder).joinpath(f'{img_path.name}'))
    print('Resized the input image')


if __name__ == '__main__':
    print('Running module3_image_resize')
    parser = argparse.ArgumentParser(description=__doc__)

    # These are positional arguments (must not specify the keyword arguments)
    parser.add_argument('input_image', type=str, help='input image path')
    parser.add_argument('output_folder', type=str, help='output folder path')

    parser.add_argument('-p', type=str, help='resize percentage')
    parser.add_argument('-hi', type=str, help='target image height in pixels')
    parser.add_argument('-w', type=str, help='target image width in pixels')

    args = parser.parse_args()

    print(args.input_image)
    print(args.output_folder)

    if args.p and not args.w and not args.hi:
        res_p(rf'{args.input_image}', rf'{args.output_folder}', float(args.p))
    elif not args.p and not args.w and args.hi:
        res_h(rf'{args.input_image}', rf'{args.output_folder}', float(args.hi))
    elif not args.p and args.w and not args.hi:
        res_w(rf'{args.input_image}', rf'{args.output_folder}', float(args.w))
    else:
        print('Invalid / Missing command line arguments. Must specify at least and only one of the optional params - '
              '`p`, `hi` or `w`')

    print('Job completed')
