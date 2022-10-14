---
layout: post
tag: CAP theorem and the financial industry
category: "other risks"
title: "CAP theorem"
description: Strong and immediate consistency and availability are the requirements for banking apps. 
author: Sarah Chen
image: images/posts/CAP_Theorem.PNG
---
![CAP](https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/CAP_Theorem.svg/330px-CAP_Theorem.svg.png)
To support all those types of computing, a robust, distributed database is a prerequisite. The distributed databases, mostly NoSQL, come in a wide variety of data models, including key-value, document, columnar and graph formats; Apache HBase, Cassandra, Redis, MongoDB, Elastic Search, Solr, Neo4j to name a few. However, to effectively pick the tool of choice, a basic idea of the CAP Theorem (Brewer’s Theorem) is essential.

The CAP (Consistency, Availability and Partition Tolerance) Theorem states that a distributed system cannot be strictly consistent, highly available and fault tolerant at the same time. The system designers MUST choose at most two out of three guarantees in the system.

# Consistency
Consistency means all users have the same view of data at any given time.  If there are multiple replicas and there is an update being processed, all users see the update go live at the same time even if they are reading from different replicas. Systems that do not guarantee immediate consistency may provide eventual consistency.

Unlike for Google or many other companies, consistency is paramount for banks and trading platforms as it is simply not tolerable to have the money records shown differently for any given moment. 

For many other companies, the strict immediate consistency that banks require is not always important. It is not a big deal if you do not see the most updated post from a social media influencer. 

# Availability

Availability means that every request receives a response about whether it was successful or failed. Whether you want to read or write you will get some response back. i.e. the system continues to work and serve data despite node failures. This is achieved by using many replicas to store data such that clients always have access to at least one working replica guarantees availability.

For example, a user searches for some goods during peak time. Once in a while Amazon or Walmart may reply to requests with an error code “try again later.” Being told this immediately is more favorable than having to wait minutes or hours before one gives up.

# Partition Tolerance

Partition tolerance means that the system will continue operate even if any number of messages sent between nodes is lost. A single node failure should not cause the entire system to collapse. A three-legged cat is partition tolerant. If it was a horse, we would have to put it out of misery.

In the above LinkedIn scenario, the site continues to operate even if the node in United States goes down or loses communication to other nodes in Asia and Europe.

# The CAP Trade-off
## CA (Consistency and Availability) – Non-distributed system

The systems which retains consistency and availability sacrificing partition tolerance cannot be a distributed system. Mostly traditional relational databases like Oracle, MySQL, and PostgreSQL are consistent and available (CA). They renounce partition tolerance hence they can only be scaled up not scaled out. They use transactions and other database techniques to assure that updates are atomic. They propagate completely or not at all. Thus, they guarantee all users will see the same state at the same time. Banking and finance applications require the data to be consistent and available.

## AP (Availability and Partition Tolerance) – True Distributed system

All distributed systems must retain partition tolerance. AP based systems trade off consistency for availability. This means that they cannot guarantee consistency in the data between nodes. Distributed NoSQL data stores like Dynamo from Amazon, Cassandra, CouchDB, and Riak adopt this AP based data stores allows users to write data to one node of the database without waiting for other nodes to come into agreement, preferring the availability over immediate consistency.

## CP (Consistency and Partition Tolerance) – True Distributed system

CP based distributed system gives up availability and prefers consistency. This means that the data is consistent between all the nodes and the system may not be fully available in case of a node going down.

For any read or write into the CP based data stores, first all the nodes must come into agreement. So, full availability takes a backseat, giving way to strong consistency.

Choose CP-based database system, when it is critical that all users need a consistent view of the data in their application more than availability. Again, CP systems are not completely available but strongly consistent.

Choose AP-based database system, when there is always a requirement that the applications could sacrifice data consistency in return of huge performance. Again, AP based systems are not immediately consistent, they guarantee data reconciliation at a little later time with eventual consistency in place.

In a nutshell, choosing between Consistency and Availability is a software trade off,

Choose Consistency over Availability when the business requirements dictate atomic reads and writes.

Choose Availability over Consistency when the business requirements allow for some flexibility, to synchronize data with some acceptable delay.

# Making the right trade-offs
Distributed systems have higher performance, lower latency, and near 100% up-time in data centers that span the entire globe. However, they are more complex and requires making appropriate trade-offs.

Banking (retail, personal or corporate) sector falls in the category of transactional data management applications which heavily rely on the **ACID** guarantees that the database provides. In the realm of Distributed Databases, normally **CA** is preferred for the banking applications, since Consistency (C) is paramount and Availability (A) is very important and partitions (P) needs to be avoided i.e partition-tolerant. 

The reason being, it is fine to loose some functionalities of the banking application due to network partition but NOT OK to be inconsistent and unavailable. But if the application wants to leverage the real characteristics of Distributed Databases of distributing the data among the nodes. then, CP (Consistent and partition-tolerant, but not highly available) is employed eg HBase, BigTable which has strong consistency models like immediate consistency, but never AP (Highly available and partition-tolerant, but not consistent). The reason being AP systems follow the weaker consistency models like Eventual consistency, Timeline consistency & session consistency. 


Aside: in the Enterprise Risk Management department, managers do not want to run any kinds of risk, including direct contact with source data.  The rational:  maybe no one will sign off on the data.    Since ERM does not want to work with source data, then the entire function has to rely on outputs from different teams: retail/consumer credit, wholesale credit, counterparty credit risk, market risk, operational risk, and etc.  *Fast is difficult here*.  That's the reality in some large banks. 

Besides having the right databases, in a large organization such as a big bank, perhaps the biggest problem is not technology, but the many  steps in between data and end product. 

