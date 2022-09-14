
from sentenceClassifier.util.util import read_yaml_file
import sys,os
from sentenceClassifier.constant import *
from sentenceClassifier.exception import sentenceClassifierException


class Configuartion:

    def __init__(self,
        config_file_path:str =CONFIG_FILE_PATH,
        current_time_stamp:str = CURRENT_TIME_STAMP
        ) -> None:
        try:
            self.config_info  = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise sentenceClassifierException(e,sys) from e


    def get_data_ingestion_config(self):

        "This function wil get data ingestion command "

        artifact_dir = self.training_pipeline_config.artifact_dir
        return artifact_dir
        #return self.config_info[KAGGLE_API_DATASET_DOWNLOAD]

    def get_training_pipeline_config(self):
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )
        except Exception as e:
            raise sentenceClassifierException(e, sys) from e
