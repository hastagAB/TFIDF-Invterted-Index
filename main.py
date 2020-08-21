from nirjas import extract
import itertools
import argparse
import os
import json
import numpy
import spacy

nlp = spacy.load("en_core_web_sm")

def newtest(filename):
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

   inputFile = filename

   data_file = extract(inputFile)
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
      idf = numpy.log(483 / (len(temp)))
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
       close1 = closest(listscores, score1)
       listscores.remove(close1)
       try:
         close2 = closest(listscores, score1)
         listscores.remove(close2)
         close3 = closest(listscores, score1)
         listscores.remove(close3)
         close4 = closest(listscores, score1)
         listscores.remove(close4)
         close5 = closest(listscores, score1)
         listscores.remove(close5)
         close6 = closest(listscores, score1)
         listscores.remove(close6)
         close7 = closest(listscores, score1)
         listscores.remove(close7)
         close8 = closest(listscores, score1)
         listscores.remove(close8)
         close9 = closest(listscores, score1)
         listscores.remove(close9)
         close10 = closest(listscores, score1)
         listscores.remove(close10)
         close11 = closest(listscores, score1)
         listscores.remove(close11)
         close12 = closest(listscores, score1)
         listscores.remove(close12)
         close13 = closest(listscores, score1)
         listscores.remove(close13)
         close14 = closest(listscores, score1)
         listscores.remove(close14)
         close15 = closest(listscores, score1)
         listscores.remove(close15)
         close16 = closest(listscores, score1)
         listscores.remove(close16)
         close17 = closest(listscores, score1)
         listscores.remove(close17)
         close18 = closest(listscores, score1)
         listscores.remove(close18)
         close19 = closest(listscores, score1)
         listscores.remove(close19)
         close20 = closest(listscores, score1)
         listscores.remove(close20)
         close21 = closest(listscores, score1)
         listscores.remove(close21)
         close22 = closest(listscores, score1)
         listscores.remove(close22)
         close23 = closest(listscores, score1)
         listscores.remove(close23)
         close24 = closest(listscores, score1)
         listscores.remove(close24)
         close25 = closest(listscores, score1)
         listscores.remove(close25)
         close26 = closest(listscores, score1)
         listscores.remove(close26)
         close27 = closest(listscores, score1)
         listscores.remove(close27)
         close28 = closest(listscores, score1)
         listscores.remove(close28)
         close29 = closest(listscores, score1)
         listscores.remove(close29)
         close30 = closest(listscores, score1)
         listscores.remove(close30)



       except:
          pass
       for i in temp1:
          if i[1] == close1:
             final.append(i[0])
          elif i[1] == close2:
             final.append(i[0])
          elif i[1] == close3:
             final.append(i[0])
          elif i[1] == close4:
             final.append(i[0])
          elif i[1] == close5:
             final.append(i[0])
          elif i[1] == close6:
             final.append(i[0])
          elif i[1] == close7:
             final.append(i[0])
          elif i[1] == close8:
             final.append(i[0])
          elif i[1] == close9:
             final.append(i[0])
          elif i[1] == close10:
             final.append(i[0])
          elif i[1] == close11:
             final.append(i[0])
          elif i[1] == close12:
             final.append(i[0])
          elif i[1] == close13:
             final.append(i[0])
          elif i[1] == close14:
             final.append(i[0])
          elif i[1] == close15:
             final.append(i[0])
          elif i[1] == close16:
             final.append(i[0])
          elif i[1] == close17:
             final.append(i[0])
          elif i[1] == close18:
             final.append(i[0])
          elif i[1] == close19:
             final.append(i[0])
          elif i[1] == close20:
             final.append(i[0])
          elif i[1] == close21:
             final.append(i[0])
          elif i[1] == close22:
             final.append(i[0])
          elif i[1] == close23:
             final.append(i[0])
          elif i[1] == close24:
             final.append(i[0])
          elif i[1] == close25:
             final.append(i[0])
          elif i[1] == close26:
             final.append(i[0])
          elif i[1] == close27:
             final.append(i[0])
          elif i[1] == close28:
             final.append(i[0])
          elif i[1] == close29:
             final.append(i[0])
          elif i[1] == close30:
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
