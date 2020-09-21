import re
import pytesseract
import cv2
import numpy
import string
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class OCR:

    # initialize RASA API
    def __init__(self):
        pass

    def ocr_core(self, filename):
        text = pytesseract.image_to_string(Image.open(filename))
        Birthdate_Result = self.Birthdate_isValid(text)
        PanNo_Result = self.PanNo_isvalid(text)
        Full_Name = self.Full_Name(text)
        data = self.Caps_isvalid(text)

        Name = Full_Name[0]
        Father_name = Full_Name[1]

        Name1 = data[-2]
        Father_name1 = data[-1]

        # print("Birth_Date: ", Birthdate_Result)
        # print("PanNo_Result: ", PanNo_Result)
        # print("Full_Name: ", Full_Name)
        # print("Name: ", Name)
        # print("Father_name: ", Father_name)
        # print("data: ", data)
        # print("Name1: ", Name1)
        # print("Father_name1: ", Father_name1)

        name = "Full_Name " + str(Name)
        father = "Father_name " + str(Father_name)
        birth = "Birth_Date " + str(Birthdate_Result)
        pan = "PanNo_Result " + str(PanNo_Result)
        data = "Name" + str(data)
        name1 = "Full_Name1 " + str(Name1)
        father1 = "Father_name1 " + str(Father_name1)

        result = [name,father, birth, pan,data,name1,father1]
        return result

    def Birthdate_isValid(self, readdata):
        Result = re.compile("([0-9]{2}\/[0-9]{2}\/[0-9]{4})")
        Result1 = Result.findall(readdata)
        return Result1

    def PanNo_isvalid(self, readdata):
        Result = re.compile("[A-Za-z]{5}\d{4}[A-Za-z]{1}")
        PanNo = Result.findall(readdata)
        return PanNo

    def Full_Name(self, readdata):

        # Initializing data variable
        name = None
        fname = None
        dob = None
        pan = None
        nameline = []
        dobline = []
        panline = []
        text0 = []
        text1 = []
        text2 = []

        # Searching for PAN
        lines = readdata.split('\n')
        for lin in lines:
            s = lin.strip()
            s = s.rstrip()
            s = s.lstrip()
            text1.append(s)

        # text1 = list(text1)
        text1 = list(filter(None, text1))
        #             print(text1)

        # List Object Returned in the following order

        lineno = 0  # to start from the first line of the text file.

        for wordline in text1:
            xx = wordline.split('\n')
            if ([w for w in xx if re.search(
                    '(INCOME|TAX|GOW|GOVT|GOVERNMENT|OVERNMENT|VERNMENT|DEPARTMENT|EPARTMENT|PARTMENT|ARTMENT|INDIA|NDIA)$',w)]):
                #text1 = list(text1)
                lineno = text1.index(wordline)
                break

        text1 = list(text1)
        text0 = text1[lineno + 1:]
        print(text0)
        return text0

    def Caps_isvalid(self, readdata):
        Result = re.compile("[A-Z]{2,25}\s[A-Z]{2,25}\s[A-Z]{2,25}|[A-Z]{2,25}\s[A-Z]{2,25}|[A-Z]{1,1}\s[A-Z]{2,25}")
        New_PanCardName = Result.findall(readdata)
        print(New_PanCardName)
        return New_PanCardName



