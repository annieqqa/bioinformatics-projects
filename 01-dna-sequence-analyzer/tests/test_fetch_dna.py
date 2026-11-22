from pathlib import Path

import pytest
from dna_sequence_analyzer.fetch_dna import DNAQuery


@pytest.mark.integration
def test_fetch_bacterial_from_ncbi():
    query: DNAQuery = DNAQuery.bacteria_genome_query()
    output_path: str = query.fetch_from_ncbi()
    assert(Path(output_path)).exists()