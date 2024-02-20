import pytest
from mesita.prettytable import PrettyTable
import mesita
import itertools
from mesita import Mesita


def test_table_with_color():
    table = PrettyTable()
    table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    table.add_row([mesita.format_string("Adelaide", ["bold", "blue"]), 1295, 1158259, 600.5])
    table.add_row(["Brisbane", 5905, 1857594, 1146.4])
    print("\n" + table.get_string())


def test_print_tables():
    table = PrettyTable()
    table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    table.add_row(["Adelaide", 1295, 1158259, 600.5])
    table.add_row(["Brisbane", 5905, 1857594, 1146.4])
    print("\n" + table.get_string())
    table = PrettyTable()
    table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    table.add_row(["Adelaide", 1300, 1158259, 600.5])
    table.add_row(["Brisbane", 5905, 1857594, 1148])
    print("\n" + table.get_string())


def test_as_columns():
    field_names1 = ["City name", "Area", "Population", "Annual Rainfall"]
    rows1 = [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4]
    ]
    rows2 = [
        ["Adelaide", 1300, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1148]
    ]
    m = Mesita(field_names1, rows1, rows2, ["nc"], ["red", "bold"], lambda x, y: x == y)
    print("\n" + m.as_columns())


def test_side_by_side():
    field_names1 = ["City name", "Area", "Population", "Annual Rainfall"]
    rows1 = [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4]
    ]
    rows2 = [
        ["Adelaide", 1300, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1148]
    ]
    m = Mesita(field_names1, rows1, rows2, ["nc"], ["red", "bold"], lambda x, y: x == y)
    print("\n" + m.side_by_side())


def test_smush_table():
    field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    rows1 = [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4]
    ]
    rows2 = [
        ["Adelaide", 1300, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1148]
    ]
    m = Mesita(field_names, rows1, rows2, ["nc"], ["red", "bold"], lambda x, y: x == y)
    print("\n" + m.smush())
