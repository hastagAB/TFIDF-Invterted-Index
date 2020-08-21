#!/usr/bin/env python3
'''
MIT License Copyright (c) 2020 Ayush Bhardwaj (classicayush@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice (including the next
paragraph) shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import itertools
import os
import json
import spacy

nlp = spacy.load("en_core_web_sm")

customize_stop_words = [
    ',', ':', ';', '.', ' ', "'",'/','(',')','<','>','\n','\"','-','*'
]

for w in customize_stop_words:
    nlp.vocab[w].is_stop = True

def tokenize(article):
  doc = nlp(article)
  tokens = [(token.text).lower() for token in doc if not token.is_stop]
  return tokens

x = {}
filecount = 0

for (root, dirs, files) in os.walk("text", topdown=True):

    for file in files:
        filepath = root + os.sep + file

        with open(filepath, encoding="utf8", errors='ignore') as f:
            filecount += 1
            print(filecount)

            for lineNumber, line in enumerate(f):
                line = line.lower() 
                words = tokenize(line) 

                for word in words: 
                    if word not in x:
                        x[word] = []
                        x[word].append(file.rsplit( ".",1)[0])

                    elif word in x.keys():
                        x[word].append(file.rsplit( ".",1)[0])

with open('InvertedIndex.json', 'w') as file:
     file.write(json.dumps(x, indent=4))

