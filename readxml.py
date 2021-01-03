# Mô tả dữ liệu đầu vào: paving.xml
# Yêu cầu bài toán: từ points của Wall vẽ ra tường, từ points của Tile vẽ ra hình dáng các viên gạch (points của Tile là toạ độ tương đối của Tile so với Wall)
# Trong phạm vi bài toàn chỉ quan tâm đến các thẻ sau: Wall, Tile
# Từ thẻ Area, có dữ liệu về vị trí các viên gạch
# points của Tile là danh sách các đỉnh để vẽ lên hình dáng viên gạch(ngăn cách nhau bằng dấu |) 
# Bên trên thẻ Wall Là danh sách các tường, points của Wall là toạ độ các đỉnh để vẽ ra tường trong hệ toạ độ 2D

import ezdxf
from xml.dom import minidom

xmldoc= minidom.parse("paving.xml")
Wall = xmldoc.getElementsByTagName("Wall")
item_tile = xmldoc.getElementsByTagName('Tile')

doc = ezdxf.new(dxfversion='R2010')
msp = doc.modelspace()

def main():
    hatch1 = msp.add_hatch(color=7)
    hatch = msp.add_hatch()

    for i in area:
        m1= i.getAttribute('wallid')

    for skill in Wall:
        x = skill.getAttribute("points").split("|")
        y0 = (x[0]).split(",")
        z0 = float (y0[0])
        z00 = float(y0[1])

        y1 = (x[1]).split(",")
        z01 = float(y1[0])
        z10 = float(y1[1])

        y2 = (x[2]).split(",")
        z02 = float(y2[0])
        z20 = float(y2[1])

        y3 = (x[3]).split(",")
        z03 = float(y3[0])
        z30 = float(y3[1])

        #print (x)
        #print(x[1])
        # print(y0,y1,y2,y3)
        # print(z0,z00,z01,z10,z02,z20,z03,z30)
        #print(y1)
        #print (x[1])

        
        hatch1.paths.add_polyline_path([(z0,z00),(z01,z10),(z02,z20),(z03,z30)], is_closed=1)

    for s in item_tile:
        x= s.getAttribute('points').replace(",0,0.0000","").split("|")
        
        x1=(x[0]).split(',')
        y01= (float(x1[0]))
        y10=float(x1[1])
        
        x2=(x[1]).split(',')
        y02= (float(x2[0]))
        y20=float(x2[1])

        x3=(x[2]).split(',')
        y03=float(x3[0])
        y30=float(x3[1])

        x4=(x[3]).split(',')
        y04=float(x4[0])
        y40=float(x4[1])

        
        hatch.set_pattern_fill('NET', color=7, scale=30.0)
        hatch.bgcolor = (144,111,65)
        hatch.paths.add_polyline_path([(y01,y10),(y02,y20),(y03,y30),(y04,y40)], is_closed=1)

    doc.saveas('brick.dxf')

main()



