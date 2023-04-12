""" 
Writen by: Trym Varland

module:: start_game.py
    This module contains the if __name__ == "__main__": statement. to start the game.
"""
from screens import Screens
import cProfile


if __name__ == "__main__": 
    """ 
    Starts the game.
    
    cProfile.run('start = Screens.main_manu(Screens)') # Used to profile the game
    """
    start = Screens.main_manu(Screens)
    