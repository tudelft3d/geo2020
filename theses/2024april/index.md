---
layout: page
title: "Thesis starting April 2024"
permalink: /theses/2024april/
---


{% assign thesis = site.data.theses_2023sep %}

{% for i in thesis %}

<article class="media">
  <figure class="media-left">
    <p class="image">
      <img src="{{ i[1][6] }}">
    </p>
  </figure>
  <div class="media-content">
    <div class="content">
      <p>
        <strong>{{ i[1][0] }} {{ i[0] }}</strong> 
        <br>
        <em>{{ i[1][1] }}</em>
        <br>
        {{ i[1][4] | markdownify }}
        <small>Supervisors: {{ i[1][2] }} + {{ i[1][3] }}</small>
        <br>
        {% if i[1][5].size > 0 %}
          <small>(company involved: {{ i[1][5] }})</small>
        {% endif %}
      </p>
    </div>
  </div>
</article>

{% endfor %}


