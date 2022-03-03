from .GetCode.GetCodeClass import GetCode


class Commands:
    def __init__(self) -> None:
        self.commands = {
            # импорты
            "import": self.himport,

            # коментарий
            "#": self.hskip, # команда которая не исполняется, нужна для комментариев

            # команды переменных
            "int": self.hint,
            "str": self.hstr,
            "flt": self.hflt,

            "copy": self.hcopy,

            # оутпут и инпут
            "print": self.hprint,     # вывод в консоль
            "println": self.hprintln, # вывод в консоль с переносом строки
            "input": self.hinput,     # ввод с консоли
            "inputln": self.hinputln, # ввод с консоли с новой строки

            # циклы
            "goto": self.hgoto, # цикл goto
            "revers": self.hrevers, # меняет чтение кода сверху в них на снизу в верх, и на оборот

            # арифметика
            "inc": self.hinc, # x++
            "dec": self.hdec, # x--
            "add": self.hadd, # x += y
            "sub": self.hsub, # x -= y
            "mul": self.hmul, # x *= y
            "div": self.hdiv, # x /= y

            # логика
            "noq": self.hnoq, # res = x !=  y
            "and": self.hand, # res = x and y == c
            "or": self.hor,   # res = x or  y == c
            "not": self.hnot  # res = not x
        }
    
    def hrevers(self, elements, args):
        if elements["vars"][args[1]]:
            if args[0] == "top":
                elements["line_trand"] = -1
            elif args[0] == "down":
                elements["line_trand"] = 1
        return elements
    
    def himport(self, elements, args):
        new_code = {}
        for src in args:
            new_code = new_code | GetCode(src + ".hex").code
        self.code = self.code | new_code
        return elements

    def hnot(self, elements, args):
        elements["vars"][args[0]] = not \
        elements["vars"][args[1]]
        return elements
    
    def hor(self, elements, args):
        elements["vars"][args[3]] =   \
        elements["vars"][args[0]] or  \
        elements["vars"][args[1]] ==  \
        elements["vars"][args[2]]
        return elements
    
    def hand(self, elements, args):
        elements["vars"][args[3]] =   \
        elements["vars"][args[0]] and \
        elements["vars"][args[1]] ==  \
        elements["vars"][args[2]]
        return elements
    
    def hnoq(self, elements, args):
        elements["vars"][args[2]] =  \
        elements["vars"][args[0]] != \
        elements["vars"][args[1]]
        return elements
    
    def hadd(self, elements, args):
        elements["vars"][args[0]] += \
        elements["vars"][args[1]]
        return elements
    
    def hsub(self, elements, args):
        elements["vars"][args[0]] -= \
        elements["vars"][args[1]]
        return elements
    
    def hmul(self, elements, args):
        elements["vars"][args[0]] *= \
        elements["vars"][args[1]]
        return elements
    
    def hdiv(self, elements, args):
        elements["vars"][args[0]] /= \
        elements["vars"][args[1]]
        return elements
    
    def hinc(self, elements, args):
        elements["vars"][args[0]] += 1
        return elements
    
    def hdec(self, elements, args):
        elements["vars"][args[0]] -= 1
        return elements
    
    def hcopy(self, elements, args):
        elements["vars"][args[0]] = \
        elements["vars"][args[1]]
        return elements

    def hgoto(self, elements, args):
        if elements["vars"][args[1]]:
            elements["line"] = elements["labels"][args[0]]
        return elements

    def hprintln(self, elements, args):
        print(
            "".join(
                [str(elements["vars"][arg])
                for arg in args]
            )
        )
        return elements
    
    def hprint(self, elements, args):
        print(
            "".join(
                [str(elements["vars"][arg])
                for arg in args]
            ), end=""
        )
        return elements
    
    def hinput(self, elements, args):
        elements["vars"][args[0]] = \
        input(elements["vars"][args[1]])
        return elements
    
    def hinputln(self, elements, args):
        elements["vars"][args[0]] = \
        input("\n" + elements["vars"][args[1]])
        return elements
    
    def hint(self, elements, args):
        elements["vars"][args[0]] = int(args[1])
        return elements
    
    def hstr(self, elements, args):
        elements["vars"][args[0]] = args[1]
        return elements
    
    def hflt(self, elements, args):
        elements["vars"][args[0]] = float(args[1])
        return elements

    def hskip(self, elements, args):
        return elements