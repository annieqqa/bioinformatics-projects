from pathlib import Path

from .dna_nucleotide import DNANucleotide
from .dna_sequence import DNASequence


def __parse(line: str) -> list[DNANucleotide]:
    """Parse the DNA sequence, ignoring the nucleotide if the key is invalid"""
    ret: list[DNANucleotide] = []
    for n in line:
        try:
            ret.append(DNANucleotide[n])
        except KeyError:
            continue
    return ret

def read_DNA(rel_path: Path) -> list[DNASequence]:
    file = rel_path.open()
    lines = file.readlines()
    file.close()

    nucleotides: list[DNANucleotide] = []
    sequences: list[DNASequence] = []

    for line in lines:
        # remove leading and trailing white spaces
        line = line.strip()
        # ignore empty line
        if len(line) == 0:
            continue

        # ignore metadata (TODO: add metadata to fields of DNASequence)
        if line.startswith(">"):
            if len(nucleotides) > 0:
                sequences.append(DNASequence(nucleotides))
                nucleotides.clear()
            continue

        # parse DNA sequence
        nucleotides += __parse(line)
    if len(nucleotides) > 0:
        sequences.append(DNASequence(nucleotides))
    return sequences
