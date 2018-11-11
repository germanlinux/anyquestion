class QuestionONS:
    def __init__(self, numero, libelle):
        self.numero = numero
        self.libelle = libelle
    def toHTML(self):
        numero = self.numero
        print(f'''<!-- question {numero}  -->
                <div class=\"card\">
                <div class=\"card-header\">
                <label for=\"question\">Question {numero}:{self.libelle}</label><br>
                </div>
                <label for=\"question{numero}-1\">OUI</label>
                <input type=\"radio\" value='O' v-model =\"question{numero}\"><br>
                <label for=\"question{numero}-2\">NON</label>
                <input type=\"radio\" value='N' v-model=\"question{numero}\"><br>
                <label for=\"question{numero}-3\">Je ne sais pas</label>
                <input type= \"radio\" value='I' v-model=\"question{numero}\"><br>
                </div>''')

class QuestionMulti:
    def __init__(self, numero, libelle, suite):
        self.numero = numero
        self.libelle = libelle
        self.suite = suite
        self.nboption = len(self.suite)/2
    def toHTML(self):
        numero = self.numero
        print(f'''<!-- question {numero}  -->
                <div class=\"card\">
                <div class=\"card-header\">
                <label for=\"question\">Question {numero}:{self.libelle}</label><br>
                </div>''')
        cp = 1
        for i in range(0,len(self.suite),2):
          print(f'''
                <label for="question{self.numero}-{cp}">{self.suite[i+1]}</label>
                <input type= checkbox value='{self.suite[i]}' v-model = "question{self.numero}X{cp}"><br>''')
          cp+=1
        print(f'''                </div>''')
class QuestionLargeText:
    def __init__(self, numero, libelle):
        self.numero = numero
        self.libelle = libelle
    def toHTML(self):
        numero = self.numero
        print(f'''<!-- question {numero}  -->
                <div class=\"card\">
                <div class=\"card-header\">
                <label for=\"question\">Question {numero}:{self.libelle}</label><br>
                </div>
                <textarea size="100"  v-model ="question{self.numero}"  cols="40" rows="5"></textarea>
                </div>''')

class QuestionText:
    def __init__(self, numero, libelle,size,placeholder):
        self.numero = numero
        self.libelle = libelle
        self.placeholder = placeholder
        self.size =size
    def toHTML(self):
        numero = self.numero
        print(f'''<!-- question {numero}  -->
                <div class=\"card\">
                <div class=\"card-header\">
                ''')
        if  self.placeholder:
            print(f'''
                <input type="text"  placeholder="{self.placeholder}" v-model ="question{self.numero}" size="{self.size}">
                </div></div>
                  ''')
        else:
            print(f'''
                <label for=\"question\">Question {numero}:{self.libelle}</label><br>
                </div>
                <input type="text"   v-model ="question{self.numero}" size="{self.size}">
                </div>''')


d1 = QuestionONS(1,"pourquoi  ?")
d2 = QuestionMulti(2,"aimez vous la pizza ?",('p', 'pred', 'n','non'))
d3 = QuestionLargeText(3,'pourquoi ?')
d4 = QuestionText(4,None,50, 'votre mail' )
d1.toHTML()
d2.toHTML()
d3.toHTML()
d4.toHTML()


print('eric')
