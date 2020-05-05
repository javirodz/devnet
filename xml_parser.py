from __future__ import print_function

import xml.etree.ElementTree as ET


def main():
    # create element tree object
    with open('xmlfile.xml', 'r') as xmlFile:
        tree = ET.parse(xmlFile)
    # get root element
    root = tree.getroot()
    print("Root Tag: " + root.tag)
    print("Using a for Loop:")
    for child in root:
        print(child.tag)
        for attrib in child:
            print(attrib.tag, end=' ')
            print(attrib.text)

    print("Using Indexes:")
    print(root[0].tag)
    print(root[0][0].tag,end=' ')
    print(root[0][0].text)
    print(root[0][1].tag,end=' ')
    print(root[0][1].text)

    print(root[1].tag)
    print(root[1][0].tag,end=' ')
    print(root[1][0].text)
    print(root[1][1].tag,end=' ')
    print(root[1][1].text)

    print(root[2].tag)
    print(root[2][0].tag,end=' ')
    print(root[2][0].text)
    print(root[2][1].tag,end=' ')
    print(root[2][1].text)

    print("Other:")
    for hostname in root.iter('hostname'):
        print(hostname.tag,end=' ')
        print(hostname.text)

if __name__ == "__main__":
    # calling main function
    main()