# Telco Churn Project

## Project Summary
### Project Objectives
- Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report
- Create modules (acquire.py, prepare.py) that make your process repeateable
- Construct a model to predict customer churn using classification techniques
- Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience
- Answer panel questions about your code, process, findings and key takeaways, and model

### Business Goals
- Find drivers for customer churn at Telco
- Construct a ML classification model that accurately predicts customer churn
- Document your process well enough to be presented or read like a report

### Audience
- CodeUp Data Science Team

### Project Deliverables
- A final report notebook
- A final report notebook presentation
- All necessary modules to make my project reproducible
- A csv file of prediction probabilities and actual values for species

### Project Context
- The telco dataset came from the CodeUp database

### Data Dictionary
- churn: If the customer churned = Yes/1; if the customer didn't churn = No/0
- churned: If the customer churned = Yes/1; if the customer didn't churn = No/0
- tenure: Number of months person has been a customer.
- monthly_charges: Individual customer's monthly charge (in dollars $)
- total_charges: Individual customer's total charges over their entire tenure (in dollars $)
- gender: Female/Male
- is_female: 1 = Yes/female, 0 = No/male
- senior citizen: 0 = No, 1 = Yes
- partner: 1 = Yes, 0 = No
- dependents: 1 = Yes, 0 = No
- paperless_billing: 1 = Yes, 0 = No
- is_automatic: derived from the payment_type column; 1 == auto bank transfer and Credit Card (auto). 0 == Mailed check and Electronic check.
- prediction (in predictions.csv): 1 = churned, 0 = didn't churn, according to model's predictions.

## Executive Summary - Conclusions & Next Steps
**Findings:**
- Early analysis showed that rate of churn goes down as tenure increases
- Biggest drivers of churn were payment type, contract type, and total charges
- Classification model predicts whether a customer will churn with 78% accuracy

**Recommendations:**
- Offer discounts for automatic payment types and one or two-year contracts
- Run advertising campaign promoting new discounts

**Next steps:**
- Test out the model on out of sample data to see how well it performs in the wild

## Pipeline Stages Breakdown
**Plan** -> Acquire -> Prepare -> Explore -> Model -> Deliver
- Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- Establish a baseline accuracy and document well.
- Train three different classification models.
- Evaluate models on train and validate datasets.
- Choose the model with that performs the best and evaluate that single model on the test dataset.
- Create csv file with the customer id, the probability of churning, and the model's prediction for each observation in my test dataset.
- Document conclusions, takeaways, and next steps in the Final Report Notebook.

Plan -> **Acquire** -> Prepare -> Explore -> Model -> Deliver
- Store functions that are needed to acquire data from the telco database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
- The final function will return a pandas DataFrame.
- Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
- Complete some initial data summarization (.info(), .describe(), .value_counts(), ...).
- Plot distributions of individual variables.

Plan -> Acquire -> **Prepare** -> Explore -> Model -> Deliver
- Store functions needed to prepare the telco data; make sure the module contains the necessary imports to run the code. The final function should do the following: - Split the data into train/validate/test. - Handle any missing values. - Handle erroneous data and/or outliers that need addressing. - Encode variables as needed. - Create any new features, if made for this project.
- Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.

Plan -> Acquire -> Prepare -> **Explore** -> Model -> Deliver
- Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, species.
- Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
- Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to churn (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
- Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.

Plan -> Acquire -> Prepare -> Explore -> **Model** -> Deliver
- Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
- Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
- Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
- Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
- Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
- Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.

Plan -> Acquire -> Prepare -> Explore -> Model -> **Deliver**
- Introduce myself and my project goals at the very beginning of my notebook walkthrough.
- Summarize my findings at the beginning like I would for an Executive Summary. (Don't throw everything out that I learned from Storytelling) .
- Walk Codeup Data Science Team through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.)
- Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.

## Reproduce My Project
You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.
- Read this README.md
- Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- Add your own env file to your directory. (user, password, host)
- Run the final_report.ipynb notebook