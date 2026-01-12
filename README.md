# APIStream Analytics

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.5.0-orange.svg)](https://spark.apache.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready real-time data pipeline built with **Apache Spark Structured Streaming** to process, analyze, and monitor API logs at scale. This project demonstrates enterprise-grade Big Data engineering practices including ETL, streaming analytics, data quality validation, and anomaly detection.

## Project Overview

APIStream Analytics simulates and processes high-volume API traffic logs in real-time, providing actionable insights into API performance, error rates, and usage patterns. The pipeline processes millions of events, aggregates metrics, detects anomalies, and stores results for further analysis.

### Key Features

- **Real-Time Streaming**: Apache Spark Structured Streaming for continuous data processing
- **Scalable ETL**: Modular data transformation and validation pipeline
- **Data Quality Checks**: Automated validation, anomaly detection, and monitoring
- **Performance Analytics**: Response time analysis, error rate tracking, throughput metrics
- **Production-Ready**: Configurable, tested, and documented for enterprise deployment
- **Cloud-Ready**: Designed for deployment on GCP (Dataproc), AWS (EMR), or Azure (Databricks)

## Architecture

```
[API Log Generator] → [Streaming Source] → [Spark Streaming]
                                                  ↓
                                         [ETL & Validation]
                                                  ↓
                                    [Aggregation & Analytics]
                                                  ↓
                              [Parquet Files] | [SQLite DB]
                                                  ↓
                                         [Visualization]
```

## Tech Stack

- **Language**: Python 3.8+
- **Big Data**: Apache Spark 3.5.0 (PySpark, Structured Streaming)
- **Storage**: Parquet (columnar), SQLite (analytics)
- **Data Quality**: Custom validation framework
- **Visualization**: Matplotlib, Plotly, Seaborn
- **Testing**: pytest
- **Configuration**: YAML

## Prerequisites

- Python 3.8 or higher
- Java 8 or 11 (required for Spark)
- 4GB+ RAM recommended
- Git

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/apistream-analytics.git
cd apistream-analytics
```

### 2. Set Up Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Settings

Edit `config/config.yaml` to customize:
- Data generation rate
- API endpoint configurations
- Output paths
- Spark settings

### 4. Run the Pipeline

**Terminal 1: Start Data Generator**
```bash
python src/data_generator.py
```

**Terminal 2: Start Spark Streaming Pipeline**
```bash
python src/spark_streaming_pipeline.py
```

**Terminal 3: Run Batch Analytics (optional)**
```bash
python src/batch_analytics.py
```

### 5. View Results

```bash
# Open Jupyter notebook for visualization
jupyter notebook notebooks/analytics_visualization.ipynb
```

## Sample Outputs

### Metrics Generated

- **Response Time Analytics**: Min, Max, Avg, P95, P99 latencies per API
- **Error Rate Tracking**: 4xx, 5xx error percentages by endpoint
- **Throughput Monitoring**: Requests per second, minute, hour
- **Anomaly Detection**: Statistical outliers in response times
- **Top N Analysis**: Slowest APIs, highest error endpoints

### Data Quality Checks

- Missing field validation  
- Schema enforcement  
- Anomaly detection (> 2 standard deviations)  
- Duplicate detection  
- Timestamp validation  

## Key Data Engineering Concepts

### 1. **Streaming Data Processing**
- Micro-batch processing with Spark Structured Streaming
- Watermarking for late-arriving data
- Stateful streaming aggregations

### 2. **ETL Pipeline Design**
- Extract: Read from streaming source
- Transform: Clean, validate, enrich data
- Load: Write to Parquet and database

### 3. **Data Quality Framework**
- Schema validation
- Null/missing value handling
- Statistical anomaly detection
- Data reconciliation

### 4. **Performance Optimization**
- Partitioning strategies for Parquet files
- Column pruning and predicate pushdown
- Memory management and caching
- Broadcast joins for dimension tables

### 5. **Production Best Practices**
- Modular, reusable code
- Configuration management
- Error handling and logging
- Unit testing
- Documentation

## Running Tests

```bash
pytest tests/ -v
```

## Cloud Deployment (Optional)

### Google Cloud Platform (Dataproc)

```bash
# Create Dataproc cluster
gcloud dataproc clusters create apistream-cluster \
    --region=us-central1 \
    --num-workers=2 \
    --worker-machine-type=n1-standard-4

# Submit Spark job
gcloud dataproc jobs submit pyspark \
    src/spark_streaming_pipeline.py \
    --cluster=apistream-cluster \
    --region=us-central1
```

### AWS EMR

```bash
# Create EMR cluster
aws emr create-cluster \
    --name "APIStream Analytics" \
    --release-label emr-6.10.0 \
    --applications Name=Spark \
    --instance-type m5.xlarge \
    --instance-count 3

# Submit job via EMR console or AWS CLI
```

## Extending the Project

### Ideas for Enhancement

1. **Kafka Integration**: Replace file-based streaming with Apache Kafka
2. **Real-Time Dashboard**: Add Grafana/Kibana for live monitoring
3. **ML-Based Anomaly Detection**: Use Spark MLlib for pattern recognition
4. **Multi-Source Ingestion**: Add support for database CDC, message queues
5. **Data Lake Integration**: Store raw data in S3/GCS, processed in BigQuery
6. **Airflow Orchestration**: Schedule and monitor with Apache Airflow
7. **Delta Lake**: Add ACID transactions and time travel
