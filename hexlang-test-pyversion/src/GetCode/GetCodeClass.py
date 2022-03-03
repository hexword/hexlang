from .mods.PreparationCode import \
               PreparationCode as \
              _PreparationCode
from .mods.ParseFunctions import \
               ParseFunctions as \
              _ParseFunctions


class GetCode:
    def __init__(self, src) -> dict:
        
        # получить файл с кодом
        code = open(
            src, "r",
            encoding = "utf-8"
        ).readlines() # перевести его в список с строками
        
        # Обработка
        code = _PreparationCode(code)
        self.code = _ParseFunctions(code)
