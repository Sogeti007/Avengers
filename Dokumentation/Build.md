# Build System mit pip

Um auf jedem System die selben Voraussetzungen zu schaffen wird eine virtuelle Umgebung mit den Standardwerkzeugen von Python aufgebaut. Dazu muss Python wie im Abschnitt "Setup für die IDE" beschrieben installiert sein. Im Anschluss wird ein virtuelle Umgebung aufgebaut. Dazu muss ein Terminal geöffnet werden und der Momentane Pfad muss dem Ordner des geklonten Repositories entsprechen. Das Klonen des Repositories wird im Abschnitt "Setup für die Versionskontrolle besprochen". In Visual Studio Code, wenn das entsprechende Verzeichnis für die IDE gewählt worden ist, kann auch einfach über die oberen Reiter unter "Terminal" ein neues Terminal direkt in der IDE geöffnet werden. Danach muss folgender Befehl ausgeführt werden:

```bash
python -m venv env
```

Es wird eine virtuelle Umgebung erstellt, welche, nachdem das Terminal wieder eingabebereit ist, mit diesem Befehl gestartet wird:

```bash
.\env\Scripts\activate
```

Hat alles geklappt, sollte nun vor dem Schriftzug auf der Konsole ein grünes "(env)" stehen und ein ausführen von `pip list` sollte

```bash
Package    Version
---------- -------
pip        21.1.1 
setuptools 56.0.0
```

Die Versionsnummern können in diesem Fall abweichen, ohne dass die Inbetriebnahme gefährdet ist. Alle nötigen Abhängigkeiten der lokalen Testumgebung können mit einem 

```bash
pip install -r .\requirements.txt
```

installiert werden. Mit einem 

```bash
python .\src\manage.py migrate
```

wird die Standard Datenbank erstellt und alle bisherigen Migrationen vollzogen. Um vollen Datenbankzugriff zu erhalten wird ein Admin User mit 

```bash
python .\src\manage.py createsuperuser
```

erstellt und es muss den Anweisungen am entsprechenden Terminal Folge geleistet werden (Name, Mail, Passwort, Passwort bestätigen, gegebenenfalls bestätigen, dass man ein unsicheres Passwort nutzen möchte). Nun kann mit einem 

```bash
python .\src\manage.py runserver
```

die Webanwendung gestartet und über den Localhost unter Port 8000 aufgerufen werden.

Die Tests können nun über ein 

```bash
coverage run --source="src/" ./src/manage.py test src -v 2 --keepdb
```

ausgeführt und ein Report dann über

```bash
coverage html
```

erstellt werden. Vor einem zweiten Test sollte der alte Report mit einem 

```bash
coverage erase
```

gelöscht werden.

