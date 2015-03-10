#SELECT THE FLAVOUT OF YOUR EGGNOGG
#The eggNOG database is pretty large, and regularily exists the need
#to select a taxonomic group for a more accurate seach.
#This script was created to select from the general database the sequences
#from a determinated taxID
#The selection is made based on the eggNOG.species.txt
#In the future the ensembl API will be used for the selection
#For now, the selection is done based on the fourth colum of the file
#Usage: python eggNOG_flavor.py [fastaFromEggnog] [speciesFromEggnog] [taxid] [outputFileName]
#fastaFromEggnog must be eggnogv*.proteins.all.fa
#speciesFromEggnog must be eggnogv4.species.txt
#for taxid the options are "Fungi", "Protists", "Metazoa","Plants"

#adapt to no run the hole script


from sys import argv

def select_species(infile, tax):
	species=open(infile)
	taxid="Ensembl "+tax
	taxlist=set()
	dicspecies={}
	for i in species:
		line=i.split("\t")
		if line[3]==taxid:
			dicspecies[line[1]]=line[0]
	species.close()
	return dicspecies

def select_sequences(infile):
	species=select_species(argv[2], argv[3])
	fasta=open(infile)
	seqs={}
	temp=0
	for i in fasta:
		if i.startswith(">"):
			temp=0
			idsd=i.split(".")
			idd=idsd[0]
			if idd[1:] in species:
				seqs[i]=""
				temp+=1
				name=i
		elif temp>=1:
			seqs[name]+=i.strip("\n")
	fasta.close()
	return seqs

def write_file(dic, output):
	out=open(output,"w")
	for key, value in dic.items():
		out.write(key)
		out.write(value+"\n")
	out.close()

if __name__ == "__main__":
	write_file(select_sequences(argv[1]),argv[4])

