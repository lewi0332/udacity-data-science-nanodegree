# The CRISP-DM Process (Cross Industry Process for Data Mining)

The lessons leading up to the first project are about helping you go through CRISP-DM in practice from start to finish. Even when we get into the weeds of coding, try to take a step back and realize what part of the process you are in, and assure that you remember the question you are trying answer and what a solution to that question looks like.

1. Business Understanding

2. Data Understanding

3. Prepare Data

4. Data Modeling

5. Evaluate the Results

6. Deploy

--- 

`3`

The first two steps of CRISP-DM are:

1. **Business Understanding** - this means understanding the problem and questions you are interested in tackling in the context of whatever domain you're working in. Examples include

   - How do we acquire new customers?
   - Does a new treatment perform better than an existing treatment?
   - How can we improve communication?
   - How can we improve travel?
   - How can we better retain information?


2. **Data Understanding** - at this step, you need to move the questions from **Business Understanding** to data. You might already have data that could be used to answer the questions, or you might have to collect data to get at your questions of interest.

---

`9`

**Business and Data Understanding**

**Business Questions**
- How do I break into the field?
- What are the placement and salaries of those who attended a coding bootcamp?
- How well can we predict an individual's salary? What aspects correlate well to salary?
- How well can we predict an individual's job satisfaction? What aspects correlate well to job satisfaction?

**Data Understanding**

You will be using the Stackoverflow survey data to get some insight into each of these questions. In the rest of the lesson, you can work along with me to answer these questions, or you can take your own approach to see if the conclusions you draw are similar to those you would find throughout this lesson.

---

`10`

**The CRISP-DM Process (Cross Industry Process for Data Mining)**

We have now defined the questions we want to answer and had a look through the data available to find the answers, that is, we have looked at the first two steps here:

1. Business Understanding

2. Data Understanding

We can now look at the third step of the process:

3. Prepare Data

Luckily stackoverflow has already collected the data for us. However, we still need to wrangle the data in a way for us to answer our questions. The wrangling and cleaning process is said to take 80% of the time of the data analysis process. You will see that will hold true through this lesson, as a majority of the remaining parts of this lesson will be around basic data wrangling strategies.

We will discuss the advantages and disadvantages of the strategies discussed in this lesson.

--- 

`18`

When looking at the first two questions:

- How to break into the field?
- What are the placement and salaries for those who attended a coding bootcamp?

We did not need to do any predictive modeling. We only used **descriptive** and a little **inferential** statistics to retrieve the results.

Therefore, all steps of CRISP-DM were not necessary for these first two questions. CRISP-DM states 6 steps:

1. Business Understanding

2. Data Understanding

3. Prepare Data

4. Data Modeling

5. Evaluate the Results

6. Deploy


For these first two questions, we did not need step `4`. In the previous notebooks, you performed steps `3` and `5` without needing step `4` at all. A lot of the hype in data science, artificial intelligence, and deep learning is integrated into step `4`, but there are still plenty of questions to be answered not using machine learning, artificial intelligence, and deep learning.

**All Data Science Problems Involve**

- Curiosity.

- The **right** data.

- A tool of some kind (Python, Tableau, Excel, R, etc.) used to find a solution (You could use your head, but that would be inefficient with the massive amounts of data being generated in the world today).

- Well communicated or deployed solution.

**Extra Useful Tools to Know But That Are NOT Necessary for ALL Projects**
- Deep Learning
- Fancy machine learning algorithms

With that, you will be getting a more in depth look at these items, but it is worth mentioning (given the massive amount of hype) that they do not solve all the problems. Deep learning cannot turn bad data into good conclusions. Or bad questions into amazing results.

---

`19`

When looking at the first two questions:

How to break into the field?
What are the placement and salaries for those who attended a coding bootcamp?
we did not need to do any predictive modeling. We only used **descriptive** and a little **inferential** statistics to retrieve the results.

Therefore, all steps of CRISP-DM were not necessary for these first two questions. The process would look closer to the following:

1. Business Understanding

2. Data Understanding

3. Prepare Data

4. Evaluate the Results

5. Deploy

However, for the last two questions:

1. How well can we predict an individual's salary? What aspects correlate well to salary?

2. How well can we predict an individual's job satisfaction? What aspects correlate well to job satisfaction?

We will need to use a predictive model. We will need to pick up at step 3 to answer these two questions, so let's get started. The process for answering these last two questions will follow the full 6 steps shown here.

In the modeling section, you will learn that step three of CRISP-DM is essential to getting the most out of your data. In this case, we are interested in using any of the variables we can from the dataset to predict an individual's salary.

The variables we use to predict are commonly called **X** (or an **X matrix**). The column we are interested in predicting is commonly called **y** (or the **response vector**).

In this case **X** is all the variables in the dataset that are not salary, while **y** is the salary column in the dataset.

On the next page, you will see what happens when we try to use sklearn to fit a model to the data, and we will do some work to get useful predictions out of our sklearn model.

---

`20`

In the modeling section, you will learn that step three of CRISP-DM is essential to getting the most out of your data. In this case, we are interested in using any of the variables we can from the dataset to predict an individual's salary.

The variables we use to predict are commonly called **X** (or an **X matrix**). The column we are interested in predicting is commonly called **y** (or the **response vector**).

In this case X is all the variables in the dataset that are not salary, while y is the salary column in the dataset.

On the next page, you will see what happens when we try to use sklearn to fit a model to the data, and we will do some work to get useful predictions out of our sklearn model.

---

`24`


There are two main 'pain' points for passing data to machine learning models in sklearn:

1. Missing Values
2. Categorical Values

Sklearn does not know how you want to treat missing values or categorical variables, and there are lots of methods for working with each. For this lesson, we will look at common, quick fixes. These methods help you get your models into production quickly, but thoughtful treatment of missing values and categorical variables should be done to remove bias and improve predictions over time.

Three strategies for working with missing values include:

1. We can remove (or “drop”) the rows or columns holding the missing values.
2. We can impute the missing values.
3. We can build models that work around them, and only use the information provided.

--- 

`25`

Though dropping rows and/or columns holding missing values is quite easy to do using numpy and pandas, it is often not appropriate.

Understanding why the data is missing is important before dropping these rows and columns. In this video you saw a number of situations in which dropping values was not a good idea. These included

1. Dropping data values associated with the effort or time an individual put into a survey.
2. Dropping data values associated with sensitive information.

In either of these cases, the missing values hold information. A quick removal of the rows or columns associated with these missing values would remove missing data that could be used to better inform models.

Instead of removing these values, we might keep track of the missing values using indicator values, or counts associated with how many questions an individual skipped.

---

`26`

n the last video, you saw cases in which dropping rows or columns associated with missing values would not be a good idea. There are other cases in which dropping rows or columns associated with missing values would be okay.

A few instances in which dropping a row might be okay are:

1. Dropping missing data associated with mechanical failures.
2. The missing data is in a column that you are interested in predicting.

Other cases when you should consider dropping data that are not associated with missing data:

1. Dropping columns with no variability in the data.
2. Dropping data associated with information that you know is not correct.

In handling removing data, you should think more about why is this missing or why is this data incorrectly input to see if an alternative solution might be used than dropping the values.

---

`27`
One common strategy for working with missing data is to understand the proportion of a column that is missing. If a large proportion of a column is missing data, this is a reason to consider dropping it.

There are easy ways using pandas to create dummy variables to track the missing values, so you can see if these missing values actually hold information (regardless of the proportion that are missing) before choosing to remove a full column.

---

`33`

Imputation is likely the most common method for working with missing values for any data science team. The methods shown here included the frequently used methods of imputing the mean, median, or mode of a column into the missing values for the column.

There are many advanced techniques for imputing missing values including using machine learning and bayesian statistical approaches. This could be techniques as simple as using k-nearest neighbors to find the features that are most similar, and using the values those features have to fill in values that are missing or complex methods like those in the very popular [AMELIA library](https://cran.r-project.org/web/packages/Amelia/Amelia.pdf).

Regardless your imputation approach, you should be very cautious of the **BIAS** you are imputing into any model that uses these imputed values. Though imputing values is very common, and often leads to better predictive power in machine learning models, it can lead to over generalizations. In extremely advanced techniques in Data Science, this can even mean [ethical implications](https://intelligence.org/files/EthicsofAI.pdf). Machines can only 'learn' from the data they are provided. If you provide biased data (due to imputation, poor data collection, etc.), it should be no surprise, you will achieve results that are biased.

---

`38`

Notice that in the earlier video in the pre-requisites, there was a mention of dropping a column to assure your X matrix is full rank. This is not true using LinearRegression within sklearn, because there is a ridge (or L2 penalty used by default). However, dropping the columns would also be okay, it is just not required, as it is with OLS without a penalty.

You will see this holds true in the upcoming content.

---


#### Categorical Variables

One of the main ways for working with categorical variables is using 0, 1 encodings.  In this technique, you create a new column for every level of the categorical variable.  The **advantages** of this approach include:

1. The ability to have differing influences of each level on the response.
2. You do not impose a rank of the categories.
3. The ability to interpret the results more easily than other encodings.

The **disadvantages** of this approach are that you introduce a large number of effects into your model.  If you have a large number of categorical variables or categorical variables with a large number of levels, but not a large sample size, you might not be able to estimate the impact of each of these variables on your response variable.  There are some rules of thumb that suggest 10 data points for each variable you add to your model.  That is 10 rows for each column.  This is a reasonable lower bound, but the larger your sample (assuming it is representative), the better.

Let's try out adding dummy variables for the categorical variables into the model.  We will compare to see the improvement over the original model only using quantitative variables.  

---
`41`

## Overfitting

Overfitting is a common problem when our model does not generalize to data it has not seen before. Assuring you build models that not only work for the data the model was trained on, but also generalize to new (test) data, is key to building models that will be successful to deploy and that will become successful in production.

---

`45`
Two techniques for deploying your results include:

1. Automated techniques built into computer systems or across the web. You will do this later in this program!

2. Communicate results with text, images, slides, dashboards, or other presentation methods to company stakeholders.

To get some practice with this second technique, you will be writing a blog post for the first project and turning in a Github repository that shares your work.

As a data scientist, communication of your results to both other team members and to less technical members of a company is a critical component

---

`RECAP`

# CRISP-DM

In working with missing values, categorical variables, and building out your model, it was probably easy to lose site of the big picture of the process. Let's take a quick second to recap that here, and pull together the results you should have arrived through your analysis.

1. Business Understanding

How do I break into the field?
What are the placement and salaries of those who attended a coding bootcamp?
How well can we predict an individual's salary? What aspects correlate well to salary?
How well can we predict an individual's job satisfaction? What aspects correlate well to job satisfaction?
2. Data Understanding

Here we used the StackOverflow data to attempt to answer our questions of interest. We did 1. and 2. in tandem in this case, using the data to help us arrive at our questions of interest. This is one of two methods that is common in practice. The second method that is common is to have certain questions you are interested in answering, and then having to collect data related to those questions.

3. Prepare Data

This is commonly denoted as 80% of the process. You saw this especially when attempting to build a model to predict salary, and there was still much more you could have done. From working with missing data to finding a way to work with categorical variables, and we didn't even look for outliers or attempt to find points we were especially poor at predicting. There was ton more we could have done to wrangle the data, but you have to start somewhere, and then you can always iterate.

4. Model Data

We were finally able to model the data, but we had some back and forth with step 3. before we were able to build a model that had okay performance. There still may be changes that could be done to improve the model we have in place. From additional feature engineering to choosing a more advanced modeling technique, we did little to test that other approaches were better within this lesson.

5. Results

Results are the findings from our wrangling and modeling. They are the answers you found to each of the questions.

6. Deploy

Deploying can occur by moving your approach into production or by using your results to persuade others within a company to act on the results. Communication is such an important part of the role of a data scientist.

---

# README Process

## Two techniques for deploying your results include:

Automated techniques built into computer systems or across the web. You will do this later in this program!

Communicate results with text, images, slides, dashboards, or other presentation methods to company stakeholders.
To get some practice with this second technique, you will be writing a blog post for the first project and turning in a Github repository that shares your work.

As a data scientist, communication of your results to both other team members and to less technical members of a company is a critical component


### Readme Showcase

[Sample Project](https://github.com/jjrunner/stackoverflow)

1. Installation - Extra libraries that are not installed with the Anaconda distribution, as well as what what version of python you are using should be noted.

2. Project Motivation - Discuss what your project is about, and what interested you in pursuing the project.

3.File Descriptions - Guide others through the files in your repository. You may not talk about every file here, but you should let them know where they can find the work they might find most interesting.

4. How To Interact With Your Project - When your project isn't meant to be interactive or used for other projects, you should instead talk about the technical details of your project. What were your results? What did you do to improve them? What methods did you try? What worked? What didn't work?

5.Licensing, Authors, Acknowledgements - You always want to give credit where necessary. Acknowledge other contributors, helpful peers, data providers, etc.

---

`RECAP`

# Readme Process

You are so ready to take on this project! I hope you are excited to create your own post! There was a lot to take away from this lesson. Here were the big points I had in mind:

**Related to Marketing Yourself**

Catchy image followed by a catchy title.


Write in small blocks of text, as large blocks of text will exhaust and demotivate your reader.


Start with an engaging question or current event that your audience is likely thinking about.


End with a recap and a call to action.


**Related to Keeping Yourself and Your Reader Motivated**

Keep your post short and sweet. 1-2 pages per post will increase audience engagement, as well as the likelihood you complete the writing of your post.


Create an outline. A useful outline for your post could just be: introduction, each of your questions, and then a conclusion. This will help you stay focused when writing your post.


Review. Review. Review. When you think you have reviewed enough, find someone else to review. The more review you have of your work, the better it will become.

The three Text portions of this class contain A LOT of useful information. Use them for reference as you complete your project, and as you continue to write more posts in the future!