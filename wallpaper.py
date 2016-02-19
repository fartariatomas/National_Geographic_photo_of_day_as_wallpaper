#!/usr/bin/env python
import requests as rq
import datetime
import gconf
import os

def find_NatGeo_img_url():
	photo_site = "http://photography.nationalgeographic.com/photography/photo-of-the-day/"
	r = rq.get(photo_site)
	first = r.text.find("images.nationalgeographic.com/wpf/media-live/photos")
	imgLink = r.text[first:first + 300]  # + 300 to be sure to include the whole link
	end = imgLink.find(".jpg") + 4  # +4 to account for .jpg letters
	del r
	return str("http://" + imgLink[:end])


def download_img(imgLink):
	file_name = "/home/tomas/Pictures/" + str(datetime.datetime.now().date()) + ".jpg"
	r2 = rq.get(imgLink)
	if r2.status_code == 200:
	    with open(file_name, 'wb') as f:
	        #r2.raw.decode_content = True
	        #shutil.copyfileobj(r2.raw, f)
	        f.write(r2.content)
	del r2
	print("image saved")
	return file_name

def set_img_as_wallpaper(img_path):
	os.system('gsettings set org.gnome.desktop.background picture-uri file://' + img_path)
	print("wallpaper set")

def main():
	imgLink = find_NatGeo_img_url()
	img_path = download_img(imgLink)
	set_img_as_wallpaper(img_path)


if __name__ == "__main__":
    main()