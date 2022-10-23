---
layout: splash
heading: sarah chen
title: Sarah Chen
description: Data scientist and gardener
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
      <!-- <a href="https://twitter.com/{{site.footer-links.twitter}}?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-size="large" data-show-screen-name="false" data-show-count="true"></a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
       --><!-- <a class="github-button" href="https://github.com/{{site.footer-links.github}}" data-show-count="false" data-size="large" aria-label="Follow @{{site.footer-links.github}} on GitHub">Follow</a> -->
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
          <h3>Summary</h3>
          <!-- <p style="margin-top: 0px !important;">I'm Sarah Chen. Analytic expert in banking and insurance.
          </p> -->
          <ul class="timeline">
            <li>Domain expert in credit, market, operational risk in financial services, and insurance pricing and reserving.</li>
            <li>Analytic lead with thirteen years of hands-on experience in development of predictive models and efficient algorithms in banking and insurance.</li>
            <li>Fellow of the <a href="https://www.casact.org/" target="_blank">Casualty Actuarial Society</a> (FCAS), Fellow of the <a href=" https://www.soa.org/" target="_blank"> Society of Actuaries</a> (FSA).</li>
            <!-- <li>Co-founder of <a href=" https://www.magicmathmandarin.org/"> Magic Math Mandarin </a></li> -->
            <li>Co-founder of Magic Math Mandarin</li>
            <li>Co-author of <a href="https://www.amazon.com/Python-SAS-Users-SAS-Oriented-Introduction/dp/1484250001" target="_blank">Python for SAS Users</a></li>
            <li><a href="https://www.math.columbia.edu/" target="_blank">Columbia University</a> 2007, B.A. Mathematics, summa cum laude</li>
          </ul>
          <p><strong>Expertise: </strong>credit and marekt/traded risk management, insurance pricing/reserving, data management, time series analysis, algorithm design,statistical, machine learning, and deep learning models , Python, R, SAS and SQL.</p>
        </div>
      </div>
      </div>
      <!--Publications STARTS-->
      <div class="blog-category-box work-category-box about-category-box" id="box_publications" style="box-shadow: none !important;">
        <div class="work-inner-box">
          <h2>2019</h2>
          <ul>
            <li>
              <div>
                <h4><a href="https://www.amazon.com/Fun-Chinese-Poems-Kids-delightfully/dp/1734315202/ref=sr_1_1?keywords=fun+chinese+poems+for+kids&qid=1579308749&sr=8-1" target="_blank">Fun Chinese Poems for Kids</a></h4>
                <p>delightfully illustrated, annotated with Pinyin, and full English translations</p>
                <p><i>Magic Math Mandarin</i></p>
              </div>
            </li>
          </ul>
          <br>
          <br>
        </div>
        <div class="work-inner-box">
          <h2>2019</h2>
          <ul>
            <li>
              <div>
                <h4><a href="https://www.amazon.com/Python-SAS-Users-SAS-Oriented-Introduction/dp/1484250001" target="_blank">Python for SAS Users</a></h4>
                <p>A SAS-Oriented Introduction to Python</p>
                <p><i>Apress</i></p>
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