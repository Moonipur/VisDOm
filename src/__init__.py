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
    || LIU     LIU MOOMO  AEAEAEA MOO     MOO     SEE     MOO       MOMOM MOOMOOMOO     LIU     MOOMOOMOO AEAEA  MOOMOOMO  SEE     SEE ||
    ||  LIU   LIU   MOO  AEA      MOO     MOO    SEESE    MOO        MOM      MOOM     LIULI       MOO     AEA  MOO    MOO SEESE   SEE ||
    ||   LIU LIU    MOO   AEAEAE  MOO     MOO   SEE SEE   MOO        MOM     MOO      LIU LIU      MOO     AEA  MOO    MOO SEE SEE SEE ||
    ||    LIULI     MOO       AEA MOO     MOO  SEESEESEE  MOO        MOM   MOOM      LIULIULIU     MOO     AEA  MOO    MOO SEE   SESEE ||
    ||     LIU     MOOMO AEAEAEA   MOOMOOMOO  SEE     SEE MOOMOOMOO MOMOM MOOMOOMOO LIU     LIU    MOO    AEAEA  MOOMOOMO  SEE     SEE ||
    ||                                                                                                                                 ||
    ||                            MOOMOOMO  MOMOMOMO        MOOMOOMO  LIU       LIU MOOMO  AEAEAEAE  MOOMOOM                           ||
    ||                           MOO    MOO MOM            MOO    MOO LIULI   LILIU  MOO  AEA       MOO                                ||
    ||                           MOO    MOO MOMOMO         MOO    MOO LIU LIULI LIU  MOO  AEA        MOOMOO                            ||
    ||                           MOO    MOO MOM            MOO    MOO LIU  LIU  LIU  MOO  AEA            MOO                           ||
    ||                            MOOMOOMO  MOM             MOOMOOMO  LIU   L   LIU MOOMO  AEAEAEAE MOOMOOM                            ||
    ||                                                                                                                                 ||
    ||                                          GIFTGIFTG       MOO     PETCHPETC     MOO                                              ||
    ||                                          GIF    GIF     MOOMO       PET       MOOMO                                             ||
    ||                                          GIF     GIF   MOO MOO      PET      MOO MOO                                            ||
    ||                                          GIF    GIF   MOOMOOMOO     PET     MOOMOOMOO                                           ||
    ||                                          GIFTGIFTG   MOO     MOO    PET    MOO     MOO                                          ||
    ||                                                                                                                                 ||
    ||                                                                                                                                 ||
    ||                                            Visualization of Omics Data (VOD program)                                            ||
    ||                                            Developed by Mr. Songphon Sutthitthasakul                                            ||
    ||                                                                                                                                 ||
    ||                                              >> CMUTEAM : CANCER RESEARCH UNIT <<                                               ||
    ||                                                                                                                       14/4/2023 ||
    -------------------------------------------------------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------------------------------------------------------
    '''
    print(header)