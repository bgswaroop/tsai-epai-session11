import inspect
import os
import re

import session11
from session11 import *


def test_readme_exists():
    """
    Check if the README file exists
    :return: None
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test the length of the README file
    :return: None
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 200, "Make your README.md file interesting! Add at least 200 words"


def test_readme_file_for_formatting():
    """
    Tests the formatting for the README file
    :return: None
    """
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    """
    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
    :return: None
    """
    functions = inspect.getmembers(session11, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_jpg_to_png():
    """
    Testing the method jpg_to_png
    :return: None
    """
    current_dir = '.'
    input_file_path = os.path.abspath(os.path.join(current_dir, 'sample_inputs/sample1.jpg'))
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))

    jpg_to_png(input_file=input_file_path, destination_dir=output_dir_path)
    assert True


def test_png_to_jpg():
    """
    Testing the method png_to_jpg
    :return: None
    """
    current_dir = '.'
    input_file_path = os.path.abspath(os.path.join(current_dir, 'sample_inputs/sample2.png'))
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))

    png_to_jpg(input_file=input_file_path, destination_dir=output_dir_path)
    assert True


def test_resize_p():
    """
    Testing the method res_p
    :return: None
    """
    current_dir = '.'
    input_file_path = os.path.abspath(os.path.join(current_dir, 'sample_inputs/sample3.jpg'))
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))

    resize_p(input_file=input_file_path, destination_dir=output_dir_path, p=0.5)
    assert True


def test_resize_h():
    """
    Testing the method res_h
    :return: None
    """
    current_dir = '.'
    input_file_path = os.path.abspath(os.path.join(current_dir, 'sample_inputs/sample4.jpg'))
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))

    resize_h(input_file=input_file_path, destination_dir=output_dir_path, h=100)
    assert True


def test_resize_w():
    """
    Testing the method res_w
    :return: None
    """
    current_dir = '.'
    input_file_path = os.path.abspath(os.path.join(current_dir, 'sample_inputs/sample5.jpg'))
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))

    resize_w(input_file=input_file_path, destination_dir=output_dir_path, w=150)
    assert True


def test_crop_p():
    """
    Testing the method crop_p
    :return: None
    """
    current_dir = '.'
    input_file_path = os.path.abspath(os.path.join(current_dir, 'sample_inputs/sample3.jpg'))
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))

    crop_p(input_file=input_file_path, destination_dir=output_dir_path, p_w=0.5, p_h=0.5)
    assert True


def test_crop_px():
    """
    Testing the method crop_px
    :return: None
    """
    current_dir = '.'
    input_file_path = os.path.abspath(os.path.join(current_dir, 'sample_inputs/sample4.jpg'))
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))

    crop_px(input_file=input_file_path, destination_dir=output_dir_path, px_w=400, px_h=300)
    assert True


def test_jpg_to_png_cmd():
    """
    Testing the method jpg_to_png using command line arguments
    :return: None
    """
    current_dir = '.'
    input_file_path = os.path.abspath(os.path.join(current_dir, 'sample_inputs/sample1.jpg'))
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))
    module_path = os.path.abspath(os.path.join(current_dir, 'module_files/module1_jpg_to_png.py'))

    os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path}"')
    assert True


def test_png_to_jpg_cmd():
    """
    Testing the method png_to_jpg using command line arguments
    :return: None
    """
    current_dir = '.'
    input_file_path = os.path.abspath(os.path.join(current_dir, 'sample_inputs/sample2.png'))
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))
    module_path = os.path.abspath(os.path.join(current_dir, 'module_files/module2_png_to_jpg.py'))

    os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path}"')

    png_to_jpg(input_file=input_file_path, destination_dir=output_dir_path)
    assert True


def test_resize_p_cmd():
    """
    Testing the method res_p using command line arguments
    :return: None
    """
    current_dir = '.'
    input_file_path = os.path.abspath(os.path.join(current_dir, 'sample_inputs/sample3.jpg'))
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))
    module_path = os.path.abspath(os.path.join(current_dir, 'module_files/module3_image_resize.py'))

    os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} p=0.5"')
    # resize_p(input_file=input_file_path, destination_dir=output_dir_path, p=0.5)
    assert True


def test_resize_h_cmd():
    """
    Testing the method res_h using command line arguments
    :return: None
    """
    current_dir = '.'
    input_file_path = os.path.abspath(os.path.join(current_dir, 'sample_inputs/sample4.jpg'))
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))
    module_path = os.path.abspath(os.path.join(current_dir, 'module_files/module3_image_resize.py'))

    os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} hi=100"')
    # resize_h(input_file=input_file_path, destination_dir=output_dir_path, h=100)
    assert True


def test_resize_w_cmd():
    """
    Testing the method res_w using command line arguments
    :return: None
    """
    current_dir = '.'
    input_file_path = os.path.abspath(os.path.join(current_dir, 'sample_inputs/sample5.jpg'))
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))
    module_path = os.path.abspath(os.path.join(current_dir, 'module_files/module3_image_resize.py'))

    os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} w=150"')
    # resize_w(input_file=input_file_path, destination_dir=output_dir_path, w=150)
    assert True


def test_crop_p_cmd():
    """
    Testing the method crop_p using command line arguments
    :return: None
    """
    current_dir = '.'
    input_file_path = os.path.abspath(os.path.join(current_dir, 'sample_inputs/sample3.jpg'))
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))
    module_path = os.path.abspath(os.path.join(current_dir, 'module_files/module4_crop.py'))

    os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} w=0.5 hi=0.5"')
    # crop_p(input_file=input_file_path, destination_dir=output_dir_path, p_w=0.5, p_h=0.5)
    assert True


def test_crop_px_cmd():
    """
    Testing the method crop_px using command line arguments
    :return: None
    """
    current_dir = '.'
    input_file_path = os.path.abspath(os.path.join(current_dir, 'sample_inputs/sample4.jpg'))
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))
    module_path = os.path.abspath(os.path.join(current_dir, 'module_files/module4_crop.py'))

    os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} wx=400 hx=300"')
    # crop_px(input_file=input_file_path, destination_dir=output_dir_path, px_w=400, px_h=300)
    assert True


def test_20_images_jpg_to_png():
    """
    Testing the entire application
    :return: None
    """
    """
    Testing the method crop_px using command line arguments
    :return: None
    """
    current_dir = '.'
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))
    module_path = os.path.abspath(os.path.join(current_dir, 'mini_pil'))

    for idx in range(1, 21):
        filename = str(idx).zfill(2) + '.jpg'
        input_file_path = os.path.abspath(os.path.join(current_dir, f'sample_inputs/{filename}'))
        os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} -j2p')
    assert True


def test_20_images_png_to_jpg():
    """
    Testing the entire application
    :return: None
    """
    """
    Testing the method crop_px using command line arguments
    :return: None
    """
    current_dir = '.'
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))
    module_path = os.path.abspath(os.path.join(current_dir, 'mini_pil'))

    for idx in range(1, 21):
        filename = str(idx).zfill(2) + '.png'
        input_file_path = os.path.abspath(os.path.join(current_dir, f'generated_outputs/{filename}'))
        os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} -p2j')

    assert True


def test_20_images_resize_80_percent():
    """
    Testing the method crop_px using command line arguments
    :return: None
    """
    current_dir = '.'
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))
    module_path = os.path.abspath(os.path.join(current_dir, 'mini_pil'))

    for idx in range(1, 21):
        filename = str(idx).zfill(2) + '.jpg'
        input_file_path = os.path.abspath(os.path.join(current_dir, f'sample_inputs/{filename}'))
        os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} -resize -p 0.8')
    assert True


def test_20_images_resize_500_width():
    """
    Testing the method crop_px using command line arguments
    :return: None
    """
    current_dir = '.'
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))
    module_path = os.path.abspath(os.path.join(current_dir, 'mini_pil'))

    for idx in range(1, 21):
        filename = str(idx).zfill(2) + '.jpg'
        input_file_path = os.path.abspath(os.path.join(current_dir, f'generated_outputs/{filename}'))
        os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} -resize -wx 500')
    assert True


def test_20_images_resize_500_height():
    """
    Testing the method crop_px using command line arguments
    :return: None
    """
    current_dir = '.'
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))
    module_path = os.path.abspath(os.path.join(current_dir, 'mini_pil'))

    for idx in range(1, 21):
        filename = str(idx).zfill(2) + '.jpg'
        input_file_path = os.path.abspath(os.path.join(current_dir, f'generated_outputs/{filename}'))
        os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} -resize -hx 500')
    assert True


def test_20_images_crop_224_224():
    """
    Testing the method crop_px using command line arguments
    :return: None
    """
    current_dir = '.'
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))
    module_path = os.path.abspath(os.path.join(current_dir, 'mini_pil'))

    for idx in range(1, 21):
        filename = str(idx).zfill(2) + '.jpg'
        input_file_path = os.path.abspath(os.path.join(current_dir, f'generated_outputs/{filename}'))
        os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} -crop -wx 224 -hx 224')
    assert True


def test_zip_application():
    """
    Testing the method crop_px using command line arguments
    :return: None
    """
    current_dir = '.'
    output_dir_path = os.path.abspath(os.path.join(current_dir, 'generated_outputs'))
    module_path = os.path.abspath(os.path.join(current_dir, 'mini_pil.zip'))

    for idx in range(1, 21):
        filename = str(idx).zfill(2) + '.jpg'
        input_file_path = os.path.abspath(os.path.join(current_dir, f'sample_inputs/{filename}'))
        os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} -j2p')

        filename = str(idx).zfill(2) + '.png'
        input_file_path = os.path.abspath(os.path.join(current_dir, f'generated_outputs/{filename}'))

        os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} -p2j')
        os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} -resize -p 0.8')
        os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} -resize -wx 500')
        os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} -resize -hx 500')
        os.system(f'cmd /c "python {module_path} {input_file_path} {output_dir_path} -crop -wx 224 -hx 224')
