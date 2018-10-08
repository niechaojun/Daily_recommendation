#coding=utf-8
from selenium import webdriver
import time
import re
import Utf8


def start(username,password):
    _option = webdriver.ChromeOptions()
    _option.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=_option)
    try:
        print 'request url     ',
        browser.get('https://music.163.com/')
        print 'ok'
        time.sleep(1)
    except Exception,e:
        print str(e)
    try:
        print 'get login url     ',
        r1 = re.findall('<li class="lb"><a hidefocus="true" class="itm-2" href="(.*?)" target="_blank" data-action="login" data-type="tencent"><i class="icn icn-qq">',browser.page_source)
        if len(r1)!=0:
            # print r1[0]
            browser.get(r1[0])
            print 'ok'
        else:
            print 'get login url error'
        time.sleep(1)
    except Exception, e:
        print str(e)
    try:
        #切换iframe
        print 'swith iframe     ',
        browser.switch_to_frame('ptlogin_iframe')
        print 'ok'
    except Exception, e:
        print str(e)
    try:
        #点击输入账号密码
        print 'Get ready input Account and Password     ',
        browser.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        print 'ok'
    except Exception, e:
        print str(e)
    try:
        #输入账号
        print 'input Account     ',
        browser.find_element_by_xpath('//*[@id="u"]').send_keys(username)
        print 'ok'
    except Exception, e:
        print str(e)
    try:
        #输入密码
        print 'input password     ',
        browser.find_element_by_xpath('//*[@id="p"]').send_keys(password)
        print 'ok'
    except Exception, e:
        print str(e)
    try:
        #点击确定
        print 'login     ',
        browser.find_element_by_xpath('//*[@id="login_button"]').click()
        print 'ok'
    except Exception, e:
        print str(e)
    # print browser.page_source
    time.sleep(1)
    try:
        print 'transfer     ',
        browser.get('https://music.163.com/')
        print 'ok'
    except Exception, e:
        print str(e)
    time.sleep(1)
    try:
        print 'click Daily recommendation     ',
        browser.switch_to_frame('g_iframe')
        browser.find_element_by_xpath('//*[@id="personalRec"]/ul/li[1]/a/span[3]').click()
        print 'ok'
    except Exception, e:
        print str(e)
    time.sleep(1)
    # print browser.page_source
    try:
        print 'get music     ',
        fp = open('song_sheet.nie','a+')
        fp .write('\n------------------------------------------------------------------------------')
        fp.write('\n'+str(time.asctime(time.localtime(time.time())))+'\r\n')
        musicname = re.findall('<b title="(.*?)">',browser.page_source)
        singer = re.findall('<div class="text" title="(.*?)"><span title=',browser.page_source)
        if len(musicname) == len(singer):
            for i in xrange(0,len(musicname)):
                fp.write(str(musicname[i])+'      ||     ' + str(singer[i]) + '\n')
        fp.close()
        print 'ok'
    except Exception, e:
        print str(e)

if __name__ == '__main__':
    username = ''
    password = ''
    start(username, password)
