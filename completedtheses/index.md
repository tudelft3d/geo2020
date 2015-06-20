---
layout: page
title: Completed MSc Geomatics theses
permalink: /completedtheses/
---


{% assign theses = site.data.mscfinished | sort: 'year' | reverse %}
<div class="row">
{% for i in theses %}
  <div class="col s12 m4">
    <a href="{{ i.link }}">
    <div class="card">
      <div class="card-image">
        <img src="img/carl.jpg">
      </div>
      <div class="card-content">
        <p><b>{{ i.name }} {{ i.surname }}</b></p>
        <p><i>{{ i.title }} ({{ i.year }})</i></p>
      </div>
    </div>
    </a>
  </div>
  {% endfor %}
  </div>

  
