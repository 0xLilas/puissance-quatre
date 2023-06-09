import numpy as np
import pygame

# Dimensions du plateau de jeu
LIGNES = 6
COLONNES = 7

# Dimensions de chaque cellule
TAILLE_CELLULE = 100

# Couleurs
BLANC = (255, 255, 255)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)
JAUNE = (255, 255, 0)
NOIR = (0, 0, 0)
VERT = (0, 255, 0)

class Plateau:
    def __init__(self):
        self.plateau = np.zeros((LIGNES, COLONNES))

    def placer_pion(self, ligne, colonne, piece):
        self.plateau[ligne][colonne] = piece

    def emplacement_valide(self, colonne):
        return self.plateau[LIGNES-1][colonne] == 0

    def obtenir_ligne_libre_suivante(self, colonne):
        for ligne in range(LIGNES):
            if self.plateau[ligne][colonne] == 0:
                return ligne

    def est_coup_gagnant(self, piece):
        # Vérifie les lignes
        for ligne in range(LIGNES):
            for colonne in range(COLONNES-3):
                if self.plateau[ligne][colonne] == piece and self.plateau[ligne][colonne+1] == piece and self.plateau[ligne][colonne+2] == piece and self.plateau[ligne][colonne+3] == piece:
                    return [(ligne, colonne), (ligne, colonne+1), (ligne, colonne+2), (ligne, colonne+3)]

        # Vérifie les colonnes
        for ligne in range(LIGNES-3):
            for colonne in range(COLONNES):
                if self.plateau[ligne][colonne] == piece and self.plateau[ligne+1][colonne] == piece and self.plateau[ligne+2][colonne] == piece and self.plateau[ligne+3][colonne] == piece:
                    return [(ligne, colonne), (ligne+1, colonne), (ligne+2, colonne), (ligne+3, colonne)]

        # Vérifie les diagonales ascendantes
        for ligne in range(LIGNES-3):
            for colonne in range(COLONNES-3):
                if self.plateau[ligne][colonne] == piece and self.plateau[ligne+1][colonne+1] == piece and self.plateau[ligne+2][colonne+2] == piece and self.plateau[ligne+3][colonne+3] == piece:
                    return [(ligne, colonne), (ligne+1, colonne+1), (ligne+2, colonne+2), (ligne+3, colonne+3)]

        # Vérifie les diagonales descendantes
        for ligne in range(3, LIGNES):
            for colonne in range(COLONNES-3):
                if self.plateau[ligne][colonne] == piece and self.plateau[ligne-1][colonne+1] == piece and self.plateau[ligne-2][colonne+2] == piece and self.plateau[ligne-3][colonne+3] == piece:
                    return [(ligne, colonne), (ligne-1, colonne+1), (ligne-2, colonne+2), (ligne-3, colonne+3)]

        return []

    def est_plein(self):
        return np.all(self.plateau != 0)

    def reinitialiser(self):
        self.plateau = np.zeros((LIGNES, COLONNES))

    def afficher_plateau(self):
        print(np.flip(self.plateau, 0))


class Joueur:
    def __init__(self, piece):
        self.piece = piece

    def jouer(self, plateau):
        colonne = int(input("Choisissez une colonne (0-6) : "))
        while not plateau.emplacement_valide(colonne):
            colonne = int(input("Colonne invalide. Choisissez une autre colonne (0-6) : "))
        return colonne


# Initialise Pygame
pygame.init()

# Dimensions de la fenêtre
LARGEUR = COLONNES * TAILLE_CELLULE
HAUTEUR = (LIGNES + 1) * TAILLE_CELLULE

# Crée la fenêtre
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

# Police de texte
police = pygame.font.Font(None, 40)

plateau = Plateau()
joueurs = [Joueur(1), Joueur(2)]
joueur_actuel = 0

partie_terminee = False
pions_gagnants = []
rect_rejouer = pygame.Rect(10, 10, 100, 40)
texte_rejouer = police.render("Rejouer", True, NOIR)

while not partie_terminee:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            partie_terminee = True
        elif evenement.type == pygame.MOUSEBUTTONDOWN:
            if not plateau.est_plein() and not pions_gagnants:
                if joueur_actuel == 0:
                    colonne = evenement.pos[0] // TAILLE_CELLULE
                    if plateau.emplacement_valide(colonne):
                        ligne = plateau.obtenir_ligne_libre_suivante(colonne)
                        plateau.placer_pion(ligne, colonne, 1)
                        if plateau.est_coup_gagnant(1):
                            pions_gagnants = plateau.est_coup_gagnant(1)
                            print("Joueur 1 a gagné !")
                        joueur_actuel = 1
                else:
                    colonne = evenement.pos[0] // TAILLE_CELLULE
                    if plateau.emplacement_valide(colonne):
                        ligne = plateau.obtenir_ligne_libre_suivante(colonne)
                        plateau.placer_pion(ligne, colonne, 2)
                        if plateau.est_coup_gagnant(2):
                            pions_gagnants = plateau.est_coup_gagnant(2)
                            print("Joueur 2 a gagné !")
                        joueur_actuel = 0

            if rect_rejouer.collidepoint(evenement.pos):
                plateau.reinitialiser()
                partie_terminee = False
                pions_gagnants = []
                joueur_actuel = 0

    fenetre.fill(BLANC)

    # Dessine les cercles de jeu
    for colonne in range(COLONNES):
        for ligne in range(LIGNES):
            pygame.draw.rect(fenetre, BLEU, (colonne * TAILLE_CELLULE, (ligne + 1) * TAILLE_CELLULE, TAILLE_CELLULE, TAILLE_CELLULE))
            pygame.draw.circle(fenetre, BLANC, (colonne * TAILLE_CELLULE + TAILLE_CELLULE // 2, (ligne + 1) * TAILLE_CELLULE + TAILLE_CELLULE // 2), TAILLE_CELLULE // 2 - 5)

    # Dessine les jetons sur le plateau
    for colonne in range(COLONNES):
        for ligne in range(LIGNES):
            if plateau.plateau[ligne][colonne] == 1:
                pygame.draw.circle(fenetre, ROUGE, (colonne * TAILLE_CELLULE + TAILLE_CELLULE // 2, HAUTEUR - ligne * TAILLE_CELLULE - TAILLE_CELLULE // 2), TAILLE_CELLULE // 2 - 5)
            elif plateau.plateau[ligne][colonne] == 2:
                pygame.draw.circle(fenetre, JAUNE, (colonne * TAILLE_CELLULE + TAILLE_CELLULE // 2, HAUTEUR - ligne * TAILLE_CELLULE - TAILLE_CELLULE // 2), TAILLE_CELLULE // 2 - 5)

    # Dessine les cercles noirs autour des jetons gagnants
    for pion in pions_gagnants:
        ligne, colonne = pion
        pygame.draw.circle(fenetre, NOIR, (colonne * TAILLE_CELLULE + TAILLE_CELLULE // 2, HAUTEUR - ligne * TAILLE_CELLULE - TAILLE_CELLULE // 2), TAILLE_CELLULE // 2 - 5, 3)

    # Dessine le bouton "Rejouer" si la partie est terminée
    if partie_terminee or pions_gagnants or plateau.est_plein():
        pygame.draw.rect(fenetre, VERT, rect_rejouer)
        rect_texte_rejouer = texte_rejouer.get_rect(center=rect_rejouer.center)
        fenetre.blit(texte_rejouer, rect_texte_rejouer)

    pygame.display.update()

pygame.quit()
