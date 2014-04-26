import os
import sys
import datahelper

index_template = 'webpage_template/index.html'
star_hist_template = 'webpage_template/star_hist.js'
index = 'index.html'
star_hist = 'star_hist.js'
webdir = 'webpages'

def init(asin):
	'''init homepage'''

	pwebdir = os.path.join(webdir,asin)
	if not os.path.exists(pwebdir):
		os.makedirs(pwebdir)
	homepage = os.path.join(pwebdir,index)
	if os.path.isfile(homepage):
		os.remove(homepage)
	try:
		open(homepage, 'wb').write(open(index_template,'rb').read())
	except IOError:
		raise

def draw_star_hist(product_data):
	'''input data to star hist template'''
	asin = product_data['ASIN']
	star_list = datahelper.get_star_list(product_data)
	star_sum = [0,0,0,0,0]
	for star in star_list:
		if star == 5: star_sum[0]+=1
		elif star == 4: star_sum[1]+=1
		elif star == 3: star_sum[2]+=1
		elif star == 2: star_sum[3]+=1
		elif star == 1: star_sum[4]+=1
		else: pass
	pwebdir = os.path.join(webdir,asin)
	if not os.path.exists(pwebdir):
		os.makedirs(pwebdir)
	pstar_hist = os.path.join(pwebdir,star_hist)
	if os.path.isfile(pstar_hist):
		os.remove(pstar_hist)
	try:
		histfile = open(pstar_hist,'wb')
		histfile.write('var star_list = %s \n' % str(star_sum))
		histfile.write(open(star_hist_template,'rb').read())
		histfile.close()
	except IOError:
		raise



if __name__ == '__main__':
	if len(sys.argv) <= 1:
		sys.argv.append('B003FGWY1O')
	product_data = datahelper.get_product_data(sys.argv[1])
	if product_data:
		init(sys.argv[1])
		draw_star_hist(product_data)
	else:
		print 'no any data'