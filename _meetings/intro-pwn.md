---
date:   2018-10-21 21:15:00 -0500
layout: meeting
published: false
title:  "Intro to Pwn"
credit: "Josh"
slides: [Slides](https://docs.google.com/presentation/d/1wxCVMbv8TRAgRJKmNtZ6WwpgiQDoZ6MyUDfbSxvw6rE/edit#slide=id.g42d8f497e0_16_0)
link-to-assets-in-github: ""
goal: "Learn to find and exploit vulnerabilities in programs"
how-to-run: [
	"Instruct members to download and get familiar with [gdb](https://www.gnu.org/software/gdb/) and [Binary Ninja](https://binary.ninja/). [Pwntools](https://github.com/Gallopsled/pwntools) is also recommended",
	"Go through the provided slides, explaining the major concepts as you go",
	"Instruct members to solve the [bof CTF challenge](http://sigpwny.com/challenges#bof)",
  "Towards the end of the meeting, step through how to solve the challenge"
]
list-of-topics: [
	"Finding and exploiting vulnerabilities in software programs",
	"Using tools such as gdb and Binary Ninja to break down programs",
  "How memory is allocated and stored using stack and heap memory"
	]
---
{% include single-meeting.html  %}

Binary exploitation can be intimidating, but the meeting will be walking through a pwn challenge from SigPwny's introductory CTF that will introduce new members to the concepts and tools they need to get started. The challenge involves exploiting a buffer overflow, which is one of the most common kinds of vulnerabilities. Depending on a member's experience level, some may struggle with the challenge more than others. Walk around the room and try to help those who seem to be struggling.
