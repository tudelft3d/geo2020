---
layout: page
title: Completed MSc Geomatics theses
permalink: /completedtheses/
---


{% assign theses = site.data.mscfinished | sort: 'year' | reverse %}
<div class="row">
{% for i in theses %}
  <div class="col s4">
    <div class="card">
      <div class="card-image">
        <img src="img/carl.jpg">
      </div>
      <div class="card-content">
        <p>{{ i.name }} {{ i.surname }}</p>
        <p><i>{{ i.title }}</i></p>
      </div>
      <div class="card-action">
      {% if i.link %}
          <a href="{{ i.link }}"><i class="fa fa-book" title="thesis"></i></a>
        {% endif %}
      </div>
    </div>
  </div>
  {% endfor %}
  </div>

  
