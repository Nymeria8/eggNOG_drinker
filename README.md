# eggNOG_drinker

Gene ontology seach and assignment using [eggNOG database](ftp://eggnog.embl.de/eggNOG/4.0/)


##The program is composed by two parts:

**eggNOG_flavor.py** : To make the database smaller and faster during the rapsearch use.
Ordinarily this kind of search is done against similiar species to the one in study. In this way,
this script makes a custom database for each search. **Restrictied to the ensembl entries of the database**
 
**In the command line:**

<pre><code>python eggNOG_flavor.py [fastaFromEggnog] [speciesFromEggnog] [taxid] [outputFileName]
</code></pre>

* fastaFromEggnog: protein sequences of the database. Should be eggnogv*.proteins.all.fa.gz
* speciesFromEggnog: list of species from the eggNOG database. Should be eggnogv*.species.txt
* taxid: the options are "Fungi", "Protists", "Metazoa","Plants"



**eggNOG_topping.py** : Parse your results from the homology search using the database files from eggnog
and the Rapsearch result file m8  **Must be placed in the same directory as eggNOG_flavour.py**

**In the command line:**

<pre><code>python eggNOG_topping.py [rapsearch.m8] [eggnog.species] [tax id] [nog.members] [NOG.funccat] [NOG.description] [output file]
</code></pre>

* rapsearch.m8: rapsearch output file .m8
* eggnog.species: file from the eggNOG database. Should be: eggnogv*.species.txt
* tax id:the options are "Fungi", "Protists", "Metazoa","Plants"
* nog.members: file from the eggNOG database. Should be *.members.txt, where * depends on the organism your studing
* NOG.funccat: file from the eggNOG database. Should be *.funccat.txt, where * depends on the organism your studing
* NOG.description: file from the eggNOG database. Should be *.description.txt, where * depends on the organism your studing

##Dependencies:
* Python(2 or 3)
* Database files from [eggNOG](ftp://eggnog.embl.de/eggNOG/4.0/)

##Limitations:
* Both scripts work with the complete database or with the ones from Ensembl: "Fungi", "Protists", "Metazoa","Plants"
* Requires the search to be made with Rapsearch2.
