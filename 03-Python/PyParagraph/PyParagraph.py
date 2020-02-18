# PyParagraph - Michael Campo

import re
import os

# In this challenge, you get to play the role of chief linguist at a local
# learning academy. As chief linguist, you are responsible for assessing the
# complexity of various passages of writing, ranging from the sophomoric
# Twilight novel to the nauseatingly high-minded research article. Having read
# so many passages, you've since come up with a fairly simple set of metrics
# for assessing complexity.

# Your task is to create a Python script to automate the analysis of any such
# passage using these metrics. Your script will need to do the following:

# * Import a text file filled with a paragraph of your choosing.

# read textfile into a string
filepath = os.path.join("raw_data", "paragraph_1.txt")
file = open(filepath, encoding="utf-8")
text = file.read()
file.close()

# * Assess the passage for each of the following:
#   - Approximate word count
#   - Approximate sentence count
#   - Approximate letter count (per word)
#   - Average sentence length (in words)

# analyze the string
letterCount = len(re.split("\S", text))
wordCount = len(re.split("\s", text))
sentenceCount = len(re.split("(?<=[.!?]) +", text))
averageLetterCount = letterCount / wordCount
averageSentenceLength = wordCount / sentenceCount

# * As an example, this passage:
#
#   “Adam Wayne, the conqueror, with his face flung back and his mane like a
#   lion's, stood with his great sword point upwards, the red raiment of his
#   office flapping around him like the red wings of an archangel. And the King
#   saw, he knew not how, something new and overwhelming. The great green trees
#   and the great red robes swung together in the wind. The preposterous
#   masquerade, born of his own mockery, towered over him and embraced the
#   world. This was the normal, this was sanity, this was nature, and he
#   himself, with his rationality, and his detachment and his black frock-coat,
#   he was the exception and the accident a blot of black upon a world of
#   crimson and gold.”
#
# ...would yield these results:
#
#   Paragraph Analysis
#   -----------------
#   Approximate Word Count: 122
#   Approximate Sentence Count: 5
#   Average Letter Count: 4.6
#   Average Sentence Length: 24.0
#

# print the results
print("Paragraph Analysis")
print("-"*18)
print("Approximate Word Count: " + str(wordCount))
print("Approximate Sentence Count: " + str(sentenceCount))
print("Average Letter Count: %.1f" %(averageLetterCount))
print("Average Sentence Length: %.1f"  %(averageSentenceLength))

# * Special Hint: You may find this code snippet helpful when determining
#   sentence length (look into regular expressions if interested in learning
#   more):
#
#   import re
#   re.split("(?<=[.!?]) +", paragraph)
