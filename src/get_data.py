import requests
import polars as pl


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
    return r


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
