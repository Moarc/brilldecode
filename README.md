## What is Brillcode?

A very apt name [given](https://jhmccloskey.tripod.com/ei/index.htm) to the encoding we're dealing with.

The Brill *Encyclopædia of Islam* CD-ROM edition (2003) uses a custom font in which regular characters are replaced with the glyphs they need for transcription.
The articles themselves are encoded in Win-1252, and the font is switched to this special font (Baskerville for Brill 02) as needed, using CSS.
With modern stuff like webfonts the custom font could be included for machines that don't have this font installed, but copypasting from the articles would still result in a mess, and it just doesn't feel right, so I wrote a shitty script to convert them into proper Unicode. (it recently became a bit less shitty)

## Further goals
- [x] iterating over the entire encyclopedia
- [ ] properly handling all the links
- [ ] popup figures
- [ ] converting Greek text
- [ ] (possibly) reading directly from the CD or an image of the CD.
- [x] output to something like [slob](https://github.com/itkach/slob)

## Postscript
I'm not sure if the Ba00/Ba01 fonts include something other than regular Win-1252 (it didn't seem so to me, the Ö's etc. are displayed properly with other fonts) - if so, I'll create another conversion table for those too.