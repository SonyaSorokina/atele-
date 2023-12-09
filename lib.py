import pywhatkit
from PIL import Image, ImageDraw, ImageFont
from pywhatkit import *
def split_to_fit(text: str, horizontalBounds, **params) -> str:
    text = text.split()
    out_text_lines = [""]
    curr_line = 0
    drawer = ImageDraw.Draw(Image.new("RGB", (0, 0)))
    for word in text:
        if drawer.textlength((out_text_lines[curr_line] + word), font = params["font"]) <= horizontalBounds:
            out_text_lines[curr_line] += word + " "
        else:
            out_text_lines[curr_line] += "\n"
            out_text_lines += [word + " "]
            curr_line += 1
    return "".join(out_text_lines)
class Label():
    info = dict()
    keywords = ["fio", "service", "price", "deadline", "furniture", "metrics"]
    alphabet = {
        "fio": "ФИО: ",
        "service": "Услуга: ",
        "price": "Цена: ",
        "deadline": "Срок: ",
        "furniture": "Фурнитура: ",
        "metrics" : "Мерки: ",
    }
    def __init__(self, **kwargs):
        for variable in self.keywords:
            try:
                self.info[variable] = kwargs[variable]
            except KeyError as e:
                self.info[variable] = None
    def getLabel(self) -> Image:
        x, y = 3508 // 3, 2480 // 2
        # A4 3508x2480
        txt = Image.new("RGB", (x, y), (255, 255, 255))

        d = ImageDraw.Draw(txt)

        font = ImageFont.truetype("cour.ttf", 80)

        output = ""
        for variable in self.keywords:
            if self.info[variable] == None:
                pass
            else:
                output = output + split_to_fit(self.alphabet[variable] + self.info[variable], x - 20, font = font) + "\n"

        d.multiline_text((20, 20), output, fill=(0, 0, 0), font=font, anchor=None, spacing=4, align='left', direction=None, features=None, language=None, stroke_width=0, stroke_fill=None, embedded_color=False, font_size=None)
        return txt

def listService():
    from PyQt5 import QtSql

    dbComboBox = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    dbComboBox.setDatabaseName('serv.db')
    dbComboBox.open()
    model = QtSql.QSqlTableModel()
    model.setTable('service')
    model.select()

    l = []
    for i in range(model.rowCount()):
        dictService = {}
        dictService["Услуга"] = model.index(i, 0).data()
        dictService["Цена"] = model.index(i, 1).data()
        dictService["Фурнитура"] = model.index(i, 2).data()
        dictService["Колво Фурнитуры"] = model.index(i, 3).data()
        l.append(dictService)
    dbComboBox.close()
    del model
    return l

def sendMessage(mobile_number):
    message = "Ваш заказ готов! Вы можете завбрать его"
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile_number, message=message)

'''


# get an image

# make a blank image for the text, initialized to transparent text color
txt = Image.new("RGB", (300, 400), (255, 255, 255))

# get a font
# fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
d.text((10, 10), "Hello", fill=(0, 0, 0))
# draw text, full opacity
d.text((10, 60), "World", fill=(0, 0, 0))

txt.show()
# txt.save(path)

# (818, 818 * 2**0.5)
# 9 labels on A4
'''
