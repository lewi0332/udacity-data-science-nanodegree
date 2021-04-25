## Advantages of Using Pipeline

Below are two videos explaining the advantages of using scikit-learn's `Pipeline` as seen in the previous video.


**Advantages of Using Pipeline Part 1:**

**1. Simplicity and Convencience**
- Automates repetitive steps - Chaining all of your steps into one estimator allows you to fit and predict on all steps of your sequence automatically with one call. It handles smaller steps for you, so you can focus on implementing higher level changes swiftly and efficiently.
- Easily understandable workflow - Not only does this make your code more concise, it also makes your workflow much easier to understand and modify. Without Pipeline, your model can easily turn into messy spaghetti code from all the adjustments and experimentation required to improve your model.
- Reduces mental workload - Because Pipeline automates the intermediate actions required to execute each step, it reduces the mental burden of having to keep track of all your data transformations. Using Pipeline may require some extra work at the beginning of your modeling process, but it prevents a lot of headaches later on.

**Advantages of Using Pipeline Part 2:**

**2. Optimizing Entire Workflow**

- GRID SEARCH: Method that automates the process of testing different hyper parameters to optimize a model.
- By running grid search on your pipeline, you're able to optimize your entire workflow, including data transformation and modeling steps. This accounts for any interactions among the steps that may affect the final metrics.
- Without grid search, tuning these parameters can be painfully slow, incomplete, and messy.

**3. Preventing Data leakage**
- Using Pipeline, all transformations for data preparation and feature extractions occur within each fold of the cross validation process.
- This prevents common mistakes where you’d allow your training process to be influenced by your test data - for example, if you used the entire training dataset to normalize or extract features from your data.
You'll see what we mean by this in a video later in this lesson about using Pipeline with GridSearchCV.


## Feature Unions
Sometimes, you don't always have all the data transformation steps you need in scikit-learn's library, which is why it is possible to actually create your own custom transformers. For the video below, just keep in mind that TextLengthExtractor is a custom transformer that is already built in a separate file and imported for this example.

## Using Feature Union

Taking the example from the previous video, let's say you wanted to extract two different kinds of features from the same text column - tfidf values, and the length of the text. Your first approach might be to create an additional column from the `text` column called `text_length` like this. Then both `text` and `text_length` can be part of your feature matrix. But now your pipeline would break. You can't run `CountVectorizer` on NumPy arrays of strings and integers.

```
df['txt_length'] = df['text'].apply(len)
X = df[['text', 'txt_length']].values
y = df['label'].values
X_train, X_test, y_train, y_test = train_test_split(X, y)

pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', RandomForestClassifier()),
])


# train classifier
pipeline.fit(Xtrain)

# predict on test data
predicted = pipeline.predict(Xtest)
```

Let's say you had a custom transformer called `TextLengthExtractor`. Now, you could leave `X_train` as just the original text column, if you could figure out how to add the text length extractor to your pipeline. If only you could fit it on the original text data, rather than the output of the previous transformer. But you need both the outputs of `TfidfTransformer` and `TextLengthExtractor` to feed into the classifier as input.

```
X = df['text'].values
y = df['label'].values
X_train, X_test, y_train, y_test = train_test_split(X, y)

pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('txt_length', TextLengthExtractor()),
    ('clf', RandomForestClassifier()),
])

# train classifier
pipeline.fit(Xtrain)

# predict on test data
predicted = pipeline.predict(Xtest)
```

- Feature unions are super helpful for handling these situations, where we need to run two steps in parallel on the same data and combine their results to pass into the next step.
- Like pipelines, feature unions are built using a list of (key, value) pairs, where the key is the string that you want to name a step, and the value is the estimator object. Also like pipelines, feature unions combine a list of estimators to become a single estimator. However, a feature union runs its estimators in parallel, rather than in a sequence as a pipeline does. In this example, the estimators run in parallel are nlp_pipeline and text_length. Notice we use a pipeline in this feature union to make sure the count vectorizer and tfidf transformer steps are still running in sequence.

```
X = df['text'].values
y = df['label'].values
X_train, X_test, y_train, y_test = train_test_split(X, y)

pipeline = Pipeline([
    ('features', FeatureUnion([

        ('nlp_pipeline', Pipeline([
            ('vect', CountVectorizer()
            ('tfidf', TfidfTransformer())
        ])),

        ('txt_len', TextLengthExtractor())
    ])),

    ('clf', RandomForestClassifier())
])

# train classifier
pipeline.fit(Xtrain)

# predict on test data
predicted = pipeline.predict(Xtest)
```

- Now, our pipeline doesn't break and uses both features! This would be equivalent to this code.

```
vect = CountVectorizer()
tfidf = TfidfTransformer()
txt_len = TextLengthExtractor()
clf = RandomForestClassifier()

# train classifier
X_train_counts = vect.fit_transform(X_train)
X_train_tfidf = tfidf.fit_transform(X_train_counts)

X_train_len = txt_len.fit_transform(X_train)
X_train_features = hstack([X_train_tfidf, X_train_len])
clf.fit(X_train_features, y_train)

# predict on test data
X_test_counts = vect.transform(X_test)
X_test_tfidf = tfidf.transform(X_test_counts)

X_test_len = txt_len.transform(X_test)
X_test_features = hstack([X_test_tfidf, X_test_len])
y_pred = clf.predict(X_test_features)
```

- The tfidf transformer and the text length extractor are fit to the input data, in this case the raw data, independently. They are then performed in parallel, and their outputs are combined and passed to the next estimator, in this case, the classifier.

Read more about feature unions in Scikit-learn's [user guide](http://scikit-learn.org/stable/modules/pipeline.html#feature-union).

## Creating Custom Transformer

In the last section, you used a custom transformer that extracted whether each text started with a verb. You can implement a custom transformer yourself by extending the base class in Scikit-Learn. Let's take a look at a a very simple example that multiplies the input data by ten.

```
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class TenMultiplier(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X * 10
```

Remember, all estimators have a fit method, and since this is a transformer, it also has a transform method.

- **FIT METHOD**: This takes in a 2d array X for the feature data and a 1d array y for the target labels. Inside the fit method, we simply return self. This allows us to chain methods together, since the result on calling fit on the transformer is still the transformer object. This method is required to be compatible with scikit-learn.
- **TRANSFORM METHOD**: The transform function is where we include the code that well, transforms the data. In this case, we return the data in X multiplied by 10. This transform method also takes a 2d array X.

Let's test our new transformer, by entering the code below in the interactive python interpreter in the terminal, ipython. We can also do this in Jupyter notebook.

```
multiplier = TenMultiplier()

X = np.array([6, 3, 7, 4, 7])
multiplier.transform(X)
```

This outputs the following:

```
array([60, 30, 70, 40, 70])
```

Nice! Next, we'll create a custom transformer that has a bit more significance. Let's build a case normalizer, which simply converts all text to lowercase. We aren't setting anything in our init method, so we can actually remove that. We can leave our fit method as is, and focus on the transform method. We can lowercase all the values in X by applying a lambda function that calls lower on each value. We'll have to wrap this in a pandas Series to be able to use this apply function.

```
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class CaseNormalizer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return pd.Series(X).apply(lambda x: x.lower()).values

case_normalizer = CaseNormalizer()

X = np.array(['Implementing', 'a', 'Custom', 'Transformer', 'from', 'SCIKIT-LEARN'])
case_normalizer.transform(X)
```

Entering the code above in ipython outputs the following:

```
array(['implementing', 'a', 'custom', 'transformer', 'from',
       'scikit-learn'], dtype=object)
```

Awesome! It's a good idea to learn how to write your own custom functions - it allows you to have more control and flexibility with your machine learning pipelines.

Another way to create custom transformers is by using this FunctionTransformer from scikit-learn's preprocessing module. This allows you to wrap an existing function to become a transformer. This provides less flexibility, but is much simpler. You can learn more about this in the link below.

Read more about using FunctionTransformer to create custom transformers [here](http://scikit-learn.org/stable/modules/preprocessing.html#custom-transformers) and [here](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer).

## Using Pipeline with GridSearchCV

As you may have seen before, grid search can be used to optimize hyper parameters of a model. Here is a simple example that uses grid search to find parameters for a support vector classifier. All you need to do is create a dictionary of parameters to search, using keys for the names of the parameters and values for the list of parameter values to check. Then, pass the model and parameter grid to the grid search object. Now when you call fit on this grid search object, it will run cross validation on all different combinations of these parameters to find the best combination of parameters for the model.

```
parameters = {
    'kernel': ['linear', 'rbf'],
    'C':[1, 10]
}

svc = SVC()
clf = GridSearchCV(svc, parameters)
clf.fit(X_train, y_train)
```

Awesome. Now consider if we had a data preprocessing step, where we standardized the data using `StandardScaler` like this.

```
scaler = StandardScaler()
scaled_data = scaler.fit_transform(X_train)

parameters = {
    'kernel': ['linear', 'rbf'],
    'C':[1, 10]
}

svc = SVC()
clf = GridSearchCV(svc, parameters)
clf.fit(scaled_data, y_train)
```

This may seem okay at first, but if you standardize your whole training dataset, and then use cross validation in grid search to evaluate your model, you've got data leakage. Let me explain. Grid search uses cross validation to score your model, meaning it splits your training data into folds of train and validation sets, trains your model on the train set, and scores it on the validation set, and does this multiple times.

However, each time, or fold, that this happens, the model already has knowledge of the validation set because all the data was rescaled based on the distribution of the whole training dataset. Important factors like the mean and standard deviation are influenced by the whole dataset. This means the model perform better than it really should on unseen data, since information about the validation set is always baked into the rescaled values of your train dataset.

The way to fix this, would be to make sure you run standard scaler only on the training set, and not the validation set within each fold of cross validation. Pipelines allow you to do just this.

```
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', SVC())
])

parameters = {
    'scaler__with_mean': [True, False]
    'clf__kernel': ['linear', 'rbf'],
    'clf__C':[1, 10]
}

cv = GridSearchCV(pipeline, param_grid=parameters)

cv.fit(X_train, y_train)
y_pred = cv.predict(X_test)
```

Now, since the rescaling is included as part of the pipeline, the standardization doesn't happen until we run grid search. Meaning in each fold of cross validation, the rescaling is done only on the data that the model is trained on, preventing leakage from the validation set. As you can see, pipelines are very valuable to removing the risk of data leakage during the data preparation process.

Note on Run Time
Running grid search can take a while, especially if you are searching over a lot of parameters! If you want to reduce it to a few minutes, try commenting out some of your parameters to grid search over just 1 or 2 parameters with a small number of values each. Once you know that works, feel free to add more parameters and see how well your final model can perform! You can try this out in the next page.
