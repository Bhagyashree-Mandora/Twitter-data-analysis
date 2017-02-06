import numpy
from matplotlib import pyplot
from sklearn import cluster, preprocessing
import pandas

trump_data = pandas.read_csv('trumpdataCleanedWithsentimentsWithState.csv')

# Extracting the variables used for clustering
username = trump_data['userName']
friend = trump_data['friendCount']
follower = trump_data['followerCount']
location = trump_data['userLocation']
sentiment = trump_data['sentiment']

# Transforming the data into a form usable for generating for the model
le = preprocessing.LabelEncoder()
transform_user = le.fit_transform(username)
transform_friend = le.fit_transform(friend)
transform_follower = le.fit_transform(follower)
transform_location = le.fit_transform(location)
transform_sentiment = le.fit_transform(sentiment)

length = len(location)
matrix = numpy.zeros((length, 5))

# Making an n-dimensional numpy array of the data
for i in range(0, length):
    matrix[i] = [transform_user[i], transform_friend[i], transform_follower[i], transform_location[i], transform_sentiment[i]]

# generating the model with k clusters
k = 3
kmeans = cluster.KMeans(n_clusters=k)
kmeans.fit(matrix)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_
inertia = kmeans.inertia_     #sum of distances of all samples from centroids
# print inertia/length

for i in range(k):
    # select only data observations with cluster label == i
    ds = matrix[numpy.where(labels == i)]
    # plot the data observations
    pyplot.plot(ds[:, 0], ds[:, 1], ds[:, 2], ds[:, 3], ds[:, 4], 'o')
    # plot the centroids
    lines = pyplot.plot(centroids[i, 0], centroids[i, 1], 'cx')
    # make the centroid x's bigger
    pyplot.setp(lines,ms=15.0)
    pyplot.setp(lines,mew=2.0)
    pyplot.title("Clusters for five variables")
pyplot.show()


# Finding the optimal value of k for five variables
# k vs inertia/length
X = [2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [1552510.42428, 1220566.18832, 980876.391469, 846457.904822, 775679.641683, 709403.012147, 657049.503805, 617171.336658, 574687.743133]
pyplot.plot(X,Y)
pyplot.xlabel("Number of Clusters (k)")
pyplot.ylabel("Average distance of samples from their closest centroid")
pyplot.title("Variation of average distance from cenroid to number of clusters- View the Elbow")
pyplot.show()