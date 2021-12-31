from math import sin, cos, pi

def vi_info(node, dim, **kwargs):
    if node.metric == '1' and node.light_menu == '2':
        ir = kwargs['ir']
        aDF = kwargs['aDF']
        irscaled = ir if ir < 0.7 else 0.7
        adfscaled = aDF if aDF < 3.2 else 3.2
        adfxpos = 400 - (300 * sin(adfscaled*pi/2.0))
        adfypos = 400 + (300 * cos(adfscaled*pi/2.0))
        (adffill, adfsweep) = ("255, 0, 0", 0) if aDF < 2.0 else ("0, 255, 0", 1)
        irxpos = 400 - (250 * sin(irscaled*pi/0.4))
        irypos = 400 + (250 * cos(irscaled*pi/0.4))
        (irfill, irsweep) = ("255, 0, 0", 0) if ir < 0.4 else ("0, 255, 0", 1)


        imname = "RIBA_lighting_{}".format(node.zone_menu)
        svg_str = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
        <svg
        id="svg5"
        version="1.1"
        viewBox="0 0 {0} {0}"
        height="{0}"
        width="{0}"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:svg="http://www.w3.org/2000/svg">
        <defs
        id="defs2" />
        <rect style="fill:rgb(255, 255, 255)" width="{0}" height="{0}"/>
        <path style="fill:rgb({1})" d="M 400 700
            A 300 300, 1, {2}, 1, {3:.0f} {4:.0f}
            L 400 400 Z"/>
        <circle  style="fill:rgb(255, 255, 255)" cx="400" cy="400" r="260"/>
        <path style="fill:rgb({5})" d="M 400 650
            A 250 250, 1, {6}, 1, {7:.0f} {8:.0f}
            L 400 400 Z"/>
        <circle  style="fill:rgb(255, 255, 255)" cx="400" cy="400" r="210"/>
        <text text-anchor="middle" x="400" y="400" style="font-size: 48px">RIBA 2030</text>
        <text text-anchor="middle" x="400" y="450" style="font-size: 48px">Lighting</text>
        <text x="20" y="770" style="font-size: 48px">Sensor: {9}</text>
        </svg>
        """.format(dim, adffill, adfsweep, adfxpos, adfypos, irfill, irsweep, irxpos, irypos, node.zone_menu)
        print(svg_str)
        return imname, bytearray(svg_str, encoding='utf-8')

    elif node.metric == '1' and node.light_menu == '2':
        svg_str = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
        <svg
        id="svg5"
        version="1.1"
        viewBox="0 0 {0} {0}"
        height="{0}"
        width="{0}"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:svg="http://www.w3.org/2000/svg">
        <defs
        id="defs2" />
        <rect style="fill:rgb(255, 255, 255)" width="{0}" height="{0}"/>
        <rect style="fill:rgb(255, 255, 255)" x="50" y="700" width="100" height="{0}"/>
        <rect style="fill:rgb(255, 255, 255)" x="175" y="700" width="100" height="{0}"/>
        <path style="fill:rgb({1})" d="M 400 700
            A 300 300, 1, {2}, 1, {3:.0f} {4:.0f}
            L 400 400 Z"/>
        <circle  style="fill:rgb(255, 255, 255)" cx="400" cy="400" r="260"/>
        <path style="fill:rgb({5})" d="M 400 650
            A 250 250, 1, {6}, 1, {7:.0f} {8:.0f}
            L 400 400 Z"/>
        <circle  style="fill:rgb(255, 255, 255)" cx="400" cy="400" r="210"/>
        <text text-anchor="middle" x="400" y="400" style="font-size: 48px">RIBA 2030</text>
        <text text-anchor="middle" x="400" y="450" style="font-size: 48px">Lighting</text>
        <text x="20" y="770" style="font-size: 48px">Sensor: {9}</text>
        </svg>
        """.format(dim, adffill, adfsweep, adfxpos, adfypos, irfill, irsweep, irxpos, irypos, node.zone_menu)