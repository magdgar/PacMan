from pygame.locals import *

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
PacManAnim = {K_UP: PacManAnimTop, K_RIGHT: PacManAnimRight, K_DOWN: PacManAnimDown, K_LEFT: PacManAnimLeft}

BlinkyAnimTop = media.pyganim.PygAnimation([('resources/blinky_up_1.png', 0.1),
                                            ('resources/blinky_up_2.png', 0.1)])
BlinkyAnimRight = media.pyganim.PygAnimation([('resources/blinky_right_1.png', 0.1),
                                            ('resources/blinky_right_2.png', 0.1)])
BlinkyAnimDown = media.pyganim.PygAnimation([('resources/blinky_down_1.png', 0.1),
                                            ('resources/blinky_down_2.png', 0.1)])
BlinkyAnimLeft = media.pyganim.PygAnimation([('resources/blinky_left_1.png', 0.1),
                                            ('resources/blinky_left_2.png', 0.1)])
BlinkyAnim = {K_UP: BlinkyAnimTop, K_RIGHT: BlinkyAnimRight, K_DOWN: BlinkyAnimDown, K_LEFT: BlinkyAnimLeft}

ClydeAnimTop = media.pyganim.PygAnimation([('resources/clyde_up_1.png', 0.1),
                                            ('resources/clyde_up_2.png', 0.1)])
ClydeAnimRight = media.pyganim.PygAnimation([('resources/clyde_right_1.png', 0.1),
                                            ('resources/clyde_right_2.png', 0.1)])
ClydeAnimDown = media.pyganim.PygAnimation([('resources/clyde_down_1.png', 0.1),
                                            ('resources/clyde_down_2.png', 0.1)])
ClydeAnimLeft = media.pyganim.PygAnimation([('resources/clyde_left_1.png', 0.1),
                                            ('resources/clyde_left_2.png', 0.1)])
ClydeAnim = {K_UP: ClydeAnimTop, K_RIGHT: ClydeAnimRight, K_DOWN: ClydeAnimDown, K_LEFT: ClydeAnimLeft}
