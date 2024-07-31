# Classification

**title of the data:** "Bank Marketing"

**description:** The data is from a Portuguese bank, which was gathered during a direct marketing campaign (phone calls), the goal of which was to get a customer to agree to a term deposit. (Often more than one call was needed for the customer to decide for or against a term deposit). The target feature indicates wether a customer agreed to a term deposit or not.

**goal:** classify customers of the bank (who have been exposed to marketing activities) into two groups: those who agreed to a term deposit and those who didn't

**source:**
The [dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing) is publicly available from the [UCI Machine Learning Repository](https://archive.ics.uci.edu).



## Imaginary business settings
Some assumptions and made-up aspects of the dataset have to be made for this project to seem relevant for a machine learning model, which is to be used in production to generate more revenue:

- A similar marketing campaign will be conducted in near future.
- The data at hand will be dynamic: the values of the columns concerning the number of calls and their duration will be updated after each call.
- It will be important to know for the bank before making the (next) call, how probable it is that the client will agree to a term deposit during (or after) the next call. 
- For this reason, a ML model will run periodically on the (constantly updated) dataset, to determine the customers with the highest probability to agree to a term deposit. Those customers will be contacted first.
- or perhaps, before making a call to a preselected customer, a marketing agent will run the ML model to determine how probable it is that the customer will agree to a term deposit. If it is highly probable, then the agent will try to be more persuasive or prepare more offers connected to the term deposit. 

<br>

## Features of the data:


```text
   1 - age (numeric)
   2 - job : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur","student",
                                       "blue-collar","self-employed","retired","technician","services") 
   3 - marital : marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)
   4 - education (categorical: "unknown","secondary","primary","tertiary")
   5 - default: has credit in default? (binary: "yes","no")
   6 - balance: average yearly balance, in euros (numeric) 
   7 - housing: has housing loan? (binary: "yes","no")
   8 - loan: has personal loan? (binary: "yes","no")
   
   Related with the last contact of the current campaign:
   9 - contact: contact communication type (categorical: "unknown","telephone","cellular") 
  10 - day: last contact day of the month (numeric)
  11 - month: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")
  12 - duration: last contact duration, in seconds (numeric)
   
   Other attributes:
  13 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
  14 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)
  15 - previous: number of contacts performed before this campaign and for this client (numeric)
  16 - poutcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")

  Output variable (desired target):
  17 - y - has the client subscribed a term deposit? (binary: "yes","no")
  ```

<br>

## Frame the problem and look at the big picture

- **Define the objective in business terms**: Increase revenue by focusing on the customers who are likely to agree to a term deposit.


- **How will your solution be used?**: ...

What are the current solutions?

How should you frame this problem (supervised/unsupervised, online/offline, etc.)

How should performance be measured?

Is the performance measure aligned with the business objective?

What would be the minimum performance needed to reach the business objective?

What are comparable problems? Can you reuse experience or tools?

Is human expertise available?

How would you solve the problem manually?

List the assumptions you or others have made so far.

Verify assumptions if possible.










<br>

## The Checklist:

https://github.com/leztien/Projects-Portfolio/blob/main/CHECKLITST.md






CHATGPT:

The goal of these campaigns is to determine whether a client will subscribe to a term deposit.

Some attributes like 'duration' are known to have a high influence on the target variable, but they need careful handling since they are not known before the call is performed.

Explore data preprocessing techniques, including handling of missing values, categorical encoding, and feature scaling.

Apply and compare various machine learning algorithms such as Logistic Regression, Decision Trees, Random Forests, Gradient Boosting, and Neural Networks.

Evaluate model performance using metrics like accuracy, precision, recall, F1-score, ROC-AUC, and confusion matrix.

Implement model validation techniques, including cross-validation.