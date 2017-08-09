#-*- coding:utf-8 -*-

"""
国义招标网
"""

import re
import urllib
from urllib import request
from bs4 import BeautifulSoup
import xlwt
from selenium import webdriver
from bs4 import BeautifulSoup

class Programme_guoyi():
	
	def get_Web_guoyi(url):
		"""
		打开国义招标网并进行关键词搜索
		返回网站
		无UI浏览器访问
		"""
		driver = webdriver.PhantomJS()
		driver.set_window_size(800,600)
		# driver.set_page_load_timeout(30)
		# driver.set_script_timeout(30)
		driver.get(url)
		driver.find_element_by_link_text(u"招标公告").click()
		driver.find_element_by_name("Keyword").clear()
		driver.find_element_by_name("Keyword").send_keys(u"医院")
		driver.find_element_by_css_selector("a > img").click()

		return driver
		driver.quite()

	def get_newWeb_guoyi(url):
		driver = webdriver.PhantomJS()
		driver.set_window_size(800,600)
		driver.get(url)

		return driver

	def get_newpageWeb_guoyi(url):
		driver = webdriver.PhantomJS()
		driver.set_window_size(800,600)
		driver.get(url)
		iframe = driver.find_element_by_xpath("iframe")
		driver.switch_to_frame(iframe)
		# driver.switch_to_default_content()

		return driver
		driver.quite()

	def get_programme_guoyi(info):
		"""doc.
   		寻找招标项目链接及名称方法
    	返回链接(数组形式)
		"""
		soup = BeautifulSoup(info.page_source)

		website = soup.find_all(href=re.compile("snid"))

		weblist=[]

		for web in website:
			gotoweb = web['href']

			weblist.append(gotoweb)

		return weblist

	def get_title_guoyi(soup):
		"""
		获取项目名称的方法
		返回项目名称
		"""
		soup_name = soup.find('span', id="ctl00_PageContent_Label_Title")
		title = soup_name.get_text()

		return title
	def get_beginningtime_guoyi(soup):
		"""
		获取公布时间的方法
		返回公布时间
		"""
		soup_beginningtime = soup.find('span', id="ctl00_PageContent_Label_ShowDate")
		beginningtime = soup_beginningtime.get_text()

		return beginningtime

	def get_number_guoyi(soup):
		"""
		获取项目编号的方法
		返回项目编号
		"""
		soup_number = soup.find('span', id="ctl00_PageContent_Label_Code")
		number = soup_number.get_text()

		return number

	def get_account_guoyi(soup):
		pass

	def get_showtime_guoyi(soup):
		pass


	def get_detail_guoyi(WBall,filename,state1,state2,state3,state4,state5,state6,state7,satet8):
		"""
		对项目内容进行细化操作
		返回
		"""
		wbk = xlwt.Workbook()
		sheet = wbk.add_sheet('sheet 1',cell_overwrite_ok=True)
		sheet.write(0,0,"招标公告日期")
		sheet.write(0,1,"链接")
		sheet.write(0,2,"地区")
		sheet.write(0,3,"招标机构")
		sheet.write(0,4,"采购单位")
		sheet.write(0,5,"项目名称")
		sheet.write(0,6,"采购内容")
		sheet.write(0,7,"开标日期")
		sheet.write(0,8,"中标公告时间")
		sheet.write(0,9,"中标公司")
		sheet.write(0,10,"总金额")
		sheet.write(0,11,"中标金额")
		sheet.write(0,12,"预算（元）")
		sheet.write(0,13,"中标公告链接")

		i = 1

		for web in WBall:
			html = get_newWeb('http://www.gmgit.com/Notice/BidInfo/' + web)

			soup = BeautifulSoup(html.page_source)

			message_list = []

			soup_message = soup.find('span', id="ctl00_PageContent_Label_Content")

			if soup_message is None:
				new_content = soup.find(src=re.compile("HtmShow"))
				content_web = new_content['src']
				new_page = 'http://www.gmgit.com/Notice/BidInfo/' + content_web

				soupother = BeautifulSoup(get_newWeb(new_page).page_source)
				newsoup_message = soupother.find('div', class_="Section1")

				for mes1 in newsoup_message.stripped_strings:
					message_list.append(mes1)
			else:
				for mes2 in soup_message.stripped_strings:
					message_list.append(mes2)
					"""将内容分块保存至数组"""

			if satet1 is True:
				sheet.write(i,0,get_beginningtime_guoyi(soup))
			else:
				None

			if state2 is True:
				sheet.write(i,1,"http://www.gmgit.com/Notice/BidInfo/" + web)
			else:
				None

			if state3 is True:	
				sheet.write(i,3,None)
			else:
				None

			if state4 is True:	
				sheet.write(i,4,None)
			else:
				None

			if state5 is True:
				sheet.write(i,5,get_title_guoyi(soup))
			else:
				None

			if state6 is True:
				sheet.write(i,6,None)
			else:
				None

			if state7 is True:
				sheet.write(i,7,get_showtime_guoyi(soup))
			else:
				None

			if state8 is True:
				sheet.write(i,12,get_account_guoyi(soup))

				
			i +=1

		print("sucess")

		wbk.save(filename)

	# get_detail_guoyi(get_programme_guoyi(get_Web_guoyi(url)))	
