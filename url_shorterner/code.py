import pyshorteners
url= "https://xioxosticcreations.tech.blog"
s=pyshorteners.Shortener().tinyurl.short(url)
print(s)