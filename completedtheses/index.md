---
layout: page
title: Completed theses
permalink: /completedtheses/
---

## Some good theses that can be used as examples

{% assign theses = site.data.mscbest | sort: 'surname' %}
<div class="row">
{% for i in theses %}
  <div class="col s12 m4">
    <a href="{{ i.link }}">
    <div class="card">
      <div class="card-image">
        <img src="img/{{ i.image }}">
      </div>
      <div class="card-content">
        <p><b>{{ i.name }} {{ i.surname }}</b> ({{ i.year }})</p>
        <p><i>{{ i.title }}</i></p>
      </div>
    </div>
    </a>
  </div>
  {% endfor %}
  </div>


## Recently completed theses

{% assign theses = site.data.mscfinished | sort: 'year' | reverse %}
<div class="row">
{% for i in theses %}
  <div class="col s12 m4">
    <a href="{{ i.link }}">
    <div class="card">
      <div class="card-image">
        <img src="img/{{ i.image }}">
      </div>
      <div class="card-content">
        <p><b>{{ i.name }} {{ i.surname }}</b> ({{ i.year }})</p>
        <p><i>{{ i.title }}</i></p>
      </div>
    </div>
    </a>
  </div>
  {% endfor %}
  </div>

  
