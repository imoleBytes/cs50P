import sys, csv
from PIL import Image, ImageOps
from os.path import splitext




def main():
    num_args = len(sys.argv)

    if num_args < 3:
        sys.exit("Too few command-line arguments")
    elif num_args > 3:
        sys.exit("Too many command-line arguments")
    
    pic1 = sys.argv[1]
    pic2 = sys.argv[2]

    pic1_ext = splitext(pic1)[1]
    pic2_ext = splitext(pic2)[1]
    # print(pic1_ext)
    # print(pic2_ext)

    if pic1_ext.lower() not in ['.jpg', '.jpeg', '.png']:
        sys.exit('Invalid input')
    elif pic2_ext.lower() not in ['.jpg', '.jpeg', '.png']:
        sys.exit('Invalid output')
    if pic1_ext != pic2_ext:
        sys.exit('Input and output have different extensions')

    shirt = Image.open('shirt.png', 'r')
    try:     
        img1 = Image.open(pic1, 'r')
        size = shirt.size

        img = ImageOps.fit(img1, size)
        img.paste(shirt, shirt)
        img.save(pic2)
    except FileNotFoundError:
        sys.exit('Input does not exist')


if __name__ == "__main__":
    main()
