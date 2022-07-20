my_type_list = [
    78, 2.25, 7 + 1j, "text",
    ["1", 2], (1, "2"), {3, 9, 7},
    {"first": 1, "second": 2}, False,
    b"text", bytearray(b'text'), None
]

for i in my_type_list:
    print(type(i))
