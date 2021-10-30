# %%
#######################################
def pilnew_image_object(image_file: str):
    from PIL import Image
#
    image_object = Image.open(image_file)
    return image_object

