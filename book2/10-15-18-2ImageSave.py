import requests

img_url = "http://dimik.pub/wp-content/uploads/2017/09/LPIP-part2-cover-med-min.jpg"# "https://goo.gl/JxktPw" python  book image
r = requests.get(img_url)
with open ("pybook2.png", "wb") as f:
    f.write(r.content)

