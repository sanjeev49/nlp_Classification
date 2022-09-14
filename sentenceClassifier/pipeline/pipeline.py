from collections import namedtuple
# from datetime import datetime
# import uuid
from sentenceClassifier.config.configuration import Configuartion
from sentenceClassifier.logger import logging, get_log_file_name
from sentenceClassifier.exception import sentenceClassifierException
from threading import Thread
# from typing import List
from sentenceClassifier.component.data_ingestion1 import DataIngestion

# from multiprocessing import Process
# from sentenceClassifier.entity.artifact_entity import ModelPusherArtifact, DataIngestionArtifact, ModelEvaluationArtifact
# from sentenceClassifier.entity.artifact_entity import DataValidationArtifact, DataTransformationArtifact, ModelTrainerArtifact
# from sentenceClassifier.entity.config_entity import DataIngestionConfig, ModelEvaluationConfig
# from sentenceClassifier.component.data_ingestion import DataIngestion
# from sentenceClassifier.component.data_validation import DataValidation
# from sentenceClassifier.component.data_transformation import DataTransformation
# from sentenceClassifier.component.model_trainer import ModelTrainer
# from sentenceClassifier.component.model_evaluation import ModelEvaluation
# from sentenceClassifier.component.model_pusher import ModelPusher
import os, sys
# from collections import namedtuple
# from datetime import datetime
# import pandas as pd
from sentenceClassifier.constant import CONFIG_FILE_PATH, EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME

Experiment = namedtuple("Experiment", ["experiment_id", "initialization_timestamp", "artifact_time_stamp",
                                       "running_status", "start_time", "stop_time", "execution_time", "message",
                                       "experiment_file_path", "accuracy", "is_model_accepted"])





class Pipeline(Thread):
    experiment: Experiment = Experiment(*([None] * 11))
    experiment_file_path = None

    def __init__(self, config ) -> None:
        try:
            os.makedirs(config.training_pipeline_config.artifact_dir, exist_ok=True)
            Pipeline.experiment_file_path=os.path.join(config.training_pipeline_config.artifact_dir,EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME)
            super().__init__(daemon=False, name="pipeline")
            self.config = config
        except Exception as e:
            raise sentenceClassifierException(e, sys) from e
    def println(self):
        print(self.config.get_data_ingestion_config())

    
    def start_data_ingestion(self):
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            
            #self.config.get_data_ingestion_config()
            print(data_ingestion)

            return data_ingestion.download_housing_data()
        except Exception as e:
            raise sentenceClassifierException(e, sys) from e

# obj = Pipeline(Configuartion)
# obj.start_data_ingestion()
obj = Pipeline(Configuartion(CONFIG_FILE_PATH))




#print(CONFIG_FILE_PATH)