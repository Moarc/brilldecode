#!/usr/bin/python3

import bz2
import bs4
import sys

try:
	f = bz2.open(sys.argv[1])
	f.peek(0)
except:
	f = open(sys.argv[1],mode='rb')
finally:
		soup = bs4.BeautifulSoup(f.read(), "lxml")
		f.close()

for span in soup.findAll('span', {"class": "Ba02"}):
	if span.string != None:
		span.string = span.string.replace("\x21", "!")
		span.string = span.string.replace("\x22", "ʾ")
		span.string = span.string.replace("\x23", "ʿ")
		span.string = span.string.replace("\x24", "Ā")
		span.string = span.string.replace("\x25", "Ă")
		span.string = span.string.replace("\x26", "Ǎ")
		span.string = span.string.replace("\x27", "ḍ")
		span.string = span.string.replace("\x2a", "Å")
		span.string = span.string.replace("\x2b", "Ạ")
		span.string = span.string.replace("\x2d", "Ṣ")
		span.string = span.string.replace("\x2f", "Ḅ")
		span.string = span.string.replace("\x30", "Ḥ")
		span.string = span.string.replace("\x31", "Č")
		span.string = span.string.replace("\x32", "Ć")
		span.string = span.string.replace("\x33", "ʝ")
		span.string = span.string.replace("\x34", "Ḍ")
		span.string = span.string.replace("\x35", "D́")
		span.string = span.string.replace("\x36", "Ē")
		span.string = span.string.replace("\x37", "Ĕ")
		span.string = span.string.replace("\x38", "Ě")
		span.string = span.string.replace("\x39", "ẖ")
		span.string = span.string.replace("\x3c", "Ǝ")
		span.string = span.string.replace("\x3d", "Ḡ")
		span.string = span.string.replace("\x3e", "Ğ")
		span.string = span.string.replace("\x40", "Ǧ")
		span.string = span.string.replace("\x5b", "Ġ")
		span.string = span.string.replace("\x5d", "Ḫ")
		span.string = span.string.replace("\x5e", "Ī")
		span.string = span.string.replace("\x5f", "I̊")
		span.string = span.string.replace("\x60", "İ")
		span.string = span.string.replace("\x7b", "Ķ")
		span.string = span.string.replace("\x7c", "Ḳ")
		span.string = span.string.replace("\x7d", "Ḷ")
		span.string = span.string.replace("\x7e", "Ł")
		span.string = span.string.replace("\x82", "Ṃ")
		span.string = span.string.replace("\x83", "N̄")
		span.string = span.string.replace("\x84", "Ń")
		span.string = span.string.replace("\x85", "Ñ")
		span.string = span.string.replace("\x86", "Ṇ")
		span.string = span.string.replace("\x87", "Ṅ")
		span.string = span.string.replace("\x88", "Ō")
		span.string = span.string.replace("\x89", "Q̇")
		span.string = span.string.replace("\x8b", "Ŕ")
		span.string = span.string.replace("\x8c", "Ṛ")
		span.string = span.string.replace("\x92", "Š")
		span.string = span.string.replace("\x93", "Ś")
		span.string = span.string.replace("\x94", "Ş")
		span.string = span.string.replace("\x95", "Ṭ")
		span.string = span.string.replace("\x96", "T́")
		span.string = span.string.replace("\x97", "Ū")
		span.string = span.string.replace("\x98", "Ú")
		span.string = span.string.replace("\x99", "Ŭ")
		span.string = span.string.replace("\x9b", "Ṿ")
		span.string = span.string.replace("\x9c", "Ẇ")
		span.string = span.string.replace("\x9f", "Ÿ")
		span.string = span.string.replace("\xa1", "Ŷ")
		span.string = span.string.replace("\xa2", "Ż")
		span.string = span.string.replace("\xa3", "Ẓ")
		span.string = span.string.replace("\xa5", "Ž")
		span.string = span.string.replace("\xa7", "ā")
		span.string = span.string.replace("\xa8", "ă")
		span.string = span.string.replace("\xa9", "ǎ")
		span.string = span.string.replace("\xaa", "ã")
		span.string = span.string.replace("\xab", "å")
		span.string = span.string.replace("\xac", "ạ")
		span.string = span.string.replace("\xae", "ạ̄")
		span.string = span.string.replace("\xb0", "ḅ")
		span.string = span.string.replace("\xb1", "ç")
		span.string = span.string.replace("\xb3", "u̱")
		span.string = span.string.replace("\xb4", "č")
		span.string = span.string.replace("\xb5", "ć")
		span.string = span.string.replace("\xb6", "ɔ")
		span.string = span.string.replace("\xb8", "d́")
		span.string = span.string.replace("\xb9", "y̱")
		span.string = span.string.replace("\xba", "ð")
		span.string = span.string.replace("\xbb", "ð̣")
		span.string = span.string.replace("\xbf", "ē")
		span.string = span.string.replace("\xc0", "ĕ")
		span.string = span.string.replace("\xc1", "ě")
		span.string = span.string.replace("\xc2", "ȩ")
		span.string = span.string.replace("\xc3", "ə")
		span.string = span.string.replace("\xc4", "ḡ")
		span.string = span.string.replace("\xc5", "ğ")
		span.string = span.string.replace("\xc6", "ǧ")
		span.string = span.string.replace("\xc7", "ġ")
		span.string = span.string.replace("\xc8", "ḥ")
		span.string = span.string.replace("\xc9", "ḫ")
		span.string = span.string.replace("\xca", "ī")
		span.string = span.string.replace("\xcb", "i̊")
		span.string = span.string.replace("\xcc", "ı")
		span.string = span.string.replace("\xcd", "ķ")
		span.string = span.string.replace("\xce", "ḳ")
		span.string = span.string.replace("\xcf", "ḷ")
		span.string = span.string.replace("\xd1", "ł")
		span.string = span.string.replace("\xd2", "ṃ")
		span.string = span.string.replace("\xd3", "n̄")
		span.string = span.string.replace("\xd4", "ń")
		span.string = span.string.replace("\xd5", "ḵ")
		span.string = span.string.replace("\xd6", "ṇ")
		span.string = span.string.replace("\xd8", "ṅ")
		span.string = span.string.replace("\xd9", "ō")
		span.string = span.string.replace("\xda", "q̇")
		span.string = span.string.replace("\xdb", "ŕ")
		span.string = span.string.replace("\xdc", "ṛ")
		span.string = span.string.replace("\xdf", "ṣ")
		span.string = span.string.replace("\xe0", "š")
		span.string = span.string.replace("\xe1", "ś")
		span.string = span.string.replace("\xe2", "ş")
		span.string = span.string.replace("\xe3", "ṫ")
		span.string = span.string.replace("\xe4", "t́")
		span.string = span.string.replace("\xe5", "ū")
		span.string = span.string.replace("\xe6", "ú")
		span.string = span.string.replace("\xe7", "ŭ")
		span.string = span.string.replace("\xe8", "ṿ")
		span.string = span.string.replace("\xe9", "ẇ")
		span.string = span.string.replace("\xea", "s̱")
		span.string = span.string.replace("\xeb", "ŷ")
		span.string = span.string.replace("\xec", "ž")
		span.string = span.string.replace("\xed", "ẓ")
		span.string = span.string.replace("\xee", "ż")
		span.string = span.string.replace("\xef", "ṯ")
		span.string = span.string.replace("\xf1", "ẕ")
		span.string = span.string.replace("\xf2", "Ḏ")
		span.string = span.string.replace("\xf3", "G̱")
		span.string = span.string.replace("\xf4", "H̱")
		span.string = span.string.replace("\xf5", "J̱")
		span.string = span.string.replace("\xf6", "Ḵ")
		span.string = span.string.replace("\xf7", "S̱")
		span.string = span.string.replace("\xf8", "Ṯ")
		span.string = span.string.replace("\xf9", "ḏ")
		span.string = span.string.replace("\xfa", "Y̱")
		span.string = span.string.replace("\xfb", "Ẕ")
		span.string = span.string.replace("\xfc", "a̱")
		span.string = span.string.replace("\xfd", "č̱")
		span.string = span.string.replace("\xff", "g̱")
print(soup);
out = open(sys.argv[1],"w")
out.write(str(soup))
out.close()