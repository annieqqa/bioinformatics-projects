import math

from dna_sequence_analyzer.dna_nucleotide import DNANucleotide
from dna_sequence_analyzer.dna_sequence import DNASequence


class TestCountNucleotides:
    def test_count_nucleotides_always_includes_4_entries(self):
        dna: DNASequence = DNASequence([])
        assert dna.count_nucleotides() == {
            DNANucleotide.A: 0,
            DNANucleotide.T: 0,
            DNANucleotide.C: 0,
            DNANucleotide.G: 0,
        }

    def test_count_nucleotides_returns_correct_numbers_of_nucleotides(self):
        dna1: DNASequence = DNASequence(
            [DNANucleotide.A, DNANucleotide.T, DNANucleotide.C, DNANucleotide.G]
        )
        assert dna1.count_nucleotides() == {
            DNANucleotide.A: 1,
            DNANucleotide.T: 1,
            DNANucleotide.C: 1,
            DNANucleotide.G: 1,
        }
        dna2: DNASequence = DNASequence(
            [
                DNANucleotide.T,
                DNANucleotide.A,
                DNANucleotide.A,
                DNANucleotide.C,
                DNANucleotide.A,
                DNANucleotide.T,
                DNANucleotide.C,
            ]
        )
        assert dna2.count_nucleotides() == {
            DNANucleotide.A: 3,
            DNANucleotide.T: 2,
            DNANucleotide.C: 2,
            DNANucleotide.G: 0,
        }

class TestCalcGCContent:
    def test_error_value_returned_for_empty_DNASequence(self):
        dna: DNASequence = DNASequence([])
        assert math.isclose(dna.calc_GC_content(), -1)

    def test_correct_gc_value_is_returned(self):
        dna: DNASequence = DNASequence(
            [DNANucleotide.A] * 123
            + [DNANucleotide.T] * 231
            + [DNANucleotide.C] * 892
            + [DNANucleotide.G] * 129
        )
        assert math.isclose(
            dna.calc_GC_content(), (892 + 129) / (123 + 231 + 892 + 129)
        )