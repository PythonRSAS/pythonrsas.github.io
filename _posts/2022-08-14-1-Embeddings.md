---
layout: post
tag: Machine Learning in Practice
category: "machine learning"
title: "Embeddings"
description: There is a trade off between accuracy and interpretability.  High accuracy models have low interpretability and potential problems.  Explainable AI (XAI) is to have your cake and eat it too.
author: Sarah Chen
image: images/posts/photos/IMG-0868.JPG
---

An embedding is a low-dimensional translation of a high-dimensional vector.  PCA (principal component analysis) is the most well known one. 

Embedding is the process of converting high-dimensional data to low-dimensional data in the form of a vector in such a way that the two are semantically similar. 

In its literal sense, “embedding” refers to an extract (portion) of anything. Generally, embeddings improve the efficiency and usability of machine learning models and can be utilised with other types of models as well. When dealing with massive amounts of data to train, building machine learning models is a nuisance. As a result, embedding comes into play.

# Benefits of Embedding

Embedding can be beneficial in a variety of circumstances in machine learning. This has been demonstrated to be quite beneficial in conjunction with a collaborative filtering mechanism in a recommendation system. The purpose of item similarity use cases is to aid in the development of such systems. Another goal is to keep data as simple as possible for training and prediction. After embedding, the performance of the machine learning model improved dramatically. 

The only disadvantage is that embedding **reduces the model’s interpretability**. In an ideal world, an embedding captures some of the input’s semantics by clustering semantically comparable inputs in the embedding space. There are numerous strategies for producing embeddings in a deep neural network, and the strategy you use is totally dependent on your purpose.

The following are the objectives.

* Similarity check
* Search and retrieval of images
* Recommendations System
* For text, use Word2Vec.
* Reduce the dimensions of high-dimensional input data
* Instead of employing one-hot encoding, a huge number of categorical variables can be compressed.
* Eliminate sparsity; when the majority of data points are zeros, it is advised that they be converted to meaningful lower dimension data points.
* Multimodal translation
* Captioning of images

# Text Embedding
The Text embedding block converts a string of characters to a vector of real values. The term “embedding” refers to the fact that this technique produces a space for the text to be embedded. The Text embedding block is inextricably linked to the Datasets view’s text encoding. They are integrated into the same procedure while performing sentiment analysis. A Text embedding block can be used only immediately following an Input block that requires the selection of a text encoded feature. Ascertain that the language model you chose corresponds to the language model selected when text encoding was established.

NNLM, GloVe, ELMo, and Word2vec—are meant to learn word embeddings. 

# Image Embedding
Image embedding reads images and uploads or evaluates them on a distant server or locally. Each image is assigned a feature vector using deep learning algorithms. It returns a data table that has been augmented with additional columns (image descriptors). Image embedding includes a variety of embedders, each of which has been trained for a specific task. Images are either transmitted to a server or assessed locally on the user’s computer, at which point vector representations are created. The SqueezeNet embedder enables a quick review on the user’s machine without the need for an internet connection. 

# Conclusion
Neural network embeddings are low-dimensional continuous vector representations of discrete data that are learned. These embeddings overcome the restrictions of traditional encoding methods and can be utilised for a variety of tasks, including locating nearest neighbours, supplying data to another model, and creating visualisations. While many topics in deep learning are discussed in academic terms, neural network embeddings are obvious and reasonably easy to execute. Embeddings are a powerful technique for dealing with discrete variables and a practical application of deep learning.

# Reference

[sklearn user guide on manifold](https://scikit-learn.org/stable/modules/manifold.html#)

[sklearn PCA decomposition](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA)

[Elements of Statistical Learning, Chapter 14](https://hastie.su.domains/ElemStatLearn/)