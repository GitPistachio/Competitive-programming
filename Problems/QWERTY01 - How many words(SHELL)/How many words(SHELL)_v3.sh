#!/bin/bash

# Project name : SPOJ: QWERTY01 - How many words(SHELL)
# Author       : Wojciech Raszka
# Date created : 2019-03-24
# Description  :
# Status       : Accepted (23483623)
# Tags         : bash
# Comment      : 22

read w
grep $w | wc -l
