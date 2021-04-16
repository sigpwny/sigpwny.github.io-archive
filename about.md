---
layout: default
title: About
members: [
  {
    name    : "Thomas",
    picture : "https://quig.dev/cdn/photos/glitch-crop.gif",
    link    : "https://quig.dev/",
    role    : "President (Current)",
    order   : 0,
    current    : True,
  },
  {
    name    : "Nicholas",
    picture : "https://nicholas.sh/images/profile.jpg",
    link    : "https://nicholas.sh",
    role    : "Officer",
    order   : 1,
    current    : True,
  },
  {
    name    : "ravi",
    picture : "https://avatars.githubusercontent.com/u/36464332",
    link    : "https://github.com/jprx",
    role    : "Former President (2019-2020)",
    order   : 2,
    current    : False,
  },
  {
    name    : "kuilin",
    picture : "https://kuilin.net/profile_upscaled.png",
    link    : "https://kuilin.net",
    role    : "Officer",
    order   : 3,
    current    : False,
  },
  {
    name    : "Husnain",
    picture : "https://klatz.co/images/arrow.png",
    link    : "https://github.com/epistemologist",
    role    : "Officer",
    order   : 4,
    current    : True,
  },
  {
    name    : "Ian",
    picture : "https://klatz.co/images/arrow.png",
    link    : "https://klatz.co",
    role    : "Former President (2017-2018)",
    order   : 5,
    current    : False,
  }
  
]
---

<div class="container mb-5">
  <div class="row">
    <div class="col panel mt-5">
      <div class="embedded-image">
        <img src="{{ site.baseurl }}/images/logo.png" class="rounded" height="350" width="300"/>
      </div>

      <br>
      <hr/>

      <p>
        SIGPwny is canonically spelled SIGPwny, but some currents might remember it as SIGPony.
        The club was originally named SIGMil, which was founded around
		2002, and reborn as SIGPwny around 2011.
      </p>
    </div>
  </div>

  <div class="col panel mt-5">
    <h2 class="my-5 header"> Our Members </h2>
    <hr/>
    <div class="row d-flex justify-content-center">
    {% assign groups = page.members | group_by: "order" | sort: "name" %}
    {% for group in groups %}
      {% assign members = group.items | sort: "name" %}
      {% for member in members %}
        <div class="card m-3">
          <a href="{{ member.link }}">
            <div class="member-image">
              <img src="{{ member.picture }}" class="rounded-circle my-3" height="150" width="150"/>
              <h4 class="mx-3">{{ member.name }}</h4>
              <p class="mx-3">{{ member.role }}</p>
            </div>
          </a>
        </div>
      {% endfor %}
    {% endfor %}
    </div>
  </div>
</div>

