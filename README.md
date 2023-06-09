# Puissance-quatre-Python
Puissance-quatre joueur contre joueur en Python utilisant les clics de souris. Requiert l'installation préalable des modules numpy et pygame.

![Capture d'écran](https://i.imgur.com/USNUIG6.png)

## Installation des modules Python

### Windows

Ouvrir l'invite de commandes dans le répertoire Python à l'aide de la commande cd.

```bash
cd C:\Users\nom\AppData\Local\Programs\Python\Python310
```

Utilisation de [pip](https://pip.pypa.io/en/stable/) pour l'installation des modules [numpy](https://numpy.org/) et [pygame](https://www.pygame.org/).

Si "pip" n'est pas reconnu en tant que module, ajouter Python dans les variables PATH de windows règle ce problème. Sinon, [réinstaller Python](https://www.python.org/downloads/) à l'aide de l'exécutable en cochant la case "Add Python to PATH".

```bash
pip install numpy
```
```bash
pip install pygame
```

### Linux

#### Debian

Ouvrir le terminal, installer [pip](https://pip.pypa.io/en/stable/) si besoin.
```bash
sudo apt-get install python3-pip
```

Utilisation de [pip](https://pip.pypa.io/en/stable/) pour l'installation des modules [numpy](https://numpy.org/) et [pygame](https://www.pygame.org/).
```bash
pip install numpy
pip install pygame
```

#### Arch Linux

```bash
sudo pacman -S python
sudo pacman -S python-pip
pip install numpy
pip install pygame
```

#### Fedora

```bash
sudo dnf install python3
sudo dnf install python3-pip
pip install numpy
pip install pygame
```

#### openSUSE

```bash
sudo zypper install python3
sudo zypper install python3-pip
pip install numpy
pip install pygame
```

## Utilisation de puissanceQuatre.py

Après exécution de puissanceQuatre.py, il est possible d'interagir avec la fenêtre pygame à l'aide de la souris.

- Clic de souris pour ajouter un jeton de couleur jaune/rouge alternativement

Lorsque la partie se finit, un bouton Rejouer apparaît en haut à gauche.


