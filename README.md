# ETL Pipeline v1

### Introduction
Building an ETL Pipeline that does the following:
- Queries data from Redshift, joins the tables called 
- Identifies and removes any duplicates
- Loads the data to the bootcamp's s3 bucket

### Requirements
  The minimum requirements:
- Docker for Windows: 
  - Installation: [Docker](https://docs.docker.com/desktop/install/windows-install/)
  - Manual installation steps for older WSL version: [Docker WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)

### Instructions on how to execute the code
- Copy the `.env.example` file to `.env` and fill out the environment variables.

- Make sure you are executing the code from the etl_pipeline folder and you have Docker Desktop running.


To run it locally first build the image.

```bash
  docker image build -t etl-pipeline.
```

Then run the etl job using docker:
```bash
  docker run --env-file .env etl-pipeline.
```