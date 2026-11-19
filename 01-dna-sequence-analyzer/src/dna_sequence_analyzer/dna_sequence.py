from __future__ import annotations

from .dna_nucleotide import DNANucleotide
from .rna_sequence import RNASequence


class DNASequence:
    """Represents a DNASequence."""

    # Fields
    __dna_complement: dict[DNANucleotide, DNANucleotide]
    __dna_sequence: list[DNANucleotide]

    def __init__(self, dna_sequence: list[DNANucleotide]) -> None:
        self.__dna_complement: dict[DNANucleotide, DNANucleotide] = {
            DNANucleotide.A: DNANucleotide.T,
            DNANucleotide.T: DNANucleotide.A,
            DNANucleotide.C: DNANucleotide.G,
            DNANucleotide.G: DNANucleotide.C,
        }
        self.__dna_sequence = dna_sequence

    def count_nucleotides(self) -> dict[DNANucleotide, int]:
        raise NotImplementedError
    
    def calc_GC_content(self) -> float:
        raise NotImplementedError

    def get_complement(self) -> DNASequence:
        raise NotImplementedError

    def to_RNA(self) -> RNASequence:
        raise NotImplementedError

    def find_protein_coding_regions(self) -> list[DNASequence]:
        raise NotImplementedError