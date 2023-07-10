""" Written by Benjamin Jack Cullen """

import os


def read_template():
    new_lines = []
    with open('./annotation.xml', 'r') as fo:
        for line in fo:
            if line != '':
                new_lines.append(line)
    return new_lines


def annotation_tag_open(output_xml_path=None, output_directory_path=None, image_h=None, image_w=None,
                        image_filename=None, output_image_path=None, _make_dirs=True):
    if _make_dirs is True:
        if not os.path.exists(output_directory_path + '\\auto\\annotations'):
            os.makedirs(output_directory_path + '\\auto\\annotations', exist_ok=True)
    with open(output_xml_path, 'w+') as fo:
        fo.write('<annotation>' + '\n')
        fo.write('    <folder>images</folder>' + '\n')
        fo.write(f'    <filename>{image_filename}</filename>' + '\n')
        fo.write(f'    <path>{output_image_path}</path>' + '\n')
        fo.write(f'    <source>' + '\n')
        fo.write(f'        <database>Unknown</database>' + '\n')
        fo.write(f'    </source>' + '\n')
        fo.write(f'    <size>' + '\n')
        fo.write(f'        <width>{image_w}</width>' + '\n')
        fo.write(f'        <height>{image_h}</height>' + '\n')
        fo.write(f'        <depth>3</depth>' + '\n')
        fo.write(f'    </size>' + '\n')


def annotation_tag_close(output_xml_path):
    with open(output_xml_path, 'a') as fo:
        fo.write('</annotation>' + '\n')


def annotate(_verbose=False, output_directory=None, name=None, output_xml_path=None,
             box_points=None, _make_dirs=True):
    # read template annotation file
    # lines = read_template()
    lines = ['	<object>',
             '		<name>?</name>',
             '		<pose>Unspecified</pose>',
             '		<truncated>0</truncated>',
             '		<difficult>0</difficult>',
             '		<bndbox>',
             '			<xmin>?</xmin>',
             '			<ymin>?</ymin>',
             '			<xmax>?</xmax>',
             '			<ymax>?</ymax>',
             '		</bndbox>',
             '	</object>']
    # get data
    xmin = str(box_points[0])
    ymin = str(box_points[1])
    xmax = str(box_points[2])
    ymax = str(box_points[3])
    # read base annotation file and create new lines for new files
    new_lines = []
    for line in lines:
        if '<name>' in line:
            line = line.replace('?', name)
        if '<xmin>' in line:
            line = line.replace('?', xmin)
        if '<ymin>' in line:
            line = line.replace('?', ymin)
        if '<xmax>' in line:
            line = line.replace('?', xmax)
        if '<ymax>' in line:
            line = line.replace('?', ymax)
        new_lines.append(line)
    # create new annotation filename
    if _make_dirs is True:
        if not os.path.exists(output_directory + '\\auto\\annotations'):
            os.makedirs(output_directory + '\\auto\\annotations', exist_ok=True)
    with open(output_xml_path, 'a') as fo:
        for new_line in new_lines:
            fo.write(new_line+'\n')
