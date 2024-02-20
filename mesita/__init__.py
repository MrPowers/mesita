from dataclasses import dataclass
from mesita.prettytable import PrettyTable
import itertools

def format_string(input, formats):
    formatting = {
        "nc": '\033[0m',  # No Color, reset all
        "bold": '\033[1m',
        "underline": '\033[4m',
        "blink": '\033[5m',
        "blue": '\033[34m',
        "white": '\033[97m',
        "red": '\033[31m',
        "invert": '\033[7m',
        "hide": '\033[8m',
        "black": '\033[30m',
        "green": '\033[32m',
        "yellow": '\033[33m',
        "purple": '\033[35m',
        "cyan": '\033[36m',
        "light_gray": '\033[37m',
        "dark_gray": '\033[30m',
        "light_red": '\033[31m',
        "light_green": '\033[32m',
        "light_yellow": '\033[93m',
        "light_blue": '\033[34m',
        "light_purple": '\033[35m',
        "light_cyan": '\033[36m',
    }
    formatted = input
    for format in formats:
        s = formatting[format]
        formatted = s + str(formatted) + s
    return formatting["nc"] + str(formatted) + formatting["nc"]


class Mesita:
    def __init__(self, field_names, rows1, rows2, match_formats, mismatch_formats, equality_fun):
        self.field_names = field_names
        self.rows1 = rows1
        self.rows2 = rows2
        self.match_formats = match_formats
        self.mismatch_formats = mismatch_formats
        self.equality_fun = equality_fun
    
    def as_columns(self):
        t = PrettyTable(["df1", "df2"])
        zipped = itertools.zip_longest(self.rows1, self.rows2)
        for r1, r2 in zipped:
            res1 = []
            res2 = []
            zipped_row = itertools.zip_longest(r1, r2, self.field_names)
            for cell1, cell2, field_name in zipped_row:
                if self.equality_fun(cell1, cell2):
                    res1.append(f"{field_name}=" + format_string(cell1, self.match_formats))
                    res2.append(f"{field_name}=" + format_string(cell2, self.match_formats))
                else:
                    res1.append(f"{field_name}=" + format_string(cell1, self.mismatch_formats))
                    res2.append(f"{field_name}=" + format_string(cell2, self.mismatch_formats))
            t.add_row([", ".join(res1), ", ".join(res2)])
        return t.get_string()

    def side_by_side(self):
        field_names1 = self.field_names
        field_names2 = list(map(lambda n: f"{n}_2", self.field_names))
        t = PrettyTable(field_names1 + ["|"] + field_names2)
        zipped = itertools.zip_longest(self.rows1, self.rows2)
        for r1, r2 in zipped:
            res1 = []
            res2 = []
            zipped_row = itertools.zip_longest(r1, r2)
            for cell1, cell2 in zipped_row:
                if self.equality_fun(cell1, cell2):
                    res1.append(format_string(cell1, self.match_formats))
                    res2.append(format_string(cell2, self.match_formats))
                else:
                    res1.append(format_string(cell1, self.mismatch_formats))
                    res2.append(format_string(cell2, self.mismatch_formats))
            t.add_row(res1 + ["|"] + res2)
        return t.get_string()

    def smush(self):
        t = PrettyTable(self.field_names)
        zipped = itertools.zip_longest(self.rows1, self.rows2)
        for r1, r2 in zipped:
            res = []
            zipped_row = itertools.zip_longest(r1, r2)
            for cell1, cell2 in zipped_row:
                if self.equality_fun(cell1, cell2):
                    res.append(format_string(cell1, self.match_formats) + " | " + format_string(cell2, self.match_formats))
                else:
                    res.append(format_string(cell1, self.mismatch_formats) + " | " + format_string(cell2, self.mismatch_formats))
            t.add_row(res)
        return t.get_string()
