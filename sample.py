from bs4 import BeautifulSoup as bs
import os 

## Data Loading 
DATA_PATH = "docs"
files = os.listdir(DATA_PATH)

def LoadDoc(file):
    path = os.path.join(DATA_PATH, file)
    with open(path, "r") as file:
        soup = bs("".join(file.readlines()), "lxml")
    return soup 


## Loading a document as a soup object
doc = LoadDoc(files[0])


# Extract Major Sections into a Dictionary
# Document should be divided into four sections - 
# repamb, suplinf, fdoc, bilcod
def GetSections(doc):
    sections = [{child.name: child} for child in doc.rule.children if child != "\n"]
    rule_document = {} 
    for section in sections:
        rule_document.update(section)

    # Just to make sure, check for duplicates 
    section_titles = [child.name for child in doc.rule.children if child != "\n"]
    assert(len(section_titles) == len(set(section_titles)))

    # Good to go -> return the dictionary 
    return rule_document

rule_doc = GetSections(doc)


## Simple Text Extraction 
supl_text = "\n".join([child.text for child in rule_doc['suplinf'].children if child != "\n"])
frdoc_text = rule_doc['frdoc'].text
bilcod_text = rule_doc['bilcod'].text

