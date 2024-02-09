from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try: 
   logger.info(f"{'>'*6} stage {STAGE_NAME} started {'<'*6}")
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f"{'>'*6} stage {STAGE_NAME} completed {'<'*6}\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



