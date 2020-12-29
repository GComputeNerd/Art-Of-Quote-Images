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

#text = input("Text = ")
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque in ligula vulputate, fermentum arcu at, viverra augue. Ut et posuere tellus. Donec varius elit orci, id bibendum nisi sollicitudin sollicitudin. Aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vel blandit magna. Donec nec felis id neque faucibus fringilla. Morbi ornare est id condimentum feugiat."
text = "Hi"

font = "monospace"
style = "normal"
fs = 80

layout.set_font_description(Pango.FontDescription(font + " " + style + " "  + str(fs)))

layout.set_width(mw)

layout.set_text(text)

height = layout.get_extents()[1].height/Pango.SCALE

while (height > mh):
    fs -= 5
    layout.set_font_description(Pango.FontDescription(font + " " + style + " "  + str(fs)))
    height = layout.get_extents()[1].height/Pango.SCALE

width = layout.get_extents()[1].width/Pango.SCALE

cr.move_to((980-width)/2 , (387-height)/2)

PangoCairo.show_layout(cr, layout)

# cf.Polygon(cr,260,40,720,40,720,347,260,347)

layout.set_font_description(Pango.FontDescription("monospace normal 18"))

layout.set_text("~ Sun Tzu, The Art of War")

w = layout.get_extents()[1].width/Pango.SCALE

cr.move_to(980+width-2*w, (387+height)/2)

PangoCairo.show_layout(cr, layout)

sunTzu.write_to_png("img.png")
