
# store the sequences.
mkdir fa_gz

for plant in /lustre/scratch124/tol/projects/darwin/data/{monocots,dicots}/*/genomic_data/{lpSchLacu1,lpCarDepa1,lpLuzSylv1,daMisOron1,daScuGale1,daPulDyse1,drAilAlti1,drChaAngu1,drGeuUrba1,lpJunEffu1,drUrtUren1,drHedHeli1,drMedArab1,drFilUlma1,dhAlnGlut1,daLycEuro1,daBalNigr1}/pacbio/fasta/*.filtered.fasta.gz; do
	if [[ $plant != *"*"* ]]; then
		nm=$(echo $plant | cut -d/ -f9)
		echo "Processing $nm."
		cat $plant >> "./fa_gz/${nm}.fa.gz"
	fi
done
