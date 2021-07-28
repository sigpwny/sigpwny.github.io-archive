import os

# reads profile.txt
# COMMENTED OUT fetches pfps from internet
# stores in dir
# codegens html and prints it to stdout
# COMMENTED OUT resizes pictures

profiles = open('profile.txt', 'r').readlines()

for line in sorted(profiles, key=lambda x: x.split(',')[1].lower()):
  title, name, link, picture = map(lambda x : x.strip(), line.split(','))
  curl_output = f'profiles/{name.lower().replace(" ", "_")}{os.path.splitext(picture)[1]}'
  # Surpress stdout cause I want to pipe stdout to clipboard and paste it into index.html
  # os.system(f'wget {picture} -O {curl_output} 1>/dev/null')
  print("<!-- BEGIN PROFILES -->")
  print(f'''
  <!-- BEGIN PROFILES -->
  <div class="card m-2 tooltip-big-text" data-balloon-length="medium" aria-label="{title}" data-balloon-pos="up">
    <a href="{link}">
        <img src="{curl_output}" class="rounded-circle my-3 team-image" height="120" width="120"/>
        <h5 class="mx-3 small-text">{name.replace(" ", "<br/>")}</h5>
    </a>
  </div>''')
  print("<!--   END PROFILES -->")

# os.system(f'mogrify -resize 250x250 -quality 35 -gravity Center profiles/*')
