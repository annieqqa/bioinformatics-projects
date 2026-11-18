# DNA Sequence Analyzer Spec

# Core Task

## Parse DNA sequence data

Create a function `read_DNA(rel_path: Path)->list[DNASequence]` that takes in a Path object corresponding to a DNA sequence data (from `pathlib`) and output a list of DNA sequences in the file.

## Count A, T, G, C nucleotides

Create a function `count_nucleotides(dna: DNASequence) -> dict[Nucleotide, int]` that takes in a DNA sequence and returns a dictionary mapping each nucleotide type to its count.

## Calculate GC content

Create a function `calc_GC_content(dna: DNASequence) -> float` that takes in a DNA sequence and return its GC content.

**GC content** is the percentage of nucleotides containing the bases guanine and cytosine relative to the total nucleotide base content in a sample of DNA or RNA [1][1]. It is given by the formula:

$$
\text{GC Content} = \frac{G + C}{A + T + G + C} \times 100\%
$$

## Identify DNA complement sequences.

Create a function `DNA_complement(dna: DNASequence) -> DNASequence` that takes in a DNA sequence and output its complement sequence. The mapping of each type of nucleotide is given by: $A\to T$,$T\to A$, $C \to G$, $G\to C$.

| Nucleotide type | Complement |
| -- | -- |
| A | T |
| T | A |
| C | G |
| G | C |

## Convert DNA into RNA

Create a function `DNA_to_RNA(dna: DNASequence) -> RNASequence` that takes a DNA sequence and output its corresponding RNA sequence. The mapping works as follows:

| DNA Nucleotide | RNA Nucleotide |
| -- | -- |
| A | U |
| T | A |
| C | G |
| G | C |

## Find possible protein-coding regions

Create a function `find_protein_coding_regions(dna: DNASequence) -> list[DNASequence]` that takes in a DNA sequence and returns a list of all possible protein-coding regions.

**Protein-coding region** is the sequence of DNA that codes for the production of proteins [2][2]. The protein-coding region begins with a start codon (`ATG`) and ends with a stop codon (`TAA`, `TAG`, `TGA`).

# Learning Objectives
1. Introduce myself to sequence analysis
2. Work with sequence files on a low level
3. Experience building a small Python library

# Stages

At the first stage I want to try not to use external libraries to understand things from a low level.

In later stages when I get more familiar with bioinformatics, I will refactor this to using standard libraries.

* [1]: <https://www.oxfordreference.com/display/10.1093/acref/9780198821489.001.0001/acref-9780198821489-e-6618> "GC content (G + C content), Oxford Reference"
* [2]: <https://www.genomicseducation.hee.nhs.uk/glossary/protein-coding-region/> "Protein-coding region, Genomics Education Programme"