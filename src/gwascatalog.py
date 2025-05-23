import polars as pl
import requests


def get_studies(
    url: str = "https://www.ebi.ac.uk/gwas/api/search/downloads/studies/v1.0.2.1",
    # outpath: str = "data/studies.tsv",
):
    """

    Args:
        url: https://www.ebi.ac.uk/gwas/api/search/downloads/studies/v1.0.2.1

    Returns:

    """
    r = requests.get(url)
    df = pl.read_csv(
        r.content, separator="\t", quote_char=None, infer_schema_length=1000000
    )
    return df


def get_associations(
    url: str = "https://www.ebi.ac.uk/gwas/api/search/downloads/alternative",
):
    r = requests.get(url)
    df = pl.read_csv(
        r.content, separator="\t", quote_char=None, infer_schema_length=1000000
    )
    return df


def save_associations(filename):
    associations = get_associations()
    associations.write_csv(filename, separator="\t")
    return f"Saved to {filename}"


def find_trait(trait, associations):
    filtered = associations.filter(
        pl.col("MAPPED_TRAIT").str.to_lowercase().str.contains(trait.lower())
        | pl.col("DISEASE/TRAIT").str.to_lowercase().str.contains(trait.lower())
        | pl.col("P-VALUE (TEXT)").str.to_lowercase().str.contains(trait.lower())
        | pl.col("STUDY").str.to_lowercase().str.contains(trait.lower())
    )
    return filtered
