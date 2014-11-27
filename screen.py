import gtk.gdk
import time

def take_screenshot():
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    i = 0;
    if (pb != None):
        a = time.asctime() + ".png"
        pb.save(a, "png")
        print a
    else:
        print "no screen"

