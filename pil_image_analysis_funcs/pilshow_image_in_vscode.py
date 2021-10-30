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

