# Regular expressions

# ​With regular expressions, we'll be able to find and operate on texts in a more ​flexible way than we have up until this point.

# What are regular expression?
# A regular expression, also known as regex or regexp, is essentially a search ​query for text that's expressed by string pattern. ​When you run a search against a particular piece of text, anything that ​matches a regular expression pattern you specified, is returned as a result ​of the search. Regular expressions let you answer the questions like what are ​all the four-letter words in a file? ​Or how many different error types are there in this error log?

# module name re
import re

log = []

resurlt = re.search(r'error', log)
print(resurlt)


# alternative workspace is linux known as grep, sed etc.

# wild-cards
# dot (.), ^ and $ are wild cards of regex
# re.search(r'p.n', 'python')  # This will return python

# Character Classes
# It lets you serarch in a define set of ways in [] brackets.
# re.search(r'[pP]ython#, 'Python')
# re.search(r'coudy[a-zA-Z]', 'cloudy9')#