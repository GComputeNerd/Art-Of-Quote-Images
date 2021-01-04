import sys
import cairo
import cairofunctions as cf
import gi
gi.require_version('Pango', '1.0')
gi.require_version('PangoCairo', '1.0')
from gi.repository import Pango, PangoCairo

sunTzu = cairo.ImageSurface.create_from_png("sun-tzu.png")
cr = cairo.Context(sunTzu)

w = sunTzu.get_width()
h = sunTzu.get_height()
mw = 460*Pango.SCALE
mh = 307

cr.set_source_rgb(0,0,0)
cr.set_source_rgb(255,255,255)

pc = PangoCairo.create_context(cr)
layout = PangoCairo.create_layout(cr)

# Sample Text
# text = "Let your plans be as dark and as impenetrable as night, and when you move, fall like a thunderbolt"
# text = "Hi"
# text = "That's Really Lame"
# text = "All War is Deception"

text = " ".join(sys.argv[1:])

# Default Font Settings
font = "monospace"
style = "normal"
fs = 50

# Set up layout
layout.set_font_description(Pango.FontDescription(font + " " + style + " "  + str(fs)))

layout.set_width(mw)

layout.set_alignment(1)

layout.set_text(text)

# Make height and width not exceed maximum 
height = layout.get_extents()[1].height/Pango.SCALE
width = layout.get_extents()[1].width

while (width > mw):
    fs -= 5
    layout.set_font_description(Pango.FontDescription(font + " " + style + " "  + str(fs)))
    width = layout.get_extents()[1].width

while (height > mh):
    fs -= 5
    layout.set_font_description(Pango.FontDescription(font + " " + style + " "  + str(fs)))
    height = layout.get_extents()[1].height/Pango.SCALE

# Get Size of bounding rectangle
width = layout.get_extents()[1].width/Pango.SCALE
height = layout.get_extents()[1].height/Pango.SCALE

x = (980-width)/2
y = (387-height)/2

cr.move_to(x, y)

PangoCairo.show_layout(cr, layout) # Display Main quote

# Rectangles for Debugging Purposes
# cf.Polygon(cr,260,40,720,40,720,347,260,347)
# cf.Polygon(cr,x,y,x+width,y,x+width,y+height,x,y+height)

# Sun Tzu, The Art of War text
layout.set_font_description(Pango.FontDescription("monospace normal 18"))

layout.set_text("~ Sun Tzu, The Art of War")
layout.set_alignment(0)

w = layout.get_extents()[1].width/Pango.SCALE


if (width - w < 0):
    cr.move_to(720-w, (387+height)/2)
else:
    cr.move_to((980+width-2*w)/2,(387+height)/2)

PangoCairo.show_layout(cr, layout)

sunTzu.write_to_png("img.png")
