from PIL import Image, ImageFilter, ImageEnhance
import pytesseract

def recognize(img: Image) -> str:
    img = img.convert('RGB')
    img = img.filter(ImageFilter.SMOOTH)

    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(3.0)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(10.0)

    originImg = img.copy()

    for y in range(1, originImg.height - 1):
        for x in range(1, originImg.width - 1):
            cnt = 0
            if (originImg.getpixel((x, y)) != (255, 255, 255)):
                if (originImg.getpixel((x, y - 1)) == (255, 255, 255)): cnt += 1
                if (originImg.getpixel((x + 1, y - 1)) == (255, 255, 255)): cnt += 1
                if (originImg.getpixel((x + 1, y)) == (255, 255, 255)): cnt += 1
                if (originImg.getpixel((x + 1, y + 1)) == (255, 255, 255)): cnt += 1
                if (originImg.getpixel((x, y + 1)) == (255, 255, 255)): cnt += 1
                if (originImg.getpixel((x - 1, y + 1)) == (255, 255, 255)): cnt += 1
                if (originImg.getpixel((x - 1, y)) == (255, 255, 255)): cnt += 1
                if (originImg.getpixel((x - 1, y - 1)) == (255, 255, 255)): cnt += 1
                if (cnt >= 6):
                    img.putpixel((x, y), (255, 255, 255))

    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    code = pytesseract.image_to_string(img)

    if (len(code) < 5):
        return None

    code = code[:5]

    replaceDict = {
        "$" : "5",
        "T" : "7",
        "§" : "5",
        "A" : "4",
        "q" : "9"
    }

    newCode = ""
    for c in code:
        newC = replaceDict.get(c, c)
        newCode += newC

    return newCode
