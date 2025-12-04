'''
This activity focuses on the effect of changing your decision threshold and the resulting predictions. Again, you will use the KNeighborsClassifier, but this time you will explore the predict_proba method of the fit estimator to change the thresholds for classifying observations. You will explore the results of changing the decision threshold on the false negative rate of the classifier for the insurance data. Here, we suppose the important thing is to not make the mistake of predicting somebody would not default when they really do.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import make_column_transformer
from sklearn.pipeline import Pipeline
from sklearn import set_config

set_config(display="diagram")


### The Dataset
'''
You continue to use the default example, and the data is again loaded and split for you below. 
'''

default = pd.read_csv('aiMl/classification/data/default.csv')
print(default.head(2))

X_train, X_test, y_train, y_test = train_test_split(default.drop('default', axis = 1), 
                                                    default['default'],
                                                   random_state=42)

transformer = make_column_transformer((OneHotEncoder(drop = 'if_binary'), ['student']),
                                     remainder = StandardScaler())


### Problem 1

#### Basic Pipeline

'''
Use the `Pipeline` function to create a pipeline `base_pipe` with steps `transformer` and `knn`. Assign `transformer` to `'transformer'` and assign a `KNeighborsClassifier()` with `n_neighbors = 10` to `'knn'`. 
'''
base_pipe = Pipeline([('transformer', transformer), ('knn', KNeighborsClassifier(n_neighbors=10))])

# Answer check
print(base_pipe)

### Problem 2

#### Accuracy of KNN with 50% probability boundary
'''
- Use the `fit` function to train `base_pipe` on `X_train` and `y_train`.
- Use the `score` function to calculate the performance of `base_pipe` on the test sets. Assign the result to `base_acc`.
- Use the `predict` function on `base_pipe` to make predictions on `X_test`. Assign the reusl to `preds`.
- Initialize the `base_fn` variable to `0`.
- Use a `for` loop to loop over `zip(preds, y_test)`. Inside the `for` loop:
    - Use an `if` block to determine the accuracy for this default setting and assign it to `base_acc`. Also, consider the proportion of false negatives here.  Assign these as `base_fn`.  
'''

base_pipe = Pipeline([('transformer', transformer), ('knn', KNeighborsClassifier(n_neighbors=10))])
base_pipe.fit(X_train, y_train)
base_acc = base_pipe.score(X_test, y_test)
preds = base_pipe.predict(X_test)
base_fn = 0
for i, j in zip(preds, y_test):
    if i == 'No':
        if j == 'Yes':
            base_fn += 1

# Answer check
print(base_acc)
print(base_fn)


### Problem 3

#### Prediction probabilities
'''
As demonstrated in Video 12.5, your fit estimator has a `predict_proba` method that will output a probability for each observation.  


Use the `predict_proba` function on `base_pipe` to predict the probabilities on `X_test`. Assign the predicted probabilities as an array using the test data to `base_probs` below. 

'''

base_pipe = Pipeline([('transformer', transformer), ('knn', KNeighborsClassifier(n_neighbors=10))])
base_pipe.fit(X_train, y_train)
base_probs = base_pipe.predict_proba(X_test)

# Answer check
pd.DataFrame(base_probs[:5], columns = ['p_no', 'p_yes'])

### Problem 4

#### A Stricter `default` estimation
'''
As discussed in the previous assignment, if you aim to minimize the number of predictions that miss default observations you may consider increasing the probability threshold to make such a classification.  Accordingly, use your probabilities from the last problem to only predict 'No' if you have a higher than 70% probability that this is the label.  Assign your new predictions as an array to `strict_preds`.  Determine the number of false negative predictions here and assign them to `strict_fn` below. 
'''
base_pipe = Pipeline([('transformer', transformer), ('knn', KNeighborsClassifier(n_neighbors=10))])
base_pipe.fit(X_train, y_train)
base_probs = base_pipe.predict_proba(X_test)
strict_preds = np.where(base_probs[:, 0] > .7, 'No', 'Yes')
strict_fn = 0
for i, j in zip(strict_preds, y_test):
    if i == 'No':
        if j == 'Yes':
            strict_fn += 1
# Answer check
print(strict_preds[:10])
print(strict_fn)


### Problem 5

#### Minimizing False Negatives

'''
Consider a 50%, 70%, and 90% decision boundary for predicting "No".  Which of these minimizes the number of false negatives?  Assign your solution as an integer -- 50, 70, or 90 -- to `ans5` below.

'''

base_pipe = Pipeline([('transformer', transformer), ('knn', KNeighborsClassifier(n_neighbors=10))])
base_pipe.fit(X_train, y_train)
base_probs = base_pipe.predict_proba(X_test)
fn_counts = {}
for threshold in [0.5, 0.7, 0.9]:
    preds = np.where(base_probs[:, 0] > threshold, 'No', 'Yes')
    fn_count = 0
    for i, j in zip(preds, y_test):
        if i == 'No':
            if j == 'Yes':
                fn_count += 1
    fn_counts[threshold] = fn_count
ans5 = min(fn_counts, key=fn_counts.get) * 100

# Answer check
print(ans5)


### Problem 6

#### Visualizing decision boundaries

'''

For this exercise, a visualization of the decision boundary using a synthetic dataset is created and plotted below.  Which of these would you choose to minimize the number of false negatives?  Enter your choice as an integer -- 1, 20, or 50 -- to `ans6` below.

<center>
    <img src = images/dbounds.png />
</center>
'''

ans6 = 1
# Answer check
print(ans6)