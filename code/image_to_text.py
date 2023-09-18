import cv2
import pytesseract

"""
This function extracts the text from our image.
"""
def img_to_data(img):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img,5)
    img = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
    img = cv2.bitwise_not(img)

    config = '-l eng --oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=config)

    buildings_dict = {
        "Barbour":{"Barbour","Charlesfield", "1966"},
        "Buxton":{"Buxton"},
        "Chapin":{"Chapin"},
        "Diman":{"Diman"},
        "Goddard":{"Goddard"},
        "Harkness":{"Harkness"},
        "Hegeman":{"Hegeman","George", "1926"},
        "Macmillan":{"Macmillan","Duncan", "167 Thayer","1998"},
        "Marcy":{"Marcy"},
        "Nelson":{"Nelson"},
        "New Pem": {"Pembroke", "1974"},
        "Perkins":{"Perkins","Power", "1960"},
        "Rock":{"Rock","Prospect", "1964"},
        "Sears":{"Sears"},
        "Ratty":{"Sharpe", "144 Thayer"},
        "Wayland":{"Wayland"},
        "Olney":{"Olney","1951"},
        "Keeney":{"Keeney","Benevolent","1957","Bronson"}
    }

    for building in buildings_dict:
        for string in buildings_dict[building]:
            if string.lower() in text.lower():
                return building

    return "default"
