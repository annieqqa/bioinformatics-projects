from __future__ import annotations

from .nucleotide import Nucleotide
from .rna_sequence import RNASequence


class DNASequence:
    """Represents a DNASequence."""

    # Fields
    __dna_complement: dict[Nucleotide, Nucleotide]
    __dna_sequence: list[Nucleotide]

    def __init__(self, dna_sequence: list[Nucleotide]) -> None:
        self.__dna_complement: dict[Nucleotide, Nucleotide] = {
            Nucleotide.A: Nucleotide.T,
            Nucleotide.T: Nucleotide.A,
            Nucleotide.C: Nucleotide.G,
            Nucleotide.G: Nucleotide.C,
        }
        self.__dna_sequence = dna_sequence

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