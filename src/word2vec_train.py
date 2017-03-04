# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 10:31:53 2017

@author: nausheenfatma
"""


from gensim.models import word2vec

class Word2VecTraining:
    
    def train(self,filepath,modelname,vocabpath):

        sentence=word2vec.LineSentence(filepath)
        
        model=word2vec.Word2Vec(sentence, sg=1,workers=5,size=100,min_count=2,window=5)
        
        model.init_sims(replace=True)
        model.save(modelname)
        
        #print model.vocab.items()
        vocab_file=open(vocabpath,"w")
        for word, vocab_obj in model.vocab.items():
            vocab_file.write(word+"\t"+str(model[word].tolist())+"\n")
            
            
        vocab_file.close()    

if __name__ == "__main__":
    w2v=Word2VecTraining()
    w2v.train("../output/sentences.txt","../output/model","../output/vocab.txt")
    #main()

