# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:44:45 2017

@author: nausheenfatma
"""
import ast
import re

""" In a Wiki XML data, phrases within double brackets are Wikipedia page links as well as DBpedia entity names.
    So we process each sentence and replace phrases within double brackets as a single token 
    by concatenating them with a an underscore.
    
    
    For example : A sample string from a Wiki XML (in lowercase) is :
    
   "autism is one of the five [[pervasive developmental disorder]]s (pdd), which are characterized by widespread abnormalities of social interactions and communication, and severely restricted interests and highly repetitive behavior.    
   of the five pdd forms, [[asperger syndrome]] is closest to autism in signs and likely causes; [[rett syndrome]] and [[childhood disintegrative disorder]] share several signs with autism, but may have unrelated causes." 

    We preprocess and convert the string into below string :

   "autism is one of the five pervasive_developmental_disorder s (pdd), which are characterized by widespread abnormalities of social interactions and communication, and severely restricted interests and highly repetitive behavior.    
   of the five pdd forms, asperger_syndrome is closest to autism in signs and likely causes; rett_syndrome and childhood_disintegrative_disorder share several signs with autism, but may have unrelated causes." 

    We use the function process_sentence_for_entities defined in this file for the same.

   Thus each wikipage link tokens (which is also a dbpedia entity) become  one atomic token. We will train the word2vec on this edited sentences. This will give us word2vec embeddings for dbpedia entities.

"""

class PagesToSentences:

      def __init__(self):
              self.sentencefilename="../temp/sentences.txt"
      
      def processWikiPagesData(self,filename):
        sentences_file=open(self.sentencefilename,"w")  
        f=open(filename)
        k=0
        for line in f:
            k=k+1
            if k>10:
                break        
            try:
                page_dict=ast.literal_eval(line)
                
                for line in page_dict["text"]: #page_dict["text"] is a list of sentences in a wikipedia page
                    #print line
                    newline=self.process_sentence_for_entities(line)
                    sentences_file.write(newline)
                
                
            except:
                pass
        sentences_file.close()
        
        
        
      def process_sentence_for_entities(self,sentence): 
            pattern=r'(\[\[)[^]]*(\]\])'
            entities_indices=[(m.start(0), m.end(0)) for m in re.finditer(pattern, sentence)]
            for item in entities_indices:
                (beg,end)=item
                entity_string=sentence[beg:end]
                entity_string=entity_string.split("|")[0]
                new_entity_string = "_".join(entity_string.split())
                sentence = sentence[0:beg] + new_entity_string + sentence[end:] 
    
            sentence=sentence.replace("[["," ")
            sentence=sentence.replace("]]"," ")
            return sentence
    
            
#def processWikiPage()
if __name__ == "__main__":
  x=  PagesToSentences()
  x.processWikiPagesData("../output/parsed_wiki_pages.txt")
