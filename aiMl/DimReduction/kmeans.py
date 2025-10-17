from sklearn.datasets import make_blobs, make_circles, make_moons
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from mpl_toolkits import mplot3d

'''
Creating Data
Using the sklearn dataset utilities, we create and plot three datasets below. Your task will be to determine a starting place for the clusters by choosing appropriate cluster centers. The clusters have been colored according to the labels created for demonstration purposes. Recall that in a real clustering scenario, you won't have labels on your data.
'''

n_samples = 1500

'''
Problem 1
Choosing Initial Centers
6 Points

Which of the following options do you think would serve as good initial cluster centers for the dataset "Cluster Group I" visualized below? Enter your answer as a string to ans1 below.

a) (-2, -5), (2, -5), (10, -5)
b) (-5, -5), (2, 2), (2, -7)
c) (-2, 5), (8, 5), (10, -5)
'''

X1, Y1 = make_blobs(n_samples=n_samples, random_state=24)
plt.scatter(X1[:, 0], X1[:, 1], c = Y1)
plt.title('Cluster Group I')
plt.grid()

ans1 = "c"

## Problem 2

## Choosing Initial Centers
'''
**6 Points**

Below, a second dataset is created.  Again, your task is to identify what appropriate starting centers could be.  Assign your answer as a string to `ans2` below.

```
a) (-6, 5), (-1, 5), (3, 5)
b) (-4, -7), (1, 6), (3, -7)
c) (-6, 6), (0, 7), (6, 7)
'''

X2, Y2 = make_blobs(n_samples=n_samples, random_state=111)
plt.scatter(X2[:, 0], X2[:, 1], c = Y2)
plt.grid()
plt.title('Cluster Group II')

ans2 = "b"

## Problem 3

### Choosing Initial Centers
'''
**6 Points**

Once again, given the data below, choose the best initial centers for clustering.  Assign your answer as a string to `ans3` below.  

```
a) (-5, -10), (7, 0), (10, 0)
b) (-5, -10), (7, 10), (10, 10)
c) (-5, -10), (7, 0), (10, 10)
'''

X3, Y3 = make_blobs(n_samples=n_samples, random_state=8)
plt.scatter(X3[:, 0], X3[:, 1], c = Y3)
plt.grid()
plt.title('Cluster Group III');

ans3 = "c"

X1, _ = make_blobs(n_samples=20, random_state=42)
plt.scatter(X1[:, 0], X1[:, 1])
plt.title('Small Sample Dataset')
plt.grid()

'''
Creating a DataFrame
Using pandas, a DataFrame is created to hold the small dataset. The features are named X1 and X2. The DataFrame is named df.
'''
#create DataFrame of samples
df = pd.DataFrame(X1, columns = ['X1', 'X2'])
df.head()

'''
Randomly Selecting Centers
As noted, we will make initial cluster centroid assignments based on a random selection of data from the samples. Below, the .sample method from the DataFrame is used to select three points at random. These are assigned to the variable centroids as a DataFrame.
'''
centroids = df.sample(3, random_state = 11).reset_index(drop = True)
centroids

### Assigning initial centroid values

'''Now, we select the individual centroid values and assign them as `c1`, `c2`, `c3` below. '''
c1 = centroids.iloc[0, :2].values
c2 = centroids.iloc[1, :2].values
c3 = centroids.iloc[2, :2].values

'''
Inner cluster sum of squares
To find the intercluster variance, we can use the np.linalg.norm function. This finds the distances squared from each of the cluster centers to each data point. These distances are assembled into a DataFrame called dist_df and the three columns represent the three cluster centers. Note that there should be a value of zero in each column because the centers were chosen as data points from the dataset.
'''

dist_df = pd.DataFrame(np.array([d1, d2, d3]).T, columns = ['d1', 'd2', 'd3'])
dist_df

## Problem 4

### What were the original centers
'''
**2 Points**

In the distance data above, which data point was the original centroid of the first column?  Assign the index of the datapoint as an integer to `ans4` below.
'''
ans4 = 7

### Finding the `argmin`
'''
For each of the observations, we want to assign them to the cluster where the intercluster variance is minimized.  To do so, we can use the `np.argmin` function and apply it across the rows.  Note that this returns a label for which cluster the point will be assigned.  These labels are added to the original DataFrame, and the points are plotted. 
'''

np.argmin(dist_df.values, axis = 1) #finding smallest variance
df['cluster label'] = np.argmin(dist_df.values, axis = 1) #create new column of labels
df.head()

sns.scatterplot(data = df, x = 'X1',y = 'X2', hue = 'cluster label', palette='tab10')
plt.title('Cluster assignments after random centroids')

## Problem 5

### Initial Cluster Assignments
'''
**2 Points**

Now that the clusters have been assigned, what do you think of the initial assignments?  Did they end up matching your intuitive assignments?  Assign your solution to `ans5` below as a boolean value, `True` representing if the cluster assignments are "good", `False` if they are "bad". 
'''
ans5 = False

'''
Compute new centroids
Using the new labels for the cluster centers, the final step is to update the random centroids based on the averages of each cluster. One approach is to use the groupby method to group by the initial labels and aggregate based on the mean. Below, we save these as a DataFrame named new_centers and plot the updated centroids in the scatterplot as red star markers.
'''

new_centers = df.groupby('cluster label').mean()
plt.figure(figsize = (14, 5))
sns.scatterplot(data = df, x = 'X1',y = 'X2', s = 100, alpha = 0.4)
plt.title('Updated Centroids');
plt.scatter(new_centers['X1'], new_centers['X2'], marker = '*', s = 400, c = 'red', edgecolor = 'black')

### Creating the Data
'''
For the last part of the assignment, the data is created with a known number of cluster centers to make the evaluation of the clustering more straightforward.  A dataset with three features and four clusters is created and plotted below.  Your task is to uncover these clusters using `KMeans`.  
'''
X, y = make_blobs(n_samples=200, n_features=3, centers = 4, random_state=42)
ax = plt.axes(projection = '3d')
ax.scatter3D(X[:, 0], X[:, 1], X[:, 2], c = y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Artificial Dataset with 4 Clusters')
plt.tight_layout()


## Problem 6

### Instantiate `KMeans`
'''
**2 Points**

To begin, you are to create an instance of the `KMeans` clusterer.  Slightly different than the lectures, we directly import the `KMeans` object. 
Instantiate a `KMeans()` classifier and assign the result to `kmeans`.
Inside the `KMeans()` classifier, set `random_state = 42`.
'''

kmeans = KMeans(n_clusters=4, random_state=42)

# Answer check
print(kmeans)

## Problem 7

### Using `KMeans`
'''
**2 Points**

To conduct the `KMeans` clustering algorithm on the data, use the `.fit()` method on `kmeans` with argument equal to `X`.  

This will run the clustering algorithm on our data and make clustering assignments accordingly.  
'''
kmeans = kmeans.fit(X)

# Answer check
print(kmeans)

## Problem 8
### Trying different numbers of clusters
'''
**2 Points**

Our first cluster model used 8 cluster centers.  


Below, use a `for` loop to create a list of inertia scores for models with $1, 2, 3, ..., 10$ cluster centers and append the `.inertia_` value for each to the list `inertias`.  Note that for each instance of `KMeans` you create, set `n_clusters` equal to `i` and the `random_state` equal to `42`.  
'''
inertias = [] 

#for each value 1 - 10

       #instantiate new KMeans instance
        #Don't Forget to set the random_state!!!
        
        #fit the model
        
        #append inertia score to inertias list
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans = kmeans.fit(X)
    inertias.append(kmeans.inertia_)

# Answer check
print(inertias)
print(type(inertias))

## Problem 9

### Plotting the results
'''
**2 Points**

Now that we have inertia values for `n_clusters` 1, 2, 3, ..., 10, a plot is drawn of the resulting centers and inertia scores.  The $x$-axis should contain the number of cluster centers and the $y$-axis should represent the inertia scores.  Uncomment the plotting code to examine a plot of these inertia values by cluster centers.  According to this plot, which do you feel is the "right" number of cluster centers for the data?  Assign your answer as an integer to `best_n_clusters` below. 
'''
#plt.plot(list(range(1, 11)), inertias, '--o')
#plt.xticks(list(range(1, 11)), list(range(1, 11)))
#plt.title('Inertia Score by n cluster centers');
best_n_clusters = 4

# Answer check
print(best_n_clusters)
print(type(best_n_clusters))

## Problem 10

### Repeat with `random` initialization of centroids
'''
**2 Points**

Note that by default, the `KMeans` clustered in sklearn uses `kmeans++` to initialize the center of the clusters.  

Repeat the implementation of Problem 4 where you loop over values $1, 2, 3, ..., 10$ for the `n_clusters` but now initialize the centers randomly by setting the argument `init` equal to `random`.  Be sure to set `random_state = 42` and save your list of inertias to `random_inertias`.  


Does the idea number of clusters change?  Enter your response to the best number of cluster centers when using `random` initialization to `best_n_clusters_random` as an integer below.
'''
random_inertias = [] 
best_n_clusters_random = 4

# Answer check
print(random_inertias)
print(type(random_inertias))