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
import html
import sys
from pathlib import Path, PurePath
import argparse
from brillcode import *

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("-d", "--cdrom", help="path to the CDROM root, for slob output")
args = parser.parse_args()

if args.cdrom:
	import slob
	mimetypes = {
		".html":"text/html; charset=utf-8",
		".css": "text/css; charset=utf-8",
		".jpg": "image/jpg"
	}

try:
	f = bz2.open(args.file,mode="rb")
	f.peek(0)
except:
	f = open(args.file,mode="rb")
finally:
	soup = bs4.BeautifulSoup(f.read().decode("raw_unicode_escape"), "html.parser")
	f.close()

for tag in soup.findAll("form"):
	tag.name = "span"

for tag in soup.findAll(class_=["Ba02", "Ba02SC", "mainentry"], string=True):
	tag.string = tag.string.translate(brillcode)

for tag in soup.findAll(class_="contributor", string=True):
	tag.string = html.unescape(tag.string)

linkedfiles = ["EncIslam.css"]

soup.find("link")["href"] = "EncIslam.css"

for inlfig in soup.findAll(class_="inlFig"):
	linkedfiles.append(args.cdrom+"/Brill"+inlfig["src"])
	inlfig["src"] = PurePath(inlfig["src"]).name

title = soup.find("meta", attrs={"name": "blob"})["content"]
for specialchar in specialchars.keys():
	title = title.translate(specialchars)
title = bs4.BeautifulSoup(title, "html.parser")

for tag in title.findAll(class_=["Ba02", "Ba02SC", "mainentry"], string=True):
	tag.string = tag.string.translate(brillcode)
soup.find("title").string = title.text

with slob.create("entry.slob") as w:
	w.add(soup.encode("utf-8"), soup.find(class_="fat").text, str(Path(args.file).with_suffix("")), content_type=mimetypes[".html"])
	for file in linkedfiles:
		print(file)
		f = open(file,mode="rb")
		w.add(f.read(), PurePath(file).name, content_type=mimetypes[PurePath(file).suffix])
		f.close()
