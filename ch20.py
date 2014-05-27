def mRNAtranscription(dna_template):
	dna2rna = {'A':'U','T':'A','C':'G','G':'C'}
	mRNA = ''
	temp = []
	for base in dna_template:
		der = dna2rna[base]
		temp.append(der)
	return mRNA.join(x for x in temp)

if __name__ == "__main__":
	print mRNAtranscription("ATCGATTG")
