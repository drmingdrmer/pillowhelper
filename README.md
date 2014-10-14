pillowhelper
============

python-pillow helper

[python-pillow][pillow] is an image processing lib.

pillowhelper wraps pillow to make it easier to use.


## Usage

### pillowhelper.open( fn )

Wrap of Image.open

### pillowhelper.maxwidth( img, n )

return a duplicated Image object scaled so that the witdh is no more than `n`

### pillowhelper.maxheight( img, n )

return a duplicated Image object scaled so that the height is no more than `n`

### pillowhelper.target_size( img, size, inside )

Get size expected by width/height limit.

Result size fits in a box defined by `size` or just covers a box defined by
`size`.

size:

    tuple ( width, height )
    string "width*height"

inside:

    bool True: inside the box. False: cover the box.

### pillowhelper.fillbox( img, size_str )

Alias of `target_size( img, size, inside=False )` and `Image.resize()`.

### pillowhelper.inbox( img, size_str )

Alias of `target_size( img, size, inside=True )` and `Image.resize()`.

### pillowhelper.fillbox( img, size_str, pos_percent )

Return a duplicated Image object cropped by box with size `size_str`, at the
position in percentage defined by `pos_percent`.

size_str:

    tuple ( width, height )
    string "width*height"

pos_percent:

    tuple ( x_in_percentage, y_in_percentage )

### pillowhelper.write( img, fn, format=None )

Wrap of Image.save. If fn is not a filename string, try to get file format
from Image object.


[pillow]: https://pypi.python.org/pypi/Pillow
