from sentenceClassifier.entity.config_entity import DataIngestionConfig
from sentenceClassifier.exception import sentenceClassifierException
import os , sys
from sentenceClassifier.logger import logging
#from sentenceClassifier.entity.artifact_entity import DataIngestionArtifact



class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20} Data Ingestin log started. {'<<'*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise sentenceClassifierException(e, sys)

    def download_housing_data(self,) -> str:
        try:
            download_url = self.data_ingestion_config.dataset_download_url
            
        except Exception as e:
            raise  sentenceClassifierException(e, sys)


a = DataIngestion(DataIngestionConfig)
a.download_housing_data() 