import os

# reads profile.txt
# COMMENTED OUT fetches pfps from internet
# stores in dir
# codegens html and prints it to stdout
# COMMENTED OUT resizes pictures

profiles = open('profile.txt', 'r').readlines()

print("<!-- BEGIN PROFILES -->")
print('''
      <div class="my-5"></div><br>
      <div class="header flicker-9">UIUCTF TEAM</div>
      <div class="gradient my-3"></div>

      <div class="row d-flex justify-content-center">
''')

# ordered by name
for line in sorted(profiles, key=lambda x: x.split(',')[1].lower()):
  title, name, link, picture = map(lambda x : x.strip(), line.split(','))
  curl_output = f'profiles/{name.lower().replace(" ", "_")}{os.path.splitext(picture)[1]}'
  # Surpress stdout cause I want to pipe stdout to clipboard and paste it into index.html
  # os.system(f'wget {picture} -O {curl_output} 1>/dev/null')
  print(f'''
  <div class="card m-2 tooltip-big-text" data-balloon-length="medium" aria-label="{title}" data-balloon-pos="up">
    <a href="{link}">
        <img src="{curl_output}" class="rounded-circle my-3 team-image" height="120" width="120"/>
        <h5 class="mx-3 small-text">{name.replace(" ", "<br/>")}</h5>
    </a>
  </div>''')
print('</div>')
print("<!--   END PROFILES -->")

print("<!-- BEGIN ARTISTS -->")
print('''
<div class="header flicker-9">ART &amp; ASSETS</div>
<div class="gradient my-3"></div>
<div class="row d-flex justify-content-center">

  <!-- pomegranate.boy -->
  <div class="card m-2 tooltip-big-text" data-balloon-length="medium" aria-label="background image for the splash page" data-balloon-pos="up">
    <a href="https://linktr.ee/pomegranate.boy">
        <img src="profiles/pomie.png" class="rounded-circle my-3 team-image" height="120" width="120"/>
        <h5 class="mx-3 small-text">pomegranate.boy</h5>
    </a>
  </div>

  <!-- pluto -->
  <div class="card m-2 tooltip-big-text" data-balloon-length="medium" aria-label="UIUCTF 2021 logo" data-balloon-pos="up">
    <a href="https://www.facebook.com/anastasiya.peskova">
        <img src="profiles/pluto.png" class="rounded-circle my-3 team-image" height="120" width="120"/>
        <h5 class="mx-3 small-text">Pluto</h5>
    </a>
  </div>

  <!-- halfprism -->
  <div class="card m-2 tooltip-big-text" data-balloon-length="medium" aria-label="poster / possible hoodie design" data-balloon-pos="up">
    <a href="https://twitter.com/halfprism_">
        <img src="profiles/halfprism.jpg" class="rounded-circle my-3 team-image" height="120" width="120"/>
        <h5 class="mx-3 small-text">halfprism</h5>
    </a>
  </div>

  <!-- graywalf -->
  <div class="card m-2 tooltip-big-text" data-balloon-length="medium" aria-label="The Best Challenge >:3" data-balloon-pos="up">
    <a href="https://www.youtube.com/c/graywalf">
        <img src="profiles/graywalf.jpg" class="rounded-circle my-3 team-image" height="120" width="120"/>
        <h5 class="mx-3 small-text">GrayWalf</h5>
    </a>
  </div>

''')

print("</div>")
print("<!--   END ARTISTS -->")

# os.system(f'mogrify -resize 250x250 -quality 35 -gravity Center profiles/*')
