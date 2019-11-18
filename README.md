# 191118_ifc4_pset_xml_parser

## IFC4.0 TC1のPSETのXMLから、項目を抽出する

psdフォルダ内に対象となるxmlファイルが格納されている。

ダウンロード先

https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/

4.0.2.1	IFC4 ADD2 TC1　の　HTML ZIPをダウンロードするとxmlファイルが中に入っている。

直リンク

https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD2_TC1/ifc4-add2-tc1.zip

日本語と英語で項目名と項目説明が書かれているが、一部日本語訳されていないものもあったので、pythonスクリプトは英語csv出力用と日本語csv出力用に分けている。

# TODO

qtoフォルダのQuantityについてはまだスクリプト作成していない。
