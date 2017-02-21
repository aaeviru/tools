# tools  
2017/02/20

---------------------------------------------------
tools:
        Python 2.7.11
        ChaSen version 2.4.5
        perl version 5.005_04 with jperl5.005_03-20000401
library:
        geta32
        numpy
        scipy
dataset:
        NTCIR Publication of unexamined patent applications
        wordnet ver 1.1
        ntc6pat(topic)


---------------------------------------------------  
python * -h  or  python * --help for more infomation   

---------------------------------------------------
1 change patent doc to utf-8
2 do morphological analysis with chasen
3 create wam file
4 create search index
5 search

---------------------------------------------------
jpTOutf.py  
jpTOutf2.py  
jpTOutf-topic.py  

---------------------------------------------------  
Query Creation    
init-topics.py:extract claims from patent documents  
chasen-topic.py:get chasen results of claims 
topic-query.py:Creat query from chasen results of claims 

---------------------------------------------------
Index Creation
chasen-index.py:get chasen results of claims,chasen to .fq  
init.py:.fq to frefile
join.py:freqfile to NTCIR.txt  

---------------------------------------------------
Stopword List  
stopword4.py:creat stopword4.txt
