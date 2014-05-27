def baseComposition(dna_seq):
	A_count = dna_seq.count('A')
	C_count = dna_seq.count('C')
	T_count = dna_seq.count('T')
	G_count = dna_seq.count('G')

	dictionary = {}
	dictionary['A'] = A_count
	dictionary['C'] = C_count
	dictionary['T'] = T_count
	dictionary['G'] = G_count
	
	return dictionary

if __name__ == "__main__":
	print baseComposition("CTATCGGCACCCTTTCAGCA")
