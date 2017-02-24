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
1 change patent doc to utf-8
jpTOutf.py  
jpTOutf2.py  

---------------------------------------------------
2 do morphological analysis with chasen
chasen-index.py

---------------------------------------------------
3 create wam file
init.py
join.py

---------------------------------------------------
4 create search index
see doc of geta3

---------------------------------------------------
5 search
see doc in getasearch

---------------------------------------------------  
Query Creation    
jpTOutf-topic.py change patent doc to utf-8
init-topics.py:extract claims from patent documents  
chasen-topic.py:get chasen results of claims 
topic-query.py:Creat query from chasen results of claims 

---------------------------------------------------
Stopword List  
stopword4.py:creat stopword4.txt
