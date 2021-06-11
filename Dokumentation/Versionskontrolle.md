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

