import logging
from pyspark.sql import SparkSession

# 1. Setup logging instead of using print()
# Professional pipelines use logs to track history in Databricks "Compute" logs.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_spark_session():
    """Returns the active Spark session or creates a new one."""
    return SparkSession.builder.getOrCreate()

def ingest_api_data():
    """
    Simulates fetching data from an API and landing it in DBFS.
    This logic is modular and easy to unit test later.
    """
    spark = get_spark_session()
    
    logger.info("Initializing Data Ingestion...")

    # Data Engineering Tip: Start with a simple schema-enforced DataFrame
    raw_data = [("Ingestion_Run_A", 10.5), ("Ingestion_Run_B", 20.3)]
    columns = ["run_id", "metric_value"]

    try:
        # Create a DataFrame (this simulates your API data)
        df = spark.createDataFrame(raw_data, columns)

        # Define your landing path (Medallion - Bronze Layer)
        landing_path = "/tmp/api_ingestion/bronze_data"

        logger.info(f"Writing data to DBFS: {landing_path}")
        
        # Writing as Parquet (Standard for Data Lakes)
        df.write.mode("overwrite").parquet(landing_path)
        
        logger.info("Ingestion Job Successful.")

    except Exception as e:
        # We catch the base Exception but log the specific error
        logger.error(f"Ingestion failed with error: {str(e)}")
        raise  # Re-raise so the Databricks Job status turns RED

if __name__ == "__main__":
    ingest_api_data()