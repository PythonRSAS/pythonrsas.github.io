---
layout: page-doc
title: Other Risks
subheading: Macro risk, inflation, and other risk.
description: Macro risk, inflation, and other risk.
color: grad-blog
image: "/images/icons/real-estate.svg"
permalink: /bigger-and-or-other-risk
image: https://drive.google.com/uc?id=1edu-wUoFkrMuoemONmOvsIMpnvkAdFXY
---

<div class="home-container">
  <div class="home-articles">
    <div class="home-wrapper">
      <div class="page-holder">
        <ul>
        {% for post in site.posts %}
          {% if post.categories contains "Other Risks" %}
                <li>
                  <a class="post-link" href="{{ site.baseurl }}{{ post.url }}">
                    <div class="page-treasure-wrapper">
                      <div class="page-treasure-image" >
                        <div style="background-image: url('{{ post.image | relative_url }}')"></div>
                      </div>
                      <div class="page-treasure">
                        <h2>{{ post.title }}</h2>
                        <p>{{ post.description }}</p>
                      </div>
                    </div>
                  </a>
                </li>
            {% endif %}
        {% endfor %}
        </ul>
      </div>
    </div>
  </div>
</div>