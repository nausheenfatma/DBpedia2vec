# DBpedia2vec

In order to run the code, goto DBpedia2vec/src folder and run the following command :

    python dbpedia2vec.py --i ../data/sample_wiki_data.xml

Check DBpedia2vec/output folder for the model and the vocab file with corresponding vectors.

In a Wiki XML data, phrases within double brackets are Wikipedia page links (which are also the DBpedia entity names since DBpedia entity names are mapped to their corressponding Wikipedia pages with the same title string).

    
    
For example : A sample string from a Wiki XML (in lowercase) is :
    
    "autism is one of the five [[pervasive developmental disorder]]s (pdd), which are characterized by widespread abnormalities of social interactions and communication, and severely restricted interests and highly repetitive behavior.Of the five pdd forms, [[asperger syndrome]] is closest to autism in signs and likely causes; [[rett syndrome]] and [[childhood disintegrative disorder]] share several signs with autism, but may have unrelated causes." 

We process each sentence and replace phrases within double brackets as a single token by concatenating them with an underscore as below :

    "autism is one of the five pervasive_developmental_disorder s (pdd), which are characterized by widespread abnormalities of social interactions and communication, and severely restricted interests and highly repetitive behavior. Of the five pdd forms, asperger_syndrome is closest to autism in signs and likely causes; rett_syndrome and childhood_disintegrative_disorder share several signs with autism, but may have unrelated causes." 

   Thus, each wikipage link tokens (which is also a dbpedia entity) become  one atomic token. We will train the word2vec on this edited sentences. This will give us embeddings for dbpedia entities as well as simple words occuring in wikipedia.





This project is inspired by a similar work described by https://github.com/idio/wiki2vec
