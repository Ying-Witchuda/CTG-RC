# Conductive-textile
Implementation of Conductive Textile Glove and Reservoir Computing for Hand Movement Monitoring
# Library for implementing reservoir computing models (echo state networks) for Hand Movement Monitoring in time series classification: 
Reservoir Computing is a framework for building recurrent neural networks (RNNs) with a fixed, randomly initialized hidden layer known as the "reservoir." The reservoir acts as a temporal feature extractor, while the output layer is trained to map the reservoir's dynamics to the desired output.
# Echo State Networks (ESN): 
ESNs are one of the most popular Reservoir Computing architectures. The reservoir is typically a randomly connected recurrent layer with a large number of neurons. The input is fed into the reservoir, and the output is taken from a subset of reservoir neurons or a linear combination of their activities. The output layer can be trained using linear regression or other simple learning algorithms.
# Required libraries:
.NumPy
.scipy.io
.pandas
.sklearn.preprocessing import OneHotEncoder
.matplotlib.pyplot
# Preprocessing dataset:
The training and test function requires in input training and test data, which must be provided as multidimensional NumPy arrays of shape [N,T,V], with:

N = number of samples
T = number of time steps in each sample
V = number of variables in each sample
Training and test labels (Y and Yte) must be provided in one-hot encoding format, i.e. a matrix [N,C], where C is the number of classes.
# Set up the Reservoir: 
Create an instance of the ESN class, which represents the Echo State Network. Specify the required parameters such as the number of input nodes, the number of reservoir nodes, and the number of output nodes.
# Train the Reservoir: 
To train the Reservoir, you need a training dataset consisting of input-output pairs. Convert your training data into numpy arrays and pass them to the model. fit method.
