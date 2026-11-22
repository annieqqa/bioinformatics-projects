"""
Fetch DNA results from NCBI.
"""
import os
from typing import Any, cast
from uuid import uuid4

from Bio import Entrez
from dotenv import load_dotenv


class DNAQuery:
    # fields
    db: str 
    term: str
    # fields with default values
    retmax: int = 5
    rettype: str = "fasta"
    output_path: str

    def __init__(
        self, db: str, term: str, retmax: int, output_name: str, rettype: str | None
    ):
        self.db = db
        self.term = term
        self.retmax = retmax
        if rettype:
            self.rettype = rettype
        self.output_path = (
            f"data/{self.db}_{output_name}_{uuid4().hex[:8]}.{self.rettype}"
        )

    @classmethod
    def bacteria_genome_query(cls):
        return cls(
            db="nuccore",
            term="bacteria[Organism] AND NC_*[Accession] AND srcdb_refseq[PROP]",
            retmax=1,
            output_name="bacterial_genome",
            rettype="fasta",
        )

    def fetch_from_ncbi(self) -> str:
        # Get email (required for NCBI query) from .env file
        load_dotenv()
        Entrez.email = os.getenv("NCBI_EMAIL")
        if not Entrez.email:
            raise ValueError("NCBI_EMAIL is missing from environment variables")

        # Make query
        with Entrez.esearch(
            db=self.db,
            term=self.term,
            retmax=self.retmax,
        ) as handle:
            results = cast(dict[str, Any], Entrez.read(handle))
        ids: int = results["IdList"]

        if ids:
            with (
                Entrez.efetch(
                    db=self.db, id=ids, rettype=self.rettype, retmode="text"
                ) as handle,
                open(self.output_path, "w") as output,
            ):
                output.write(handle.read())
                print(f"Fetched data to path: {self.output_path}")
        return self.output_path