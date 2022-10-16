import re

regex = re.compile(r'(?<=abc)def')
print(regex.search("abcdef").group())

regex = re.compile(r'.*(?<=abc)def')
print(regex.match("sssabcdef").group())

regex = re.compile(r'(?:set|let) var = (\w+|\d+)')
print(regex.match("set var = 12").groups())
