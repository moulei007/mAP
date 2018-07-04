# -*- coding:utf-8 -*-
'''
    @Time:2018/6/26
    @Author: moulei
    @Email: 1144545359@qq.com
'''

import os
import glob
from xml.dom.minidom import parse
import xml.dom.minidom

xml_dir = 'xml'
txt_dir = 'xml2txt'

if not os.path.exists(txt_dir):
    os.makedirs(txt_dir)

def main():
    xml_files = glob.glob(xml_dir + '/*.xml')
    for xml_num, xml_name in enumerate(xml_files):
        dom_tree = parse(xml_name)
        # 根节点
        # root = dom_tree.documentElement
        # 获取文件名
        filename = dom_tree.getElementsByTagName('filename')[0].childNodes[0].data
        filename_list = filename.split(".")
        # 获取图片的长,宽
        # width = dom_tree.getElementsByTagName('width')[0].childNodes[0].data
        # height = dom_tree.getElementsByTagName('height')[0].childNodes[0].data
        objects = dom_tree.getElementsByTagName("object")
        # 获取内容，保存到list中
        txt_list = []
        for obj in objects:
            obj_name = obj.getElementsByTagName("name")[0].childNodes[0].data
            left = obj.getElementsByTagName("xmin")[0].childNodes[0].data
            top = obj.getElementsByTagName("ymin")[0].childNodes[0].data
            right = obj.getElementsByTagName("xmax")[0].childNodes[0].data
            bottom = obj.getElementsByTagName("ymax")[0].childNodes[0].data
            box = [obj_name, left, top, right, bottom]
            txt_list.append(box)
        # 将读取到的信息写入到txt文件中
        txt = open(txt_dir + '/' + str(filename_list[0]) + '.txt', "a")
        for lines in txt_list:
            for element in lines:
                txt.write(element)
                if lines.index(element) < len(lines) - 1:
                    txt.write(" ")
                else:
                    txt.write("\n")
        print(xml_name, "...")


if __name__ == '__main__':
    main()
