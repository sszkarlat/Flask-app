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

Przy tej okazji warto wspomnieć o [Jinja](https://boringowl.io/blog/jinja)<br>. Nie będę się tutaj rozwodził o samej składni czy strukturze, wspomnę jednak dlaczego z niej tutaj skorzystać. Otóż, Jijna pozwala nam unikną powielania tego samego fragmentu kodu w kilku miejscach. Dodatkowo, jeżeli będziemy musieli zmienić nazwę stron, czy stsowany na niej język czy podlinkować jakiś fragment z Bootstrap wystarczy, że zrobimy to tylko w jednym miejscu.<br>
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
Po tych zmianach plik index.html będzie prezentował się o wiele krócej, prócz elementów składni Jinja będzie zawierał tylko formularz html.
```html
{% extends "layout.html" %}
{% block body %}

<form action="/" method="post">
    <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
    <button type="button">Greet</button>
</form>

{% endblock %}
```



