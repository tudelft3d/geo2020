---
layout: page
title: Example theses
color: dark
logo: fa-book
permalink: /exampletheses/
---

## Some good theses that can be used as examples

{% assign theses = site.data.mscbest | sort: 'year' | reverse %}

{% for i in theses %}

<article class="media">
  <figure class="media-left">
    <a href="{{ i.link }}"><p class="image is-128x128">
      <img src="img/{{ i.image }}">
    </p>
  </a>
  </figure>
  <div class="media-content">
    <div class="content">
      <p>
        <strong>{{ i.title }}</strong> 
        <br>
        {{ i.name }} {{ i.surname }} <small>({{ i.year }})</small> 
      </p>
    </div>
  </div>
</article>

{% endfor %}


## Recently completed theses

We maintain a [list of all the MSc Geomatics theses](https://www.tudelft.nl/onderwijs/opleidingen/masters/gm/msc-geomatics/programme/student-graduation-work), and alternatively you can [search in the TU Delft repository for programme:'Geomatics'](http://repository.tudelft.nl/islandora/search/mods_note_programme_s%3A%22Geomatics%22?collection=education&sort=mods_originInfo_dateSort_dt%20desc).
  
