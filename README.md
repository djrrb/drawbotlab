# drawbotlab
Some helpers for <a href="http://drawbot.readthedocs.org">DrawBot</a>.

Requires an installation of the python drawBot library (<code>from drawBot import *</code>).

The glyph module requires <a href="http://robofab.org">robofab</a> and <a href="https://github.com/behdad/fonttools/">fontTools</a>.

## Color

* RGBColor and CMYKColor objects, for easy color definition
* Genericized <code>fillColor()</code> and <code>strokeColor()</code> functions, that accept color objects, RGB tuples, or CMYK tuples

## Glyph

* DrawBot pen for converting from robofab glyph
* <code>drawGlyph()</code>, which acts like the function in the <a href="https://github.com/typemytype/drawBotRoboFontExtension">DrawBot RoboFont Extension</a>

## Shape

* <code>roundedRect(x, y, width, height, [radius, curvature])</code>, which acts like <code>rect()</code> but less pointy!

## Math

* <code>norm(value, start, stop)</code>, which interpolates. Similar to <a href="https://processing.org/reference/norm_.html">the function in Processing</a>.
* <code>lerp(start, stop, amt)</code>, which gets an interpolated value. Similar to <a href="https://processing.org/reference/lerp_.html">the function in Processing</a>.
