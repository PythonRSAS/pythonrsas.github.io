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
        <div class="statistics" onclick="location.href='{{ site.baseurl }}/asic-design';">
          <img src="{{ "/images/icons/credit-risk.svg" | relative_url }}" alt="credit risk"/>
          <h4>Temporary Closed</h4>
          <p>Learn how to design a chip using which you could create electronics applications.</p>
          {% for post in site.posts %}
            {% if post.categories contains 'finance' %}
              {% if post.class contains 'Credit Risk' %}
                {% capture credit_risk_count %} {{ credit_risk_count | plus: 1 }} {% endcapture %}
              {% endif %}
            {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ asic_design_count }} posts</p>
        </div>
        <div class="credit-risk" onclick="location.href='{{ site.baseurl }}/credit-risk';">
          <img src="{{ "/images/icons/credit-risk.svg" | relative_url }}" alt="credit risk"/>
          <h4>Credit Risk</h4>
          <p>Learn how to design a chip using which you could create electronics applications.</p>
          {% for post in site.posts %}
            {% if post.categories contains 'finance' %}
              {% if post.class contains 'Credit Risk' %}
                {% capture credit_risk_count %} {{ credit_risk_count | plus: 1 }} {% endcapture %}
              {% endif %}
            {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ asic_design_count }} posts</p>
        </div>
        <div class="deep-learning" onclick="location.href='{{ site.baseurl }}/deep-learning';">
            <img src="{{ "/images/icons/deep-learning.svg" | relative_url }}" />
            <h4>Deep Learning</h4>
            <p>Learn how to create deep neural networks to solve challenging problems.</p>
            {% for post in site.posts %}
            {% if post.categories contains 'software' %}
              {% if post.class contains 'TensorFlow.js' or post.class contains 'Keras' or post.class contains 'Deep Learning' %}
                {% capture deep_learning_count %} {{ deep_learning_count | plus: 1 }} {% endcapture %}
              {% endif %}
            {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ deep_learning_count }} posts</p>
        </div>
        <div class="machine-learning" onclick="location.href='{{ site.baseurl }}/machine-learning';">
            <img src="{{ "/images/icons/machine-learning.svg" | relative_url }}" />
            <h4>Machine Learning</h4>
            <p>Learn how to create algorithms that don't require you to write rules.</p>
            {% for post in site.posts %}
            {% if post.categories contains 'software' %}
              {% if post.class contains 'Machine Learning' %}
                {% capture machine_learning_count %} {{ machine_learning_count | plus: 1 }} {% endcapture %}
              {% endif %}
            {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ machine_learning_count }} posts</p>
        </div>
        <div class="python-for-sas" onclick="location.href='{{ site.baseurl }}/python-for-sas';">
          <img src="{{ "/images/icons/python.svg" | relative_url }}"/>
          <h4>Python for SAS Users</h4>
          <p>Learn how to make your USB webcam or camera to understand world's information.</p>
          {% for post in site.posts %}
            {% if post.categories contains 'software' %}
              {% if post.class contains 'Computer Vision' %}
                {% capture computer_vision_count %} {{ computer_vision_count | plus: 1 }} {% endcapture %}
              {% endif %}
            {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ computer_vision_count }} posts</p>
        </div>
        <div class="commercial-real-estates" onclick="location.href='{{ site.baseurl }}/commercial-real-estates';">
          <img src="{{ "/images/icons/real-estate.svg" | relative_url }}"/>
          <h4>Commercial Real Estate</h4>
          <p>Learn how to make use of your brain to write code.</p>
          {% for post in site.posts %}
            {% if post.categories contains 'software' %}
              {% if post.class contains 'Programming' %}
                {% capture programming_count %} {{ programming_count | plus: 1 }} {% endcapture %}
              {% endif %}
            {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ programming_count }} posts</p>
        </div>
        <div class="resources" onclick="location.href='{{ site.baseurl }}/resources';">
          <img src="{{ "/images/icons/resources.svg" | relative_url }}" />
          <h4>Resources</h4>
          <p>Learn how to make use of internet to learn anything free.</p>
          {% for post in site.posts %}
            {% if post.categories contains 'hardware' or post.categories contains 'software' %}
              {% if post.class contains 'Resources' %}
                {% capture resources_count %} {{ resources_count | plus: 1 }} {% endcapture %}
              {% endif %}
            {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ resources_count }} posts</p>
        </div>
        <div class="education" onclick="location.href='{{ site.baseurl }}/education';">
          <img src="{{ "/images/icons/education.svg" | relative_url }}" />
          <h4>Education</h4>
          <p>Learn how traveling creates peace within you.</p>
          {% for post in site.posts %}
            {% if post.categories contains 'travel' %}
                {% capture travel_count %} {{ travel_count | plus: 1 }} {% endcapture %}
            {% endif %}
          {% endfor %}
          <p class="no_of_posts">{{ travel_count }} posts</p>
        </div>
      </div>
    </div>
  </div>
</div>