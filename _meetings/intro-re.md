---
date:   2018-10-21 21:15:00 -0500
layout: meeting
published: false
title:  "Intro to Reverse Engineering"
credit: "Chirag Nanda"
slides: https://drive.google.com/file/d/1gurpqZch4aER_x08tXD3mNOBzNdXa7LG/view
link-to-assets: ""
goal: "Learn about Reverse Engineering and tools used in this process"
how-to-run: [
        "Send an email instructing people to install ida or binary ninja",
        "Run through the slides",
        "Give an example on how these tools are used as well as how binutils like strings, ltrace and strace are used",
        "Instruct and help people to complete the how2re CTF challenge: (http://sigpwny.com/challenges#how2re)",
        "Solve the challenge at the end of the meeting (on the projector)"
]
list-of-topics: [
        "Reverse Engineering is the process of understanding a program's functionality and behavior",
        "Disassemblers are programs that translate machine language into assembly language",
        "Debuggers like gdb detect errors in computer programs",
        "Binutils are programming tools for managing binary programs",
        "Hardware reversing is the process of physically taking apart an engineered product"
        ]
---

{% include single-meeting.html  %}
Reverse Engineering is essential in understanding, debugging and cracking software as well as analyzing malware. To understand the process of reverse engineering, it is important to learn how to use tools like disassemblers, debuggers as well as some basic Unix commands and Misc Binutils like strings, ltrace and strace. This meeting will briefly introduce these tools.
* *Hint for the ctf challenge:* Try running the strings command to gain a better understanding of what the file is. Ltrace will also be useful in this challenge.
