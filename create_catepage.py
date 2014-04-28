#-*- coding:utf-8-*-
import os
import sys
import datahelper
from create_webpage import page_template

cate_page = 'category.html'
star_pie = 'star_pie.js'
webdir = 'webpages'
varpage = 'variables.js'
avgstar_hist = 'avgstar_hist.js'
rev_count_hist = 'rev_count_hist.js'


def init(category):
	'''init category hompage'''

	pwebdir = os.path.join(webdir,category)
	if not os.path.exists(pwebdir):
		os.makedirs(pwebdir)
	homepage = os.path.join(pwebdir,cate_page)
	varpg = os.path.join(pwebdir,varpage)
	if os.path.isfile(homepage):
		os.remove(homepage)
	if os.path.isfile(varpg):
		os.remove(varpg)
	try:
		open(homepage, 'wb').write(open(page_template(cate_page),'rb').read())
		vfile = open(varpg,'wb')
		vfile.write('cate_name = %s' % category)
		vfile.write(open(page_template(varpage),'rb').read())
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

	pwebdir = os.path.join(webdir,category)
	if not os.path.exists(pwebdir):
		os.makedirs(pwebdir)
	pstar_pie = os.path.join(pwebdir,star_pie)
	if os.path.isfile(pstar_pie):
		os.remove(pstar_pie)
	try:
		piefile = open(pstar_pie,'wb')
		piefile.write('var rate = %s \n' % str(star_num))
		piefile.write(open(page_template(star_pie),'rb').read())
		piefile.close()
	except IOError:
		raise

def draw_avgstar_revNo_hist(cate_data,category):
	'''intput data to avgstar hist template'''
	infoli = datahelper.get_revNo_avgstar(cate_data)
	asin_list = []
	rev_count_list = []
	avgstar_list = []
	for item in infoli:
		asin_list.append(str(item['ASIN']))
		rev_count_list.append(item['review_count'])
		avgstar_list.append(float(item['avg_star']))

	pwebdir = os.path.join(webdir,category)
	pavgstar_hist = os.path.join(pwebdir,avgstar_hist)
	prevNo_hist = os.path.join(pwebdir,rev_count_hist)

	if not os.path.exists(pwebdir):
		os.makedirs(pwebdir)
	if os.path.isfile(pavgstar_hist):
		os.remove(pavgstar_hist)
	if os.path.isfile(prevNo_hist):
		os.remove(prevNo_hist)

	try:
		avgfile = open(pavgstar_hist,'wb')
		refile = open(prevNo_hist,'wb')

		avgfile.write('var asin_list = %s \n\
					   var avgstar_list = %s \n' \
					   % (str(asin_list),str(avgstar_list)))
		refile.write('var asin_list = %s \n\
					  var rev_count_list = %s\n' \
					  % (str(asin_list),str(rev_count_list)))

		avgfile.write(open(page_template(avgstar_hist),'rb').read())
		refile.write(open(page_template(rev_count_hist),'rb').read())

		avgfile.close()
		refile.close()
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
		draw_avgstar_revNo_hist(cate_data,sys.argv[1])
	else:
		print 'no any data'
