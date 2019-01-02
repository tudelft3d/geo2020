---
layout: page
title: Example theses
permalink: /exampletheses/
---



## Some good theses that can be used as examples

{% assign theses = site.data.mscbest | sort: 'year' | reverse %}

<div class="columns is-multiline is-mobile">
  
{% for i in theses %}
  
  <div class="column is-one-third">
    <div class="card">
      <a href="{{ i.link }}">
      <div class="card-image">
        <figure class="image">
          <img src="img/{{ i.image }}">
        </figure>
      </div>
      </a>
      <div class="card-content">
          <div class="media-content">
            <p class="title is-4">{{ i.name }} {{ i.surname }}</p>
            <p class="subtitle is-6">({{ i.year }})</p>
          </div>
          <div class="content">
            {{ i.title }}
          </div>
      </div>
    </div>
  </div>
{% endfor %}
</div>


## Recently completed theses

We maintain a [list of all the MSc Geomatics theses](https://www.tudelft.nl/onderwijs/opleidingen/masters/gm/msc-geomatics/programme/graduation-project/student-graduation-work/), and alternatively you can [search in the TU Delft repository for programme:'Geomatics'](http://repository.tudelft.nl/islandora/search/mods_note_programme_s%3A%22Geomatics%22?collection=education&sort=mods_originInfo_dateSort_dt%20desc).
  
