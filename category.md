---
layout: page-default
heading: blog
title: Category Page
subheading: Personal Website of Sarah Chen
description: I'm Sarah Chen. Co-author of “Python for SAS Users”.  Domain expert in banking and insurance (added).  Loving math and using computers to do things, and super passionate about education for youth (Mandarin Chinese, real world practical and beautiful mathematics, computer programming).
color: grad-blog
image: /images/icons/logo.png
permalink: /category
---

{% include colorful-header.html %}

<div class="home-container">
  <div class="home-articles">
    <div class="home-wrapper">
      <div class="gem-box">
        <div class="python-for-sas" onclick="location.href='{{ site.baseurl }}/python-for-sas';">
          <img src="{{ "/images/icons/python.svg" | relative_url }}"/>
          <h4>Python for SAS Users</h4>
          <p>Extension of the book "Python for SAS Users".</p>
          {% for post in site.posts %}
            {% if post.categories contains 'python for sas' %}
                {% capture python_for_sas_count %} {{ python_for_sas_count | plus: 1 }} {% endcapture %}
              {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ python_for_sas_count }} posts</p>
        </div>
        <div class="insurance" onclick="location.href='{{ site.baseurl }}/insurance';">
          <img src="{{ "/images/icons/insurance.svg" | relative_url }}" alt="insurance"/>
          <h4>Insurance</h4>
          <p>Actuarial trainings and the changing world.</p>
          {% for post in site.posts %}
            {% if post.categories contains 'insurance' %}
                {% capture insurance_count %} {{ insurance_count | plus: 1 }} {% endcapture %}
              {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ insurance_count }} posts</p>
        </div>
        <div class="credit-risk" onclick="location.href='{{ site.baseurl }}/credit-risk';">
          <img src="{{ "/images/icons/credit-risk.svg" | relative_url }}" alt="credit risk"/>
          <h4>Credit Risk</h4>
          <p>Credit risk, PD, LGD, and EAD models.</p>
          {% for post in site.posts %}
              {% if post.categories contains 'credit risk' %}
                {% capture credit_risk_count %} {{ credit_risk_count | plus: 1 }} {% endcapture %}
              {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ credit_risk_count }} posts</p>
        </div>
        <div class="deep-learning" onclick="location.href='{{ site.baseurl }}/deep-learning';">
            <img src="{{ "/images/icons/deep-learning.svg" | relative_url }}" />
            <h4>Deep Learning</h4>
            <p>Deep learning in non-computer vision problems.</p>
            {% for post in site.posts %}
            {% if post.categories contains 'deep learning' %}
                {% capture deep_learning_count %} {{ deep_learning_count | plus: 1 }} {% endcapture %}
              {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ deep_learning_count }} posts</p>
        </div>
        <div class="machine-learning" onclick="location.href='{{ site.baseurl }}/machine-learning';">
            <img src="{{ "/images/icons/machine-learning.svg" | relative_url }}" />
            <h4>Statistical and Machine learning</h4>
            <p>Fundamental concepts, techniques, and interpretability.</p>
            {% for post in site.posts %}
              {% if post.categories contains 'machine learning' %}
                {% capture machine_learning_count %} {{ machine_learning_count | plus: 1 }} {% endcapture %}
            {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ machine_learning_count }} posts</p>
        </div>
        <div class="commercial-real-estates" onclick="location.href='{{ site.baseurl }}/fraud-and-risk';">
          <img src="{{ "/images/icons/real-estate.svg" | relative_url }}"/>
          <h4>Fraud and Risk</h4>
          <p>Fraud, AML, ACH and payments.</p>
          {% for post in site.posts %}
            {% if post.categories contains 'fraud and risk' %}
                {% capture fraud_and_risk_count %} {{ fraud_and_risk_count | plus: 1 }} {% endcapture %}
            {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ fraud_and_risk_count }} posts</p>
        </div>
        <div class="education" onclick="location.href='{{ site.baseurl }}/education';">
          <img src="{{ "/images/icons/education.svg" | relative_url }}" />
          <h4>Education</h4>
          <p>Different perspectives on educations.</p>
          {% for post in site.posts %}
            {% if post.categories contains 'education' %}
                {% capture education_count %} {{ education_count | plus: 1 }} {% endcapture %}
            {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ education_count }} posts</p>
        </div>
        <div class="market-risk" onclick="location.href='{{ site.baseurl }}/market-risk';">
          <img src="{{ "/images/icons/market.svg" | relative_url }}" />
          <h4>Market and Traded Risk</h4>
          <p>Market risk VaR and simulations.</p>
          {% for post in site.posts %}
            {% if post.categories contains 'market risk' %}
                {% capture market_risk_count %} {{ market_risk_count | plus: 1 }} {% endcapture %}
            {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ market_risk_count }} posts</p>
        </div>
      </div>
    </div>
  </div>
</div>