---
layout: default
title: About
members: [
  {
    name    : "Nicholas Sebastian Husin",
    picture : "https://nicholas.sh/images/profile.jpg",
    link    : "https://nicholas.sh",
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
        SIGPwny is spelled SIGPwny, but some alums might remember it as SIGPony.
        SIGPwny was originally named SIGMil. SIGMil was founded around 2002, and reborn as SIGPwny around 2011.
      </p>
    </div>
  </div>

  <div class="col panel mt-5">
    <h2 class="my-5 header"> Our Members </h2>
    <hr/>
    <div class="row d-flex justify-content-center">
    {% assign members = page.members | sort: "name" %}
    {% for member in members %}
      <div class="card m-3">
        <a href="{{ member.link }}">
          <div class="member-image">
            <img src="{{ member.picture }}" class="rounded-circle my-3" height="150" width="150"/>
            <h4 class="mx-3">{{ member.name }}</h4>
          </div>
        </a>
      </div>
    {% endfor %}
    </div>
  </div>
</div>
