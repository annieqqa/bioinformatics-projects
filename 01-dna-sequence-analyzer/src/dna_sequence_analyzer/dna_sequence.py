from .rna_sequence import RNASequence
from .nucleotide import Nucleotide
class DNASequence:
    def __init__(self) -> None:
        raise NotImplementedError

    def count_nucleotides(self) -> dict[Nucleotide, int]:
        raise NotImplementedError
    
    def calc_GC_content(self) -> float:
        raise NotImplementedError

    def get_complement(self) -> DNASequence:
        raise NotImplementedError

    def to_RNA(self) -> RNASequence:
        raise NotImplementedError

    def find_protein_coding_regions(self) -> list[DNASequence]:
        raise NotImplementedError