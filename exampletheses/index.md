---
layout: page
title: Example theses
permalink: /exampletheses/
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

We maintain a [list of all the MSc Geomatics theses](http://www.tudelft.nl/en/study/master-of-science/master-programmes/geomatics/programme/graduation-project/finished-msc-thesis-projects/), and alternatively you can [search in the TU Delft repository for programme:'Geomatics'](http://repository.tudelft.nl/search/ir/?sort=date&q=programme%3A%22Geomatics%22&rows=20&start=0&fmt=&faculty=&department=&type=&year=&classification=&publisher=&jel_classification=).
  
