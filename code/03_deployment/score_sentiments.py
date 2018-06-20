# This script generates the scoring and schema files
# Creates the schema, and holds the init and run functions needed to 
# operationalize the Iris Classification sample

# Import data collection library. Only supported for docker mode.
# Functionality will be ignored when package isn't found

# Prepare the web service definition by authoring
# init() and run() functions. Test the functions
# before deploying the web service.
import os
import numpy as np
import sys, json
from azureml.api.schema.dataTypes import DataTypes
from azureml.api.schema.sampleDefinition import SampleDefinition
from azureml.api.realtime.services import generate_schema
import pandas

def init():
    from tatk.pipelines.text_classification.text_classifier import TextClassifier
    from sklearn.linear_model import LogisticRegression
    import os

    home_dir = os.getcwd() 
    model_file = os.path.join(home_dir, 'sk_model.zipc')

    # load the model from file into a global object
    global model
    model = TextClassifier.load(model_file)

def run(input_df):
    from tatk.pipelines.text_classification.text_classifier import TextClassifier
    from sklearn.linear_model import LogisticRegression
    import json

    pred = model.predict(input_df)
    json_str = pred.to_json()
    return json.dumps(json_str)


def main(): 
    from tatk.pipelines.text_classification.text_classifier import TextClassifier
    from sklearn.linear_model import LogisticRegression
    import pandas
    
    init()
    df = pandas.DataFrame(data=[['please add your good text here.']], columns=['tweets'])
    #input1 = pandas.DataFrame(data=[['please add your good text here.']], columns=['tweets'])
    inputs = {"input_df": SampleDefinition(DataTypes.PANDAS, df)}
    
    #Generate the schema
    generate_schema(run_func=run, inputs=inputs, filepath='service-schema.json')
    print("Schema generated")


if __name__ == "__main__":
    main()
