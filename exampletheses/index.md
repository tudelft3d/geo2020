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

We maintain a [list of all the MSc Geomatics theses](https://www.tudelft.nl/onderwijs/opleidingen/masters/gm/msc-geomatics/programme/graduation-project/student-graduation-work/), and alternatively you can [search in the TU Delft repository for programme:'Geomatics'](http://repository.tudelft.nl/islandora/search/mods_note_programme_s%3A%22Geomatics%22?collection=education&sort=mods_originInfo_dateSort_dt%20desc).
  
