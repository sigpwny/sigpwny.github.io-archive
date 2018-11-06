---
date: 2018-11-05 20:00:00 -0500
layout: meeting
published: true
title:  "Intro to Pwn"
credit: "Josh"
slides: https://docs.google.com/presentation/d/1wxCVMbv8TRAgRJKmNtZ6WwpgiQDoZ6MyUDfbSxvw6rE/edit#slide=id.g42d8f497e0_16_0)
link-to-assets: ""
goal: "Learn about the pwn CTF category: finding and exploiting
vulnerabilities in programs running on remote servers."
how-to-run: [
	"Instruct members to download and get familiar with gdb and Binary
	Ninja. Pwntools is also recommended.",
	"Go through the provided slides, explaining the major concepts as you go.",
	"Instruct members to solve the bof CTF challenge.",
  "Towards the end of the meeting, step through how to solve the challenge."
]
list-of-topics: [
	"Finding and exploiting vulnerabilities in software programs",
	"Using tools such as gdb and Binary Ninja to disassemble programs",
  "How memory is allocated and stored using stack and heap memory"
	]
---
{% include single-meeting.html  %}

Binary exploitation can be intimidating, but the meeting will be walking through a pwn challenge from [pwnable.kr](http://pwnable.kr/play.php) that will introduce new members to the concepts and tools they need to get started. The challenge involves exploiting a buffer overflow, which is one of the most common kinds of vulnerabilities. Depending on a member's experience level, some may struggle with the challenge more than others. Walk around the room and try to help those who seem to be struggling.
