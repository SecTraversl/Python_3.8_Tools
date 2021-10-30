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

