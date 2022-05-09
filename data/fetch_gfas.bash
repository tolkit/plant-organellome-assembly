
# store the sequences.
mkdir gfas

for gfa in /lustre/scratch124/tol/projects/darwin/data/{monocots,dicots}/*/working/mito_chloro/*.gfa; do
    nm=$(echo $gfa | cut -d/ -f9)
    nm2=$(echo $gfa | cut -d/ -f12)
    echo "Copying $nm."
    cp $gfa "./gfas/${nm}_${nm2}"
done
