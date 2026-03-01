import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    data_train: str = os.path.join("artifacts", "train.csv")
    data_test: str = os.path.join("artifacts", "test.csv")
    data_raw: str = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self):
        self.dataIngestion = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")

        try:
            df = pd.read_csv("notebook/data/stud.csv")

            os.makedirs(os.path.dirname(self.dataIngestion.data_raw), exist_ok=True)

            df.to_csv(self.dataIngestion.data_raw, index=False, header=True)

            logging.info("Splitting data into train and test")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.dataIngestion.data_train, index=False, header=True)
            test_set.to_csv(self.dataIngestion.data_test, index=False, header=True)

            logging.info("Data ingestion completed")

            return (
                self.dataIngestion.data_train,
                self.dataIngestion.data_test,
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()