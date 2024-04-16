# Greeting :wave:
Przedstawiona tutaj apka, to wprowadzenie w tematykę aplikacji webowych opartych o framework Flask.

## Struktura projektu :newspaper:
Projekt składać się musi z:
- app.py - główna aplikacja posiadająca wszystkie ścieżki i powiązania pomiędzy stronami
- static - folder ze statyczną zawartością witryny, tj. zdjęciami, arkuszami stylów CSS
- templates - katalog, w którym mamy do czynienia ze stronami html
- requirements.txt - plik tekstowy z bibliotekami do importu

## Uruchamianie :star:
Aby uruchomić naszą aplikację musimy być w lokalizacji pliku app.py. Jeżeli tam jesteśmy to wprowadzamy komendę.
```bash
flask run
```

Jeżeli jednak nie mamy zainstalowanego frameworka Flaska to wprowadzamy komendę, aby go zainstalować. 
```bash
pip install flask
```

## app.py :anchor:
W pliku app.py powinniśmy pamiętać o importach

```python
from flask import Flask, render_template, request
```

Kolejno definujemy zmienną app, która będzie funkcją Flask, urchamianą dla głównego pliku
```python
app = Flask(__name__)
```

Kolejno możemy przejść do definiowania scieżek.
```python
@app.route("/")
def index():
    return render_template("index.html")
```
Tutaj dla głównej lokalizacji naszej witryny program zwróci nam wyrenderowaną stronę index.html.

Jeżeli natomiast użytkownik wyśle komunikat wyrenderowana zostanie strona greet.html.
```python
@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name", "world")
    return render_template("greet.html", name=name)
```
Przesyłanie metodą GET nie zapewnia odpowiedniego poziomu bezpieczeństwa. Użytkownik może podać w formie hasło czy nr karty kredytowej. Metoda GET przesyła dane w adresie strony URL, umieszczając je po znaku zapytania. Dlatego my skorzystaliśmy z metody POST, która przesyła dane w sposób niezuważalny dla zwykłego użytkownika.

Można nieco uprościć sprawę, tak, aby na podstawie metody renderować odpowiednią stronę. Jeżeli przesyłamy dane w formularzu (klikamy przycisk submit) to renderowana jest strona z powitaniem greet.html. Natomiast na początku załadowania witryny, renderowana jest strona główna index.html, a więc wykorzystywana jest metoda GET.
```python
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        return render_template("greet.html", name=name)
    return render_template("index.html")
```

## index.html
Nasza stronka index.html, będzie zgodnie z konwencją, tą stroną, która uruchamia się jako pierwsza po wczytaniu witryny. W naszym projekcie umieściliśmy na tej właśnie stronie formularz, w którym prosimy użytkownika o podanie swojego imienia.
```html
<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Greeting</title>
    </head>

    <body>

        <form action="/" method="post">
            <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
        <button type="button">Greet</button>
        
    </form>
    </body>

</html>
```

Przy tej okazji warto wspomnieć o [Jinja](https://boringowl.io/blog/jinja).<br>
Nie będę się tutaj rozwodził na temat samej składni czy struktury, wspomnę jednak dlaczego warto z niej tutaj skorzystać. Otóż, Jijna pozwala nam uniknąć powielania tego samego fragmentu kodu w kilku miejscach. Dodatkowo, jeżeli będziemy musieli zmienić nazwę strony, czy stosowany na niej język czy podlinkować jakiś fragment z Bootstrap wystarczy, że zrobimy to tylko w jednym miejscu.<br>
To proste, wystarczy, że w tej samej lokalizacji co plik index.html umieścimy plik layout.html, który będzie zawierał trzon naszej witryny.
```html
<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Greeting</title>
    </head>

    <body>
        {% block body %}{% endblock %}
    </body>

</html>
```
Po tych zmianach plik index.html będzie prezentował się o wiele krócej, prócz elementów składni Jinja, będzie zawierał tylko i wyłacznie formularz html.
```html
{% extends "layout.html" %}
{% block body %}

<form action="/" method="post">
    <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
    <button type="button">Greet</button>
</form>

{% endblock %}
```

## greet.html
Jeżeli użytkownik wprowadzi swoje imię na stronie pojawia się fraza: "Hello, {name}". Jeżeli użytkownik wyśle pusty formularz, otrzyma komunikat "Hello, world". Plik greet.html
```html
{% extends "layout.html" %}
{% block body %}

Hello, {% if name %}{{ name }}{% else %}world{% endif %}

{% endblock %}
```



