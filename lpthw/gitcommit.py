"""
Commit to the git repository after adding or appending content using gitpython
"""
#!/bin/python

from git import Repo
import os.path as osp 
from lxml import etree

join = osp.join

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository you want to work with
if __name__=="__main__":
    repo = Repo("D:\\Free-Tamil-Ebooks")
    print repo.working_dir
    filename="Test.xml"
    xml_file_path = osp.join(repo.working_tree_dir, filename)
    print xml_file_path
    doc = etree.parse(xml_file_path)    # retreive and parse the XML file using lxml
    ## Sample Additional content
    content ="<book><bookid>e86ad2d0-55c1-4644-874f-4e88c0a98168</bookid><title>எழுதுகோல் கவிதைகள்</title><author>ச. ரவிச்சந்திரன்</author><image>https://i0.wp.com/freetamilebooks.com/wp-content/uploads/2018/03/ezhuthikol-kavithaigal.jpg?fit=809%2C1200</image><link>http://freetamilebooks.com/ebooks/ezhuthukol_kavithaigal/</link><epub>http://freetamilebooks.com/download/%e0%ae%8e%e0%ae%b4%e0%af%81%e0%ae%a4%e0%af%81%e0%ae%95%e0%af%8b%e0%ae%b2%e0%af%8d-%e0%ae%95%e0%ae%b5%e0%ae%bf%e0%ae%a4%e0%af%88%e0%ae%95%e0%ae%b3%e0%af%8d-epub/</epub><pdf /><category>கவிதைகள்</category><date/></book>"
    root=doc.getroot() # Get root node
    # print etree.tostring(root) # Print the root and its contents
    newnode=etree.XML(content) # Create a new node from the content
    root.append(newnode) # Append the new node
    # print etree.tostring(doc.getroot()) # After insert verify its content added to root
    # Open the file and update it 
    f = open(xml_file_path, 'wb')
    f.write(etree.tostring(root))
    f.close()
    f = open(xml_file_path, 'rb')
    repo.index.add(f)
    f.close()
    repo.index.commit('Added new node custom message')

