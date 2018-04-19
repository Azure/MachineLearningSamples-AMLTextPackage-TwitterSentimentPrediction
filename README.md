# Use word embeddings to predict Twitter sentiment following Team Data Science Process & AML Package for Text Analytics


## Link to the Microsoft DOCS site

Documentation that walks you through this example is available at: 

[https://docs.microsoft.com/azure/machine-learning/team-data-science-process/predict-twitter-sentiment-amltextpackage](https://docs.microsoft.com/azure/machine-learning/team-data-science-process/predict-twitter-sentiment-amltextpackage)


## Link to the Gallery GitHub repository

The public GitHub repository for this example contains all the code samples:
[https://github.com/Azure/MachineLearningSamples-AMLTextPackage-TwitterSentimentPrediction](https://github.com/Azure/MachineLearningSamples-AMLTextPackage-TwitterSentimentPrediction)



## Summary

Sentiment analysis is a widely research topic in the Natural Language Processing domain. It has the applications in consumer reviews mining, public opinion mining and advertisement on online forums. Many of the sentiment analysis approaches use handcrafted features but the popularity of unsupervised and semi supervised approached to generate word embeddings have made these embedding techniques an important way to generate features. In this sample we are going to demonstrate the usage of Word Embedding algorithm **Word2Vec** to predict sentiment polarity. Word2Vec word features are used as input into logistic regression or convolutional neural networks to produce the final sentiment classification models. This end-to-end process is implemented in [Azure Machine Learning Workbench](https://docs.microsoft.com/en-us/azure/machine-learning/preview/overview-what-is-azure-ml) using Azure Machine Learning Package for Text Analytics and Team Data Science Process (TDSP). 


## Objective

The aim of this sample is to highlight how to use Azure Machine Learning package for Text Analytics and Team Data Science Process (TDSP) to predict the sentiment of Twitter text data. Here are the key points addressed:

* Train a Word2Vec embeddings model
* Use Word2Vec embeddings in Logistic Model and Keras CNN classification models
* Persist and deploy models as web service in Azure Container Services (AKS)

## Description of project: Twitter sentiment polarity classification
This article uses a sample to show you how to instantiate and execute a Machine Learning project. The sample uses the TDSP structure and templates in Azure Machine Learning Workbench. The complete sample is provided in this walkthrough. The modeling task predicts sentiment polarity (positive or negative) by using the text from tweets. This article outlines the data-modeling tasks that are described in the walkthrough. The walkthrough covers the following tasks:

1. Data exploration, training, and deployment of a machine learning model that address the prediction problem that's described in the use case overview. Twitter sentiment data is used for these tasks.
2. Execution of the project by using the TDSP template from Azure Machine Learning for this project. For project execution and reporting, the TDSP lifecycle is used.
3. Operationalization of the solution directly from Azure Machine Learning in Azure Container Service.

The project highlights the use of Text Analytics Package for Azure Machine Learning.

For code samples, click the View Project icon on the right and visit the project GitHub repository.

## Key components needed to run this example:

* An Azure [subscription](https://azure.microsoft.com/en-us/free/)
* Azure Machine Learning Workbench with a workspace created. See [installation guide](quick-start-installation.md). 
* You can run through the sample 'locally' on a [Data Science Virtual Machine (DSVM)](https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/overview).
* To provision DSVM for Windows 2016, follow the instructions [here](https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-data-science-provision-vm). We recommend using [NC6 Standard (56 GB, K80 NVIDIA Tesla)](https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-data-science-linux-dsvm-intro).


# Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
