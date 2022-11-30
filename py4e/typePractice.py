# Showing how to change types from string to int
sval = '123'
print(sval)
print(type(sval))

ival = int(sval)
print(ival)
print(type(ival))

# Showing how to change types from string to float
sval2 = '456'
print(sval2)
print(type(sval2))

ival2 = float(sval2)
print(ival2)
print(type(ival2))

# If eever you run into a string that has escaped characters you can remove them with text_after = re.sub(regex_search_term, regex_replacement, text_before)
