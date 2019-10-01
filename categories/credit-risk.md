---
layout: page-doc
title: Credit Risk
subheading: Learn how to design a chip using which you could create electronics applications.
description: Learn how to design a chip using which you could create electronics applications.
color: grad-blog
image: "/images/icons/credit-risk.svg"
permalink: /credit-risk
---

<div class="home-container">
  <div class="home-articles">
    <div class="home-wrapper">
      <div class="page-holder">
        <ul>
        {% for post in site.posts %}
          {% if post.categories contains 'hardware' %}
          		{% if post.class contains 'ASIC Design' %}
		            <li>
                  <a class="post-link" href="{{ site.baseurl }}{{ post.url }}">
                    <div class="page-treasure-wrapper">
                      <div class="page-treasure-image" >
                        <div style="background-image: url('{{ post.image }}')"></div>
                      </div>
                      <div class="page-treasure">
                        <h2>{{ post.title }}</h2>
                        <p>{{ post.description }}</p>
                      </div>
                    </div>
                  </a>
                </li>
            	{% endif %}
            {% endif %}
        {% endfor %}
        </ul>
      </div>
    </div>
  </div>
</div>