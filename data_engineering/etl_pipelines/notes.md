# Data Engineering 

## Course Roadmap

- Data Engineering
    - Data Pipelines
    - ETL (Extract Transform Load) Pipelines
- NLP Pipelines
    - Text Processing
    - Modeling
- Machine Learning Pipelines
    - Scikit-learn pipelines
    - Feature Union
    - Grid Search
- Data Engineering Project
    - Classify disaster response messages
    - Skills: data pipelines, NLP pipelines, machine learning pipelines, supervised learning


## Data Pipelines: ETL vs ELT

Data pipeline is a generic term for moving data from one place to another. For example, it could be moving data from one server to another server.

## ETL
An [ETL pipeline](https://en.wikipedia.org/wiki/Extract,_transform,_load) is a specific kind of data pipeline and very common. ETL stands for Extract, Transform, Load. Imagine that you have a database containing web [log data](https://en.wikipedia.org/wiki/Log_file). Each entry contains the IP address of a user, a timestamp, and the link that the user clicked.

What if your company wanted to run an analysis of links clicked by city and by day? You would need another data set that maps IP address to a city, and you would also need to extract the day from the timestamp. With an ETL pipeline, you could run code once per day that would extract the previous day's log data, map IP address to city, aggregate link clicks by city, and then load these results into a new database. That way, a data analyst or scientist would have access to a table of log data by city and day. That is more convenient than always having to run the same complex data transformations on the raw web log data.

Before cloud computing, businesses stored their data on large, expensive, private servers. Running queries on large data sets, like raw web log data, could be expensive both economically and in terms of time. But data analysts might need to query a database multiple times even in the same day; hence, pre-aggregating the data with an ETL pipeline makes sense.

## ELT
ELT (Extract, Load, Transform) pipelines have gained traction since the advent of cloud computing. Cloud computing has lowered the cost of storing data and running queries on large, raw data sets. Many of these cloud services, like [Amazon Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/), or [IBM Db2](https://www.ibm.com/cloud/db2-warehouse-on-cloud) can be queried using SQL or a SQL-like language. With these tools, the data gets extracted, then loaded directly, and finally transformed at the end of the pipeline.

However, ETL pipelines are still used even with these cloud tools. Oftentimes, it still makes sense to run ETL pipelines and store data in a more readable or intuitive format. This can help data analysts and scientists work more efficiently as well as help an organization become more data driven.

## Outline of the Lesson

1. Extract data from different sources such as:
- csv files
- json files
- APIs

2. Transform data
- combining data from different sources
- data cleaning
- data types
- parsing dates
- file encodings
- missing data
- duplicate data
- dummy variables
- remove outliers
- scaling features
- engineering features
3. Load
- send the transformed data to a database

4. ETL Pipeline
- code an ETL pipeline

This lesson contains many Jupyter notebook exercises where you can practice the different parts of an ETL pipeline. Some of the exercises are challenging, but they also contain hints to help you get through them. You'll notice that the "transformation" section is relatively long. You'll oftentimes hear data scientists say that cleaning and transforming data is how they spend a majority of their time. This lesson reflects that reality.

## Big Data Courses at Udacity
"Big Data" gets a lot of buzz these days, and it is definitely an important part of a data engineer's and, sometimes, a data scientists's work. With "Big Data", you need special tools that can work on distributed computer systems.

This ETL course focuses on the practical fundamentals of ETL. Hence, you'll be working with a local data set so that you do not need to worry about learning a new tool. Udacity has other courses where the primary focus is on tools used for distributed data sets.

Here are links to other big data courses at Udacity:

[Intro to Hadoop and MapReduce](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617)
[Deploying a Hadoop Cluster](https://www.udacity.com/course/deploying-a-hadoop-cluster--ud1000)
[Real-time Analytics with Apache Storm](https://www.udacity.com/course/real-time-analytics-with-apache-storm--ud381)
[Big Data Analytics in Health Care](https://www.udacity.com/course/big-data-analytics-in-healthcare--ud758)

## World Bank Data

In the next section, you'll find a series of exercises. These are relatively brief and focus on extracting, or in other words, reading in data from different sources. The goal is to familiarize yourself with different types of files and see how the same data can be formatted in different ways. This lesson assumes you have experience with pandas and basic programming skills.


This lesson uses data from the World Bank. The data comes from two sources:

1. [World Bank Indicator Data](https://data.worldbank.org/indicator) - This data contains socio-economic indicators for countries around the world. A few example indicators include population, arable land, and central government debt.
2. [World Bank Project Data](https://datacatalog.worldbank.org/dataset/world-bank-projects-operations) - This data set contains information about World Bank project lending since 1947.

Both of these data sets are available in different formats including as a csv file, json, or xml. You can download the csv directly or you can use the World Bank APIs to extract data from the World Bank's servers. You'll be doing both in this lesson.

The end goal is to clean these data sets and bring them together into one table. As you'll see, it's not as easy as one might hope. By the end of the lesson, you'll have written an ETL pipeline to extract, transform, and load this data into a new database.

The goal of the lesson is to combine these data sets together so that you can run a linear regression model predicting World Bank Project total costs. You will not actually build the model; instead, you will get the data ready so that a data analyst or data scientist could more easily build the model.

## How to Tackle the Exercises

This course assumes you have experience manipulating data with the Pandas library, which is covered in the data analyst nanodegree. Some of these transformation exercises are challenging. The most challenging exercises are marked (challenging). If an exercise is marked as a challenge, it means you’ll get something out of solving it, but it’s not essential for understanding the lesson material or for getting through the final project at the end of this data engineering course.

Throughout the exercises, you might have to read the pandas documentation or search outside the classroom for how to do a certain processing technique. That is not just expected but also encouraged. As a data scientist professional, you will oftentimes have to research how to do something on your own much like what software engineers do. See this answer on Quora about [how often do people use stackoverflow when working on data science projects?](https://www.quora.com/How-often-do-people-use-stackoverflow-when-working-on-data-science-projects).

Use Google and other search engines when you're not sure how to do something!

What You Will do in the Next Section
In the next section of the lesson, you'll learn about the extract portion of an ETL pipeline. You’ll get practice with a series of exercises. These exercises are relatively brief and focus on extracting, or in other words, reading in data from different sources. The goal is to familiarize yourself with different types of files and see how the same data can be formatted in different ways.

For a review of pandas, click on the "Extracurricular" section of the classroom. Open the Prerequisite: Python for Data Analysis course, and go to Lesson 7: Pandas.

# Extract 

## Overview of the Extract Part of the Lesson

## Summary of the data file types you'll work with

**CSV files**
CSV stands for comma-separated values. These types of files separate values with a comma, and each entry is on a separate line. Oftentimes, the first entry will contain variable names. Here is an example of what CSV data looks like. This is an abbreviated version of the first three lines in the World Bank projects data csv file.
```
id,regionname,countryname,prodline,lendinginstr
P162228,Other,World;World,RE,Investment Project Financing
P163962,Africa,Democratic Republic of the Congo;Democratic Republic of the Congo,PE,Investment Project Financing
```

**JSON**
JSON is a file format with key/value pairs. It looks like a Python dictionary. The exact same CSV file represented in JSON could look like this:

```
[{"id":"P162228","regionname":"Other","countryname":"World;World","prodline":"RE","lendinginstr":"Investment Project Financing"},{"id":"P163962","regionname":"Africa","countryname":"Democratic Republic of the Congo;Democratic Republic of the Congo","prodline":"PE","lendinginstr":"Investment Project Financing"},{"id":"P167672","regionname":"South Asia","countryname":"People\'s Republic of Bangladesh;People\'s Republic of Bangladesh","prodline":"PE","lendinginstr":"Investment Project Financing"}]
```

Each line in the data is inside of a squiggly bracket {}. The variable names are the keys, and the variable values are the values.

There are other ways to organize JSON data, but the general rule is that JSON is organized into key/value pairs. For example, here is a different way to represent the same data using JSON:
```
{"id":{"0":"P162228","1":"P163962","2":"P167672"},"regionname":{"0":"Other","1":"Africa","2":"South Asia"},"countryname":{"0":"World;World","1":"Democratic Republic of the Congo;Democratic Republic of the Congo","2":"People\'s Republic of Bangladesh;People\'s Republic of Bangladesh"},"prodline":{"0":"RE","1":"PE","2":"PE"},"lendinginstr":{"0":"Investment Project Financing","1":"Investment Project Financing","2":"Investment Project Financing"}}
```

**XML**
Another data format is called XML (Extensible Markup Language). XML is very similar to HTML at least in terms of formatting. The main difference between the two is that HTML has pre-defined tags that are standardized. In XML, tags can be tailored to the data set. Here is what this same data would look like as XML.

```
<ENTRY>
  <ID>P162228</ID>
  <REGIONNAME>Other</REGIONNAME>
  <COUNTRYNAME>World;World</COUNTRYNAME>
  <PRODLINE>RE</PRODLINE>
  <LENDINGINSTR>Investment Project Financing</LENDINGINSTR>
</ENTRY>
<ENTRY>
  <ID>P163962</ID>
  <REGIONNAME>Africa</REGIONNAME>
  <COUNTRYNAME>Democratic Republic of the Congo;Democratic Republic of the Congo</COUNTRYNAME>
  <PRODLINE>PE</PRODLINE>
  <LENDINGINSTR>Investment Project Financing</LENDINGINSTR>
</ENTRY>
<ENTRY>
  <ID>P167672</ID>
  <REGIONNAME>South Asia</REGIONNAME>
  <COUNTRYNAME>People's Republic of Bangladesh;People's Republic of Bangladesh</COUNTRYNAME>
  <PRODLINE>PE</PRODLINE>
  <LENDINGINSTR>Investment Project Financing</LENDINGINSTR>
</ENTRY>
```

XML is falling out of favor especially because JSON tends to be easier to navigate; however, you still might come across XML data. The World Bank API, for example, can return either XML data or JSON data. From a data perspective, the process for handling HTML and XML data is essentially the same.

**SQL databases**
SQL databases store data in tables using primary and foreign keys. In a SQL database, the same data would look like this:

```
id	regionname	countryname	prodline	lendinginstr
P162228	Other	World;World	RE	Investment Project Financing
P163962	Africa	Democratic Republic of the Congo;Democratic Republic of the Congo	PE	Investment Project Financing
P167672	South Asia	People's Republic of Bangladesh;People's Republic of Bangladesh	PE	Investment Project Financing
```

**Text Files**
This course won't go into much detail about text data. There are other Udacity courses, namely on natural language processing, that go into the details of processing text for machine learning.

Text data present their own issues. Whereas CSV, JSON, XML, and SQL data are organized with a clear structure, text is more ambiguous. For example, the World Bank project data country names are written like this

```
Democratic Republic of the Congo;Democratic Republic of the Congo
```

In the World Bank Indicator data sets, the Democratic Republic of the Congo is represented by the abbreviation "Congo, Dem. Rep." You'll have to clean these country names to join the data sets together.

## Extracting Data from the Web
In this lesson, you'll see how to extract data from the web using an APIs (Application Programming Interface). APIs generally provide data in either JSON or XML format.

Companies and organizations provide APIs so that programmers can access data in an official, safe way. APIs allow you to download, and sometimes even upload or modify, data from a web server without giving you direct access.

## Outliers - How to Find Them

## Outlier Detection Resources [Optional]
Here are a couple of links to outlier detection processes and algorithms. Since this is an ETL course rather than a statistics course, you don't need to read these in order to complete the lesson.

[scikit-learn novelty and outlier detection](http://scikit-learn.org/stable/modules/outlier_detection.html)
[statistical and machine learning methods for outlier detection](https://towardsdatascience.com/a-brief-overview-of-outlier-detection-techniques-1e0b2c19e561)