from ctypes import c_byte


class TokenType(c_byte):
    # Data types
    WORD = 1            # Обозначение слова
    COMMENT = 2         # Однострочный комментарий (//)
    MULTI_COMMENT = 3   # Многострочный комментарий (/* ... */)
    CHAR = 4            # Символьный литерал (например, 'a')
    STRING = 5          # Строковый литерал (например, "hello world")
    INTEGER = 6         # Целое число (например, 10)
    BYTE = 7            # Байт (-128 до 127)
    HEX = 8             # Шестнадцатеричное число (например, 0xC4)
    LONG = 9            # Длинное целое число (например, 1024010240)
    FLOAT = 10          # Число с плавающей точкой (например, 1.131)
    DOUBLE = 11         # Двойное число (например, 1.1234124)

    # Keys
    PUBLIC = 12         # Ключевое слово "public"
    PRIVATE = 13        # Ключевое слово "private"
    PROTECTED = 14      # Ключевое слово "protected"
    FINAL = 15          # Ключевое слово "final"
    STATIC = 16         # Ключевое слово "static"
    VAR = 17            # Ключевое слово "var" (автоопределение типа)
    FUNC = 18           # Ключевое слово "func"
    CLASS = 19          # Ключевое слово "class"
    INTERFACE = 20      # Ключевое слово "interface"
    ENUM = 21           # Ключевое слово "enum"
    IF = 22             # Ключевое слово "if"
    ELSE = 23           # Ключевое слово "else"
    FOR = 24            # Ключевое слово "for"
    WHILE = 25          # Ключевое слово "while"
    DO_WHILE = 26       # Ключевое слово "do-while"
    BREAK = 27          # Ключевое слово "break"
    CONTINUE = 28       # Ключевое слово "continue"
    RETURN = 29         # Ключевое слово "return"
    USE = 30            # Ключевое слово "use"
    INCLUDE = 31        # Ключевое слово "include"
    FOREACH = 32        # Ключевое слово "foreach"
    MATCH = 33          # Ключевое слово "match"
    CASE = 34           # Ключевое слово "case"

    # Binary symbols
    PLUS = 35           # Оператор сложения (+)
    MINUS = 36          # Оператор вычитания (-)
    MULTI = 37          # Оператор умножения (*)
    DIVIDE = 38         # Оператор деления (/)
    EQ = 39             # Оператор присваивания (=)
    PERCENT = 40        # Оператор остатка от деления (%)
    PLUS_PLUS = 41      # Инкремент (++)
    MINUS_MINUS = 42    # Декремент (--)
    PLUS_EQ = 43        # Оператор сложения и присваивания (+=)
    MINUS_EQ = 44       # Оператор вычитания и присваивания (-=)
    MULTI_EQ = 45       # Оператор умножения и присваивания (*=)
    DIVIDE_EQ = 46      # Оператор деления и присваивания (/=)
    PERCENT_EQ = 47     # Оператор остатка и присваивания (%=)

    # Conditional symbols
    EQ_EQ = 48          # Оператор равенства (==)
    EXC_LEQ = 49        # Оператор неравенства (!=)
    LT = 50             # Оператор "меньше" (<)
    LT_EQ = 51          # Оператор "меньше или равно" (<=)
    GT = 52             # Оператор "больше" (>)
    GT_EQ = 53          # Оператор "больше или равно" (>=)
    AND = 54            # Логическое "и" (and)
    OR = 55             # Логическое "или" (or)
    NOT = 56            # Логическое "не" (not)
    AMP_AMP = 57        # Логическое "и" (&&)
    BAR_BAR = 58        # Логическое "или" (||)
    EXCL = 59           # Логическое "не" (!)
    AMP = 60            # Побитовое "и" (&)
    BAR = 61            # Побитовое "или" (|)
    QUESTION = 62       # Знак вопроса (?)
    COLON = 63          # Двоеточие (:)
    CARET = 64          # Побитовый "исключающее или" (^)
    TILDE = 65          # Побитовая инверсия (~)
    L_PAREN = 66        # Левая круглая скобка (()
    R_PAREN = 67        # Правая круглая скобка ())
    L_BRACKET = 68      # Левая квадратная скобка ([)
    R_BRACKET = 69      # Правая квадратная скобка (])
    L_BRACE = 70        # Левая фигурная скобка ({)
    R_BRACE = 71        # Правая фигурная скобка (})
    COMMA = 72          # Запятая (,)
    SEMICOLON = 73      # Точка с запятой (;)
    PASS = 74           # Пробельный символ (пропуск)

    EOF = 75            # Конец файла (End Of File)

    _names_ = {
        1: "WORD", 2: "COMMENT", 3: "MULTI_COMMENT", 4: "CHAR", 5: "STRING", 6: "INTEGER",
        7: "BYTE", 8: "HEX", 9: "LONG", 10: "FLOAT", 11: "DOUBLE", 12: "PUBLIC",
        13: "PRIVATE", 14: "PROTECTED", 15: "FINAL", 16: "STATIC", 17: "VAR", 18: "FUNC",
        19: "CLASS", 20: "INTERFACE", 21: "ENUM", 22: "IF", 23: "ELSE", 24: "FOR",
        25: "WHILE", 26: "DO_WHILE", 27: "BREAK", 28: "CONTINUE", 29: "RETURN", 30: "USE",
        31: "INCLUDE", 32: "FOREACH", 33: "MATCH", 34: "CASE", 35: "PLUS", 36: "MINUS",
        37: "MULTI", 38: "DIVIDE", 39: "EQ", 40: "PERCENT", 41: "PLUS_PLUS", 42: "MINUS_MINUS",
        43: "PLUS_EQ", 44: "MINUS_EQ", 45: "MULTI_EQ", 46: "DIVIDE_EQ", 47: "PERCENT_EQ", 48: "EQ_EQ",
        49: "EXC_LEQ", 50: "LT", 51: "LT_EQ", 52: "GT", 53: "GT_EQ", 54: "AND",
        55: "OR", 56: "NOT", 57: "AMP_AMP", 58: "BAR_BAR", 59: "EXCL", 60: "AMP",
        61: "BAR", 62: "QUESTION", 63: "COLON", 64: "CARET", 65: "TILDE", 66: "L_PAREN",
        67: "R_PAREN", 68: "L_BRACKET", 69: "R_BRACKET", 70: "L_BRACE", 71: "R_BRACE", 72: "COMMA",
        73: "SEMICOLON", 74: "PASS", 75: "EOF"
    }

    def name(self):
        return TokenType._names_.get(self.value, "UNKNOWN")
