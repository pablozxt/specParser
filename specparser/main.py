def main():
    import xml.etree.ElementTree as ET 
    import os
    
    xml_file = input('\n' + 'Define Bluebeam markup xml file to parse: ').strip('"')
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    xml_file_split = os.path.split(xml_file)
    dest_filename = os.path.splitext(xml_file_split[1])[0]
    #dest_file = open(os.path.split(xml_file)[1], w+)
    print(dest_filename)

if __name__ == "__main__":
    main()