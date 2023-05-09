import easyocr
class Ocr:
    def __init__(self, lang):
        self.text = ""
        self.lang = lang

    def get_text(self, img):
        # image_path = "path/to/image.png"
        # with open(image_path, 'rb') as f:
        #     image_data = f.read()
        reader = easyocr.Reader([self.lang], gpu=False, verbose=False)
        self.text = reader.readtext(image=img, paragraph=True)[0][1]

        return self.text

