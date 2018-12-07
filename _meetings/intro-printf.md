---
date:   2018-10-21 21:15:00 -0500
layout: meeting
published: true
title:  "Printf Meeting"
credit: "Joseph Ravichandran"
slides: https://docs.google.com/presentation/d/1WO3gKaJcloAdKZSHb9uZVnc08eAD4zA-jIO9U-i_ptM/edit?usp=sharing
link-to-assets: ""
goal: "Learn the basics of exploiting format string attacks"
how-to-run: [
	"This concept is best explained with first explaining a little, and then introducing a challenge",
	"First talk about how printf works, then give a simple challenge, then introduce more advanced concepts, etc.",
	"The challenges should begin with simply using %s to print a string, then using %x a few times to see the stack, then $n%x to print a specific offset, and finally using %n to overwrite information.",
]
list-of-topics: [
	"reversing",
	"pwn"
	]
---

{% include single-meeting.html  %}

This week's meeting will be covering format string vulnerabilities in the C printf function. If a program allows you to specify a format string argument to a printf call, you can do all sorts of stuff, from redirecting program flow to overwritting arbitrary memory locations!
