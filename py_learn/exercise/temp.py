import re

question = """
From: author@example.com
User-Agent: Thunderbird 1.5.0.9 (X11/20061227)
MIME-Version: 1.0
To: editor@example.com
"""

# extract mail id
pattern = re.compile(r'', re.MULTILINE)

matcher = pattern.finditer(question)

for match in matcher:
    pass
    # print(match.span(), match.group())

p = re.compile('(a(b)c)d')
m = p.match('abcd')

# find double word in the string
mystr = """This is the the string the the so sad sad"""

p = re.compile(r'\b(\w+)\s\1\b', re.MULTILINE)
m = p.finditer(mystr)

# for i in m:
#     print(i.span())

#Non-capturng and named groups

p = re.compile(r'([abc])+')
m = p.finditer("abc")


#named groups

p = re.compile(r'(?P<first>\w*) (?P<last>\w+)')
m = p.match("sujeet Kumar")

# print(m.groupdict())
#

#split
p = re.compile(r'\W+')
m = p.split('sujeet ( kumar ( )')


#subn and sub for replacement

p = re.compile(r'(blue|red|white)')
m = p.subn('color', "this is red white and blue color")


p = re.compile(r'ma*n')
m = p.match('main')

print(m.span())

if __name__ == '__main__':
    print('running...')
