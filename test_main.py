# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 1
# Simple Pay Calculator

import os.path
import sys
from main import main

def test_problem_1():

    try:
        exists = os.path.exists("test_main.py")
        assert exists == True
    except:
        sys.exit()

    set_keyboard_input(['poonam'])
    main()
    output = get_display_output()

    assert output == [
            "Input your name ",
            "\npoonam" 
    ]

