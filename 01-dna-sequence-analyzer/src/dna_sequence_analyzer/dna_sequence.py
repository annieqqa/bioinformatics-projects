from __future__ import annotations

from typing import override

from .dna_nucleotide import DNANucleotide
from .rna_sequence import RNASequence

_DNA_COMPLEMENT: dict[DNANucleotide, DNANucleotide] = {
    DNANucleotide.A: DNANucleotide.T,
    DNANucleotide.T: DNANucleotide.A,
    DNANucleotide.C: DNANucleotide.G,
    DNANucleotide.G: DNANucleotide.C,
}

class DNASequence:
    """Represents a DNASequence."""

    # Fields
    __dna_sequence: list[DNANucleotide]

    def __init__(self, dna_sequence: list[DNANucleotide]) -> None:
        self.__dna_sequence = dna_sequence

    def count_nucleotides(self) -> dict[DNANucleotide, int]:
        """Returns a dictionary mapping each nucleotide type to its count in the sequence."""
        count: dict[DNANucleotide, int] = {dn: 0 for dn in DNANucleotide}
        for nucleotide in self.__dna_sequence:
            count[nucleotide] += 1
        return count


    def calc_GC_content(self) -> float:
        """Returns the GC content of the DNA sequence.
        If number of nucleotides is 0, return error value (-1)."""
        count = self.count_nucleotides()
        return self.__get_GC(
            count[DNANucleotide.A],
            count[DNANucleotide.T],
            count[DNANucleotide.G],
            count[DNANucleotide.C],
        )

    def get_complement(self) -> DNASequence:
        """Returns complement sequence."""
        return DNASequence([_DNA_COMPLEMENT[dn] for dn in self.__dna_sequence])

    def to_RNA(self) -> RNASequence:
        raise NotImplementedError

    def find_protein_coding_regions(self) -> list[DNASequence]:
        raise NotImplementedError

    @override
    def __eq__(self, other: object) -> bool:
        """Equality holds when nucleotide sequence is the same"""
        if not isinstance(other, DNASequence):
            return NotImplemented
        return self.__dna_sequence == other.__dna_sequence
    # HELPER METHODS (PRIVATE TO CLASS)
    @staticmethod
    def __get_GC(a: int, t: int, g: int, c: int) -> float:
        """Calculates the GC content given the count of a,t,g,c nucleotides"""
        gc: int = g + c
        atgc: int = a + t + gc
        # return error value (-1) for zero division
        if atgc == 0:
            return -1
        # return GC content for non-zero number of nucleotides
        return gc / (a + t + gc)