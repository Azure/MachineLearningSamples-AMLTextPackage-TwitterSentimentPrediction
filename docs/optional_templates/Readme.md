# docs/optional_templates

## Folder hosting optional data science project templates. 

These templates can be used, as necessary for for documentation of your project. Some of these may be moved to customer docs or deliverable_docs. For example, project-charter may be prepared at the beginning of the project and shared with the customer as a deliverable. model-report may also be another stand-alone deliverable document, or information from this document may be included in the \/deliverable\_docs/ProjectReport.md.

Optional templates include:

### project-charter.md
This template helps to define business background, scope, metrics (KPIs - key performance indicators), success criteria, architecture, etc. This can be initially used with the customer to define the project as accurately as possible, and set expectations about deliverables and success criteria.

### data-dictionaries.md
This document provides the descriptions of the data that is provided by the client. As appropriate, this may be placed in customer_docs.

### Raw-Data-Dictionary.csv
This file should contain information about raw data files, and all the fields in these files. For example, column name, variable type, variable range etc. One file may be prepared for each raw data file.

### data-definition.md
Data and feature definitions. 
NOTE: In this file, links need to be replace by links your data sets.

### DataPipelines.txt
Describe the data pipeline and provide a logical diagram. List how frequently the data is moved - real time/stream, near real time, batched with frequency etc.

### data-summary-report.md
This file may be generated for each data file received or processed. The [Interactive Data Exploration, Analysis, and Reporting (IDEAR)](https://github.com/Azure/Azure-TDSP-Utilities) utility can help you explore and visualize the data in an interactive way, and generate the data report along with the process of exploration and visualization.

### model-report.md
Report describing the final model to be delivered - typically comprised of one or more of the models built during the life of the project.

### project-exit-report.md
This is a report (alternative to the /docs/deliberable_docs/ProjectReport.md) that can be used as a deliverable final report to the customer.

### Notes:
Any notes you want to keep about the Docs
