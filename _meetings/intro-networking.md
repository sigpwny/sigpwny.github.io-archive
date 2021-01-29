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
	"TCP Handshake - A TCP connection is started through a three-way handshake of packets: SYN SYNACK ACK.",
	"TCP vs UDP - TCP is reliable and ordered. UDP is less reliable but faster.",
	"Netcat aka nc - An incredibly useful command tool for connecting to CTF challenges.",
	"Wireshark - A GUI tool for analyzing network traffic on a packet level."
	]
---


Come learn how computers communicate, how these messages can be monitored and how they can be spoofed. We will primarily be covering the tcp stack and will have activities that require analysis and forging of packets using Wireshark and Scapy. "TCP is a networking protocol that is one of the main internet protocols. It is reliable, ordered, and error-checking. A TCP connection is started through a three-way handshake: client sends SYN to server, server sends SYNACK to client, client sends ACK to server, and the TCP session is started. At this point, there's a reliable, not-lossy connection that you can send data over. More details can be found [on Wikipedia](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Connection_establishment).
