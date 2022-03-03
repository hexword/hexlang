import sys
from src.Commands import Commands
from src.GetCode.GetCodeClass import GetCode


class Main(Commands):
    def __init__(self) -> None:
        src = sys.argv[1]

        self.code = GetCode(src).code
        Commands.__init__(self)

        # запуск основной функции
        self.RunFunction(
            "main", {}, []
        )

    def RunFunction(self, name: str, func_elements_vars, args):

        # парс функции
        content = self.code[name]["content"]
        content_len = len(content) - 1

        # инициализация переменных для чтения функции
        func_elements = {
            "vars": {},
            "labels": self.code[name]["labels"],
            "line": 0,
            "line_trand": 1
        }

        # добавление указаных переменных в запущеную функцию
        fargs = self.code[name]["args"]
        if fargs:
            for i in range(0, len(fargs)):
                func_elements["vars"][fargs[i]] = func_elements_vars[args[i]]

        # запуск команд функции
        while func_elements["line"] < content_len + 1 \
        and func_elements["line"] > -1:
            
            # исполнение команды
            content_line = content[func_elements["line"]]
            if content_line[0] in self.commands:
                func_elements = self.commands[content_line[0]](
                    func_elements, content_line[1]
                )

            # если вызов функции на языке hexlang
            elif content_line[0] in self.code:
                name, f_vars, args = self.RunFunction(
                    content_line[0],
                    func_elements["vars"],
                    content_line[1]
                )

                # получение значений исполненой функции
                fargs = self.code[name]["args"]
                if fargs:
                    for i in range(0, len(fargs)):
                        func_elements["vars"][args[i]] = f_vars[fargs[i]]

            # сдвиг чтения кода по его тренду
            func_elements["line"] += func_elements["line_trand"]
            
        return name, func_elements["vars"], args


if __name__ == '__main__':
    Main()
