---
layout: page
title: Meetings
---

#### We package our meetings for re-usability. Hopefully, others can learn from them too!

{% assign meetings = site.meetings | sort: "date" %}
{% for meeting in meetings reversed %}
{% if meeting.published %}
- #### [{{ meeting.title }}]({{ site.baseurl }}{{ meeting.url }})
{% endif %}
{% endfor %}
