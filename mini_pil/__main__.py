"""
This application combines the functionality of all the four modules:
1. jpg to png
2. pmg to jpg
3. resize
4. crop
"""
import argparse

import module1_jpg_to_png
import module2_png_to_jpg
import module3_image_resize
import module4_crop

# print('Successfully imported all the modules')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)

    # These are positional arguments (must not specify the keyword arguments)
    parser.add_argument('input_image', type=str, help='input image path')
    parser.add_argument('output_folder', type=str, help='output folder path')

    parser.add_argument('-p', type=str, help='resize percentage')

    parser.add_argument('-hx', type=str, help='target image height in pixels')
    parser.add_argument('-wx', type=str, help='target image width in pixels')

    parser.add_argument('-wp', type=str, help='crop width percentage')
    parser.add_argument('-hp', type=str, help='crop height percentage')

    parser.add_argument('-j2p', action='store_true', help='Convert jpeg image to png')
    parser.add_argument('-p2j', action='store_true', help='Convert png to jpeg')
    parser.add_argument('-resize', action='store_true', help='resize image')
    parser.add_argument('-crop', action='store_true', help='crop image')

    args = parser.parse_args()

    print(args.input_image)
    print(args.output_folder)

    if args.j2p and not args.p2j and not args.resize and not args.crop:
        module1_jpg_to_png.j2p(rf'{args.input_image}', rf'{args.output_folder}')

    elif not args.j2p and args.p2j and not args.resize and not args.crop:
        module2_png_to_jpg.p2j(rf'{args.input_image}', rf'{args.output_folder}')

    elif not args.j2p and not args.p2j and args.resize and not args.crop:
        if args.p and not args.wx and not args.hx:
            module3_image_resize.res_p(rf'{args.input_image}', rf'{args.output_folder}', float(args.p))
        elif not args.p and not args.wx and args.hx:
            module3_image_resize.res_h(rf'{args.input_image}', rf'{args.output_folder}', float(args.hx))
        elif not args.p and args.wx and not args.hx:
            module3_image_resize.res_w(rf'{args.input_image}', rf'{args.output_folder}', float(args.wx))
        else:
            print('Invalid / Missing command line arguments. Must specify at least and only one of the optional '
                  'params - `p`, `hx` or `wx`')

    elif not args.j2p and not args.p2j and not args.resize and args.crop:
        if args.wp and args.hp and not args.wx and not args.hx:
            module4_crop.crp_p(rf'{args.input_image}', rf'{args.output_folder}', float(args.wp), float(args.hp))
        elif not args.wp and not args.hp and args.wx and args.hx:
            module4_crop.crp_px(rf'{args.input_image}', rf'{args.output_folder}', float(args.wx), float(args.hx))
        else:
            print('Invalid / Missing command line arguments. Must specify either `wp` & `hp` or `wx` & `hx`')

        print('Jobs completed')
    else:
        print('Must select exactly one of the options: `-j2p`, `-p2g`, `-crop`, `-resize`')
else:
    print(f'Not running main, as the application name is : {__name__}')
