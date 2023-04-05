from PIL import Image, ImageFilter, ImageOps
import os, sys
from time import sleep
import random


def main():
    # Function that slowly prints the text 
    def speak(text):
        for char in text:
            sleep(0.06)
            sys.stdout.write(char)
            sys.stdout.flush()
    # Start of the game
    speak('\n\033[1;34mWelcome to the best Image Manipulator you will ever use !\n')
    speak('\033[1;34mWhich image would you like to pick from 1 - 10... To quit, press "Q"...\n')
    speak('\033[1;33mImage 1 : Cat\n')
    speak('\033[1;33mImage 2 : Car\n')
    speak('\033[1;33mImage 3 : Lebron James\n')
    speak('\033[1;33mImage 4 : Drake\n')
    speak('\033[1;33mImage 5 : Kobe\n')
    speak('\033[1;33mImage 6 : Will Smith\n')
    speak('\033[1;33mImage 7 : AI\n')
    speak('\033[1;33mImage 8 : Panda\n')
    speak('\033[1;33mImage 9 : Rapper\n')
    speak('\033[1;33mImage 10 : Shoes\n')
    speak('\033[1;31mIf you pick a number not in the range from 1 - 10, we will pick a random image for you!\n')

    num = input("").lower()

    if num == 'q':
        quit()
    elif num == "1":
        image = Image.open("1.jpg")
    elif num == "2":
        image = Image.open("2.jpg")
    elif num == "3":
        image = Image.open("3.jpg")
    elif num == "4":
        image = Image.open("4.jpg")
    elif num == "5":
        image = Image.open("5.jpg")
    elif num == "6":
        image = Image.open("6.jpg")
    elif num == "7":
        image = Image.open("7.jpg")
    elif num == "8":
        image = Image.open("8.jpg")
    elif num == "9":
        image = Image.open("9.jpg")
    elif num == "10":
        image = Image.open("10.jpg")
    else:
        num = random.randint(1, 10)
        image = Image.open(f"{num}.jpg")
    image.show()
    

    sleep(1.5)
    os.system('cls') #Clears terminal 

   # Function for the changes so if user messes up input, the code will run again from here not the full code
    def modifications():
        # All the things the user can decide to do 
        speak('\033[1;33mIf you want to convert the image from ".jpg" to ".png", press 1\n')
        speak('\033[1;36mIf you want to change the thumbnail size of the image, press 2\n')
        speak('\033[1;31mIf you want to change the rotation of the image, press 3\n')
        speak('\033[1;35mIf you want to make the image black & white, press 4\n')
        speak('\033[1;32mIf you want to blur the image, press 5\n')
        speak('\033[1;33mIf you want to add a border to your image, press 6\n')
        speak('\033[1;31mPress "Q" to quit\n')

        changes = input("").lower()

        sleep(1.5)
        os.system('cls') #Clears terminal 

        if changes == "1":
            png_filename = input('\033[1;34mEnter a name for the new PNG file: ')

            # Get the path to the directory containing your code
            code_dir = os.path.dirname(os.path.abspath(__file__))

            # Create the "png_pics" subdirectory if it doesn't exist
            png_dir = os.path.join(code_dir, "png_pics")
            if not os.path.exists(png_dir):
                os.mkdir(png_dir)

            png_filepath = os.path.join(png_dir, png_filename + ".png")

            while os.path.exists(png_filepath):
                speak(f"{png_filepath} already exists.")
                png_filename = input('\033[1;34mEnter a different name for the new PNG file: ')
                png_filepath = os.path.join(png_dir, png_filename + ".png")

            image.save(png_filepath, format="PNG")

        elif changes == "2":
            # variable that will help us determine if to run the code or not for thumbnail sizes
            valid_input = False
            while not valid_input:
                thumb_size = input('\n\033[1;34mEnter a thumbnail size (200, 400, or 600): ')
                image_filename = input('\033[1;34mEnter a name for the new PNG file: ')

                if thumb_size not in ["200", "400", "600"]:
                    speak('\033[1;31mInvalid input. Please enter one of the three values available ~~~ 200, 400, or 600')
                else:
                    valid_input = True

            # Code that will create the folders depending on size. Name will be something like 'thumbnail_400'
            code_dir = os.path.dirname(os.path.abspath(__file__))
            thumb_dir = os.path.join(code_dir, f"thumbnail_{thumb_size}")

            # Check to see if folder exists and only to create one if none exists
            if not os.path.exists(thumb_dir):
                os.mkdir(thumb_dir)

            thumb_filepath = os.path.join(thumb_dir, f"{image_filename}_thumb{thumb_size}.jpg")

            while os.path.exists(thumb_filepath):
                speak(f"{thumb_filepath} already exists\n")
                thumb_filename = input('\033[1;34mEnter a different name for the new Thumbnail file: \n')
                thumb_filepath = os.path.join(thumb_dir, thumb_filename + ".jpg")

            image.thumbnail((int(thumb_size), int(thumb_size)))
            image.save(thumb_filepath, format="JPEG")

        elif changes == "3":

            angle = int(input('\033[1;34mProvide a rotation angle: '))
            rotated_filename = input('\033[1;34mWhat would you like to name your new rotated image: ')
            rotated_image = image.rotate(angle)

            code_dir = os.path.dirname(os.path.abspath(__file__))
            rotated_dir = os.path.join(code_dir, "rotated")
            if not os.path.exists(rotated_dir):
                os.mkdir(rotated_dir)

            rotated_filepath = os.path.join(rotated_dir, rotated_filename + ".jpg")

            while os.path.exists(rotated_filepath):
                speak(f"{rotated_filepath} already exists\n")
                rotated_filename = input('\033[1;34mEnter a different name for the new Rotated file: \n')
                rotated_filepath = os.path.join(rotated_dir, rotated_filename + ".jpg")

            rotated_image.save(rotated_filepath, format="JPEG")
            
        elif changes == "4":
            # Pass argument 'L' which changes image to greyscale
            bw_image = image.convert("L")

            bw_filename = input('\033[1;34mEnter a name for the black and white image: ')

            code_dir = os.path.dirname(os.path.abspath(__file__))

            bw_dir = os.path.join(code_dir, "black-white")
            if not os.path.exists(bw_dir):
                os.mkdir(bw_dir)

            bw_filepath = os.path.join(bw_dir, bw_filename + ".jpg")

            while os.path.exists(bw_filepath):
                speak(f"{bw_filepath} already exists\n")
                bw_filename = input('\033[1;34mEnter a different name for the new Black & White file: \n')
                bw_filepath = os.path.join(bw_dir, bw_filename + ".jpg")

            bw_image.save(bw_filepath, format="JPEG")

        elif changes == "5":
            blur_radius = int(input('\033[1;34mEnter a blur radius : '))
            blurred_image = image.filter(ImageFilter.GaussianBlur(radius=blur_radius))

            blur_filename = input('\033[1;34mEnter a name for the blurred image: ')

            code_dir = os.path.dirname(os.path.abspath(__file__))

            blur_dir = os.path.join(code_dir, "blurred")
            if not os.path.exists(blur_dir):
                os.mkdir(blur_dir)

            blur_filepath = os.path.join(blur_dir, blur_filename + ".jpg")

            while os.path.exists(blur_filepath):
                speak(f"{blur_filepath} already exists\n")
                blur_filename = input('\033[1;34mEnter a different name for the new Blurred file: \n')
                blur_filepath = os.path.join(blur_dir, blur_filename + ".jpg")

            blurred_image.save(blur_filepath, format="JPEG")

        elif changes == "6":
            valid_input = False
            while not valid_input:
                border = input('\033[1;34mEnter a number between 1 - 10. If your number does not meet the range of numbers, the border will be set to 5 as default: ')
                if border.isdigit() and int(border) in range(1, 11):
                    border = int(border)
                    valid_input = True
                else:
                    border = 5
                    valid_input = True

            valid_color = False
            while not valid_color:
                color = input('\033[1;34mEnter a border color from the following ~~~ red, black, or yellow: ').lower()
                if color in ["red", "black", "yellow"]:
                    valid_color = True
                else:
                    color = "black"
                    valid_color = True

            border_filename = input('\033[1;34mEnter a name for the bordered image: ')

            code_dir = os.path.dirname(os.path.abspath(__file__))
            border_dir = os.path.join(code_dir, "Bordered")
            if not os.path.exists(border_dir):
                os.makedirs(border_dir)

            border_filepath = os.path.join(border_dir, border_filename + ".jpg")

            while os.path.exists(border_filepath):
                speak(f"{border_filepath} already exists\n")
                border_filename = input('\033[1;34mEnter a different name for the new Bordered file: \n')
                border_filepath = os.path.join(border_dir, border_filename + ".jpg")

            bordered_image = ImageOps.expand(image, border=border, fill=color)
            bordered_image.save(border_filepath, format="JPEG")

        elif changes == "q":
            quit()

        else:
            speak('\033[1;31mYou provided an invalid value. Please pick a number from 1 - 6 or press "Q" to quit\n')
            modifications()

    modifications()

    sleep(1.5)
    os.system('cls') #Clears terminal 

    speak('\033[1;32mWould you like to keep working with Image Manipulator? (y/n)\n')
    end = input("").lower()
    
    sleep(1.5)
    os.system('cls') #Clears terminal 

    if end == "y":
        main()
    else:
        speak('\033[1;32mSee you Later!')
        quit()

main() # Calling main function to run the code.

