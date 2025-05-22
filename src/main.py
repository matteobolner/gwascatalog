import requests
import polars as pl

associations = pl.read_csv(
    "data/gwas_catalog_v1.0.2-associations_e114_r2025-05-13.tsv",
    quote_char=None,
    separator="\t",
    infer_schema_length=100000,
)


def find_trait(trait, associations):
    filtered = associations.filter(
        pl.col("MAPPED_TRAIT").str.to_lowercase().str.contains(trait.lower())
        | pl.col("DISEASE/TRAIT").str.to_lowercase().str.contains(trait.lower())
    )
    return filtered
