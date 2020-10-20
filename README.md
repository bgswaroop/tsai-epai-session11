# EPAi session11 assignment
---

The following requirements need to be met to successfully run the code : 
Dependencies  :   python > = 3.7.4 \
Python packages  :   refer to requirements.txt

---
## Session11 objectives
This assignment, helps to code the concepts that are learnt in the session 11 of the EPAi module. 
In particular, this assignment focuses on the following topics  : 

 - Modules: Introduction
 - Import Variants
 
---

The test cases can be executed by executing _pytest_, from python shell
 
---

### Functions



**jpg_to_png(input_file, destination_dir)**

    Convert the input jpeg image to png image
     : param input_file :  any jpeg file
     : param destination_dir :  the output directory where the 'png' file needs to be saved.
     : return :  None

**png_to_jpg(input_file, destination_dir)**

    Convert the input jpeg image to png image
     : param input_file :  any jpeg file
     : param destination_dir :  the output directory where the 'png' file needs to be saved.
     : return :  None

**resize_p(input_file, destination_dir, p)**

    Convert the input jpeg image to png image
     : param input_file :  any jpeg file
     : param destination_dir :  the output directory where the 'png' file needs to be saved.
     : param p :  the resize percentage
     : return :  None

**resize_w(input_file, destination_dir, w)**

    Convert the input jpeg image to png image
     : param input_file :  any jpeg file
     : param destination_dir :  the output directory where the 'png' file needs to be saved.
     : param w :  target image width in pixels
     : return :  None

**resize_h(input_file, destination_dir, h)**

    Convert the input jpeg image to png image
     : param input_file :  any jpeg file
     : param destination_dir :  the output directory where the 'png' file needs to be saved.
     : param h :  target image height in pixels
     : return :  None

**crop_px(input_file, destination_dir, px_w, px_h)**

    Convert the input jpeg image to png image
     : param input_file :  any jpeg file
     : param destination_dir :  the output directory where the 'png' file needs to be saved.
     : param px_w :  target image width in pixels
     : param px_h :  target image height in pixels
     : return :  None

**crop_p(input_file, destination_dir, p_w, p_h)**

    Convert the input jpeg image to png image
     : param input_file :  any jpeg file
     : param destination_dir :  the output directory where the 'png' file needs to be saved.
     : param p_w :  target image width in percentage
     : param p_h :  target image height in percentage
     : return :  None

---

### Unit Tests


**test_readme_exists()**

    Check if the README file exists
     : return :  None

**test_readme_contents()**

    Test the length of the README file
     : return :  None

**test_readme_file_for_formatting()**

    Tests the formatting for the README file
     : return :  None

**test_function_name_had_cap_letter()**

    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
     : return :  None

**test_jpg_to_png()**

    Testing the method jpg_to_png
     : return :  None

**test_png_to_jpg()**

    Testing the method png_to_jpg
     : return :  None

**test_resize_p()**

    Testing the method res_p
     : return :  None

**test_resize_h()**

    Testing the method res_h
     : return :  None

**test_resize_w()**

    Testing the method res_w
     : return :  None

**test_crop_p()**

    Testing the method crop_p
     : return :  None

**test_crop_px()**

    Testing the method crop_px
     : return :  None

**test_jpg_to_png_cmd()**

    Testing the method jpg_to_png using command line arguments
     : return :  None

**test_png_to_jpg_cmd()**

    Testing the method png_to_jpg using command line arguments
     : return :  None

**test_resize_p_cmd()**

    Testing the method res_p using command line arguments
     : return :  None

**test_resize_h_cmd()**

    Testing the method res_h using command line arguments
     : return :  None

**test_resize_w_cmd()**

    Testing the method res_w using command line arguments
     : return :  None

**test_crop_p_cmd()**

    Testing the method crop_p using command line arguments
     : return :  None

**test_crop_px_cmd()**

    Testing the method crop_px using command line arguments
     : return :  None

**test_20_images_jpg_to_png()**

    Testing the entire application
     : return :  None
    Testing the method crop_px using command line arguments
     : return :  None

**test_20_images_png_to_jpg()**

    Testing the entire application
     : return :  None
    Testing the method crop_px using command line arguments
     : return :  None

**test_20_images_resize_80_percent()**

    Testing the method crop_px using command line arguments
     : return :  None

**test_20_images_resize_500_width()**

    Testing the method crop_px using command line arguments
     : return :  None

**test_20_images_resize_500_height()**

    Testing the method crop_px using command line arguments
     : return :  None

**test_20_images_crop_224_224()**

    Testing the method crop_px using command line arguments
     : return :  None

**test_zip_application()**

    Testing the method crop_px using command line arguments
     : return :  None


---

#### 