import argparse
import os
import image_to_text
import helpers

def main():
    """
    To run each test, you must add the image paths you are running the tests on

    e.g.
    python3 main.py -i ./data/new/Wellness/Sternlicht1.jpg

        """

    # create the command line parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image",
                        required=False,
                        help="Path to image")
    parser.add_argument("-d", "--dir",
                        required=False,
                        help="Path to directory")
    args = parser.parse_args()


    if args.dir is not None:
        if not os.path.exists(args.dir):
            print('The directory path you specified: ' + args.dir + ' does not exist. Try running something like: '
                                                                '\n python3 main.py -i ../data/new/Perkins/')
        else:
            print('Running detection on ' + args.dir)

            data_imgs = helpers.load_images(args.dir)
            for data in data_imgs:
                building = image_to_text.img_to_data(data)
                print(building)

                imgs = helpers.load_results("./data/old/" + building + "/")

                for img in imgs:
                    img.show()

    elif args.image is not None:
        if not os.path.exists(args.dir):
            print('The file path you specified: ' + args.image + ' does not exist. Try running something like: '
                                                                '\n python3 main.py -i ../data/new/Perkins/perkins.png')

        img = helpers.load_image(args.image)
        building = image_to_text.img_to_data(img)
        imgs = helpers.load_results("./data/old/" + building + "/")

        for img in imgs:
            img.show()


if __name__ == '__main__':
    main()