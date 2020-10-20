import os.path
import sys
import types

module_path = './mini_pil'


def jpg_to_png(input_file, destination_dir):
    """
    Convert the input jpeg image to png image
    :param input_file: any jpeg file
    :param destination_dir: the output directory where the 'png' file needs to be saved.
    :return: None
    """

    module_file = 'module1_jpg_to_png.py'
    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'r') as f:
        source_code = f.read()

    module_name = 'jpg_to_png'
    mod = types.ModuleType(module_name)
    mod.__file__ = module_abs_file_path

    sys.modules[module_name] = mod
    code = compile(source_code, filename=module_abs_file_path, mode='exec')
    exec(code, mod.__dict__)

    mod.j2p(input_file, destination_dir)


def png_to_jpg(input_file, destination_dir):
    """
    Convert the input jpeg image to png image
    :param input_file: any jpeg file
    :param destination_dir: the output directory where the 'png' file needs to be saved.
    :return: None
    """

    module_file = 'module2_png_to_jpg.py'
    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'r') as f:
        source_code = f.read()

    module_name = 'png_to_jpg'
    mod = types.ModuleType(module_name)
    mod.__file__ = module_abs_file_path

    sys.modules[module_name] = mod
    code = compile(source_code, filename=module_abs_file_path, mode='exec')
    exec(code, mod.__dict__)

    mod.p2j(input_file, destination_dir)


def resize_p(input_file, destination_dir, p):
    """
    Convert the input jpeg image to png image
    :param input_file: any jpeg file
    :param destination_dir: the output directory where the 'png' file needs to be saved.
    :param p: the resize percentage
    :return: None
    """

    module_file = 'module3_image_resize.py'
    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'r') as f:
        source_code = f.read()

    module_name = 'image_resize'
    mod = types.ModuleType(module_name)
    mod.__file__ = module_abs_file_path

    sys.modules[module_name] = mod
    code = compile(source_code, filename=module_abs_file_path, mode='exec')
    exec(code, mod.__dict__)

    mod.res_p(input_file, destination_dir, p)


def resize_w(input_file, destination_dir, w):
    """
    Convert the input jpeg image to png image
    :param input_file: any jpeg file
    :param destination_dir: the output directory where the 'png' file needs to be saved.
    :param w: target image width in pixels
    :return: None
    """

    module_file = 'module3_image_resize.py'
    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'r') as f:
        source_code = f.read()

    module_name = 'image_resize'
    mod = types.ModuleType(module_name)
    mod.__file__ = module_abs_file_path

    sys.modules[module_name] = mod
    code = compile(source_code, filename=module_abs_file_path, mode='exec')
    exec(code, mod.__dict__)

    mod.res_w(input_file, destination_dir, w)


def resize_h(input_file, destination_dir, h):
    """
    Convert the input jpeg image to png image
    :param input_file: any jpeg file
    :param destination_dir: the output directory where the 'png' file needs to be saved.
    :param h: target image height in pixels
    :return: None
    """

    module_file = 'module3_image_resize.py'
    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'r') as f:
        source_code = f.read()

    module_name = 'image_resize'
    mod = types.ModuleType(module_name)
    mod.__file__ = module_abs_file_path

    sys.modules[module_name] = mod
    code = compile(source_code, filename=module_abs_file_path, mode='exec')
    exec(code, mod.__dict__)

    mod.res_h(input_file, destination_dir, h)


def crop_px(input_file, destination_dir, px_w, px_h):
    """
    Convert the input jpeg image to png image
    :param input_file: any jpeg file
    :param destination_dir: the output directory where the 'png' file needs to be saved.
    :param px_w: target image width in pixels
    :param px_h: target image height in pixels
    :return: None
    """

    module_file = 'module4_crop.py'
    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'r') as f:
        source_code = f.read()

    module_name = 'crop'
    mod = types.ModuleType(module_name)
    mod.__file__ = module_abs_file_path

    sys.modules[module_name] = mod
    code = compile(source_code, filename=module_abs_file_path, mode='exec')
    exec(code, mod.__dict__)

    mod.crp_px(input_file, destination_dir, px_w, px_h)


def crop_p(input_file, destination_dir, p_w, p_h):
    """
    Convert the input jpeg image to png image
    :param input_file: any jpeg file
    :param destination_dir: the output directory where the 'png' file needs to be saved.
    :param p_w: target image width in percentage
    :param p_h: target image height in percentage
    :return: None
    """

    module_file = 'module4_crop.py'
    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'r') as f:
        source_code = f.read()

    module_name = 'crop'
    mod = types.ModuleType(module_name)
    mod.__file__ = module_abs_file_path

    sys.modules[module_name] = mod
    code = compile(source_code, filename=module_abs_file_path, mode='exec')
    exec(code, mod.__dict__)

    mod.crp_p(input_file, destination_dir, p_w, p_h)

