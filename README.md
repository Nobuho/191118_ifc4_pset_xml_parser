# ifc4-pset-xml-csv-converter

convert IFC4.0 TC1 Pset (default set of propaties and quantities) xml to csv.

## Description

IFC4.0 TC1 has default Pset for property and quantity.This script extract the [name] and [discription] from the XMLs as csv.

### Note

These XML fields have some language for each, in this script extract EN and JP. But some of field are not translated, so if you need all of properties you should use EN ver.

## Requirement

### Library

lxml

## Install

1. Download the pset xml file from official BuildingSMART website.

    Download (select : 4.0.2.1 IFC4 ADD2 TC1 -> HTML ZIP ) 

    https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/

1. Unzip the file and pick up folder [psd] and [qto]

1. Copy them inside of [pset_xml] folder

## Usage

1. Run the scripts then you will get .csv file.

## TODO

- Make a script for qto xml