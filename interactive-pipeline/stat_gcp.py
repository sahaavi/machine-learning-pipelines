import tensorflow_data_validation as tfdv
from apache_beam.options.pipeline_options import PipelineOptions, SetupOptions, GoogleCloudOptions
import argparse
import apache_beam as beam
import os

# Global variables for configuration
PROJECT_ID = 'ml-pipelines-422521'
JOB_NAME = 'ml-pipelines-job'
GCS_STAGING_LOCATION = 'gs://ml-pipelines-s/staging'
GCS_TMP_LOCATION = 'gs://ml-pipelines-s/tmp'
GCS_DATA_LOCATION = 'gs://ml-pipelines-s/data'
GCS_STATS_OUTPUT_PATH = 'gs://ml-pipelines-s/data/stats_output'
PATH_TO_WHL_FILE = '/home/avisaha/machine-learning-pipelines/tensorflow_data_validation-1.15.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl'

# Parse command line arguments
parser = argparse.ArgumentParser()
args, beam_args = parser.parse_known_args()

# Set the Google Application Credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../credential_file.json"

# Create and set PipelineOptions
beam_options = PipelineOptions(
    beam_args,
    runner='DataflowRunner',
    project=PROJECT_ID,
    job_name=JOB_NAME,
    staging_location=GCS_STAGING_LOCATION,
    temp_location=GCS_TMP_LOCATION,
    region='us-east1',
    google_cloud_options=GoogleCloudOptions(
        credentials_file=os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
)
)

# Set up extra packages for the pipeline
setup_options = beam_options.view_as(SetupOptions)
setup_options.extra_packages = [PATH_TO_WHL_FILE]

# Create the Pipeline with the specified options
with beam.Pipeline(options=beam_options) as pipeline:
    # Generate statistics from TFRecord
    tfdv.generate_statistics_from_tfrecord(
        data_location=GCS_DATA_LOCATION,
        output_path=GCS_STATS_OUTPUT_PATH
    )
