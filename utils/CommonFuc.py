import re
from typing import Optional
import PySide6.QtCore
from PySide6.QtGui import QValidator

class SteelTpyeValidator(QValidator):
    def validate(self, input_text, pos):
        if re.match(r'^[^\u4e00-\u9fa5\s]*$', input_text):
            return QValidator.Acceptable
        elif input_text == '' or input_text[pos-1] in '+-':
            return QValidator.Intermediate
        else:
            return QValidator.Invalid

    def fixup(self, input_text):
        filtered_text = re.sub(r'[\u4e00-\u9fa5\s]', '', input_text)
        return filtered_text
    
    
    
    
class ParamValidator(QValidator):
    
    def validate(self, input_text, pos):
        if re.match(r'^[+-]?(\d+(\.\d{0,3})?|\.\d{0,3})?$', input_text):
            return QValidator.Acceptable
        elif input_text == '' or input_text[pos-1] in '+-':
            return QValidator.Intermediate
        else:
            return QValidator.Invalid

    def fixup(self, input_text):
        filtered_text = re.sub(r'[^+-\d.]', '', input_text)
        return filtered_text