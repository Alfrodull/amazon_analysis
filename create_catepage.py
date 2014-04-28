#-*- coding:utf-8-*-
import os
import sys
import datahelper
from create_webpage import page_template

cate_page = 'category.html'
star_pie = 'star_pie.js'
webdir = 'webpages'

def init(category):
	'''init category hompage'''

	pwebdir = os.path.join(webdir,category)
	if not os.path.exists(pwebdir):
		os.makedirs(pwebdir)
	homepage = os.path.join(pwebdir,cate_page)
	if os.path.isfile(homepage):
		os.remove(homepage)
	try:
		open(homepage, 'wb').write(open(page_template(cate_page),'rb').read())
	except IOError:
		raise

def draw_star_pie(cate_data,category):
	'''intput data to star pie template'''
	star_info_li = datahelper.get_cate_star(cate_data)
	star_num = [0,0,0,0,0]
	for item in star_info_li:
		star_num[0] += item['5']
		star_num[1] += item['4']
		star_num[2] += item['3']
		star_num[3] += item['2']
		star_num[4] += item['1']
	sum = star_num[0] + star_num[1] + star_num[2] + star_num[3] + star_num[4]
	rate = []
	for num in star_num:
		rate.append(float('%.1f'% (num*1.0/sum*100.0)))

	pwebdir = os.path.join(webdir,category)
	if not os.path.exists(pwebdir):
		os.makedirs(pwebdir)
	pstar_pie = os.path.join(pwebdir,star_pie)
	if os.path.isfile(pstar_pie):
		os.remove(pstar_pie)
	try:
		piefile = open(pstar_pie,'wb')
		piefile.write('var rate = %s \n' % str(rate))
		piefile.write(open(page_template(star_pie),'rb').read())
		piefile.close()
	except IOError:
		raise

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		default_cate = 'Home & Kitchen>Furniture>Home Office Furniture'
		sys.argv.append(default_cate)
		sys.argv.append('1')
	elif len(sys.argv) <= 2:
		sys.argv.append('1')
	cate_data = datahelper.get_category(sys.argv[1],sys.argv[2])
	if cate_data:
		init(sys.argv[1])
		draw_star_pie(cate_data,sys.argv[1])
	else:
		print 'no any data'
