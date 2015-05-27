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

PacManDeathAnim = media.pyganim.PygAnimation([('resources/pac_death_0.png', 0.1),
                                              ('resources/pac_death_1.png', 0.1),
                                              ('resources/pac_death_2.png', 0.1),
                                              ('resources/pac_death_3.png', 0.1),
                                              ('resources/pac_death_4.png', 0.1),
                                              ('resources/pac_death_5.png', 0.1),
                                              ('resources/pac_death_6.png', 0.1),
                                              ('resources/pac_death_7.png', 0.1),
                                              ('resources/pac_death_8.png', 0.1),
                                              ('resources/pac_death_9.png', 0.1),
                                              ('resources/pac_death_10.png', 0.1)])



PacManAnimTop = PacManAnimDown.getCopy()
PacManAnimTop.flip(False, True)
PacManAnimTop.makeTransformsPermanent()
PacManAnim = {K_UP: PacManAnimTop, K_RIGHT: PacManAnimRight, K_DOWN: PacManAnimDown, K_LEFT: PacManAnimLeft, K_DELETE : PacManDeathAnim}

BlinkyAnimTop = media.pyganim.PygAnimation([('resources/blinky_up_1.png', 0.1),
                                            ('resources/blinky_up_2.png', 0.1)])
BlinkyAnimRight = media.pyganim.PygAnimation([('resources/blinky_right_1.png', 0.1),
                                            ('resources/blinky_right_2.png', 0.1)])
BlinkyAnimDown = media.pyganim.PygAnimation([('resources/blinky_down_1.png', 0.1),
                                            ('resources/blinky_down_2.png', 0.1)])
BlinkyAnimLeft = media.pyganim.PygAnimation([('resources/blinky_left_1.png', 0.1),
                                            ('resources/blinky_left_2.png', 0.1)])
BlinkyAnim = {K_UP: BlinkyAnimTop, K_RIGHT: BlinkyAnimRight, K_DOWN: BlinkyAnimDown, K_LEFT: BlinkyAnimLeft}

PinkyAnimTop = media.pyganim.PygAnimation([('resources/pinky_up_1.png', 0.1),
                                            ('resources/pinky_up_2.png', 0.1)])
PinkyAnimRight = media.pyganim.PygAnimation([('resources/pinky_right_1.png', 0.1),
                                            ('resources/pinky_right_2.png', 0.1)])
PinkyAnimDown = media.pyganim.PygAnimation([('resources/pinky_down_1.png', 0.1),
                                            ('resources/pinky_down_2.png', 0.1)])
PinkyAnimLeft = media.pyganim.PygAnimation([('resources/pinky_left_1.png', 0.1),
                                            ('resources/pinky_left_2.png', 0.1)])
PinkyAnim = {K_UP: PinkyAnimTop, K_RIGHT: PinkyAnimRight, K_DOWN: PinkyAnimDown, K_LEFT: PinkyAnimLeft}

InkyAnimTop = media.pyganim.PygAnimation([('resources/inky_up_1.png', 0.1),
                                            ('resources/inky_up_2.png', 0.1)])
InkyAnimRight = media.pyganim.PygAnimation([('resources/inky_right_1.png', 0.1),
                                            ('resources/inky_right_2.png', 0.1)])
InkyAnimDown = media.pyganim.PygAnimation([('resources/inky_down_1.png', 0.1),
                                            ('resources/inky_down_2.png', 0.1)])
InkyAnimLeft = media.pyganim.PygAnimation([('resources/inky_left_1.png', 0.1),
                                            ('resources/inky_left_2.png', 0.1)])
InkyAnim = {K_UP: InkyAnimTop, K_RIGHT: InkyAnimRight, K_DOWN: InkyAnimDown, K_LEFT: InkyAnimLeft}

ClydeAnimTop = media.pyganim.PygAnimation([('resources/clyde_up_1.png', 0.1),
                                            ('resources/clyde_up_2.png', 0.1)])
ClydeAnimRight = media.pyganim.PygAnimation([('resources/clyde_right_1.png', 0.1),
                                            ('resources/clyde_right_2.png', 0.1)])
ClydeAnimDown = media.pyganim.PygAnimation([('resources/clyde_down_1.png', 0.1),
                                            ('resources/clyde_down_2.png', 0.1)])
ClydeAnimLeft = media.pyganim.PygAnimation([('resources/clyde_left_1.png', 0.1),
                                            ('resources/clyde_left_2.png', 0.1)])
ClydeAnim = {K_UP: ClydeAnimTop, K_RIGHT: ClydeAnimRight, K_DOWN: ClydeAnimDown, K_LEFT: ClydeAnimLeft}
