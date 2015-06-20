---
layout: page
title: News
permalink: /news/
---


{% for post in site.posts %}
  <h4><small>{{ post.date | date_to_string }}</small><br><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h4>
{% endfor %}

<hr>

<a href="{{ site.baseurl }}/feed.xml"><i class="fa fa-rss"></i> RSS</a>
