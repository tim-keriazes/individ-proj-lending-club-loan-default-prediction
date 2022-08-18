# <a name="top"></a>Lending Tree Loan Default Prediction 
![]()

by: Tim Keriazes

<p>
  <a href="https://github.com/tim-keriazes" target="_blank">
    <img alt="Matthew" src="https://img.shields.io/github/followers/tim-keriazes?label=Follow_Tim&style=social" />
  </a>
</p>


***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___

<img src="https://docs.google.com/drawings/d/e/2PACX-1vR19fsVfxHvzjrp0kSMlzHlmyU0oeTTAcnTUT9dNe4wAEXv_2WJNViUa9qzjkvcpvkFeUCyatccINde/pub?w=1389&amp;h=410">

## <a name="project_description"></a>Project Description:
Financial institutions across the globe have a need to accurately parse which customers are appropriate candidates for their financial offerings. Based on a customer's historical financials, institutions aqcuire the ability to accurately assess risk and make appropriate business decisions. In this project, I will analyze the lending_club_loan_two.csv dataset to discover drivers for loan defaults. I will use my discoveries to build a machine learning model that would help predict the status of a customer's loan, and in turn, whether or not they are likely candidates to default on a loan.

[[Back to top](#top)]

***
## <a name="planning"></a>Project Planning/Outline: 
1. Investigating the dataset/data dictionary
2. Establishing initial questions/hypotheses
3. Data acquisition
4. Data preparation
5. Exploration and Data Analysis
6. Identify drivers
7. Encode features
8. Split data
9. Model
10. Evaluate Models
11. Test
12. Conclusions/Next Steps 


[[Back to top](#top)]
        
### Hypothesis
1. Loan status is correlated with sub_grade
2. Loan status is correlated with revol_util
3. Loan status is correlated with int_rate


### Target variable
loan_status (Charged Off or Fully Paid)

### Need to haves (Deliverables):
Machine learning classification model accurately predicting target variable

***

## <a name="findings"></a>Key Findings:

1. 80% of the observations were fully paid, so if we predict all of the observations are fully paid, baseline would predict correctly 80% of the time, establishing a baseline accuracy of 80%
2. high loan amount, high installment, looks like it has more charge offs
3. high int rate, looks like high charge offs
4. high loan amount for renters looks like higher charge offs
5. high int rate, high dti, higher charge offs
6. low subgrade/grade, looks like higher charge offs


[[Back to top](#top)]




***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Used
---
| Attribute | Definition |   |
| ----- | ----- |----- |
|	LoanStat|	Description|
|0	|loan_amnt|	The listed amount of the loan applied for by the borrower. If at some point in time, the credit department reduces the loan amount, then it will be reflected in this value.
|1	|term|	The number of payments on the loan. Values are in months and can be either 36 or 60.
|2	|int_rate|	Interest Rate on the loan
|3	|installment|	The monthly payment owed by the borrower if the loan originates.
|4	|grade|	LC assigned loan grade
|5	|sub_grade|	LC assigned loan subgrade
|6	|emp_title|	The job title supplied by the Borrower when applying for the loan.*
|7	|emp_length|	Employment length in years. Possible values are between 0 and 10 where 0 means less than one year and 10 means ten or more years.
|8	|home_ownership|	The home ownership status provided by the borrower during registration or obtained from the credit report. Our values are: RENT, OWN, MORTGAGE, OTHER
|9	|annual_inc|	The self-reported annual income provided by the borrower during registration.
|10	|verification_status|	Indicates if income was verified by LC, not verified, or if the income source was verified
|11	|issue_d|	The month which the loan was funded
|12	|loan_status|	Current status of the loan
|13	|purpose|	A category provided by the borrower for the loan request.
|14	|title|	The loan title provided by the borrower
|15	|zip_code|	The first 3 numbers of the zip code provided by the borrower in the loan application.
|16	|dti|	A ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income.
|17	|earliest_cr_line|	The month the borrower's earliest reported credit line was opened
|18	|open_acc|	The number of open credit lines in the borrower's credit file.
|19	|pub_rec|	Number of derogatory public records
|20	|revol_bal|	Total credit revolving balance
|21	|revol_util|	Revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit.
|22	|total_acc|	The total number of credit lines currently in the borrower's credit file
|23	|initial_list_status|	The initial listing status of the loan. Possible values are – W, F
|24	|application_type|	Indicates whether the loan is an individual application or a joint application with two co-borrowers
|25	|mort_acc|	Number of mortgage accounts.
|26	|pub_rec_bankruptcies|	Number of public record bankruptcies

***

## <a name="wrangle"></a>Data Acquisition and Preparation
Aqcuired the data from kaggle

https://www.kaggle.com/datasets/jeandedieunyandwi/lending-club-dataset

[[Back to top](#top)]

![]()


### Wrangle steps: 
1. Analyze data
2. ID nulls
3. Handle nulls
4. drop duplicate information
5. handle outliers
6. build clean_lending() function to accomplish this for wrangle file

*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - wrangle.py 
    - explore.py
    - modeling.py


### Takeaways from exploration:
1. 80% fully paid
2. EDA Outlier Analysis (remove_outliers() function)
get rid of dti > 40
get rid of total_acc > 115
get rid of annual_inc > 250,000
get rid of revol_util > 200
get rid of pub_rec > 25
get rid of open_acc > 60
get rid of small proportion of home_ownership values for ['OTHER','ANY','NONE']

3. Heatmap takeaways:
loan amount and installment are appear to be highly correlated
loan amount and revol balance appear to be correlated
loan amount and annual income appear to be correlated
annual income and installment appear to be correlated

***
#### Summary:

high loan amount, high installment, looks like it has more charge offs
high int rate, looks like high charge offs
high loan amount for renters looks like higher charge offs
high int rate, high dti, higher charge offs
low subgrade/grade, looks like higher charge offs


## <a name="model"></a>Modeling:
1. split
2. encode categoricals
3. verify shape
4. drop unneeded features


[[Back to top](#top)]

### Model Preparation:
1. establish baseline
2. fit models on train sets only


### Baseline
    
- Baseline Results: 80% of the observations were fully paid, so if we predict all of the observations are fully paid, baseline would predict correctly 80% of the time, establishing a baseline accuracy of 80%
    

- Selected features to input into models:
    - features = [loan_amnt,int_rate,installment, annual_inc, dti, revol_bal,revol_util , mort_acc,grade_encoded, home_ownership_encoded,  w, Source Verified, Verified ]

***

### Models:
- Will run the following classification models:
1. Decision Tree
2. Random Forest
3. KNN
    

- Other indicators of model performance with breif defiition and why it's important:
1. Precision
2. Recall
3. F1 Score
4. Baseline comparison
    
    
#### Model 1: Decision Tree


- Model 1 results:
- Lots of trials of varying depths, started at 3 resulting in charge off precision of 60% increasing depth to 15 increased charge off precision 16% to 76% and Paid precision to 86%



### Model 2 : Random Forest


- Model 2 results:
- After trials, better performance with lower n values, n=3 yielded 86% precision on fully paid

### Model 3 : KNN

- Model 3 results:
- After trials, better performance with lower n values, n=3 yielded 86% precision on fully paid, and 70% charged off
## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

<!-- | Model | Validation/Out of Sample RMSE | R<sup>2</sup> Value |
| ---- | ----| ---- |
| Baseline | 0.167366 | 2.2204 x 10<sup>-16</sup> |
| Linear Regression (OLS) | 0.166731 | 2.1433 x 10<sup>-3</sup> |  
| Tweedie Regressor (GLM) | 0.155186 | 9.4673 x 10<sup>-4</sup>|  
| Lasso Lars | 0.166731 | 2.2204 x 10<sup>-16</sup> |  
| Quadratic Regression | 0.027786 | 2.4659 x 10<sup>-3</sup> |   -->


- {} model performed the best


## Testing the Model

- Model Testing Results
