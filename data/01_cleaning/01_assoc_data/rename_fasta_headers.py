import os, sys, re
from Bio import SeqIO


## the input folder will be whatever you type after this python script (i.e. python rename_fastaheaders.py input_folder/)
input_folder = sys.argv[1]


## check if "/" at end of input_folder specification. Otherwise, it is added. Need "/" to open files later in script.
if input_folder.endswith("/"):
	pass
else:
	input_folder = input_folder + "/"

print(input_folder)

### list files in input_folder
for file in os.listdir(input_folder):
	## only look at files that end with ".fna"
	if file.endswith("ognames.fna"):
		## open the file. genome_contigs is now a file object. to change its name, must say genome_contigs.name
		genome_contigs = open(input_folder + file,'r')
		genome = re.sub(".fna","",genome_contigs.name)
		## replace the filepath in front. Now what is left is the genome name.
		genome = re.sub(input_folder,"",genome)

		# make new file name to deposit the relabeled fasta headers
		new_file_name = re.sub(".fna","_renamed.fna",genome_contigs.name)
		# open a file to write that has the new_file name
		new_file = open(new_file_name,'w')

		# now rename the headers with the genome + number of proteins using SeqIO
		## first initialize protein count for genome at 0
		contig_count = int(0)
		## then tell SeqIO to parse the genome_contigs folder as a fasta
		sequences = SeqIO.parse(genome_contigs,'fasta')
		## iterate through the sequences by each sequence
		for sequence in sequences:
			# add one to the protein count
			contig_count +=1
			# tell SeqIO to change the record id to the genome name + protein count
			oldseq = sequence.id
			sequence.id = "amPh" + "_" + str(contig_count)
			# tell SeqIO to write the new sequence name with its sequence to the out_file_name as a fasta
			SeqIO.write(sequence,new_file,'fasta')
			print(oldseq + "\t" + sequence.id)
			
