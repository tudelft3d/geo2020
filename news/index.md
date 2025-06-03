---
layout: page
title: News
color: light
logo: fa-newspaper
permalink: /news/
---

<h2>Subscribe to receive the news</h2>
<div id="mc_embed_shell">
	<div id="mc_embed_signup">
	    <form action="https://tudelft.us12.list-manage.com/subscribe/post?u=e232253e1c3c3152374abfdd1&amp;id=53540258a3&amp;f_id=004d8fe0f0" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_self" novalidate="">
	    	<p>By e-mail:</p>
	    	<p class="control has-icons-left">
	    		<input class="input" type="email" name="EMAIL" id="mce-EMAIL" placeholder="Email" />
	    		<span class="icon is-small is-left">
			    	<i class="fas fa-envelope"></i>
			    </span>
			</p>
			<div style="position: absolute; left: -5000px;" aria-hidden="true">
			        /* real people should not fill this in and expect good things - do not remove this or risk form bot signups */
			        <input type="text" name="b_e232253e1c3c3152374abfdd1_53540258a3" tabindex="-1" value="">
			    </div>
		        <div class="optionalParent">
		            <div class="clear foot">
		                <input type="submit" name="subscribe" id="mc-embedded-subscribe" class="button" value="Subscribe">
		            </div>
		        </div>
		</form>
	</div>
</div>
<br />
<p>Or with <a href="{{ site.baseurl }}/feed.xml"><i class="fa fa-rss"></i> RSS</a></p>

<hr>

<h2>All news</h2>

{% for post in site.posts %}

<h5><small>{{ post.date | date_to_string }}</small><br><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h5>

{% endfor %}

<br><br>





