#!/usr/bin/env python2.7
# coding: utf-8

from PIL import Image

def open( fn ):
    return Image.open( fn )

def maxwidth( img, n ):
    return inbox( img, str(n) + '*100000000' )

def maxheight( img, n ):
    return inbox( img, '100000000*' + str(n) )

def target_size( img, size, inside ):
    w, h = img.size

    ratio_w = float( size[ 0 ] ) / w
    ratio_h = float( size[ 1 ] ) / h

    if inside:
        ratio = min( [ ratio_w, ratio_h ] )
    else:
        ratio = max( [ ratio_w, ratio_h ] )

    w, h = int(round(w*ratio)), int(round(h*ratio))
    return w, h

def fillbox( img, size_str ):

    size = parse_size( size_str )
    w, h = target_size( img, size, False )

    return img.resize( ( w, h ), Image.BILINEAR )

def crop( img, size_str, pos_percent=None ):

    size = parse_size( size_str )
    pos_percent = pos_percent or ( 0.5, 0.5 )
    xp, yp = pos_percent

    w, h = img.size

    # only one of dw and dh is zero
    dw, dh = (w - size[0]), (h - size[1])
    x, y = dw*xp, dh*yp

    box = ( x, y,
            x + size[0], y + size[1] )

    return img.crop( box )

def inbox( img, size_str ):
    size = parse_size( size_str )
    w, h = target_size( img, size, True )

    return img.resize( ( w, h ), Image.BILINEAR )

def write( img, fn, format=None ):
    if type( fn ) in (type( '' ), type( u'' )):
        fmt = None
    else:
        fmt = img.format

    img.save( fn, format=format or fmt )

def parse_size( size_str ):
    if type( size_str ) in ( type(()), type([]) ):
        return size_str

    w, h = size_str.split( '*', 1 )
    return int( w ), int( h )


if __name__ == "__main__":
    import sys
    def chain():
        # fillbox:n*n inbox:n*n write:fn
        cmds = sys.argv
        fn = cmds[ 1 ]
        cmds = cmds[ 2: ]

        im = Img( fn )

        for cmd_arg in cmds:
            cmd, arg = cmd_arg.split( ":", 1 )
            getattr( im, cmd )( arg )
            img[ 'img' ] = commands[ cmd ]( img, arg )
    chain()
