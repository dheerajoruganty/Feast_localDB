# Importing dependencies
from feast import FeatureStore
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump
import pandas as pd
from datetime import datetime

entity_df = pd.read_parquet(path="breast_cancer/data/target_df.parquet")  

features=[
        "df1_feature_view:mean radius",
        "df1_feature_view:mean texture",
        "df1_feature_view:mean perimeter",
        "df1_feature_view:mean area",
        "df1_feature_view:mean smoothness",
        "df2_feature_view:mean compactness",
        "df2_feature_view:mean concavity",
        "df2_feature_view:mean concave points",
        "df2_feature_view:mean symmetry",
        "df2_feature_view:mean fractal dimension",
        "df3_feature_view:radius error",
        "df3_feature_view:texture error",
        "df3_feature_view:perimeter error",
        "df3_feature_view:area error",
        "df3_feature_view:smoothness error",
        "df3_feature_view:compactness error",
        "df3_feature_view:concavity error",
        "df4_feature_view:concave points error",
        "df4_feature_view:symmetry error",
        "df4_feature_view:fractal dimension error",
        "df4_feature_view:worst radius",
        "df4_feature_view:worst texture",
        "df4_feature_view:worst perimeter",
        "df4_feature_view:worst area",
        "df4_feature_view:worst smoothness",
        "df4_feature_view:worst compactness",
        "df4_feature_view:worst concavity",
        "df4_feature_view:worst concave points",
        "df4_feature_view:worst symmetry",
        "df4_feature_view:worst fractal dimension",
    ]

# Getting our FeatureStore
store = FeatureStore(repo_path="/Users/dheeraj/DSAN/PPOL/feast_feature_store/breast_cancer")

# Retrieving the saved dataset and converting it to a DataFrame
training_df = store.get_historical_features(
    features=features,
    entity_df=entity_df
).to_df()

print(training_df.head())


# Separating the features and labels
labels = training_df['target']
features = training_df.drop(
    labels=['event_timestamp', "patient_id","target"], 
    axis=1)

# Splitting the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(features, 
                                                    labels, 
                                                    stratify=labels)

# Creating and training LogisticRegression
reg = LogisticRegression(solver='lbfgs', max_iter=10000)
reg.fit(X=X_train[sorted(X_train)], y=y_train)

# Saving the model
dump(value=reg, filename="model.joblib")