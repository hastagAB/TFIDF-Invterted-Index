from nirjas import extract
import itertools
import argparse
import os
import json
import numpy
import spacy

nlp = spacy.load("en_core_web_sm")

def newtest(filename):


   def licenseComment(data):
      '''
      function to extract only the relevant comment(i.e license text) from the input file
      '''

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


   customize_stop_words = [
      ',', ':', ';', '.', ' ', "'",'/','(',')','<','>','\n','\"','-','*'
   ]

   for w in customize_stop_words:
      nlp.vocab[w].is_stop = True

   def tokenize(article):
      doc = nlp(article)
      tokens = [(token.text).lower() for token in doc if not token.is_stop]
      return tokens

   inputFile = filename

   data_file = extract(inputFile) # Extract Comment using Nirjas
   data = json.loads(data_file) 
   data1 = licenseComment(data)

   x = tokenize(data1)

   with open('InvertedIndexWithTFIDF.json') as f:
      y = json.load(f)

   with open('InvertedIndex.json') as f:
      z = json.load(f)

   old = {k:v for k, v in z.items() if k in x}
   new = {k:v for k, v in y.items() if k in x}

   keywords = list(new.keys())

   tfidfList = {}
   total_terms = len(x)
   for word in keywords:
      tf = (x.count(word)) / (total_terms)
      temp = set(old.get(word))
      idf = numpy.log(484 / (len(temp))) 
      tfidfList[word] = tf*idf

   
   def closest(lst, K): 
      return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))] 
   
   final = []

   for words in keywords:
       score1 = tfidfList[words]
       temp1 = new[words]
       listscores = []
       for i in temp1:
         listscores.append(i[1])
       close = []
       for _ in range(31): # for taking top 30 closest tfidf score results
          try:
            temp = closest(listscores, score1)
            close.append(temp)
            listscores.remove(temp)
          except:
             pass

       for i in temp1:
          for _ in range(31):
             if i[1] in close:
                final.append(i[0])

   result = max(final,key=final.count)
   return result

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("inputFile", help="Specify the input file which needs to be scanned")

  args = parser.parse_args()
  filename = args.inputFile

  result = newtest(filename)

  matches = []

  matches.append({
      'shortname': result,
      'sim_score': 1,
      'sim_type': "InvertedIndexWithTFIDF",
      'description': ""
      })

  result = matches
  result = list(result)
  result = {"file": os.path.abspath(filename), "results": result}
  result = json.dumps(result, sort_keys=True, ensure_ascii=False, indent=4)
  print(result)
