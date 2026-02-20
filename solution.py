import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    if not is_column_valid(new_column): 
        return pd.DataFrame()

    for col in df.columns:
        if not is_column_valid(col):
            return pd.DataFrame()

    if not is_role_valid(df, role):
        return pd.DataFrame()

    expr = new_column + "=" + role;
    return df.eval(expr)

def is_column_valid(new_column: str) -> bool:
    return bool(re.fullmatch(r"[a-zA-Z_]+", new_column))

def is_role_valid(df: pd.DataFrame, role: str) -> bool:
    parts = re.split(r"[\+\-\*]", role.strip())
    for part in parts:
        if part.strip() not in df.columns:
            return False
    return True
