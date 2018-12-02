class HeaderHTML:
    def __init__(self):
        self.chaine ='''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <title><%= title %></title>
    <script src="/js/vue.js"></script>
    <script src="/js/axios.min.js"></script>
    <!-- Bootstrap Core CSS -->
    <link href="/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>
<div id="app">

    <h2> {{message}} </h2>
<div class="container">
<div class="alert alert-secondary" role="alert">

  <label for="code postal">Code postal de l'évènement</label><br>
  <input type="text"  placeholder="code postal" v-model ="code"/><br>
  <br>
  <label for="sondeur">zone libre</label><br>
  <input type="text"  placeholder="nom, lieux, tag" size="40" v-model ="sondeur"/><br>
  <hr>
{{nbitem-1}} Formulaire(s)  <button  type="button" class="btn btn-danger"   v-on:click="plustous">Envoyer les formulaires sur le serveur</button>
</div>
<br><hr>
<div class="alert alert-primary" role="alert"><a name="debut">Début du questionnaire</a></div>
'''
    def toHTML(self):
         print(self.chaine)
class FooterHTML:
    def __init__(self):
        self.chaine ='''
<br><hr>
<button  type="button" class="btn btn-success" v-on:click="plusun">Sauvegarder le formulaire</button>
</div>
</div>
</body>
  <script src="/javascripts/eg.js"></script>
</html>'''

    def toHTML(self):
         print(self.chaine)



