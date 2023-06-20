# Conductive-textile
Implementation of Conductive Textile Glove and Reservoir Computing for Hand Movement Monitoring
Library for implementing reservoir computing models (echo state networks) for Hand Movement Monitoring in time series classification. 
Reservoir Computing is a framework for building recurrent neural networks (RNNs) with a fixed, randomly initialized hidden layer known as the "reservoir." The reservoir acts as a temporal feature extractor, while the output layer is trained to map the reservoir's dynamics to the desired output.
Echo State Networks (ESN): ESNs are one of the most popular Reservoir Computing architectures. The reservoir is typically a randomly connected recurrent layer with a large number of neurons. The input is fed into the reservoir, and the output is taken from a subset of reservoir neurons or a linear combination of their activities. The output layer can be trained using linear regression or other simple learning algorithms.
