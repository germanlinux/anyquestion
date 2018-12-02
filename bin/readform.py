from  classhtml  import *
from headerhtml import *
import sys
import json
argv_json = sys.argv[1]
with open(argv_json,'r') as fichier:
    lignes = fichier.readlines()
lig = ''
lig =lig.join(lignes)
#print(json.loads(lig))
form = json.loads(lig)
#print(form)
head = HeaderHTML()
head.toHTML()

for item in form['questions'] :
    if item['type'].lower() == 'ONS'.lower():
        ql = QuestionONS(item['numero'], item['libelle'])
        ql.toHTML()
    if item['type'].lower() == 'LargeText'.lower() :
        ql = QuestionLargeText(item['numero'], item['libelle'] )
        ql.toHTML()
    if  item['type'].lower() == 'Multi'.lower():
        ql = QuestionMulti(item['numero'], item['libelle'], item['choix'])
        ql.toHTML()
    if  item['type'].lower() == 'text'.lower():
        libelle = None
        if 'libelle' in item:
            libelle = item['libelle']
        placeholder = None
        if 'placeholder' in item:
            placeholder = item['placeholder']
        ql = QuestionText(item['numero'], libelle,10,placeholder)
        ql.toHTML()
    if  item['type'].lower() == 'simple'.lower():
        ql = Question(item['numero'], item['libelle'], item['choix'])
        ql.toHTML()
foot = FooterHTML()
foot.toHTML()
