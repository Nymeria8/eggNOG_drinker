#Parse your results from the homology search using the database files from eggnog.
#This script uses all kinds of toppings to export a tab delimited file with all the information organized:
#*NOG.members.txt
#*NOG.description.txt
#*NOG.funccat.txt
#eggnog*.species.txt
#plust the rapsearch output
#usage:
#python eggNOG_topping.py [rapsearch.m8] [eggnog.species] [tax id] [nog.members] [NOG.funccat] [NOG.description] [output file]
#for taxid the options are "Fungi", "Protists", "Metazoa","Plants"
#The tab-dellimited output file is organized as
#Gene  NOG_name  Category   Subcategory   Specie

#To do: add argparse

from sys import argv
from eggNOG_flavor import select_species

#############RAPSEACH PARSER############################################

def rapsearch_result(infile):
	"""recives the rapsearch output and
	returns a dictionary with the sequence name and respective hit"""
	rap=open(infile)
	dicrap={}
	for i in rap:
		q=i.split("\t")
		if i.startswith("#")==False:
			if q[0] not in dicrap:
				dicrap[q[0]]=[q[1]]
			else:
				dicrap[q[0]].append(q[1])
	rap.close()
	return dicrap



##############CUTOFF BASED ON THE HITS##################################

def members_names(infile):
	"""reads the file nog.members and uses the SPECIES to make a cutoff
	in the sequences ids.
	Return a dictionary with nogname and sequence name and another with
	nog name and specie name"""
	f=open(infile)
	f.readline()
	dic_correspondance={}
	dic_nog_specie={}
	for i in f:
		el=i.split("\t")
		if el[1].split(".")[0] in dic_specie:
			dic_nog_specie[el[0]]=dic_specie[el[1].split(".")[0]]
			dic_correspondance[el[1]]=el[0]
	f.close()
	return dic_correspondance, dic_nog_specie

def hits_cutoff(hits,members):
	"""Returns a dictionary with the nog names and their respective
	sequences"""
	cutoff_hits={}
	for key,value in hits.items():
		for el in value:
			if el in members:
				cutoff_hits[members[el]]=key
				break
	return cutoff_hits

#arg1-hits rapsearch
#arg2-speciesfile
#arg3 - taxid
#arg4 - membersfile
dic_specie=select_species(argv[2], argv[3])#species tax id
correspondance, nog_specie=members_names(argv[4])
hits=hits_cutoff(rapsearch_result(argv[1]), correspondance)

##################GET INFORMATION#######################################

def get_foam(infile):#get data from eggNOG_foam.txt (por como default)
	"""Extract data from the eggNOG_foam and make a dictionary with it"""
	f=open(infile)
	foam={}
	for i in f:
		a=i.strip("\n")
		foam[a[0]]=a[2:]
	f.close()
	return foam

def define_categories(infile):
	"""uses NOG.funccat and hits
	makes a dictionary using the get_foam information and the nog names.
	The output is a dictionary cutted of by hits list where the key is
	the nog name and the value is the categories correspondent"""
	foam=get_foam("eggNOG_foam.txt")
	f=open(infile)
	cat_genes={}
	for i in f:
		el=i.split("\t")
		if el[0] in hits:
			cat_genes[el[0]]=""
			for leter in el[1]:
				if leter in foam:
					cat_genes[el[0]]+=foam[leter]+":"
	f.close()
	return cat_genes


def get_description(infile):
	"""uses the NOG.description file
	makes a dictionary with the nog name and the respective description"""
	f=open(infile)
	dic_des={}
	for i in f:
		el=i.split("\t")
		if el[0] in hits:
			dic_des[el[0]]=el[1]
	f.close()
	return dic_des

###################WRITE FILE###########################################

def write_file(output):
	"""organize and write the other methods outputs"""
	cats=define_categories(argv[5])#receives funcat
	subcat=get_description(argv[6])#recives nog.description
	out=open(output,"w")
	out.write("Gene\tNOG name\tCategory\tSubcategory\tSpecie\n")
	for key, value in hits.items():
		out.write(value+"\t"+key+"\t"+cats[key]+"\t"+subcat[key]+"\t"+nog_specie[key]+"\n")
	out.close()

write_file(argv[7])
			
	
