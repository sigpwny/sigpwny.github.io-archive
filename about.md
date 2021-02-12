---
layout: default
title: About
members: [
  {
    name    : "Thomas Quig",
    picture : "https://quig.dev/fs/photos/sunflower-pfp.jpg",
    link    : "https://quig.dev/",
    role    : "President",
    order   : 0,
  },
  {
    name    : "Nicholas S. Husin",
    picture : "https://nicholas.sh/images/profile.jpg",
    link    : "https://nicholas.sh",
    role    : "Officer",
    order   : 1,
  },
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
        SIGPwny is canonically spelled SIGPwny, but some alums might remember it as SIGPony.
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

