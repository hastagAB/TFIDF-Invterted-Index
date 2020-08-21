from nirjas import extract
import itertools
import os
import json
import numpy
import spacy

nlp = spacy.load("en_core_web_sm")

customize_stop_words = [
    ',', ':', ';', '.', ' ', "'",'/','(',')','<','>','\n','\"','-','*'
]

def licenseComment(data):
    list = ['source', 'free', 'under','use',  'copyright', 'grant', 'software', 'license','licence', 'agreement', 'distribute', 'redistribution', 'liability', 'rights', 'reserved', 'general', 'public', 'modify', 'modified', 'modification', 'permission','permitted' 'granted', 'distributed', 'notice', 'distribution', 'terms', 'freely', 'licensed', 'merchantibility','redistributed', 'see', 'read', '(c)', 'copying', 'legal', 'licensing', 'spdx']

    MLmapCount, CSLmapCount, SLmapCount = [], [], []
    comment = ""
    tempCount = 0
    for id, item in enumerate(data[0]["multi_line_comment"]):
        count = 0
        if 'spdx-license-identifier' in item['comment'].lower():
            return item['comment']

        for i in list:
            if i in item['comment'].lower():
                count+=1

        if count > tempCount:
            tempCount = count
            comment = item['comment']

    if "cont_single_line_comment" in data[0]:
      for id, item in enumerate(data[0]["cont_single_line_comment"]):
          count = 0
          if 'spdx-license-identifier' in item['comment'].lower():
              return item['comment']

          for i in list:
              if i in item['comment'].lower():
                  count+=1
          if count > tempCount:
              tempCount = count
              comment = item['comment']

    if "single_line_comment" in data[0]:
      for id, item in enumerate(data[0]["single_line_comment"]):
          count = 0
          if 'spdx-license-identifier' in item['comment'].lower():
              return item['comment']

          for i in list:
              if i in item['comment'].lower():
                  count+=1
          if count > tempCount:
              tempCount = count
              comment = item['comment']
        
    return comment

for w in customize_stop_words:
    nlp.vocab[w].is_stop = True

def tokenize(article):
  doc = nlp(article)
  tokens = [(token.text).lower() for token in doc if not token.is_stop]
  return tokens

x = {}
testcount = 0

for (root, dirs, files) in os.walk("text", topdown=True):

    for file in files:
        filepath = root + os.sep + file

        with open(filepath, encoding="utf8", errors='ignore') as f:

            testcount += 1
            print(testcount)

            data_file = extract(filepath)
            data = json.loads(data_file)
            data1 = licenseComment(data)
            terms = tokenize(data1)
            with open('InvertedIndex.json') as f:
                y = json.load(f)
            new = {k:v for k, v in y.items() if k in terms}
            keywords = list(new.keys())


            for word in keywords: 
                tf = (terms.count(word)) / (len(terms))
                temp = set(new.get(word))
                idf = numpy.log(483 / (len(temp)))
                if word not in x:
                    x[word] = []
                    x[word].append([file.rsplit( ".",1)[0], tf*idf])

                elif word in x.keys():
                    x[word].append([file.rsplit( ".",1)[0], tf*idf])


with open('InvertedIndexWithTFIDF.json', 'w') as file:
     file.write(json.dumps(x, indent=4))

print('completed!')


