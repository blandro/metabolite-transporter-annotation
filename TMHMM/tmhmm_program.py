import biolib
import os
from Bio import SeqIO
deeptmhmm = biolib.load('DTU/DeepTMHMM')

# Divide large fasta file
def split_fasta(input_fasta, output_prefix, chunk_size):

    os.makedirs("fasta_batches_split", exist_ok=True)

    fasta_sequences = SeqIO.parse(open(input_fasta), 'fasta')
    batch_number = 1
    sequences_in_batch = []
    
    for i, fasta in enumerate(fasta_sequences):
        sequences_in_batch.append(fasta)
        
        if (i + 1) % chunk_size == 0:
            
            output_file = f"fasta_batches_split/{output_prefix}_batch_{batch_number}.fasta"
            SeqIO.write(sequences_in_batch, output_file, "fasta")
            sequences_in_batch = []
            batch_number += 1
    
    if sequences_in_batch:
        output_file = f"fasta_batches_split/{output_prefix}_batch_{batch_number}.fasta"
        SeqIO.write(sequences_in_batch, output_file, "fasta")


# Process each batch w/ DeepTMHMM
def process_fasta_batches(output_prefix, batch_count):

    os.makedirs("fasta_batches_processed", exist_ok=True)

    for batch_number in range(1, batch_count + 1):
        
        batch_file = f"fasta_batches_split/{output_prefix}_batch_{batch_number}.fasta"
        print(f"Processing {batch_file}...")
        deeptmhmm_job = deeptmhmm.cli(args=f"--fasta {batch_file}")
        deeptmhmm_job.save_files(f"fasta_batches_processed/{batch_number}")


input_fasta = "TCDB_fasta.txt"
output_prefix = "TCDB_fasta_split"
chunk_size = 100
batch_count = (len(list(SeqIO.parse(input_fasta, "fasta"))) + chunk_size - 1) // chunk_size

# Execution
split_fasta(input_fasta, output_prefix, chunk_size)
process_fasta_batches(output_prefix, batch_count)