import pandas as pd
from sqlalchemy import create_engine
import yaml

# Load the engine to connect to the database
def get_engine():
    """
    This function access to the config.yaml file to get the user database information and access the tables created
    by posgreSQL through the files .sql in the sql folder. It returns the engine ready to load the datasets.
    """
    with open("../config.yaml", "r") as f:
        config = yaml.safe_load(f)

    db = config["database"]

    uri = f"postgresql+psycopg2://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['name']}"
    # f.close()
    return create_engine(uri)

# Get the information of a table.
def extract_table(table_name: str) -> pd.DataFrame:
    engine = get_engine()
    query = f"SELECT * FROM {table_name};"
    return pd.read_sql(query, engine)