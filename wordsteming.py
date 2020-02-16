from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ['python','pythoner','pythoning','pythoned','pythonly']


new_text = """
Java specifies a default way in which objects can be serialized. Java classes can override this default behavior.
Custom serialization can be particularly useful when trying to serialize an object that has some unserializable attributes.
This can be done by providing two methods inside the class that we want to serialize
"""

words = word_tokenize(new_text)
for w in words:
    print(ps.stem(w))
