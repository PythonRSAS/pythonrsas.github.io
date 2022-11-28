---
layout: page-default
heading: blog
title: Category Page
subheading: Analytics for financial risk management and investment
description: I'm Sarah Chen.  Analytic expert in banking and insurance.
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
            {% if post.categories contains 'Python for SAS' %}
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
        <div class="other-risks" onclick="location.href='{{ site.baseurl }}/other-risks';">
          <img src="{{ "/images/icons/real-estate.svg" | relative_url }}"/>
          <h4>other risks</h4>
          <p>Risks that financial institutions encounter day to day</p>
          {% for post in site.posts %}
            {% if post.categories contains 'other risks' %}
                {% capture other_risks_count %} {{ other_risks_count | plus: 1 }} {% endcapture %}
            {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ other_risks_count }} posts</p>
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