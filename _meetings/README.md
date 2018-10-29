# meetings
All meetings have 15m presentations, followed by an activity. We want to
wrap these up in a packaged format so we can publish them, get cred for the
club, and reuse them in future years.

Your task is to copy a template and fill it with content, then send it to
the website admin. You can also preview how it'll look on the website
locally.

---

**Please download [this
template](https://raw.githubusercontent.com/sigpwny/sigpwny.github.io/master/_meetings/EXAMPLE.md)
and fill it out. Explanation of the fields below. It will eventually look
like [this example currently live on the
website](https://sigpwny.github.io/meetings/intro-mtg).** 
```
---
date:   2018-10-21 21:15:00 -0500
layout: meeting
published: true
title:  "Example"
slides: link-to-google-docs
link-to-assets-in-github: ""
goal: "Demonstrate an example."
how-to-run: [
	"As concisely as possible, how to run this meeting.",
	"If you're unsure, ask Ian and/or the person who ran it.",
	"Don't forget to drop a comma after each line.",
]
list-of-topics: [
	"reversing",
	"pwn"
	]
---

{% include single-meeting.html  %}

Description goes here! Any additional information.
AKA "how to run this meeting again in the future."

You have [full markdown formatting](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) here, please use it!
```

* Markdown file formatted with a markdown header.
	* **title**: 
	* **slides**: \<link to slides hosted on Google Docs\>
	* **link-to-assets-in-github**:
		* Optional; leave as `""` if you have none.
		* Get access to this repository. 
		* Create a folder titled after the meeting you are boxing.
		* Add the files needed for this meeting. Try to avoid stuff in
		excess of 10mb (host it elsewhere).
	* **goal**: Goal of the meeting, as concisely as possible.
	* **how-to-run**: leave `""` if there are none. Try to clearly and concisely summarize what needs to be done to run this meeting. Usually going to be "presenter runs through the slides and solves the exercise themselves."
	* **list-of-topics**: Summarize the slides into the major bullet points.
	Try to keep it to three. Everything in the list must be quoted.
	* **Content Section**:
		* Expand on the goal, deploy instructions, topics, or offer
		teaching instructions.
		* Most importantly, offer instructions 
* Once you complete this file, send it to the
	website admin, currently @Flyrom / Trevor.

#### (Optional) See the fruits of your labor (preview the thing you're creating)
* Install Jekyll (& ruby)
* `git clone github.com/sigpwny/sigpwny.github.io`
* `cd sigpwny.github.io`
* Move your markdown file into `_meetings`
* `jekyll serve`
* open localhost:4000 in your web browser

---

#### Meetings come in one of five formats
Get all files from the presenter.

They'll have **additional** components depending on the meeting type.
 * pwn - libc.so.X (where X is a number, usu. 6), LD_PRELOAD command
 * reversing - nothing
 * crypto - 
 * web - Dockerfile

---

### Jekyll Details (don't read unless you're website admin)

* New packaged meetings (`meeting_name.md`) go into `_meetings` dir, copy
`EXAMPLE.md` and set jekyll front matter appropriately
* meeting formatting is handled by `_includes/single-meeting.html`
* Use `layout: meeting`. Meetings use a [jekyll layout](https://jekyllrb.com/docs/layouts/).
* meetings are a jekyll
"[collection](https://jekyllrb.com/docs/collections/)", if you need more
info about how they actually work / need to do design work.
