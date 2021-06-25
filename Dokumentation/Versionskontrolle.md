# Setup für die Versionscontrolle

Für die Versionskontrolle wurde sich für [GitLab](https://about.gitlab.com/) entschieden. Benötigt wurde:

* Account für jedes Teammitglied
* Integration in Visual Studio Code (generell für jeden GIT Anbieter)
* Einfach und verlässlich
* Kostenlos für öffentliche Repositories

Einrichtung über die GUI auf der entsprechenden Webseite von [GitLab](https://gitlab.com/users/sign_in). Als Werkzeug unter Windows wird  [Git for Windows](https://git-scm.com/downloads) verwendet.

Checkout des Repositories funktioniert über:

```bash
git clone "https://gitlab.com/JulianAtSogeti/praxisprojektbootcamp.git"
```

Falls nicht schon als Standardeinstellung sollte jedes Teammitglied seinen Namen und seine E-Mail einstellen:

```bash
git config --global user.name "Name Nachname"
git config --global user.email name.nachname@sogeti.com
```

Branches werden benannt nach folgenden Regeln:

```bash
git checkout main
git pull origin main
git checkout -b boot-X
```

Wenn Userstories Tasks haben:

```
git checkout main
git pull origin main
git checkout -b boot-X-task-Y
```

Wenn Änderungen an einem Branch vorgenommen wurden können diese in einem Commit zugefügt und der Commit ausgeführt werden. Angenommen Datei "foo.py" wird geändert, so kann die Änderung mit einem

```bash
git add foo.py
```

dem neuen Commit zugefügt werden. Ein

```
git status
```

gibt Informationen über über die aktuellen Änderungen und die für den Commit vorgemerkten Änderungen. Sind alle Dateien für einen Commit vorgemerkt kann der Commit mit

```bash
git commit -m"Nachricht"
```

durchgeführt werden. Die Zeichenkette "Nachricht" sollte dabei mit einer ausgetauscht werden, die den momentanen Commit beschreibt.  Der Commit ist jetzt nur Lokal vorhanden und muss noch auf den entsprechenden Branch gepushed werden. Dazu muss, sicherheitshalber, zuerst gepulled werden:

```bash
git pull origin branch-name
git push -u origin branch-name
```

Notwendige Account Passwörter müssen eingegeben werden. Häufiges Pullen und möglichst kleine Commits sind eine gute Angewohnheit. 

 
