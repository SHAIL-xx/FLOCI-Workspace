import os
import boto3
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("FLOCI_ENDPOINT_URL", "http://localhost:4566")
region = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

print(f"Connecting to Floci at {endpoint}...")

s3 = boto3.client(
    "s3",
    endpoint_url=endpoint,
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", "test"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", "test"),
    region_name=region
)

try:
    response = s3.list_buckets()
    print("Successfully connected to Floci! Buckets:", response.get("Buckets", []))
except Exception as e:
    print("Could not connect to Floci (ensure the container is running):", e)
