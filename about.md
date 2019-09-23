---
layout: splash
heading: sarah chen
title: Sarah Chen
description: Personal Website
color: grad-about
permalink: /
---

<div class="blog-intro {{ page.color }} about-header-fix">
  <div class="profile-wrapper">
    <div class="profile-pic"><img src="{{ "./images/icons/base-person.png" | relative_url }}" /></div>
    <div class="profile-description">
      <h1>{{ site.name }}</h1>
      <p>{{ site.subheading }}</p>
    </div>
  </div>
  <div class="home-follow-wrapper">
    <div class="home-follow">
      <script async defer src="https://buttons.github.io/buttons.js"></script>
      <a href="https://twitter.com/gogul_ilango?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-size="large" data-show-screen-name="false" data-show-count="true">Follow @gogul_ilango</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
      <a class="github-button" href="https://github.com/Gogul09" data-show-count="true" data-size="large" aria-label="Follow @Gogul09 on GitHub">Follow</a>
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
              <a href="mailto:{{ site.footer-links.email }}?Subject=Hello"><img src="/images/icons/mail.png" title="Shoot me a mail" /></a>
              <a href="https://github.com/{{ site.footer-links.github }}" target="_blank"><img src="{{ "./images/icons/github.png" | relative_url }}" title="GitHub" /></a>
              <a href="https://www.linkedin.com/in/{{ site.footer-links.linkedin }}" target="_blank"><img src="{{ "./images/icons/linkedin.png" | relative_url }}" title="LinkedIn" /></a>
              <a href="https://www.quora.com/profile/{{ site.footer-links.quora }}" target="_blank"><img src="{{ "./images/icons/quora.png" | relative_url }}" title="Quora" /></a>
              <a href="https://twitter.com/{{ site.footer-links.twitter }}" target="_blank"><img src="/{{ ".images/icons/twitter.png" | relative_url }}" title="Twitter" /></a>
              <a href="https://www.youtube.com/c/{{ site.footer-links.youtube }}" target="_blank"><img src="{{ "./images/icons/youtube.png" | relative_url }}" title="YouTube" /></a>
            </div>
          <p class="about-quote">"There are no constraints on the human mind, no walls around the human spirit, no barriers to our progress except those we ourselves erect" <br>Ronald Reagan</p>
          <h3>Biography</h3>
          <p style="margin-top: 0px !important;">I'm Sarah Chen. Loving math and using computers to do things, and super passionate about education for youth (Mandarin Chinese, real world practical and beautiful mathematics, computer programming).
          </p>
          <ul class="timeline">
            <li>Co-author of Python for SAS Users: A SAS oriented introduction to Python.</li>
            <li>Domain expert in bank credit risk, forecasting, stress testing, fraud risk, insurance pricing and reserving.</li>
            <li>Twelve years of hands-on experience in development of predictive models and efficient algorithms in banking and insurance.</li>
            <li>Fellow of the Casualty Actuarial Society (FCAS), Fellow of the Society of Actuaries (FSA).</li>
            <li>Co-founder of Magic Math Mandarin https://www.magicmathmandarin.org/.</li>
          </ul>
          <p><strong>Expertise: </strong>credit risk (wholesale in C&I and CRE), personal auto pricing, actuarial reserve analysis, statistical inference, time series analysis, algorithm design, TensorFlow, machine learning models (regression/boosting/bagging/stacking), natural language processing (NLP), deep learning models (LSTM/GRU/CNN/autoencoders), Python, R, SAS.</p>
          <div class="highlight-box">
            <p>In case you're wondering, this site </p>
            <ul style="margin: 0px !important;">
              <li>Hosted proudly through <a href="https://github.com/" target="_blank">GitHub</a>.</li>
              <li>Designed and developed on a <a href="https://www.microsoft.com/en-in/software-download/windows10" target="_blank">Windows 10</a> machine.</li>
              <li>Written using my favorite text-editor <a href="https://www.sublimetext.com/3" target="_blank">Sublime Text 3</a>.</li>
              <li>Handcrafted using the awesome <a href="https://jekyllrb.com/" target="_blank">Jekyll</a>.</li>
              <li>Uses the beautiful <a href="https://fonts.google.com/" target="_blank">Google Fonts</a>.</li>
              <li>Uses handcrafted icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a>.</li>
            </ul>
          </div>
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