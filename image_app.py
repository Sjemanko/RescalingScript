import os 
from PIL import Image
import sys


class Image_converter:
    char = "> "

    def start(self):
        print("Hello, pls input .jpg/.png filename to convert: ")
        while True:
            try:
                first_file = str(input(Image_converter.char))
                if first_file[-1] == '"':
                    first_file = first_file[1:-1]
                if os.path.isfile(first_file) and (first_file[-4:] == '.jpg' or first_file[-4:] == '.png'):
                    img = Image.open(first_file)
                    break
                print("Wrong filename, try again.")
            except RuntimeError:
                print("Unable to open file. Check if the filename is correct.")
        return img

    def image_scaling(self, img):
        while True:
            try:
                argument = int(input("Input a percentage value to rescaling (recommended 25(%), 50(%), 75(%))\n" + Image_converter.char))
                if int(argument) < 100 and int(argument) > 1:
                    break
            except ValueError:
                print("Numbers only, try again")
        rescaled_img = img.resize((round(img.size[0]*argument/100), round(img.size[1]*argument/100)))
        return rescaled_img


    def saving(self, rescaled_img):
        while True:
            try:     
                filename_question = input("How to save converted file?\n" + Image_converter.char)
                if (filename_question[-4:] == '.jpg' or filename_question[-4:] == '.png') and len(filename_question) >= 5:
                    rgb_im = rescaled_img.convert('RGB')            # Possibility of changing from .jpg to .png
                    rgb_im.save(filename_question)                  # Saving
                    break
                print("Wrong filename format, try again.")
            except TypeError:
                print("Saving failed")
        print("Saving successful")




object_app = Image_converter()
start_app = object_app.start()
scaled_img = object_app.image_scaling(start_app)
object_app.saving(scaled_img)
input("Press to continue..")