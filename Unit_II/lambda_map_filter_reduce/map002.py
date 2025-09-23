# With map() functions, it's not only easier, but it's also much more flexible.
languages = ['java','python','c','c++','pearl','php']
lst = []

for language in languages:
    language = language.upper()
    lst.append(language)

print(lst)





languages = ['java','python','c','c++','pearl','php']
x = map(str.upper, languages)
print(list(x))