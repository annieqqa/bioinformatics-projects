from typing import override

from dna_sequence_analyzer.rna_nucleotide import RNANucleotide


class RNASequence:
    """Represents an RNASequence."""

    # Fields
    __rna_nucleotides: list[RNANucleotide]

    def __init__(self, rna_nucleotides: list[RNANucleotide]) -> None:
        self.__rna_nucleotides = rna_nucleotides

    @override
    def __eq__(self, other: object) -> bool:
        """Equality holds when nucleotide sequence is the same"""
        if not isinstance(other, RNASequence):
            return NotImplemented
        return self.__rna_nucleotides == other.__rna_nucleotides