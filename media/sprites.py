from pygame.locals import *

import media.pyganim


PacManAnimRight = media.pyganim.PygAnimation([('resources/pacman/PacMan.png', 0.1),
                                              ('resources/pacman/PacMan2.png', 0.1),
                                              ('resources/pacman/PacMan3.png', 0.1),
                                              ('resources/pacman/PacMan2.png', 0.1)])
PacManAnimLeft = PacManAnimRight.getCopy()
PacManAnimLeft.flip(True, False)
PacManAnimLeft.makeTransformsPermanent()

PacManAnimDown = media.pyganim.PygAnimation([('resources/pacman/PacMan4.png', 0.1),
                                             ('resources/pacman/PacMan5.png', 0.1),
                                             ('resources/pacman/PacMan6.png', 0.1),
                                             ('resources/pacman/PacMan5.png', 0.1)])

PacManDeathAnim = media.pyganim.PygAnimation([('resources/pacman/death_1.png', 0.2),
                                              ('resources/pacman/death_2.png', 0.1),
                                              ('resources/pacman/death_3.png', 0.1),
                                              ('resources/pacman/death_4.png', 0.1),
                                              ('resources/pacman/death_5.png', 0.1),
                                              ('resources/pacman/death_6.png', 0.1),
                                              ('resources/pacman/death_7.png', 0.1),
                                              ('resources/pacman/death_8.png', 0.1),
                                              ('resources/pacman/death_9.png', 0.1),
                                              ('resources/pacman/death_10.png', 0.1),
                                              ('resources/pacman/death_11.png', 0.1)])


PacManAnimTop = PacManAnimDown.getCopy()
PacManAnimTop.flip(False, True)
PacManAnimTop.makeTransformsPermanent()
PacManAnim = {K_UP: PacManAnimTop, K_RIGHT: PacManAnimRight, K_DOWN: PacManAnimDown, K_LEFT: PacManAnimLeft, K_DELETE : PacManDeathAnim}

BlinkyAnimTop = media.pyganim.PygAnimation([('resources/blinky/blinky_up_1.png', 0.1),
                                            ('resources/blinky/blinky_up_2.png', 0.1)])
BlinkyAnimRight = media.pyganim.PygAnimation([('resources/blinky/blinky_right_1.png', 0.1),
                                            ('resources/blinky/blinky_right_2.png', 0.1)])
BlinkyAnimDown = media.pyganim.PygAnimation([('resources/blinky/blinky_down_1.png', 0.1),
                                            ('resources/blinky/blinky_down_2.png', 0.1)])
BlinkyAnimLeft = media.pyganim.PygAnimation([('resources/blinky/blinky_left_1.png', 0.1),
                                            ('resources/blinky/blinky_left_2.png', 0.1)])
BlinkyAnim = {K_UP: BlinkyAnimTop, K_RIGHT: BlinkyAnimRight, K_DOWN: BlinkyAnimDown, K_LEFT: BlinkyAnimLeft, K_DELETE : BlinkyAnimRight}

PinkyAnimTop = media.pyganim.PygAnimation([('resources/pinky/pinky_up_1.png', 0.1),
                                            ('resources/pinky/pinky_up_2.png', 0.1)])
PinkyAnimRight = media.pyganim.PygAnimation([('resources/pinky/pinky_right_1.png', 0.1),
                                            ('resources/pinky/pinky_right_2.png', 0.1)])
PinkyAnimDown = media.pyganim.PygAnimation([('resources/pinky/pinky_down_1.png', 0.1),
                                            ('resources/pinky/pinky_down_2.png', 0.1)])
PinkyAnimLeft = media.pyganim.PygAnimation([('resources/pinky/pinky_left_1.png', 0.1),
                                            ('resources/pinky/pinky_left_2.png', 0.1)])
PinkyAnim = {K_UP: PinkyAnimTop, K_RIGHT: PinkyAnimRight, K_DOWN: PinkyAnimDown, K_LEFT: PinkyAnimLeft, K_DELETE : BlinkyAnimRight}

InkyAnimTop = media.pyganim.PygAnimation([('resources/inky/inky_up_1.png', 0.1),
                                            ('resources/inky/inky_up_2.png', 0.1)])
InkyAnimRight = media.pyganim.PygAnimation([('resources/inky/inky_right_1.png', 0.1),
                                            ('resources/inky/inky_right_2.png', 0.1)])
InkyAnimDown = media.pyganim.PygAnimation([('resources/inky/inky_down_1.png', 0.1),
                                            ('resources/inky/inky_down_2.png', 0.1)])
InkyAnimLeft = media.pyganim.PygAnimation([('resources/inky/inky_left_1.png', 0.1),
                                            ('resources/inky/inky_left_2.png', 0.1)])
InkyAnim = {K_UP: InkyAnimTop, K_RIGHT: InkyAnimRight, K_DOWN: InkyAnimDown, K_LEFT: InkyAnimLeft, K_DELETE : InkyAnimRight}

ClydeAnimTop = media.pyganim.PygAnimation([('resources/clyde/clyde_up_1.png', 0.1),
                                            ('resources/clyde/clyde_up_2.png', 0.1)])
ClydeAnimRight = media.pyganim.PygAnimation([('resources/clyde/clyde_right_1.png', 0.1),
                                            ('resources/clyde/clyde_right_2.png', 0.1)])
ClydeAnimDown = media.pyganim.PygAnimation([('resources/clyde/clyde_down_1.png', 0.1),
                                            ('resources/clyde/clyde_down_2.png', 0.1)])
ClydeAnimLeft = media.pyganim.PygAnimation([('resources/clyde/clyde_left_1.png', 0.1),
                                            ('resources/clyde/clyde_left_2.png', 0.1)])
ClydeAnim = {K_UP: ClydeAnimTop, K_RIGHT: ClydeAnimRight, K_DOWN: ClydeAnimDown, K_LEFT: ClydeAnimLeft, K_DELETE : ClydeAnimRight}
