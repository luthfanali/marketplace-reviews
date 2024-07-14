from MarketplaceReviews import logger
from MarketplaceReviews.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from MarketplaceReviews.pipeline.stage_02_preprocessing import PreprocessingPipeline
from MarketplaceReviews.pipeline.stage_03_train_model import TrainingPipeline
from MarketplaceReviews.pipeline.stage_04_model_evaluation import TrainEvaluationPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"\n\n")
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<< ".upper())
    
    obj = DataIngestionPipeline()
    obj.pipeline()
    
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<< ]\n\n".upper())
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Preprocessing"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<< ".upper())
    
    obj = PreprocessingPipeline()
    obj.dump_data_pipeline()
    obj.preprocessing_pipeline()
    
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<< ]\n\n".upper())
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<< ".upper())
    
    obj = TrainingPipeline()
    obj.pipeline()
    
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<< ]\n\n".upper())
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation Stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<< ".upper())
    
    obj = TrainEvaluationPipeline()
    obj.pipeline()
    
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<< ]\n\n".upper())
except Exception as e:
    logger.exception(e)
    raise e