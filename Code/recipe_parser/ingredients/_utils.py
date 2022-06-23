import re


def cleanhtml(raw_html: str) -> str:
    """
    """
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext


def stardardize_input(string: str) -> str:
    """Use regex to normalize string to standard input to make parsing simple
    """
    pass


# String Methods
def decimal_to_string(decimal):
    """
    """
    # Don't love this
    problem_fractions = {0.13: "1/8", 0.67: "2/3", 0.33: "1/3"}
    if decimal in problem_fractions:
        return problem_fractions.get(decimal)

    ratio = float(decimal).as_integer_ratio()
    return "/".join(str(d) for d in ratio)


def string_to_decimal(string):
    """
    """
    numbers = string.split("/")
    return float(numbers[0]) / float(numbers[1])


def _process_and_colloquial(string):
    """
    """
    measurements = {"third": "1/3", "half": "1/2", "quarter": "1/4", "fourth": "1/4"}
    splits = string.split(" and a ")
    return float(splits[0]) + measurements.get(splits[1], "")


def _process_and(string):
    """
    """
    splits = string.split(" and ")
    return float(splits[0]) + string_to_decimal(splits[1])


def _process(string):
    """
    """
    splits = string.split(" ")
    return float(splits[0]) + string_to_decimal(splits[1])


def string_to_float(string):
    """
    NOT GOOD NAMING
    """
    patterns = ["\d+\s(and)\s\d\/\d", "\d+\s\d\/\d"]
    pattern_dict = {"\d+\s(and)\s\d\/\d": _process_and, "\d+\s\d\/\d": _process}

    for pattern in patterns:
        pt = re.compile(pattern)
        match = re.search(pt, string)
        if match:
            return pattern_dict[pattern](match.group())

    return 0


def reformat_string(string):
    """
    """
    patterns = ["\d+\s(and)\s\d\/\d", "\d+\s\d\/\d", "\d+\/\d+", "\d+"]
    pattern_dict = {
        "\d+\s(and)\s\d\/\d": lambda x: float_to_string(_process_and(x)),
        "\d+\s\d\/\d": lambda x: x,
        "\d+\/\d+": lambda x: x,
        "\d+": lambda x: x,
    }

    for pattern in patterns:
        pt = re.compile(pattern)
        match = re.search(pt, string)
        if match:
            return pattern_dict[pattern](match.group())

    return 0


def float_to_string(value):
    """
    """
    if value < 1:
        if (value - int(value)) < 0.001:
            return str(0)

        return decimal_to_string(value)

    if value == 1:
        return str(1)

    else:
        if (value - int(value)) < 0.001:
            return str(int(value))

        return "{} {}".format(
            str(int(value)), decimal_to_string(round(value - int(value), 2))
        )


named = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}
quarter = {0.25: "quarter", 0.33: "third", 0.5: "half"}


def float_to_regex(value, error_str="-1"):
    """
    """
    if value < 1:
        if value < 0.001:
            return [str(0)]

        return [decimal_to_string(value)]

    if value == 1:
        return [str(1), "one"]

    else:
        if (value - int(value)) < 0.001:
            if value < 10:
                return [str(int(value)), named[int(value)]]

            else:
                return [str(int(value))]

        a = "{} {}".format(
            str(int(value)), decimal_to_string(round(value - int(value), 2))
        )
        b = "{} and {}".format(
            str(int(value)), decimal_to_string(round(value - int(value), 2))
        )
        c = "{} and a {}".format(
            str(int(value)), quarter.get(round(value - int(value), 2), error_str)
        )
        return [a, b, c]
