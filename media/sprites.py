from pygame.locals import *

from objects.Container import *
import media.pyganim


PacManAnimRight = media.pyganim.PygAnimation([('resources/PacMan.png', 0.1),
                                              ('resources/PacMan2.png', 0.1),
                                              ('resources/PacMan3.png', 0.1),
                                              ('resources/PacMan2.png', 0.1)])
PacManAnimLeft = PacManAnimRight.getCopy()
PacManAnimLeft.flip(True, False)
PacManAnimLeft.makeTransformsPermanent()

PacManAnimDown = media.pyganim.PygAnimation([('resources/PacMan4.png', 0.1),
                                             ('resources/PacMan5.png', 0.1),
                                             ('resources/PacMan6.png', 0.1),
                                             ('resources/PacMan5.png', 0.1)])

PacManAnimTop = PacManAnimDown.getCopy()
PacManAnimTop.flip(False, True)
PacManAnimTop.makeTransformsPermanent()

PacManAnim = {}
PacManAnim[K_UP] = PacManAnimTop
PacManAnim[K_RIGHT] = PacManAnimRight
PacManAnim[K_DOWN] = PacManAnimDown
PacManAnim[K_LEFT] = PacManAnimLeft

