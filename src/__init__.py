import os, sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.cm import ScalarMappable as sm
import scipy.cluster.hierarchy as sch
import argparse
import math

def Head_prog():
    header = '''
    -------------------------------------------------------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------------------------------------------------------
    ||                                                                                                                                 ||
    || LIEW   LIEW MOOMO  AEAEAEA MOO     MOO     SEE     MOO       MOMOM MOOMOOMOO     LIE     MOOMOOMOO AEAEA  MOOMOOMO  SEE     SEE ||
    || LIEW   LIEW  MOO  AEA      MOO     MOO    SEESE    MOO        MOM      MOOM     LIEWL       MOO     AEA  MOO    MOO SEESE   SEE ||
    ||  LIEW LIEW   MOO   AEAEAE  MOO     MOO   SEE SEE   MOO        MOM     MOO      LIE WLI      MOO     AEA  MOO    MOO SEE SEE SEE ||
    ||    LIEWL     MOO       AEA MOO     MOO  SEESEESEE  MOO        MOM   MOOM      LIELLIEWL     MOO     AEA  MOO    MOO SEE   SESEE ||
    ||     LIE     MOOMO AEAEAEA   MOOMOOMOO  SEE     SEE MOOMOOMOO MOMOM MOOMOOMOO LIEW   LIEW    MOO    AEAEA  MOOMOOMO  SEE     SEE ||
    ||                                                                                                                                 ||
    ||                            MOOMOOMO  MOMOMOMO        MOOMOOMO  LIEW     LIEW MOOMO  AEAEAEAE  MOOMOOM                           ||
    ||                           MOO    MOO MOM            MOO    MOO LIEWL   LIEWL  MOO  AEA       MOO                                ||
    ||                           MOO    MOO MOMOMO         MOO    MOO LIE LIEWL LIE  MOO  AEA        MOOMOO                            ||
    ||                           MOO    MOO MOM            MOO    MOO LIE  LIE  LIE  MOO  AEA            MOO                           ||
    ||                            MOOMOOMO  MOM             MOOMOOMO  LIE   L   LIE MOOMO  AEAEAEAE MOOMOOM                            ||
    ||                                                                                                                                 ||
    ||                                          GIFTGIFTG       MOO     PETCHPETC     MOO                                              ||
    ||                                          GIF    GIF     MOOMO       PET       MOOMO                                             ||
    ||                                          GIF     GIF   MOO MOO      PET      MOO MOO                                            ||
    ||                                          GIF    GIF   MOOMOOMOO     PET     MOOMOOMOO                                           ||
    ||                                          GIFTGIFTG   MOO     MOO    PET    MOO     MOO                                          ||
    ||                                                                                                                                 ||
    ||                                                                                                                                 ||
    ||                                           Visualization of Omics Data (VisOm program)                                           ||
    ||                                            Developed by Mr. Songphon Sutthitthasakul                                            ||
    ||                                                                                                                                 ||
    ||                                              >> CMUTEAM : CANCER RESEARCH UNIT <<                                               ||
    ||                                                                                                                       14/4/2023 ||
    -------------------------------------------------------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------------------------------------------------------
    '''
    print(header)