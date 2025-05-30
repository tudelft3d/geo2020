---
layout: page
title: News
permalink: /news/
---

<p>Subscribe to receive the news with <a href="{{ site.baseurl }}/feed.xml"><i class="fa fa-rss"></i> RSS</a></p>

<hr>

{% for post in site.posts %}

<h5><small>{{ post.date | date_to_string }}</small><br><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h5>

{% endfor %}

<br><br>





