import ezdxf

# Create a new DXF document.
doc = ezdxf.new(dxfversion='R2010')

# Create new table entries (layers, linetypes, text styles, ...).
doc.layers.new('TEXTLAYER', dxfattribs={'color': 2})

# DXF entities (LINE, TEXT, ...) reside in a layout (modelspace,
# paperspace layout or block definition).
msp = doc.modelspace()

# 3560,-5120|-4400,-5120|-4640,-5360|3800,-5360
#3560,2840|3560,-5120|3800,-5360|3800,3080
#-4400,2840|3560,2840|3800,3080|-4640,3080
#-4400,-5120|-4400,2840|-4640,3080|-4640,-5360
#hatch = msp.add_hatch(color=3)
#hatch.paths.add_polyline_path([(3560,-5120), (-4400,-5120), (-4640,-5360),(3800,-5360)], is_closed=1)
#hatch = msp.add_hatch(color=1)
#hatch.paths.add_polyline_path([(3560,2840), (3560,-5120), (3800,-5360),(3800,3080)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(1.00,1.00), (601.00,1.00), (601.00,601.00),(1.00,601.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(1.00,603.00), (601.00,603.00), (601.00,1203.00),(1.00,1203.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(603.00,1.00), (1203.00,1.00), (1203.00,601.00),(603.00,601.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(603.00,603.00), (1203.00,603.00), (1203.00,1203.00),(603.00,1203.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(1205.00,1.00),(1805.00,1.00),(1805.00,601.00),(1205.00,601.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(1205.00,603.00),(1805.00,603.00),(1805.00,1203.00),(1205.00,1203.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(1807.00,1.00),(2407.00,1.00),(2407.00,601.00),(1807.00,601.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(1807.00,603.00),(2407.00,603.00),(2407.00,1203.00),(1807.00,1203.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(2409.00,1.00),(3009.00,1.00),(3009.00,601.00),(2409.00,601.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(2409.00,603.00),(3009.00,603.00),(3009.00,1203.00),(2409.00,1203.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(3011.00,1.00),(3611.00,1.00),(3611.00,601.000),(3011.00,601.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(3011.00,603.00),(3611.00,603.00),(3611.00,1203.00),(3011.00,1203.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(3613.00,1.00),(4213.00,1.00),(4213.00,601.00),(3613.00,601.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(3613.00,603.00),(4213.00,603.00),(4213.00,1203.00),(3613.00,1203.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(4215.00,1.00),(4815.00,1.00),(4815.00,601.00),(4215.00,601.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(4215.00,603.00),(4815.00,603.00),(4815.00,1203.00),(4215.00,1203.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(4817.00,1.00),(5417.00,1.00),(5417.00,601.00),(4817.00,601.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(4817.00,603.00),(5417.00,603.00),(5417.00,1203.00),(4817.00,1203.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(5419.00,1.00),(6019.00,1.00),(6019.00,601.00),(5419.00,601.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(5419.00,603.00),(6019.00,603.00),(6019.00,1203.00),(5419.00,1203.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(6021.00,1.00),(6621.00,1.00),(6621.00,601.00),(6021.00,601.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(6021.00,603.00),(6621.00,603.00),(6621.00,1203.00),(6021.00,1203.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(6623.00,1.00),(7223.00,1.00),(7223.00,601.00),(6623.00,601.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(6623.00,603.00),(7223.00,603.00),(7223.00,1203.00),(6623.00,1203.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(7225.00,1.00),(7825.00,1.00),(7825.00,601.00),(7225.00,601.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(7225.00,603.00),(7825.00,603.00),(7825.00,1203.00),(7225.00,1203.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(7960.00,1.00),(7960.00,601.00),(7827.00,601.00),(7827.00,1.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(7960.00,603.00),(7960.00,1203.00),(7827.00,1203.00),(7827.00,603.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(1.00,1205.00),(601.00,1205.00),(601.00,1805.00),(1.00,1805.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(1.00,1807.00),(601.00,1807.00),(601.00,2407.00),(1.00,2407.00)], is_closed=1)
#55-74
hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(603.00,1205.00),(1203.00,1205.00),(1203.00,1805.00),(603.00,1805.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(603.00,1807.00),(1203.00,1807.00),(1203.00,2407.00),(603.00,2407.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(1205.00,1205.00),(1805.00,1205.00),(1805.00,1805.00),(1205.00,1805.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(1205.00,1807.00),(1805.00,1807.00),(1805.00,2407.00),(1205.00,2407.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(1807.00,1205.00),(2407.00,1205.00),(2407.00,1805.00),(1807.00,1805.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(1807.00,1807.00),(2407.00,1807.00),(2407.00,2407.00),(1807.00,2407.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(2409.00,1205.00),(3009.00,1205),(3009.00,1805.00),(2409.00,1805.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(2409.00,1807.00),(3009.00,1807.00),(3009.00,2407.00),(2409.00,2407.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(3011.00,1205.00),(3611.00,1205.00),(3611.00,1805.00),(3011.00,1805.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(3011.00,1807.00),(3611.00,1807.00),(3611.00,2407.00),(3011.00,2407.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(3613.00,1205.00),(4213.00,1205.00),(4213.00,1805.00),(3613.00,1805.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(3613.00,1807.00),(4213.00,1807.00),(4213.00,2407.00),(3613.00,2407.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(4215.00,1205.00),(4815.00,1205.00),(4815.00,1805.00),(4215.00,1805.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(4215.00,1807.00),(4815.00,1807.00),(4815.00,2407.00),(4215.00,2407.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(4817.00,1205.00),(5417.00,1205.00),(5417.00,1805.00),(4817.00,1805.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(4817.00,1807.00),(5417.00,1807.00),(5417.00,2407.00),(4817.00,2407.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(5419.00,1205.00),(6019.00,1205.00),(6019.00,1805.00),(5419.00,1805.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(5419.00,1807.00),(6019.00,1807.00),(6019.00,2407.00),(5419.00,2407.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(6021.00,1205.00),(6621.00,1205.00),(6621.00,1805.00),(6021.00,1805.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(6021.00,1807.00),(6621.00,1807.00),(6621.00,2407.00),(6021.00,2407.00)], is_closed=1)
#
hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(6623.00,1205.00),(7223.00,1205.00),(7223.00,1805.00),(6623.00,1805.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(6623.00,1807.00),(7223.00,1807.00),(7223.00,2407.00),(6623.00,2407.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(7225.00,1205.00),(7825.00,1205.00),(7825.00,1805.00),(7225.00,1805.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(7225.00,1807.00),(7825.00,1807.00),(7825.00,2407.00),(7225.00,2407.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(7960.00,1205.00),(7960.00,1805.00),(7827.00,1805.00),(7827.00,1205.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(7960.00,1807.00),(7960.00,2407.00),(7827.00,2407.00),(7827.00,1807.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(601.00,2800.00),(1.00,2800.00),(1.00,2409.00),(601.00,2409.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(1203.00,2800.00),(603.00,2800.00),(603.00,2409.00),(1203.00,2409.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(1805.00,2800.00),(1205.00,2800.00),(1205.00,2409.00),(1805.00,2409.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(2407.00,2800.00),(1807.00,2800.00),(1807.00,2409.00),(2407.00,2409.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(3009.00,2800.00),(2409.00,2800.00),(2409.00,2409.00),(3009.00,2409.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(3611.00,2800.00),(3011.00,2800.00),(3011.00,2409.00),(3611.00,2409.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(4213.00,2800.00),(3613.00,2800.00),(3613.00,2409.00),(4213.00,2409.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(4815.00,2800.00),(4215.00,2800.00),(4215.00,2409.00),(4815.00,2409.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(5417.00,2800.00),(4817.00,2800.00),(4817.00,2409.00),(5417.00,2409.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(6019.00,2800.00),(5419.00,2800.00),(5419.00,2409.00),(6019.00,2409.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(6621.00,2800.00),(6021.00,2800.00),(6021.00,2409.00),(6621.00,2409.00)], is_closed=1)

hatch = msp.add_hatch(color=7)
hatch.paths.add_polyline_path([(7223.00,2800.00),(6623.00,2800.00),(6623.00,2409.00),(7223.00,2409.00)], is_closed=1)

hatch = msp.add_hatch(color=5)
hatch.paths.add_polyline_path([(7825.00,2800.00),(7225.00,2800.00),(7225.00,2409.00),(7825.00,2409.00)], is_closed=1)

# hatch = msp.add_hatch(color=7)
# hatch.paths.add_polyline_path([(7827.00,2800.00),(7827.00,2409.00),(7960.00,2409.00),(7960.00,2800.00)], is_closed=1)

doc.saveas('Tuong.dxf')