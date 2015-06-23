# drawbotlab
Some helpers for <a href="http://drawbot.readthedocs.org">DrawBot</a> that I tend to use and reuse. I used to just copy/paste these things into my drawbot scripts, but it seems cleaner to just call them and use them like this:

<pre>from drawbotlab.color import RGBColor
from drawbotlab.shape import roundedRect
myBlue = RGBColor(b=1)
myBlue.setFill()
roundedRect(50, 50, 200, 100, r=20)</pre>

Requires an installation of the python drawBot library (<code>from drawBot import *</code>). The glyph module requires <a href="http://robofab.org">RoboFab</a> and <a href="https://github.com/behdad/fonttools/">fontTools</a>.

Drawbotlab doesn't have an installer or anything like that. To use it, simply place the folder, or a pth file pointing to the folder, in your Python site-packages.

## What’s inside?

### Color

* RGBColor and CMYKColor objects, for easy color definition and selection.
* Genericized <code>fillColor()</code> and <code>strokeColor()</code> functions, that accept color objects, RGB tuples, or CMYK tuples

### Glyph

* DrawBot pen for converting from robofab glyph
* <code>drawGlyph()</code>, which acts like the function in the <a href="https://github.com/typemytype/drawBotRoboFontExtension">DrawBot RoboFont Extension</a>
* <code>ufoText()</code>, which acts like Drawbot's native <code>text()</code> but draws from a robofab font
* <code>ufoTextSize()</code>, which gets the dimensions of a UFO-based textblock

### Shape

* <code>roundedRect(x, y, width, height, [radius, curvature])</code>, which acts like <code>rect()</code> but less pointy!

### Math

* <code>norm(value, start, stop)</code>, which interpolates. Similar to <a href="https://processing.org/reference/norm_.html">the function in Processing</a>.
* <code>lerp(start, stop, amt)</code>, which gets an interpolated value. Similar to <a href="https://processing.org/reference/lerp_.html">the function in Processing</a>.
