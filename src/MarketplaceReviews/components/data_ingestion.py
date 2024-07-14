import pandas as pd

from sqlalchemy import create_engine 
from tqdm import tqdm

from MarketplaceReviews import logger
from MarketplaceReviews.entity.config_entity import DataIngestionSQLConfig

class DataIngestionSQL:
    def __init__(self, config: DataIngestionSQLConfig):
        self.config = config

    def sql_to_csv(self) -> None:
        """get data from the SQL database
        """
        try:
            db = create_engine(self.config.source_URI)  
            conn = db.connect()

            logger.info(f"Querying reviews data from SQL Database.")
            df_reviews = pd.read_sql_table("reviews", conn)
            
            logger.info(f"Dump data from SQL Database to CSV.")
            df_reviews.to_csv(self.config.reviews_path, index=False)
                
            logger.info(f"Data dumped from SQL query into {self.config.root_dir} directory")
            conn.close()
        except Exception as e:
            conn.close()
            logger.error(e)
            raise e