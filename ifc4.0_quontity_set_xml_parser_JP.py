from lxml import etree
import csv
from glob import glob
import codecs


for f in glob("pset_xml\qto\*.xml"):

    tree = etree.parse(f)
    root = tree.getroot()

    mynsmap = {}
    mynsmap = root.nsmap

    QtoSet_Name = [i.text for i in root.iterfind('Name', namespaces=mynsmap)]
    ApplicableClasses = [i.text for i in root.iterfind('ApplicableClasses/ClassName', namespaces=mynsmap)]

    QtoDef_Names = [i.text for i in root.iterfind('QtoDefs/QtoDef/Name', namespaces=mynsmap)]
    QtoDef_Definitions = [i.text for i in root.iterfind('QtoDefs/QtoDef/Definition', namespaces=mynsmap)]
    QtoDef_Type = [i.text for i in root.iterfind('QtoDefs/QtoDef/QtoType', namespaces=mynsmap)]

    QtoDef_NameAliase_jp =[i.text for i in root.iterfind('QtoDefs/QtoDef/NameAliases/NameAlias[@lang="ja-JP"]', namespaces=mynsmap)]
    QtoDef_DinfinitionAlias_jp =[i.text for i in root.iterfind('QtoDefs/QtoDef/DefinitionAliases/DefinitionAlias[@lang="ja-JP"]', namespaces=mynsmap)]

    # print(set_list)

    set_list =[]

    for i in range(len(QtoDef_NameAliase_jp)):
        row = []
        row.append(QtoSet_Name[0])
        row.append(ApplicableClasses[0])
        row.append(QtoDef_NameAliase_jp[i])
        try:
            row.append(QtoDef_DinfinitionAlias_jp[i])
        except:
            row.append("none")
        set_list.append(row)

    with codecs.open('qset_list_JP.csv', 'a', 'cp932') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(set_list)


