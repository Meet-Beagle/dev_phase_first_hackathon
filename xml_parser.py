import xml.etree.ElementTree as ET
import pandas as pd


def basic_read():
    tree = ET.parse('mock_data.xml', )
    root = tree.getroot()
    print(root.tag)
    # print(dict(root))
    for child in root:
        print(child.tag, child.attrib)
        print('    |')
        for grand_child in child:
            print('    |', 8*'-', grand_child.tag, grand_child.text)


pd.read_json()
