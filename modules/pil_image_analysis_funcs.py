#######################################
###### PIL IMAGE ANALYSIS FUNCS #######
#######################################

from PIL import Image
from PIL.ExifTags import TAGS

# %%
#######################################
def piltest_image_object(image_object: PIL.Image.Image):
    """Tests if the given object is a PIL.Image.Image object, prints the output of various tests, and returns a boolean True or False if the object is a PIL.Image.Image object.

    Examples:
        >>> from PIL import Image\n
        >>> pic1 = Image.open('1.jpg')\n
        >>> piltest_image_object(pic1)\n
        The code 'type(image_object)' ...yields the following:  <class 'PIL.JpegImagePlugin.JpegImageFile'>\n
        The code 'type(image_object.convert("L"))' ...yields the following:  <class 'PIL.Image.Image'>\n
        The code 'isobject(image_object, PIL.Image.Image)' ...yields the following:  True\n
        
        Is the given object a PIL.Image.Image object?\n
        True\n

    References:
        https://stackoverflow.com/questions/58236138/pil-and-python-static-typing

    Args:
        image_object (PIL.Image.Image): Reference an existing image
        
    Returns:
        bool: Returns a boolean True or False
    """
    from PIL import Image
#    
    basic_type = type(image_object)
    convert_method = type(image_object.convert("L"))
    results = isinstance(image_object, PIL.Image.Image)
    print(f'The code \'type(image_object)\' ...yields the following:  {basic_type}')
    print(f'The code \'type(image_object.convert("L"))\' ...yields the following:  {convert_method}')
    print(f'The code \'isobject(image_object, PIL.Image.Image)\' ...yields the following:  {results}')
#   
    print('\nIs the given object a PIL.Image.Image object?')
    return results

# %%
#######################################
def pilnew_image_object(image_file: str):
    from PIL import Image
#
    image_object = Image.open(image_file)
    return image_object

# %%
#######################################
def pilshow_image_in_gui_viewer(image_file: str):
    """Displays the referenced image file in an image viewer if you are working in the GUI.

    Args:
        image_file (str): Reference the path of the image.
    """
    from PIL import Image
#    
    theimage = Image.open(image_file)
    theimage.show()

# %%
#######################################
def pilshow_image_in_vscode(image_file: str):
    """When used with a VS Code "Interactive Window", displays the referenced image file.

    Args:
        image_file (str): Reference the path of the image.
    """
    from PIL import Image
#   
    image_object = Image.open(image_file)
    return image_object

# %%
#######################################
def pilget_exif_data(image_file: str):
    from PIL import Image
    from PIL.ExifTags import TAGS
    
    theimage = Image.open(image_file)
    dict_exif_data = theimage.getexif()
    for name,data in dict_exif_data.items():
        tagname = TAGS.get(name, "unknown-tag")
        print(f"TAG:{name} ({tagname}) is assigned {data}")

