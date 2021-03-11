The first two steps of CRISP-DM are:

1. Business Understanding - this means understanding the problem and questions you are interested in tackling in the context of whatever domain you're working in. Examples include

How do we acquire new customers?
Does a new treatment perform better than an existing treatment?
How can improve communication?
How can we improve travel?
How can we better retain information?
2. Data Understanding - at this step, you need to move the questions from Business Understanding to data. You might already have data that could be used to answer the questions, or you might have to collect data to get at your questions of interest.


The CRISP-DM Process (Cross Industry Process for Data Mining)
We have now defined the questions we want to answer and had a look through the data available to find the answers, that is, we have looked at the first two steps here:

1. Business Understanding

2. Data Understanding

We can now look at the third step of the process:

3. Prepare Data

Luckily stackoverflow has already collected the data for us. However, we still need to wrangle the data in a way for us to answer our questions. The wrangling and cleaning process is said to take 80% of the time of the data analysis process. You will see that will hold true through this lesson, as a majority of the remaining parts of this lesson will be around basic data wrangling strategies.

We will discuss the advantages and disadvantages of the strategies discussed in this lesson.

When looking at the first two questions:

How to break into the field?
What are the placement and salaries for those who attended a coding bootcamp?
we did not need to do any predictive modeling. We only used descriptive and a little inferential statistics to retrieve the results.

Therefore, all steps of CRISP-DM were not necessary for these first two questions. CRISP-DM states 6 steps:

1. Business Understanding

2. Data Understanding

3. Prepare Data

4. Data Modeling

5. Evaluate the Results

6. Deploy

For these first two questions, we did not need step 4. In the previous notebooks, you performed steps 3 and 5 without needing step 4 at all. A lot of the hype in data science, artificial intelligence, and deep learning is integrated into step 4, but there are still plenty of questions to be answered not using machine learning, artificial intelligence, and deep learning.

All Data Science Problems Involve
Curiosity.

The right data.

A tool of some kind (Python, Tableau, Excel, R, etc.) used to find a solution (You could use your head, but that would be inefficient with the massive amounts of data being generated in the world today).

Well communicated or deployed solution.
Extra Useful Tools to Know But That Are NOT Necessary for ALL Projects
Deep Learning
Fancy machine learning algorithms
With that, you will be getting a more in depth look at these items, but it is worth mentioning (given the massive amount of hype) that they do not solve all the problems. Deep learning cannot turn bad data into good conclusions. Or bad questions into amazing results.


When looking at the first two questions:

How to break into the field?
What are the placement and salaries for those who attended a coding bootcamp?
we did not need to do any predictive modeling. We only used descriptive and a little inferential statistics to retrieve the results.

Therefore, all steps of CRISP-DM were not necessary for these first two questions. The process would look closer to the following:

1. Business Understanding

2. Data Understanding

3. Prepare Data

4. Evaluate the Results

5. Deploy

However, for the last two questions:

How well can we predict an individual's salary? What aspects correlate well to salary?

How well can we predict an individual's job satisfaction? What aspects correlate well to job satisfaction?

We will need to use a predictive model. We will need to pick up at step 3 to answer these two questions, so let's get started. The process for answering these last two questions will follow the full 6 steps shown here.

1. Business Understanding

2. Data Understanding

3. Prepare Data

4. Model Data

5. Evaluate the Results

6. Deploy

Data Modeling Process

1. Instantiate

2. Fit

3. Predict

4. Score


There are two main 'pain' points for passing data to machine learning models in sklearn:

Missing Values
Categorical Values
Sklearn does not know how you want to treat missing values or categorical variables, and there are lots of methods for working with each. For this lesson, we will look at common, quick fixes. These methods help you get your models into production quickly, but thoughtful treatment of missing values and categorical variables should be done to remove bias and improve predictions over time.

Three strategies for working with missing values include:

We can remove (or “drop”) the rows or columns holding the missing values.
We can impute the missing values.
We can build models that work around them, and only use the information provided.

Though dropping rows and/or columns holding missing values is quite easy to do using numpy and pandas, it is often not appropriate.

Understanding why the data is missing is important before dropping these rows and columns. In this video you saw a number of situations in which dropping values was not a good idea. These included

Dropping data values associated with the effort or time an individual put into a survey.
Dropping data values associated with sensitive information.
In either of these cases, the missing values hold information. A quick removal of the rows or columns associated with these missing values would remove missing data that could be used to better inform models.

Instead of removing these values, we might keep track of the missing values using indicator values, or counts associated with how many questions an individual skipped.


n the last video, you saw cases in which dropping rows or columns associated with missing values would not be a good idea. There are other cases in which dropping rows or columns associated with missing values would be okay.

A few instances in which dropping a row might be okay are:

Dropping missing data associated with mechanical failures.
The missing data is in a column that you are interested in predicting.
Other cases when you should consider dropping data that are not associated with missing data:

Dropping columns with no variability in the data.
Dropping data associated with information that you know is not correct.
In handling removing data, you should think more about why is this missing or why is this data incorrectly input to see if an alternative solution might be used than dropping the values.

One common strategy for working with missing data is to understand the proportion of a column that is missing. If a large proportion of a column is missing data, this is a reason to consider dropping it.

There are easy ways using pandas to create dummy variables to track the missing values, so you can see if these missing values actually hold information (regardless of the proportion that are missing) before choosing to remove a full column.