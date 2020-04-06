from textblob import TextBlob
import sys
import os

file = open(sys.argv[1], "r")
text = file.read()

unicode_content = text.decode('utf-8')
xml_content = unicode_content.encode('ascii', 'xmlcharrefreplace')

blob = TextBlob(xml_content)

output = ""
synonyms = set()
for word in blob.words:
    for synset in word.synsets:
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())

for syn in synonyms:
    output += syn + "\n"

with open('synonyms.txt', 'w') as outfile:
    outfile.write(output)

print("New file: "+os.getcwd()+"/synonyms.txt")