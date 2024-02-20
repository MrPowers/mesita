# mesita

mesita is a library for printing tables in the terminal.

You can use it to print a table and customize the cells with different font styles and colors.

mesita is also good for diffing two tables and comparing differences.  You can print tables side-by-side or even mix two tables into one.

mesita is leveraged by unit testing libraries like chispa and beavis.

## Format strings in the Terminal

Here's how to print a string that's bold and blue in the Terminal:

```python
mesita.format_string("Adelaide", ["bold", "blue"])
```

## Print table comparisons

Suppose you have the following tables that are similar.  Here is the first table:

```
+-----------+------+------------+-----------------+
| City name | Area | Population | Annual Rainfall |
+-----------+------+------------+-----------------+
|  Adelaide | 1295 |  1158259   |      600.5      |
|  Brisbane | 5905 |  1857594   |      1146.4     |
+-----------+------+------------+-----------------+
```

Here is the other table:

```
+-----------+------+------------+-----------------+
| City name | Area | Population | Annual Rainfall |
+-----------+------+------------+-----------------+
|  Adelaide | 1300 |  1158259   |      600.5      |
|  Brisbane | 5905 |  1857594   |       1148      |
+-----------+------+------------+-----------------+
```

**Tables as two columns**

Here's how to print the tables as two columns:

```
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
```

![two_columns](https://github.com/MrPowers/mesita/blob/main/images/two_columns.png)

**Tables side-by-side**

Here's how to print the tables side-by-side:

```python
m = Mesita(field_names1, rows1, rows2, ["nc"], ["red", "bold"], lambda x, y: x == y)
print("\n" + m.side_by_side())
```

![side_by_side](https://github.com/MrPowers/mesita/blob/main/images/side_by_side.png)

**Tables combined into one**

And here's how to print the tables combined into a single table:

```python
m = Mesita(field_names, rows1, rows2, ["nc"], ["red", "bold"], lambda x, y: x == y)
print("\n" + m.smush())
```

![smush](https://github.com/MrPowers/mesita/blob/main/images/smush.png)
