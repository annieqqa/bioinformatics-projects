from __future__ import annotations

from types import MappingProxyType
from typing import override

from dna_sequence_analyzer.rna_nucleotide import RNANucleotide

from .dna_nucleotide import DNANucleotide
from .rna_sequence import RNASequence

_DNA_COMPLEMENT: MappingProxyType[DNANucleotide, DNANucleotide] = MappingProxyType(
    {
        DNANucleotide.A: DNANucleotide.T,
        DNANucleotide.T: DNANucleotide.A,
        DNANucleotide.C: DNANucleotide.G,
        DNANucleotide.G: DNANucleotide.C,
    }
)

_DNA_RNA_MAP: MappingProxyType[DNANucleotide, RNANucleotide] = MappingProxyType(
    {
        DNANucleotide.A: RNANucleotide.A,
        DNANucleotide.T: RNANucleotide.U,
        DNANucleotide.C: RNANucleotide.C,
        DNANucleotide.G: RNANucleotide.G,
    }
)


class DNASequence:
    """Represents a DNASequence."""

    # Fields
    __dna_nucleotides: list[DNANucleotide]

    def __init__(self, dna_nucleotides: list[DNANucleotide]) -> None:
        self.__dna_nucleotides = dna_nucleotides

    def count_nucleotides(self) -> dict[DNANucleotide, int]:
        """Returns a dictionary mapping each nucleotide type to its count in the sequence."""
        count: dict[DNANucleotide, int] = {dn: 0 for dn in DNANucleotide}
        for nucleotide in self.__dna_nucleotides:
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
        return DNASequence([_DNA_COMPLEMENT[dn] for dn in self.__dna_nucleotides])

    def to_RNA(self) -> RNASequence:
        """Returns corresponding rna sequence after transcription."""
        return RNASequence([_DNA_RNA_MAP[dn] for dn in self.__dna_nucleotides])

    def find_protein_coding_regions(self) -> list[DNASequence]:
        raise NotImplementedError

    @override
    def __eq__(self, other: object) -> bool:
        """Equality holds when nucleotide sequence is the same"""
        if not isinstance(other, DNASequence):
            return NotImplemented
        return self.__dna_nucleotides == other.__dna_nucleotides
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