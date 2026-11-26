import math

from dna_sequence_analyzer.dna_nucleotide import DNANucleotide
from dna_sequence_analyzer.dna_sequence import DNASequence
from dna_sequence_analyzer.rna_nucleotide import RNANucleotide
from dna_sequence_analyzer.rna_sequence import RNASequence


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
        dna2: DNASequence = DNASequence([DNANucleotide[n] for n in "TAACATC"])
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


class TestGetComplement:
    def test_empty_dna_sequence_has_empty_complement_sequence(self):
        dna: DNASequence = DNASequence([])
        assert dna.get_complement() == DNASequence([])

    def test_correct_complement_is_returned(self):
        dna: DNASequence = DNASequence([DNANucleotide[n] for n in "TAACATC"])
        assert dna.get_complement() == DNASequence(
            [DNANucleotide[n] for n in "ATTGTAG"]
        )


class TestToRNA:
    def test_empty_dna_maps_to_empty_rna(self):
        dna: DNASequence = DNASequence([DNANucleotide[n] for n in "TAACATC"])
        assert dna.to_RNA() == RNASequence([RNANucleotide[n] for n in "UAACAUC"])


class TestFindPCR:
    def test_PCR_with_no_matches_returns_empty_list(self):
        dna: DNASequence = DNASequence([DNANucleotide[n] for n in "ATGA"])
        assert dna.find_protein_coding_regions() == []

    def test_PCR_with_non_overlapping_matches(self):
        dna: DNASequence = DNASequence([DNANucleotide[n] for n in "ATGTAAATGTGAATGTAG"])
        assert dna.find_protein_coding_regions() == [
            DNASequence([DNANucleotide[n] for n in "ATGTAA"]),
            DNASequence([DNANucleotide[n] for n in "ATGTGA"]),
            DNASequence([DNANucleotide[n] for n in "ATGTAG"]),
        ]

    def test_PCR_with_overlapping_matches(self):
        dna: DNASequence = DNASequence([DNANucleotide[n] for n in "ATGTAATGTGATGTAG"])
        assert dna.find_protein_coding_regions() == [
            DNASequence([DNANucleotide[n] for n in "ATGTAA"]),
            DNASequence([DNANucleotide[n] for n in "ATGTGA"]),
            DNASequence([DNANucleotide[n] for n in "ATGTAG"]),
        ]