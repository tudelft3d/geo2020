---
layout: page
title: "Thesis starting April 2023"
permalink: /theses/2023april/
---


{% assign thesis = site.data.theses_2023april %}

{% for i in thesis %}

<article class="media">
  <figure class="media-left">
    <p class="image">
      <img src="img/{{i[1][4]}}">
    </p>
  </figure>
  <div class="media-content">
    <div class="content">
      <p>
        <strong>{{ i[1][0] }} {{ i[0] }}</strong> 
        <br>
        <em>{{ i[1][5] }}</em>
        <br>
        {{ i[1][3] | markdownify }}
        <small>Supervisors: {{ i[1][1] }} + {{ i[1][2] }}</small>
        <br>
        <small>{{ i[1][6] }}</small>
      </p>
    </div>
  </div>
</article>

{% endfor %}


