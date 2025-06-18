# comment
# comment

# comment

line = ["was", "", "# ", "as", "baba"]
i = 0
for x in line:
    if len(x) == 0:
        continue
    elif x.startswith("# "):
        continue
    else:
        i += 1
print(i)