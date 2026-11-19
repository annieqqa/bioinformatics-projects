from __future__ import annotations

from enum import Enum


class DNANucleotide(Enum):
    """Represents a Nucleotide for both DNA and RNA."""
    A = "A"
    T = "T"
    C = "C"
    G = "G"
