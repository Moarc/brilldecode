#!/usr/bin/python3

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

# SPDX-License-Identifier: GPL-3.0-or-later

import bz2
import bs4
import re
import sys

brillcode = {
		"\x21": "!",
		"\x22": "’",
		"\x23": "ʿ",
		"\x24": "Ā",
		"\x25": "Ă",
		"\x26": "Ǎ",
		"\x27": "ḍ",
		"\x2a": "Å",
		"\x2b": "Ạ",
		"\x2d": "Ṣ",
		"\x2f": "Ḅ",
		"\x30": "Ḥ",
		"\x31": "Č",
		"\x32": "Ć",
		"\x33": "j̲",
		"\x34": "Ḍ",
		"\x35": "D́",
		"\x36": "Ē",
		"\x37": "Ĕ",
		"\x38": "Ě",
		"\x39": "h̲",
		"\x3c": "Ǝ",
		"\x3d": "Ḡ",
		"\x3e": "Ğ",
		"\x40": "Ǧ",
		"\x5b": "Ġ",
		"\x5d": "Ḫ",
		"\x5e": "Ī",
		"\x5f": "I̊",
		"\x60": "İ",
		"\x7b": "Ķ",
		"\x7c": "Ḳ",
		"\x7d": "Ḷ",
		"\x7e": "Ł",
		"\x82": "Ṃ",
		"\x83": "N̄",
		"\x84": "Ń",
		"\x85": "Ñ",
		"\x86": "Ṇ",
		"\x87": "Ṅ",
		"\x88": "Ō",
		"\x89": "Q̇",
		"\x8b": "Ŕ",
		"\x8c": "Ṛ",
		"\x92": "Š",
		"\x93": "Ś",
		"\x94": "Ş",
		"\x95": "Ṭ",
		"\x96": "T́",
		"\x97": "Ū",
		"\x98": "Ú",
		"\x99": "Ŭ",
		"\x9b": "Ṿ",
		"\x9c": "Ẇ",
		"\x9f": "Ÿ",
		"\xa1": "Ŷ",
		"\xa2": "Ż",
		"\xa3": "Ẓ",
		"\xa5": "Ž",
		"\xa7": "ā",
		"\xa8": "ă",
		"\xa9": "ǎ",
		"\xaa": "ã",
		"\xab": "å",
		"\xac": "ạ",
		"\xae": "ạ̄",
		"\xb0": "ḅ",
		"\xb1": "ç",
		"\xb3": "u̱",
		"\xb4": "č",
		"\xb5": "ć",
		"\xb6": "ɔ",
		"\xb8": "d́",
		"\xb9": "y̲",
		"\xba": "ð",
		"\xbb": "ð̣",
		"\xbf": "ē",
		"\xc0": "ĕ",
		"\xc1": "ě",
		"\xc2": "ȩ",
		"\xc3": "ə",
		"\xc4": "ḡ",
		"\xc5": "ğ",
		"\xc6": "ǧ",
		"\xc7": "ġ",
		"\xc8": "ḥ",
		"\xc9": "ḫ",
		"\xca": "ī",
		"\xcb": "i̊",
		"\xcc": "ı",
		"\xcd": "ķ",
		"\xce": "ḳ",
		"\xcf": "ḷ",
		"\xd1": "ł",
		"\xd2": "ṃ",
		"\xd3": "n̄",
		"\xd4": "ń",
		"\xd5": "k̲",
		"\xd6": "ṇ",
		"\xd8": "ṅ",
		"\xd9": "ō",
		"\xda": "q̇",
		"\xdb": "ŕ",
		"\xdc": "ṛ",
		"\xdf": "ṣ",
		"\xe0": "š",
		"\xe1": "ś",
		"\xe2": "ş",
		"\xe3": "ṫ",
		"\xe4": "t́",
		"\xe5": "ū",
		"\xe6": "ú",
		"\xe7": "ŭ",
		"\xe8": "ṿ",
		"\xe9": "ẇ",
		"\xea": "s̲",
		"\xeb": "ŷ",
		"\xec": "ž",
		"\xed": "ẓ",
		"\xee": "ż",
		"\xef": "t̲",
		"\xf1": "z̲",
		"\xf2": "D̲",
		"\xf3": "G̲",
		"\xf4": "H̲",
		"\xf5": "J̲",
		"\xf6": "K̲",
		"\xf7": "S̲",
		"\xf8": "T̲",
		"\xf9": "d̲",
		"\xfa": "Y̲",
		"\xfb": "Z̲",
		"\xfc": "a̲",
		"\xfd": "č̲",
		"\xff": "g̲"
		}

digraphs = {
		"alṢ ": "al-",
		"ḍlṢ ": "’l-"
	}

brilldecode = re.compile("|".join(re.escape(character) for character in brillcode.keys()))

try:
	f = bz2.open(sys.argv[1])
	f.peek(0)
except:
	f = open(sys.argv[1],mode="rb")
finally:
		soup = bs4.BeautifulSoup(f.read().decode("raw_unicode_escape"), "lxml")
		f.close()

for tag in soup.findAll(class_=["Ba02", "Ba02SC", "mainentry"]):
	if tag.string != None:
		tag.string = brilldecode.sub(lambda x: brillcode[x.group()], tag.string)
	# if tag.name == "form":
	# 	tag.name = "span"

title = re.split(r"(\[.*\])", soup.find("title").string)
title[0] = brilldecode.sub(lambda x: brillcode[x.group()], title[0])
brilldecode = re.compile("|".join(re.escape(character) for character in digraphs.keys()))
title[0] = brilldecode.sub(lambda x: digraphs[x.group()], title[0])
soup.find("title").string = "".join(title)

print(soup)
