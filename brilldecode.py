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
from tqdm import tqdm
import argparse
from brillcode import *

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("cdrom", help="path to the CDROM root")
parser.add_argument("output", help="output .slob file. Defaults to ei.slob", default="ei.slob")
args = parser.parse_args()

import slob

w = slob.create(PurePath(args.output))
linkedfiles = ["EncIslam.css"]
missingfiles = 0

entries = sorted(Path(PurePath(args.cdrom+"/Brill/Data/EncIslam")).glob('[CDS][0-9]/*.html'))

for entry in tqdm(entries, unit="entries"):
	try:
		f = bz2.open(entry,mode="rb")
		f.peek(0)
	except:
		f = open(entry,mode="rb")
	finally:
		soup = bs4.BeautifulSoup(f.read().decode("raw_unicode_escape"), "html.parser")
		f.close()

	for tag in soup.findAll("form"):
		tag.name = "span"

	for tag in soup.findAll(class_=["Ba02", "Ba02SC", "mainentry"], string=True):
		tag.string = tag.string.translate(brillcode)

	for tag in soup.findAll(class_="contributor", string=True):
		tag.string = html.unescape(tag.string)

	soup.find("link")["href"] = "EncIslam.css"

	for inlfig in soup.findAll(class_="inlFig"):
		linkedfiles.append(str(PurePath(args.cdrom+"/Brill"+inlfig["src"])))
		inlfig["src"] = PurePath(inlfig["src"]).name

	title = soup.find("meta", attrs={"name": "blob"})["content"]
	title = title.translate(specialchars)
	title = bs4.BeautifulSoup(title, "html.parser")
	for tag in title.findAll(class_=["Ba02", "Ba02SC", "mainentry"], string=True):
		tag.string = tag.string.translate(brillcode)
	soup.find("title").string = title.text

	w.add(soup.encode("utf-8"), re.split(r"( \[.*\])", title.text)[0], ' '.join(soup.find(class_="fat").text.split()), entry.name.removesuffix(".html"), content_type=mimetypes[".html"])

for file in tqdm(sorted(set(linkedfiles)), unit="figures"):
	try:
		f = open(file,mode="rb")
		w.add(f.read(), Path(file).name, content_type=mimetypes[PurePath(file).suffix])
		f.close()
	except:
		missingfiles += 1

w.finalize()
