# -*- coding: UTF-8 -*-
from search_crawler import write_to_csv

exp_shopping_websites = [
	'https://www.yargici.com/',
	'https://www.beymen.com/',
	'https://www.altinyildizclassics.com/',
	'https://global.tommy.com/tr/tr/Collections/start',
	'http://shop.vakko.com/tr',
	'http://www.hotic.com.tr',
	'http://www.ipekyol.com',
	'http://shop.sarar.com',
	'http://www.mudo.com.tr/instashop',
	'http://www.kigili.com',
	'http://www.faiksonmez.com',
	'http://www.bpoint.com.tr/',
	'https://www.lanvin.com/tr/',
	'https://row.jimmychoo.com/tr/home',
	'https://www.ysl.com/tr',
	'https://www.sephora.com.tr',
	'https://www.esteelauder.com.tr',
	'https://www.kiehls.com.tr',
	'https://www.loccitane.com.tr',
	'https://www.balenciaga.com/tr/women/small-leather-goods',
	'https://www.cremedelamer.com/stores',
	'https://www.silkandcashmere.com',
#	'https://www.michaelkors.global/en_TR/women/_/N-hu9v1z',
	'https://www.hugoboss.com/tr/boss/',
	'https://www.roman.com.tr/tasarim-elbise',
	'https://www.beforetrend.com/',
	'https://www.vakkorama.com.tr/kadin-elbise',
	'https://kkdesignn.com/koleksiyon.aspx?kid=16&category/Ust-Giyim',
	'https://zeyneptosun.com/shop/?currency=EUR'
]

cheap_shopping_sites = [
	'https://www.morhipo.com/boyner-outlet',
	'https://www.trendyol.com/',
	'https://www.lcwaikiki.com/tr-TR/TR/dt/indirimli-urunler-kadin',
	'https://www.defacto.com.tr/kadin-indirimli-urunler',
	'https://www.tchibo.com.tr',
	'https://www.koton.com',
	'https://www.n11.com',
	'https://www.gittigidiyor.com/',
	'https://www2.hm.com/tr_tr/index.html',
	'https://www.tozlu.com/TR/kadin',
	'https://www.btmmoda.com',
	'https://www.mistoptan.com/indirim/',
	'https://www.hopi.com.tr',
	'https://www.kuponrazzi.com/',
	'https://indirimkuponum.net/',
	'https://www.picodi.com/tr/',
	'https://indirimkodu.com/',
	'http://www.ucuzabilet.com',
	'https://www.kidsmodasi.com/index.php?route=information/contact',
	'https://www.migros.com.tr',
	'https://www.rossmann.com.tr',
	'https://www.gratis.com',
	'https://www.buyukzavotlar.com',
	'https://tr.uspoloassn.com/firsat-urunleri-17-04/',
	'https://www.modanisa.com',
	'https://www.watsons.com.tr',
	'https://www.patirti.com',
	'https://www.byedz.com',
	'https://www.instagram.com/p/BzBllF7p8Pl/?igshid=zuagaeeucofz',
	'https://www.instagram.com/p/BzBJX9HHGVw/?igshid=5x3tft9uacuj',
	'https://www.instagram.com/p/BzBeH74nQgu/?igshid=1ak6pa599nrwf',
	'https://www.instagram.com/p/BzAT0pEHzXH/?igshid=1uvdy7karo97m',
	'https://www.instagram.com/p/BzA_QjFgCwH/?igshid=1wjy7m5cv03xr',
	'https://www.instagram.com/p/BzBHYM9hs_w/?igshid=z1wun23do3js',
	'https://www.instagram.com/antreexport/',
#	'https://www.adidas.com.tr/tr/kadin-outlet',
#	'https://www.newbalance.com.tr',
	'https://www.boyner.com.tr/',
	'https://www.nike.com/tr/',
	'https://www.kamilkoc.com.tr/otobus-bileti',
	'https://www.bilet.com/otobus-bileti'
] 

#generating google search queries: each query = adjective + name
adj_cheap = ['ucuz', 'indirimli',  'kampanyalı', 'fırsat', 'sezon+sonu', 
			'sezon+ortası', 'çılgın', 'uygun+fiyatlar', 'çılgın+indirim', 
			'promosyon', 'yüzde+elliye+varan', 'lcw', 'lcw+com']
adj_neutral = ['bayan', 'erkek', 'çocuk', 'kız', 'bebek', 'yazlık', 'bay', 
				'kadın']
adj_expensive = ['tasarım', 'lüks', 'couture', 'elit', 'tasarım', 'kişiye+özel', 
					'vintage']
names = ['ayakkabı', 'tişört', 'giyim', 'sandalet', 'etek', 'şort', 'pantolon', 
			'bluz', 'takım+elbise', 'abiye+elbise', 'topuklu+ayakkabı', 
			'sırt+çantası', 'okul+çantası', 'çanta', 'spor+ayakkabı', 'takı', 
			'saat', 'aksesuar', 'eşofman', 'uçak+bileti', 'otobüs+bileti', 
			'bilet', 'araba+kirala']
'''
	query_type :=
	C : Cheap
	E : Expensive
	N : Neutral

	user_type :=
	T : Test
	C : Cheap
	E : Expensive
'''
num_outer_iter = 3
num_inner_iter = 3
for x in range(1, num_outer_iter):
	print('Outer iteration', x, 'of', num_outer_iter)
	user_agent = iphone[1] #Apple iPhone XR (Safari)
	print('user-agent:', user_agent)
	write_to_csv(adj_cheap, names, cheap_shopping_sites, num_inner_iter, 
					user_agent, 'C', 'C', 'Mobile', 'iOS')
	write_to_csv(adj_neutral, names, cheap_shopping_sites, num_inner_iter, 
					user_agent, 'N', 'C', 'Mobile', 'iOS')
	write_to_csv(adj_expensive, names, exp_shopping_websites, num_inner_iter, 
					user_agent, 'E', 'E', 'Mobile', 'iOS')
	write_to_csv(adj_expensive, names, cheap_shopping_sites, num_inner_iter,
					user_agent, 'E', 'C', 'Mobile', 'iOS')
	write_to_csv(adj_cheap, names, exp_shopping_websites, num_inner_iter, 
					user_agent, 'C', 'E', 'Mobile', 'iOS')
	write_to_csv(adj_neutral, names, exp_shopping_websites, num_inner_iter, 
					user_agent, 'N', 'E', 'Mobile', 'iOS')
	print("\n\n")
