import urllib.request
import pandas as pd
from pathlib import Path

# TODO low priority for this whole section - threaded loading animation

cache_path = Path('.cache')
dependency_path = cache_path / 'dependency_df.csv'
expression_path = cache_path / 'expression_df.csv'

if not cache_path.is_dir():
    cache_path.mkdir()
if not dependency_path.exists():
    print("Downloading cancer gene dependency data - this may take a few minutes!")
    urllib.request.urlretrieve('https://zenodo.org/records/17609722/files/dependency_df_nan.csv?download=1',dependency_path)
if not expression_path.exists():
    print("Downloading RNA expression level data - this may take a few minutes!")
    urllib.request.urlretrieve('https://zenodo.org/records/17609575/files/expression_df_nan.csv?download=1',expression_path)

print("Loading cancer gene dependency data into program - this may take a few minutes!")
dependency_df = pd.read_csv(dependency_path)
print("Loading RNA expression level data into program - this may take a few minutes!")
expression_df = pd.read_csv(expression_path)

print(f"Dependency data ({dependency_df.shape[0]} rows x {dependency_df.shape[1]} columns)):")
print(dependency_df.head())
print(f"Expression data ({expression_df.shape[0]} rows x {expression_df.shape[1]} columns):")
print(dependency_df.head())

# now do the actual program :P
