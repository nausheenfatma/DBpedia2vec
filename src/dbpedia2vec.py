# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 11:05:03 2017

@author: nausheenfatma
"""
import sys
import logging
import argparse
from XMLCustomParser import *
from JsonPagesToCleanSentences import *
from word2vec_train import *

def main():
  parser = argparse.ArgumentParser(prog="DBpedia2vec", 
                                    description="DBpedia2vec embeddings training using Wikipedia dump",
                                    formatter_class=argparse.RawTextHelpFormatter)
  parser.add_argument('--i', metavar='wikipedia xml input file', dest="INFILE", type=str, default=sys.stdin, help="<input-file>", required=True,)
  args = parser.parse_args()

  
  #STEP 1 : parsing wiki documents from xml
  a=WikiXmlHandler()
  a.parse(args.INFILE)
  print "Step 1 complete"
  
  #STEP 2 : reading wkidocuments and joining the page link tokens with underscore into a single token
  x=PagesToSentences()
  x.processWikiPagesData(a.pages_file)
  print "Step 2 complete"
  
  #STEP 3 : word2vec training of sentences
  w2v=Word2VecTraining()
  w2v.train(x.sentencefilename,"../output/model","../output/vocab.txt")  
  print "Step 3 complete. Check output folder!!"
    
if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    logging.basicConfig()
    start_time=time.time()
    main()
