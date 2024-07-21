def extract_image_links(html):
    links = []
    index_img = 0
    html = html.replace('>', '')
    list_img = html.split('<img ')
    for img in list_img:
        if '.jpg' in img or '.png' in img or '.gif' in img or '.jpeg' in img:
            first_apost = img.index("'")
            second_apost = img.rindex("'")
            links.append(img[first_apost+1:second_apost])

    return links



sample_html = "<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> <img src='https://example.com/image3.gif'>"
image_links = extract_image_links(sample_html)
if image_links:
  for image_link in image_links:
    print(image_link)
else:
  print("Нет ссылок с картинками в HTML тексте.")