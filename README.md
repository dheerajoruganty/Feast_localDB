# FEAST with a local Data Base

## Overview

This repo demonstrates the use of Feast as part of a real-time breast cancer prediction application.
* I have used the breast cancer data from sklearn to start with. This data is only 567 rows as of writing this readme.
* This repo is mainly designed to be a good starting point for feast and how to use it. 
* I have included all the steps to set up feast for `x86` and `arm64` cpu architectures.
* Please make sure that you use a separate conda env as this would otherwise mess up few compatibilities. I have included a `myEnv.yaml` file in this repo for `arm64` processors.
* Also for `arm64` processors, I have included the script that would install and configure feast for this repo to be run named `setupArm64.sh`.

## To do:
* Expand the dataset to more than 10000 rows to actually see the difference in latency.
* Use an S3 bucket to retrieve the features
* Make the readme better.
* Create the `myEnv.yaml` file
* Create the `setupArm64.sh` file
* Benchmarking latency of Feast v/s Regular loading
* Output the accuracy of model

## Requirements for ARM64 Based MacOS

* `brew` for Mac OS
* `Python 3.10.x` or `Python 3.9.x`


## Requirements for x86 based pcs:

* `Python 3.10.x` or `Python 3.9.x`

## Setup

### Installing Feast for x86:

Install Feast using pip:

```
pip install feast==0.36.0
```

## Installing Feast for Arm64:

As everything in life with ARM64 is difficult, Feast is no different.

In terminal:


```
brew install xz protobuf openssl zlib
```

Activate the Conda Environment. Then run these:

```
pip install --upgrade pip
pip install cryptography -U

export CFLAGS="-I$(brew --prefix protobuf)/include"
export LDFLAGS="-L$(brew --prefix protobuf)/lib"

# Please set the protobuf version below
pip install protobuf==4.23.3 --force-reinstall --no-deps --config-settings="--build-option=--cpp_implementation"
```

## Setting up a Feature Store:

We have already set up a feature repository in [breast_cancer/](breast_cancer/). It isn't necessary to create a new
feature repository, but it can be done using the following command

```
feast init -t feature_repo # Command only shown for reference.
```

Since we don't need to `init` a new repository, all we have to do is configure the 
[feature_store.yaml/](breast_cancer/feature_store.yaml) in the feature repository. This is already setup right now. 
We will be using a local database to store the features. A standard feature store would usually be created with either AWS or GCP as the online feature store as they are more reliable.

```
project: breast_cancer
registry: data/registry.db
provider: local
online_store:
    path: data/online_store.db
```
### Modify the `definitions.py` file:

There are 5 file sources defined in definitions.py which need to be modified. Modify just the path to the files. Use entire syspath.
```
f_source1 = FileSource(
    path=r"/Users/dheeraj/DSAN/PPOL/feast_feature_store/breast_cancer/data/data_df1.parquet",
    file_format=ParquetFormat(),
#     event_timestamp_column="event_timestamp",
 )
```

Deploy the feature store by running `apply` from within the `breast_cancer/` folder
```
cd breast_cancer/
feast apply
```
```
Registered entity patient_id
Registered feature view df1_feature_view
Registered feature view df2_feature_view
Registered feature view df3_feature_view
Registered feature view df4_feature_view
Registered feature view target_feature_view
Deploying infrastructure for df1_feature_view
Deploying infrastructure for df2_feature_view
Deploying infrastructure for df3_feature_view
Deploying infrastructure for df4_feature_view
Deploying infrastructure for target_feature_view
```

## Train and test the model
- Navigate back to the base directory.

Entities and features have been registered with feast. Next, we move on to create a parquet file which contains the entire dataset to train and test the model. this can be found in `create_dataset.py`. Run this file.


```{.bash}
python create_dataset.py
```

A new file named `breast_cancer_dataset.parquet` should be created here: `/data/breast_cancer_dataset.parquet`


### Training the dataset:

Run the `train.py` file to train the model and store the results. A new file named `model.joblib` should be created after this. In this step, we are dumping the model to the base repo

```
python train.py
```

Next we load features into the online store using the `materialize-incremental` command. To do this, Navigate into the `breast_cancer/` and run the command below.
This command will load the latest feature values from a data source into the online store.

```
CURRENT_TIME=$(date -u +"%Y-%m-%dT%H:%M:%S")
feast materialize-incremental $CURRENT_TIME
```

Return to the root of the repository
```
cd ..
```



## Testing demo

Once the model has been trained it can be used for testing the model. In this step, simply run the command below to get the results of the test.

```
python predict.py
```
