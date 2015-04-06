import media.pyganim

PacManAnimRight = media.pyganim.PygAnimation([('media/PacMan.png', 0.1),
                                              ('media/PacMan2.png', 0.1),
                                              ('media/PacMan3.png', 0.1),
                                              ('media/PacMan2.png', 0.1)])
PacManAnimLeft = PacManAnimRight.getCopy()
PacManAnimLeft.flip(True, False)
PacManAnimLeft.makeTransformsPermanent()

PacManAnimDown = media.pyganim.PygAnimation([('media/PacMan4.png', 0.1),
                                             ('media/PacMan5.png', 0.1),
                                             ('media/PacMan6.png', 0.1),
                                             ('media/PacMan5.png', 0.1)])

PacManAnimTop = PacManAnimDown.getCopy()
PacManAnimTop.flip(False, True)
PacManAnimTop.makeTransformsPermanent()

