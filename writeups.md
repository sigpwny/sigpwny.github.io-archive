---
layout: page
title: Writeups
---

{% for competition in site.writeups %}
  [{{ competition.title }}]({{ competition.url }})
{% endfor %}