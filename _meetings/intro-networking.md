---
date:   2018-12-6 21:15:00 -0500
layout: meeting
published: true
title:  "Intro to Networking"
credit: "Isaac Warren"
slides: https://docs.google.com/presentation/d/1cuQ4Im_6wZsEFV0ayru_7Djxenv7MgOFh7Db6toDFaM/edit#slide=id.p
link-to-assets: ""
goal: "Introduce members to TCP/UDP and tools to solve networking CTF challenges."
how-to-run: [
	"Presenter runs through the slides and solves the exercise themselves."
]
list-of-topics: [
	"TCP Handshake - TODO (syn synack ack starts a tcp session)",
	"TCP vs UDP - TODO explain the differences in about a line",
	"Netcat aka nc - an incredibly useful command tool for connecting to CTF challenges",
	"Wireshark - a GUI tool for analyzing network traffic on a packet level"
	]
---

{% include single-meeting.html  %}

Come learn how computers communicate, how these messages can be monitored and how they can be spoofed. We will primarily be covering the tcp stack and will have activities that require analysis and forging of packets using Wireshark and Scapy. TODO: link to https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Connection_establishment and say something like "TCP is this. the TCP handshake is this. it accomplishes this. more details at <wiki link>".
