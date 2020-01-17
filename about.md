---
layout: splash
heading: sarah chen
title: Sarah Chen
description: Personal Website of Sarah Chen
color: grad-about
permalink: /
---

<div class="blog-intro {{ page.color }} about-header-fix">
  <div class="profile-wrapper">
    <div class="profile-pic"><img src="{{ "./images/avatar.jpg" | relative_url }}" /></div>
    <div class="profile-description">
      <h1>{{ site.name }}</h1>
      <p>{{ site.subheading }}</p>
    </div>
  </div>
  <div class="home-follow-wrapper">
    <div class="home-follow">
      <script async defer src="https://buttons.github.io/buttons.js"></script>
      <a href="https://twitter.com/{{site.footer-links.twitter}}?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-size="large" data-show-screen-name="false" data-show-count="true"></a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
      <a class="github-button" href="https://github.com/{{site.footer-links.github}}" data-show-count="true" data-size="large" aria-label="Follow @{{site.footer-links.github}} on GitHub">Follow</a>
    </div>
  </div>
</div>

<div class="about-container">
  <div class="home-articles">
    <div class="home-wrapper about-wrapper">
      <div class="category-tab about-category-tab" id="category-tab">
        <ul>
          <li id="tab_summary" onclick="showAboutTabBox(this.id)">summary</li>
          <li id="tab_publications" onclick="showAboutTabBox(this.id)">publications</li>
        </ul>
      </div>
      <!--Summary STARTS-->
      <div class="blog-category-box work-category-box about-category-box" id="box_summary" style="box-shadow: none !important;">
        <div>
          <div class="about_me_body">
            <div class="social">
              {% if site.footer-links.email %}
              <a href="mailto:{{ site.footer-links.email }}?Subject=Hello"><img src="{{ "./images/icons/mail.png" | relative_url }}" title="Shoot me a mail" /></a>
              {% endif %}
              {% if site.footer-links.github %}
              <a href="https://github.com/{{ site.footer-links.github }}" target="_blank"><img src="{{ "./images/icons/github.png" | relative_url }}" title="GitHub" /></a>
              {% endif %}
              {% if site.footer-links.linkedin %}
              <a href="https://www.linkedin.com/in/{{ site.footer-links.linkedin }}" target="_blank"><img src="{{ "./images/icons/linkedin.png" | relative_url }}" title="LinkedIn" /></a>
              {% endif %}
              {% if site.footer-links.quora %}
              <a href="https://www.quora.com/profile/{{ site.footer-links.quora }}" target="_blank"><img src="{{ "./images/icons/quora.png" | relative_url }}" title="Quora" /></a>
              {% endif %}
              {% if site.footer-links.twitter %}
              <a href="https://twitter.com/{{ site.footer-links.twitter }}" target="_blank"><img src="{{ "./images/icons/twitter.png" | relative_url }}" title="Twitter" /></a>
              {% endif %}
              {% if site.footer-links.youtube %}
              <a href="https://www.youtube.com/c/{{ site.footer-links.youtube }}" target="_blank"><img src="{{ "./images/icons/youtube.png" | relative_url }}" title="YouTube" /></a>
              {% endif %}
            </div>
          <p class="about-quote">“Simple can be harder than complex: You have to work hard to get your thinking clean to make it simple. But it’s worth it in the end because once you get there, you can move mountains.”<br>― Steve Jobs</p>
          <h3>Biography</h3>
          <p style="margin-top: 0px !important;">I'm Sarah Chen. Loving math and using computers to do things, and super passionate about education for youth (Mandarin Chinese, real world practical and beautiful mathematics, computer programming).
          </p>
          <ul class="timeline">
            <li>Co-author of <a href="https://www.amazon.com/Python-SAS-Users-SAS-Oriented-Introduction/dp/1484250001">Python for SAS Users</a></li>
            <li>Domain expert in bank credit and market risk, fraud risk, and insurance pricing and reserving.</li>
            <li>Analytic lead with twelve years of hands-on experience in development of predictive models and efficient algorithms in banking and insurance.</li>
            <li>Fellow of the <a href="https://www.casact.org/">Casualty Actuarial Society</a> (FCAS), Fellow of the <a href=" https://www.soa.org/"> Society of Actuaries</a>(FSA).</li>
            <li>Co-founder of <a href=" https://www.magicmathmandarin.org/"> Magic Math Mandarin </a></li>
          </ul>
          <p><strong>Expertise: </strong>credit and market risk, fraud risk, personal auto pricing, actuarial reserve analysis, statistical inference, time series analysis, algorithm design, TensorFlow, machine learning models (regression/boosting/bagging/stacking), natural language processing (NLP), deep learning models (LSTM/GRU/CNN/autoencoders), Python, R, SAS and SQL.</p>
        </div>
      </div>
    </div>
      <!--Publications STARTS-->
      <div class="blog-category-box work-category-box about-category-box" id="box_publications" style="box-shadow: none !important;">
        <div class="work-inner-box">
          <h2>2017</h2>
          <ul>
            <li>
              <div>
                <h4><a href="https://link.springer.com/chapter/10.1007/978-981-10-7895-8_25" target="_blank">This site is under construction</a></h4>
                <p>Sarah</p>
                <p><i>CVIP-2017, Springer pp 317-330</i></p>
              </div>
            </li>
          </ul>
          <br>
          <br>
        </div>
      </div>
      <!--Publications ENDS-->
    </div>
  </div>
</div>

<script src="//cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@0.5.0"></script>
<script type="text/javascript">
  document.getElementById("box_summary").style.display = "block";
  document.getElementById("tab_summary").style.fontWeight = "bold";
  document.getElementById("tab_summary").style.borderBottom = "1px solid black";
</script>