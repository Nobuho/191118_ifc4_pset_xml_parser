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


# for f in glob("pset_xml\qto\Qto_DoorBaseQuantities.xml"):

#     tree = etree.parse(f)
#     root = tree.getroot()

#     mynsmap = {}
#     mynsmap = root.nsmap

#     QtoSet_Name = [i.text for i in root.iterfind('Name', namespaces=mynsmap)]
#     ApplicableClasses = [i.text for i in root.iterfind('ApplicableClasses/ClassName', namespaces=mynsmap)]

#     QtoDef_Names = [i.text for i in root.iterfind('QtoDefs/QtoDef/Name', namespaces=mynsmap)]
#     QtoDef_Definitions = [i.text for i in root.iterfind('QtoDefs/QtoDef/Definition', namespaces=mynsmap)]
#     QtoDef_Type = [i.text for i in root.iterfind('QtoDefs/QtoDef/QtoType', namespaces=mynsmap)]

#     QtoDef_NameAliases =[i for i in root.iterfind('QtoDefs/QtoDef/NameAliases', namespaces=mynsmap)]
#     QtoDef_NameAliases_list = [[mem.text for mem in elm] for elm in QtoDef_NameAliases]
#     QtoDef_NameAliases_lang_list = [[mem.attrib["lang"] for mem in elm] for elm in QtoDef_NameAliases]
#     QtoDef_NameAliases_lang_list_merge = [",".join(map(str,i)) for i in QtoDef_NameAliases_lang_list]
    
#     QtoDef_DinfinitionAliases =[i for i in root.iterfind('QtoDefs/QtoDef/DefinitionAliases', namespaces=mynsmap)]
#     QtoDef_DifinitionAliases_list = [[mem.text for mem in elm] for elm in QtoDef_DinfinitionAliases]
#     QtoDef_DifinitionAliases_lang_list = [[mem.text for mem in elm] for elm in QtoDef_DinfinitionAliases]
#     QtoDef_DifinitionAliases_lang_list_merge = [",".join(map(str,i)) for i in QtoDef_DifinitionAliases_lang_list]

#     # print(set_list)

#     dicts = [[a, b, c, d, e] for a, b, c, d, e in zip(
#         QtoDef_Names,
#         QtoDef_Definitions,
#         QtoDef_Type,
#         QtoDef_NameAliases_lang_list_merge,
#         QtoDef_DifinitionAliases_lang_list_merge)]

# with codecs.open('qset_list_ENJP.csv', 'a', 'cp932', 'ignore') as f:
#     writer = csv.writer(f, delimiter='\t')
#     writer.writerows(set_list)
