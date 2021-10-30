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

