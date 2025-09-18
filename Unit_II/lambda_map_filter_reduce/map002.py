# With map() functions, it's not only easier, but it's also much more flexible.
languages = ['java','python','c','c++','pearl','php']
x = map(str.upper, languages)
print(list(x))