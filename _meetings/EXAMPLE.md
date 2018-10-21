---
date:   2018-10-12 15:45:50 -0500
layout: meeting
published: true
title:  "Example"
slides: link-to-google-docs
link-to-assets-in-github: "should be a link to the folder in the github
repo"
list-of-topics: [reversing,pwn]
---

<p>{{ page.slides }}</p>

<h4>Topics Covered</h4>
<!-- TODO: trevor: make these render not like dogshit (lists should be
moved to the right slightly) -->
<div>
	<ul>
		{% for topic in page.list-of-topics %}
		<li>{{ topic }}<li>
		{% endfor %}
	</ul>
</div>
