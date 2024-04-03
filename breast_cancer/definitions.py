# Importing dependencies
from google.protobuf.duration_pb2 import Duration
from feast import Entity, Field, FeatureView, FileSource, ValueType, Field
from feast.types import Float64, Int64, Int32
from feast.data_format import ParquetFormat

# Declaring an entity for the dataset
patient = Entity(
    name="patient_id",
    value_type=ValueType.INT64, 
    description="The ID of the patient")

# Declaring the source of the first set of features
f_source1 = FileSource(
    path=r"/Users/dheeraj/DSAN/PPOL/feast_feature_store/breast_cancer/data/data_df1.parquet",
    file_format=ParquetFormat(),
    event_timestamp_column="event_timestamp",
 )

# Defining the first set of features
df1_fv = FeatureView(
    name="df1_feature_view",
    ttl=None,
    entities=[patient],
    schema=[
        Field(name="mean radius", dtype=Float64),
        Field(name="mean texture", dtype=Float64),
        Field(name="mean perimeter", dtype=Float64),
        Field(name="mean area", dtype=Float64),
        Field(name="mean smoothness", dtype=Float64)
        ],    
    source=f_source1
)

# Declaring the source of the second set of schema
f_source2 = FileSource(
    path=r"/Users/dheeraj/DSAN/PPOL/feast_feature_store/breast_cancer/data/data_df2.parquet",
    file_format=ParquetFormat(),
    # event_timestamp_column="event_timestamp",
)

# Defining the second set of schema
df2_fv = FeatureView(
    name="df2_feature_view",
    ttl=None,
    entities=[patient],
    schema=[
        Field(name="mean compactness", dtype=Float64),
        Field(name="mean concavity", dtype=Float64),
        Field(name="mean concave points", dtype=Float64),
        Field(name="mean symmetry", dtype=Float64),
        Field(name="mean fractal dimension", dtype=Float64)
        ],    
    source=f_source2
)

# Declaring the source of the third set of schema
f_source3 = FileSource(
    path=r"/Users/dheeraj/DSAN/PPOL/feast_feature_store/breast_cancer/data/data_df3.parquet",
    file_format=ParquetFormat(),
    # event_timestamp_column="event_timestamp",
)

# Defining the third set of schema
df3_fv = FeatureView(
    name="df3_feature_view",
    ttl=None,
    entities=[patient],
    schema=[
        Field(name="radius error", dtype=Float64),
        Field(name="texture error", dtype=Float64),
        Field(name="perimeter error", dtype=Float64),
        Field(name="area error", dtype=Float64),
        Field(name="smoothness error", dtype=Float64),
        Field(name="compactness error", dtype=Float64),
        Field(name="concavity error", dtype=Float64)
        ],    
    source=f_source3
)

# Declaring the source of the fourth set of schema
f_source4 = FileSource(
    path=r"/Users/dheeraj/DSAN/PPOL/feast_feature_store/breast_cancer/data/data_df4.parquet",
    # event_timestamp_column="event_timestamp",
    file_format=ParquetFormat(),
)

# Defining the fourth set of schema
df4_fv = FeatureView(
    name="df4_feature_view",
    ttl=None,
    entities=[patient],
    schema=[
        Field(name="concave points error", dtype=Float64),
        Field(name="symmetry error", dtype=Float64),
        Field(name="fractal dimension error", dtype=Float64),
        Field(name="worst radius", dtype=Float64),
        Field(name="worst texture", dtype=Float64),
        Field(name="worst perimeter", dtype=Float64),
        Field(name="worst area", dtype=Float64),
        Field(name="worst smoothness", dtype=Float64),
        Field(name="worst compactness", dtype=Float64),
        Field(name="worst concavity", dtype=Float64),
        Field(name="worst concave points", dtype=Float64),
        Field(name="worst symmetry", dtype=Float64),
        Field(name="worst fractal dimension", dtype=Float64),        
        ],    
    source=f_source4
)

# Declaring the source of the targets
target_source = FileSource(
    path=r"/Users/dheeraj/DSAN/PPOL/feast_feature_store/breast_cancer/data/target_df.parquet", 
    # created_timestamp_column="event_timestamp",
    file_format=ParquetFormat(),
)

# Defining the targets
target_fv = FeatureView(
    name="target_feature_view",
    entities=[patient],
    ttl=None,
    schema=[
        Field(name="target", dtype=Int32)        
        ],    
    source=target_source
)