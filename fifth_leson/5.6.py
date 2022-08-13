import re

with open("5.6_source.txt", "r", encoding="utf-8") as f:
    lessons = [l.strip().split(":") for l in f.readlines()]

result = dict()
for name, l_count in lessons:
    l_sum = sum(list(map(int, re.findall("\d+", l_count))))
    result[name] = l_sum

print(result)

