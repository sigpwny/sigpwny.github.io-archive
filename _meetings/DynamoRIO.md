---
date:   2019-03-22 03:35:00 -0500
layout: meeting
published: true
title:  "DynamoRIO"
credit: "Joshua Park"
slides: https://drive.google.com/file/d/1qTYClj78ijU9e2R06vbs7ujchqjPsa2y/view
link-to-assets: https://drive.google.com/drive/folders/19vbPQN3U4DShHBiwn2I_1CZ3zuFNaBXs?usp=sharing
goal: "Learn to use DynamoRIO to low-level CTF challenges and analyze binaries"
how-to-run: [
	"Make sure people have access to the vm or have DynamoRIO installed on their local machine.",
	"Go through the basics of how DynamoRIO works and a brief rundown of how to use the API.",
	"Introduce the first challenge and let the members work on them. After about 5-10 minutes or so walk through how to solve the it. Repeat for all the challenges.",
]
list-of-topics: [
	"binary exploitation",
	"reversing"
	]
---

{% include single-meeting.html  %}

This weeks meeting is covering a useful API called DynamoRIO. It's used to manipulate code at runtime and can be helpful for many CTF challenges as well as for analyzing binaries in various instruction architectures including IA-32, AMD64, ARM, and AArch64. Make sure you have access to the VM in order to use the library or download it on your local machine at the [DynamoRIO website](https://www.dynamorio.org/). If decide to download it, try to get `helloworld.c` working with DynamoRIO to make sure it's working.
