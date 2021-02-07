def to_long(string):
    """
    :param string: input string
    :return: Long integer, if input is invalid, return None
    :limitation: string must consists of of numbers and optional single "+" or "-" which is indicating sign.
                 Otherwise would return None. The maximum number is unbounded.
    """
    if string and isinstance(string, str):
        first_char = string[0]
        sign, result = 1, 0L
        if first_char == '+':
            sign = 1
            string = string[1:]
        elif first_char == '-':
            sign = -1
            string = string[1:]
        for char in string:
            result *= 10
            try:
                result += int(char)
            except:
                return None
        return result * sign
