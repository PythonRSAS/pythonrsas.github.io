---
layout: post
tag: CAP theorem, banks, financial industry
category: "other risks"
title: "CAP theorem"
description: Strong and immediate consistency and availability are the requirements for banking apps. 
author: Sarah Chen
image: images/posts/photos/IMG-0683.jpg
---

Amazon found that every 100 milliseconds of latency, costs them 1% in sales. The application users, customers, and website visitors make an instant judgement about the application and the business. If the application is fast, a strong first impression is made. It’s a win for user experience.

# Fast

Customers will always want faster delivery. 

Besides having the right databases, in a large organization such as a big bank, perhaps the biggest problem is not technology, but the many unnecessary steps in between data and end product. 

In the Enterprise Risk Management department, managers do not want to run any kinds of risk, including direct contact with source data.  The rational:  maybe no one will sign off on the data.    Since ERM does not want to work with source data, then the entire function has to rely on outputs from different teams: retail/consumer credit, wholesale credit, counterparty credit risk, market risk, operational risk, and etc.  

## Large scale systems
how to choose a database


How does Google return search results so quickly? How is Facebook so fast even with 1.35 billion users? How can large eCommerce sites like Amazon and Flipkart serve fast despite huge influx of online traffic on a festive day? How are Amazon and Flipkart are rolling in money by up-selling, cross-selling and down selling?

Is it a magic?

No, it’s Distributed Computing. The terms “Concurrent Computing”, “Parallel Computing”, and “Distributed Computing” overlap and Distributed Computing has lots of computing paradigms in itself, like Cloud Computing, Grid Computing, Cluster Computing and the latest being Edge Computing.

Distributed Systems for Distributed Computing
To support all those types of computing, a robust, distributed database is a prerequisite. The distributed databases, mostly NoSQL, come in a wide variety of data models, including key-value, document, columnar and graph formats; Apache HBase, Cassandra, Redis, MongoDB, Elastic Search, Solr, Neo4j to name a few. However, to effectively pick the tool of choice, a basic idea of the CAP Theorem (Brewer’s Theorem) is essential.

No alt text provided for this image
CAP Theorem states that a distributed system cannot be strictly consistent, highly available and fault tolerant at the same time. The system designers MUST choose at most two out of three guarantees in the system.

There is no silver bullet. “One data store to have them all (Consistency, Availability and Partition Tolerance)” is something that Lord of the Rings fans would understand quickly.

CAP Theorem is very important in the Big Data world, when we need to choose if the system needs to be highly consistent or highly available under a network partition.

1.    Consistency

2.    Availability

3.    Partition Tolerance

Consistency
All the users or clients of the database have the same view of data, irrespective of any update or deletion. If there are multiple replicas and there is an update being processed, all users see the update go live at the same time even if they are reading from different replicas. Systems that do not guarantee immediate consistency may provide eventual consistency.

For example, they may guarantee that any update will propagate to all replicas in a certain amount of time. Until that deadline is reached, some queries may receive the new data while others will receive older, out-of-date answers. This is called eventual consistency.

No alt text provided for this image


Immediate consistency is not always important. Take for instance, a socio-professional platform like LinkedIn that shows the connections count for each user. The connections count is displayed in user’s own profile and in other network suggestions as mutual connections, albeit the counts differ for the mutual and actual connection. Consider that the connections database is replicated in the United States, Europe, and Asia. When a user in India gets 10 connections and that change takes a few minutes to propagate to the United States and Europe replicas. This may be enough for such a system because an accurate connections and mutual connections count is not always essential. If a user in the United States and one in Europe were talking on the phone as one was expanding connections, the other user would see the update seconds later and that would be okay. If the update took minutes due to network congestion or hours due to a network outage, the delay would still not be a terrible thing.

cap theorem bargunan somasundaram


Now imagine a banking application built on this system. A person in the United States and another in India could coordinate their actions to withdraw money from the same account at the same time. The ATM that each person uses would query its nearest database replica, which would claim the money is available and may be withdrawn. If the updates propagated slowly, both of them would have the cash before the bank realized the money was already gone. Here immediate consistency is necessary.

1.   Availability

A guarantee that every request receives a response about whether it was successful or failed. Whether you want to read or write you will get some response back. i.e. the system continues to work and serve data despite node failures. This is achieved by using many replicas to store data such that clients always have access to at least one working replica guarantees availability.

For example, a user in LinkedIn might try accessing a resource like shared post or video during peak time. Now due to overloading the LinkedIn will reply to requests with an error code “try again later.” Being told this immediately is more favorable than having to wait minutes or hours before one gives up.

cap theorem availability bargunan somasundaram


1.   Partition Tolerance

Partition tolerance means that the system will continue operate even if any number of messages sent between nodes is lost. A single node failure should not cause the entire system to collapse. A three-legged cat is partition tolerant. If it was a horse, we would have to put it out of misery.

In the above LinkedIn scenario, the site continues to operate even if the node in United States goes down or loses communication to other nodes in Asia and Europe.

The CAP Trade-off
1.CA (Consistency and Availability) – Non-distributed system

No alt text provided for this image
The systems which retains consistency and availability sacrificing partition tolerance cannot be a distributed system. Mostly traditional relational databases like Oracle, MySQL, and PostgreSQL are consistent and available (CA). They renounce partition tolerance hence they can only be scaled up not scaled out. They use transactions and other database techniques to assure that updates are atomic. They propagate completely or not at all. Thus, they guarantee all users will see the same state at the same time. Banking and finance applications require the data to be consistent and available.

1. AP (Availability and Partition Tolerance) – True Distributed system

No alt text provided for this image
All distributed systems must retain partition tolerance. AP based systems trade off consistency for availability. This means that they cannot guarantee consistency in the data between nodes. Distributed NoSQL data stores like Dynamo from Amazon, Cassandra, CouchDB, and Riak adopt this AP based data stores allows users to write data to one node of the database without waiting for other nodes to come into agreement, preferring the availability over immediate consistency.

3. CP (Consistency and Partition Tolerance) – True Distributed system

No alt text provided for this image
CP based distributed system gives up availability and prefers consistency. This means that the data is consistent between all the nodes and the system may not be fully available in case of a node going down.

For any read or write into the CP based data stores, first all the nodes must come into agreement. So, full availability takes a backseat, giving way to strong consistency.

When to opt for what?
Choose CP-based database system, when it is critical that all users need a consistent view of the data in their application more than availability. Again, CP systems are not completely available but strongly consistent.

ca vs cp cap theorem bargunan somasundaram
Choose AP-based database system, when there is always a requirement that the applications could sacrifice data consistency in return of huge performance. Again, AP based systems are not immediately consistent, they guarantee data reconciliation at a little later time with eventual consistency in place.

ca vs cp trade off bargunan somasundaram


In a nutshell, choosing between Consistency and Availability is a software trade off,

Choose Consistency over Availability when the business requirements dictate atomic reads and writes.
Choose Availability over Consistency when the business requirements allow for some flexibility, to synchronize data with some acceptable delay.
Conclusion
CAP based ca vs cp databases bargunan somasundaram
Given the astronomical level of computation requirements today, scaling up is obsolete; scaling out is the only optimum solution. Distributed systems (horizontally scalable) enable us to achieve those levels of computing power and availability that were simply not possible in the past. The distributed data stores have higher performance, lower latency, and near 100% up-time in data centers that span the entire globe. Distributed systems are more complex than their single-network counterparts. Understanding the complexity incurred in distributed systems, making the appropriate trade-offs for the task at hand (CAP), and selecting the right tool for the job is necessary with horizontal scaling.


105
 12 Comments
Like
Comment
Share
Alan Praveen
Alan Praveen
Simple and lucid writing that a non-technical person like me
could appreciate the information and insights provided. keep it up
Like Reply 1 Like
2y

Ramesh Natarajan
Ramesh Natarajan
Good Article.. What do you consider for banking sector data? CP or AP?
Like Reply 1 Like
2y

Bargunan Somasundaram
Bargunan Somasundaram
Thanks you for your question :)
Banking (retail, personal or corporate) sector falls in the category of transactional data management applications which heavily rely on the ACID guarantees that the database provides. In the realm of Distributed Databases, normally CA is preferred for the banking applications, since Consistency (C) is paramount and Availability (A) is very important and partitions (P) needs to be avoided i.e partition-tolerant. The reason being, it is fine to loose some functionalities of the banking application due to network partition but NOT OK to be inconsistent and unavailable. But if the application wants to leverage the real characteristics of Distributed Databases of distributing the data among the nodes. then, CP (Consistent and partition-tolerant, but not highly available) is employed eg HBase, BigTable which has strong consistency models like immediate consistency, but never AP (Highly available and partition-tolerant, but not consistent). The reason being AP systems follow the weaker consistency models like Eventual consistency, Timeline consistency & session consistency. 