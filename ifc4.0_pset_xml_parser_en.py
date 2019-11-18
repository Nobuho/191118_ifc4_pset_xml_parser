from lxml import etree
import csv
from glob import glob
import codecs

for f in glob("psd/*.xml"):

    tree = etree.parse(f)

    name_pset = tree.xpath('//PropertySetDef/Name')

    names_prop = tree.xpath('//PropertyDef/Name')

    names_en = tree.xpath(
        '//PropertySetDef/PropertyDefs/PropertyDef/NameAliases/NameAlias[@lang="en"]')
    note_en = tree.xpath(
        '//PropertySetDef/PropertyDefs/PropertyDef/Definition')

    # names_jp = tree.xpath(
    #     '//PropertySetDef/PropertyDefs/PropertyDef/NameAliases/NameAlias[@lang="ja-JP"]')
    # note_jp = tree.xpath(
    #     '//PropertySetDef/PropertyDefs/PropertyDef/DefinitionAliases/DefinitionAlias[@lang="ja-JP"]')

    list_names_prop = []

    pset_list = []

    for i in range(len(names_en)):
        row = []
        row.append(name_pset[0].text)
        row.append(names_en[i].text)
        row.append(note_en[i].text)
        # row.append(names_jp[i].text)
        # row.append(note_jp[i].text)
        pset_list.append(row)

    print(pset_list)

    with codecs.open('pset_list_EN.csv', 'a', 'cp932', 'ignore') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(pset_list)
