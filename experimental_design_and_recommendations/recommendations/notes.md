Collaborative Filtering
There are two main ways to implement collaborative filtering:

Model Based Collaborative Filtering
Neighborhood Based Collaborative Filtering
In this lesson, we will cover Neighborhood Based Collaborative Filtering, which is used to identify items or users that are "neighbors" with one another.

There are a number of ways we might go about finding an individual's closest neighbors - the metrics we will take a closer look at include:

Pearson's correlation coefficient
Spearman's correlation coefficient
Kendall's Tau
Euclidean Distance
Manhattan Distance
On the next page, you will work through a few examples to get more familiar with how each of these metrics is computed, and why you might use one over another.

$$CORR(\textbf{x}, \textbf{y}) = \frac{\sum\limits_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum\limits_{i=1}^{n}(x_i-\bar{x})^2}\sqrt{\sum\limits_{i=1}^{n}(y_i-\bar{y})^2}} $$