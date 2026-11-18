# DNA Sequence Analyzer Spec

# Core Task

## Parse DNA sequence data

Create a function `read_DNA(rel_path: Path)->list[DNASequence]` that takes in a Path object corresponding to a DNA sequence data (from `pathlib`) and output a list of DNA sequences in the file.

## Define relevant classes

Define `DNASequence`, `RNASequence` and `Nucleotide` classes.

## Count A, T, G, C nucleotides

Add instance method `count_nucleotides(self) -> dict[Nucleotide, int]` to `DNASequence` that returns a dictionary mapping each nucleotide type to its count in the sequence.

## Calculate GC content

Add instance method `calc_GC_content(self) -> float` to `DNASequence` that returns the GC content of the DNA sequence.

**GC content** is the percentage of nucleotides containing the bases guanine and cytosine relative to the total nucleotide base content in a sample of DNA or RNA [1][1]. It is given by the formula:

$$
\text{GC Content} = \frac{G + C}{A + T + G + C} \times 100\%
$$

## Identify DNA complement sequences.

Add instance method `get_complement(self) -> DNASequence` to `DNASequence` that returns its complement sequence. The mapping of each type of nucleotide is given by: $A\to T$,$T\to A$, $C \to G$, $G\to C$.

| Nucleotide type | Complement |
| -- | -- |
| A | T |
| T | A |
| C | G |
| G | C |

## Convert DNA into RNA

Add instance method `to_RNA(self) -> RNASequence`to `DNASequence` that returns its corresponding RNA sequence. The mapping works as follows:

| DNA Nucleotide | RNA Nucleotide |
| -- | -- |
| A | U |
| T | A |
| C | G |
| G | C |

## Find possible protein-coding regions

Add instance method `find_protein_coding_regions(self) -> list[DNASequence]` to `DNASequence` that returns a list of all possible protein-coding regions.

**Protein-coding region** is the sequence of DNA that codes for the production of proteins [2][2]. The protein-coding region begins with a start codon (`ATG`) and ends with a stop codon (`TAA`, `TAG`, `TGA`).

# Testing

The tests are stored in `tests` directory. To run the tests, run `pytest` in project root (in this case, `01-dna-sequence-analyzer`)

# Learning Objectives
1. Introduce myself to sequence analysis
2. Work with sequence files on a low level
3. Experience building a small Python library

# Stages

At the first stage I want to try not to use external libraries to understand things from a low level.

In later stages when I get more familiar with bioinformatics, I will refactor this to using standard libraries.

[1]: <https://www.oxfordreference.com/display/10.1093/acref/9780198821489.001.0001/acref-9780198821489-e-6618> "GC content (G + C content), Oxford Reference"
[2]: <https://www.genomicseducation.hee.nhs.uk/glossary/protein-coding-region/> "Protein-coding region, Genomics Education Programme"