# ============================================================
#  app.py — Version Streamlit complète, stable et sécurisée
# ============================================================

import streamlit as st
import json
import os
from datetime import datetime
from io import BytesIO
import pandas as pd

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import simpleSplit

import qrcode


# ------------------------------------------------------------
# 1) COLLER ICI TON RAW_DATA COMPLET
# ------------------------------------------------------------

RAW_DATA = [
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 48,
        "WPj_g": 430,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 420,
        "WfWPj_Neutre_g": 430,
        "WfWPj_Contrôle_g": 440,
        "Cadrage_renvoyé_WPj": 430,
        "Cadrage_Puissance": 420,
        "Cadrage_Neutre": 430,
        "Cadrage_Contrôle": 440,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 49,
        "WPj_g": 431,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 421,
        "WfWPj_Neutre_g": 431,
        "WfWPj_Contrôle_g": 441,
        "Cadrage_renvoyé_WPj": 430,
        "Cadrage_Puissance": 420,
        "Cadrage_Neutre": 430,
        "Cadrage_Contrôle": 440,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 50,
        "WPj_g": 431,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 421,
        "WfWPj_Neutre_g": 431,
        "WfWPj_Contrôle_g": 441,
        "Cadrage_renvoyé_WPj": 430,
        "Cadrage_Puissance": 420,
        "Cadrage_Neutre": 430,
        "Cadrage_Contrôle": 440,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 51,
        "WPj_g": 432,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 422,
        "WfWPj_Neutre_g": 432,
        "WfWPj_Contrôle_g": 442,
        "Cadrage_renvoyé_WPj": 430,
        "Cadrage_Puissance": 420,
        "Cadrage_Neutre": 430,
        "Cadrage_Contrôle": 440,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 52,
        "WPj_g": 432,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 422,
        "WfWPj_Neutre_g": 432,
        "WfWPj_Contrôle_g": 442,
        "Cadrage_renvoyé_WPj": 430,
        "Cadrage_Puissance": 420,
        "Cadrage_Neutre": 430,
        "Cadrage_Contrôle": 440,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 53,
        "WPj_g": 433,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 423,
        "WfWPj_Neutre_g": 433,
        "WfWPj_Contrôle_g": 443,
        "Cadrage_renvoyé_WPj": 430,
        "Cadrage_Puissance": 420,
        "Cadrage_Neutre": 430,
        "Cadrage_Contrôle": 440,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 54,
        "WPj_g": 433,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 423,
        "WfWPj_Neutre_g": 433,
        "WfWPj_Contrôle_g": 443,
        "Cadrage_renvoyé_WPj": 430,
        "Cadrage_Puissance": 420,
        "Cadrage_Neutre": 430,
        "Cadrage_Contrôle": 440,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 55,
        "WPj_g": 434,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 424,
        "WfWPj_Neutre_g": 434,
        "WfWPj_Contrôle_g": 444,
        "Cadrage_renvoyé_WPj": 430,
        "Cadrage_Puissance": 420,
        "Cadrage_Neutre": 430,
        "Cadrage_Contrôle": 440,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 56,
        "WPj_g": 434,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 424,
        "WfWPj_Neutre_g": 434,
        "WfWPj_Contrôle_g": 444,
        "Cadrage_renvoyé_WPj": 430,
        "Cadrage_Puissance": 420,
        "Cadrage_Neutre": 430,
        "Cadrage_Contrôle": 440,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 57,
        "WPj_g": 435,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 425,
        "WfWPj_Neutre_g": 435,
        "WfWPj_Contrôle_g": 445,
        "Cadrage_renvoyé_WPj": 430,
        "Cadrage_Puissance": 420,
        "Cadrage_Neutre": 430,
        "Cadrage_Contrôle": 440,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 58,
        "WPj_g": 435,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 425,
        "WfWPj_Neutre_g": 435,
        "WfWPj_Contrôle_g": 445,
        "Cadrage_renvoyé_WPj": 430,
        "Cadrage_Puissance": 420,
        "Cadrage_Neutre": 430,
        "Cadrage_Contrôle": 440,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 59,
        "WPj_g": 436,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 426,
        "WfWPj_Neutre_g": 436,
        "WfWPj_Contrôle_g": 446,
        "Cadrage_renvoyé_WPj": 430,
        "Cadrage_Puissance": 420,
        "Cadrage_Neutre": 430,
        "Cadrage_Contrôle": 440,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 60,
        "WPj_g": 437,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 427,
        "WfWPj_Neutre_g": 437,
        "WfWPj_Contrôle_g": 447,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 61,
        "WPj_g": 437,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 427,
        "WfWPj_Neutre_g": 437,
        "WfWPj_Contrôle_g": 447,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 62,
        "WPj_g": 438,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 428,
        "WfWPj_Neutre_g": 438,
        "WfWPj_Contrôle_g": 448,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 63,
        "WPj_g": 438,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 428,
        "WfWPj_Neutre_g": 438,
        "WfWPj_Contrôle_g": 448,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 64,
        "WPj_g": 439,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 429,
        "WfWPj_Neutre_g": 439,
        "WfWPj_Contrôle_g": 449,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 65,
        "WPj_g": 439,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 429,
        "WfWPj_Neutre_g": 439,
        "WfWPj_Contrôle_g": 449,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 66,
        "WPj_g": 440,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 430,
        "WfWPj_Neutre_g": 440,
        "WfWPj_Contrôle_g": 450,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 67,
        "WPj_g": 440,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 430,
        "WfWPj_Neutre_g": 440,
        "WfWPj_Contrôle_g": 450,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 68,
        "WPj_g": 441,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 431,
        "WfWPj_Neutre_g": 441,
        "WfWPj_Contrôle_g": 451,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 69,
        "WPj_g": 441,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 431,
        "WfWPj_Neutre_g": 441,
        "WfWPj_Contrôle_g": 451,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 70,
        "WPj_g": 442,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 432,
        "WfWPj_Neutre_g": 442,
        "WfWPj_Contrôle_g": 452,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 71,
        "WPj_g": 442,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 432,
        "WfWPj_Neutre_g": 442,
        "WfWPj_Contrôle_g": 452,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 72,
        "WPj_g": 443,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 433,
        "WfWPj_Neutre_g": 443,
        "WfWPj_Contrôle_g": 453,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 73,
        "WPj_g": 444,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 434,
        "WfWPj_Neutre_g": 444,
        "WfWPj_Contrôle_g": 454,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 74,
        "WPj_g": 444,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 434,
        "WfWPj_Neutre_g": 444,
        "WfWPj_Contrôle_g": 454,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 75,
        "WPj_g": 445,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 435,
        "WfWPj_Neutre_g": 445,
        "WfWPj_Contrôle_g": 455,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 76,
        "WPj_g": 445,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 435,
        "WfWPj_Neutre_g": 445,
        "WfWPj_Contrôle_g": 455,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 77,
        "WPj_g": 446,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 436,
        "WfWPj_Neutre_g": 446,
        "WfWPj_Contrôle_g": 456,
        "Cadrage_renvoyé_WPj": 440,
        "Cadrage_Puissance": 430,
        "Cadrage_Neutre": 440,
        "Cadrage_Contrôle": 450,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 78,
        "WPj_g": 446,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 436,
        "WfWPj_Neutre_g": 446,
        "WfWPj_Contrôle_g": 456,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 79,
        "WPj_g": 447,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 437,
        "WfWPj_Neutre_g": 447,
        "WfWPj_Contrôle_g": 457,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 80,
        "WPj_g": 447,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 437,
        "WfWPj_Neutre_g": 447,
        "WfWPj_Contrôle_g": 457,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 81,
        "WPj_g": 448,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 438,
        "WfWPj_Neutre_g": 448,
        "WfWPj_Contrôle_g": 458,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 82,
        "WPj_g": 448,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 438,
        "WfWPj_Neutre_g": 448,
        "WfWPj_Contrôle_g": 458,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 83,
        "WPj_g": 449,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 439,
        "WfWPj_Neutre_g": 449,
        "WfWPj_Contrôle_g": 459,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 84,
        "WPj_g": 450,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 440,
        "WfWPj_Neutre_g": 450,
        "WfWPj_Contrôle_g": 460,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 85,
        "WPj_g": 450,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 440,
        "WfWPj_Neutre_g": 450,
        "WfWPj_Contrôle_g": 460,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 86,
        "WPj_g": 451,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 441,
        "WfWPj_Neutre_g": 451,
        "WfWPj_Contrôle_g": 461,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 87,
        "WPj_g": 451,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 441,
        "WfWPj_Neutre_g": 451,
        "WfWPj_Contrôle_g": 461,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 88,
        "WPj_g": 452,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 442,
        "WfWPj_Neutre_g": 452,
        "WfWPj_Contrôle_g": 462,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 89,
        "WPj_g": 452,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 442,
        "WfWPj_Neutre_g": 452,
        "WfWPj_Contrôle_g": 462,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 90,
        "WPj_g": 453,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 443,
        "WfWPj_Neutre_g": 453,
        "WfWPj_Contrôle_g": 463,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 91,
        "WPj_g": 453,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 443,
        "WfWPj_Neutre_g": 453,
        "WfWPj_Contrôle_g": 463,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 92,
        "WPj_g": 454,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 444,
        "WfWPj_Neutre_g": 454,
        "WfWPj_Contrôle_g": 464,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 93,
        "WPj_g": 454,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 444,
        "WfWPj_Neutre_g": 454,
        "WfWPj_Contrôle_g": 464,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 94,
        "WPj_g": 455,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 445,
        "WfWPj_Neutre_g": 455,
        "WfWPj_Contrôle_g": 465,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 95,
        "WPj_g": 456,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 446,
        "WfWPj_Neutre_g": 456,
        "WfWPj_Contrôle_g": 466,
        "Cadrage_renvoyé_WPj": 450,
        "Cadrage_Puissance": 440,
        "Cadrage_Neutre": 450,
        "Cadrage_Contrôle": 460,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 96,
        "WPj_g": 456,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 446,
        "WfWPj_Neutre_g": 456,
        "WfWPj_Contrôle_g": 466,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 97,
        "WPj_g": 457,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 447,
        "WfWPj_Neutre_g": 457,
        "WfWPj_Contrôle_g": 467,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 98,
        "WPj_g": 457,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 447,
        "WfWPj_Neutre_g": 457,
        "WfWPj_Contrôle_g": 467,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 99,
        "WPj_g": 458,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 448,
        "WfWPj_Neutre_g": 458,
        "WfWPj_Contrôle_g": 468,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 100,
        "WPj_g": 458,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 448,
        "WfWPj_Neutre_g": 458,
        "WfWPj_Contrôle_g": 468,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 101,
        "WPj_g": 459,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 449,
        "WfWPj_Neutre_g": 459,
        "WfWPj_Contrôle_g": 469,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 102,
        "WPj_g": 459,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 449,
        "WfWPj_Neutre_g": 459,
        "WfWPj_Contrôle_g": 469,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 103,
        "WPj_g": 460,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 450,
        "WfWPj_Neutre_g": 460,
        "WfWPj_Contrôle_g": 470,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 104,
        "WPj_g": 460,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 450,
        "WfWPj_Neutre_g": 460,
        "WfWPj_Contrôle_g": 470,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 105,
        "WPj_g": 461,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 451,
        "WfWPj_Neutre_g": 461,
        "WfWPj_Contrôle_g": 471,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 106,
        "WPj_g": 462,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 452,
        "WfWPj_Neutre_g": 462,
        "WfWPj_Contrôle_g": 472,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 107,
        "WPj_g": 462,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 452,
        "WfWPj_Neutre_g": 462,
        "WfWPj_Contrôle_g": 472,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 108,
        "WPj_g": 463,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 453,
        "WfWPj_Neutre_g": 463,
        "WfWPj_Contrôle_g": 473,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 109,
        "WPj_g": 463,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 453,
        "WfWPj_Neutre_g": 463,
        "WfWPj_Contrôle_g": 473,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 110,
        "WPj_g": 464,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 454,
        "WfWPj_Neutre_g": 464,
        "WfWPj_Contrôle_g": 474,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 111,
        "WPj_g": 464,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 454,
        "WfWPj_Neutre_g": 464,
        "WfWPj_Contrôle_g": 474,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 112,
        "WPj_g": 465,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 455,
        "WfWPj_Neutre_g": 465,
        "WfWPj_Contrôle_g": 475,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 113,
        "WPj_g": 465,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 455,
        "WfWPj_Neutre_g": 465,
        "WfWPj_Contrôle_g": 475,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 114,
        "WPj_g": 466,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 456,
        "WfWPj_Neutre_g": 466,
        "WfWPj_Contrôle_g": 476,
        "Cadrage_renvoyé_WPj": 460,
        "Cadrage_Puissance": 450,
        "Cadrage_Neutre": 460,
        "Cadrage_Contrôle": 470,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 115,
        "WPj_g": 466,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 456,
        "WfWPj_Neutre_g": 466,
        "WfWPj_Contrôle_g": 476,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 116,
        "WPj_g": 467,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 457,
        "WfWPj_Neutre_g": 467,
        "WfWPj_Contrôle_g": 477,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 117,
        "WPj_g": 468,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 458,
        "WfWPj_Neutre_g": 468,
        "WfWPj_Contrôle_g": 478,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 118,
        "WPj_g": 468,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 458,
        "WfWPj_Neutre_g": 468,
        "WfWPj_Contrôle_g": 478,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 119,
        "WPj_g": 469,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 459,
        "WfWPj_Neutre_g": 469,
        "WfWPj_Contrôle_g": 479,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 120,
        "WPj_g": 469,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 459,
        "WfWPj_Neutre_g": 469,
        "WfWPj_Contrôle_g": 479,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 121,
        "WPj_g": 470,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 460,
        "WfWPj_Neutre_g": 470,
        "WfWPj_Contrôle_g": 480,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 122,
        "WPj_g": 470,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 460,
        "WfWPj_Neutre_g": 470,
        "WfWPj_Contrôle_g": 480,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 123,
        "WPj_g": 471,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 461,
        "WfWPj_Neutre_g": 471,
        "WfWPj_Contrôle_g": 481,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 124,
        "WPj_g": 471,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 461,
        "WfWPj_Neutre_g": 471,
        "WfWPj_Contrôle_g": 481,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 125,
        "WPj_g": 472,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 462,
        "WfWPj_Neutre_g": 472,
        "WfWPj_Contrôle_g": 482,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 126,
        "WPj_g": 472,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 462,
        "WfWPj_Neutre_g": 472,
        "WfWPj_Contrôle_g": 482,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 127,
        "WPj_g": 473,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 463,
        "WfWPj_Neutre_g": 473,
        "WfWPj_Contrôle_g": 483,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 128,
        "WPj_g": 473,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 463,
        "WfWPj_Neutre_g": 473,
        "WfWPj_Contrôle_g": 483,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 129,
        "WPj_g": 474,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 464,
        "WfWPj_Neutre_g": 474,
        "WfWPj_Contrôle_g": 484,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 130,
        "WPj_g": 475,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 465,
        "WfWPj_Neutre_g": 475,
        "WfWPj_Contrôle_g": 485,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 131,
        "WPj_g": 475,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 465,
        "WfWPj_Neutre_g": 475,
        "WfWPj_Contrôle_g": 485,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 132,
        "WPj_g": 476,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 466,
        "WfWPj_Neutre_g": 476,
        "WfWPj_Contrôle_g": 486,
        "Cadrage_renvoyé_WPj": 470,
        "Cadrage_Puissance": 460,
        "Cadrage_Neutre": 470,
        "Cadrage_Contrôle": 480,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 133,
        "WPj_g": 476,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 466,
        "WfWPj_Neutre_g": 476,
        "WfWPj_Contrôle_g": 486,
        "Cadrage_renvoyé_WPj": 480,
        "Cadrage_Puissance": 470,
        "Cadrage_Neutre": 480,
        "Cadrage_Contrôle": 490,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 134,
        "WPj_g": 477,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 467,
        "WfWPj_Neutre_g": 477,
        "WfWPj_Contrôle_g": 487,
        "Cadrage_renvoyé_WPj": 480,
        "Cadrage_Puissance": 470,
        "Cadrage_Neutre": 480,
        "Cadrage_Contrôle": 490,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 135,
        "WPj_g": 477,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 467,
        "WfWPj_Neutre_g": 477,
        "WfWPj_Contrôle_g": 487,
        "Cadrage_renvoyé_WPj": 480,
        "Cadrage_Puissance": 470,
        "Cadrage_Neutre": 480,
        "Cadrage_Contrôle": 490,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 136,
        "WPj_g": 478,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 468,
        "WfWPj_Neutre_g": 478,
        "WfWPj_Contrôle_g": 488,
        "Cadrage_renvoyé_WPj": 480,
        "Cadrage_Puissance": 470,
        "Cadrage_Neutre": 480,
        "Cadrage_Contrôle": 490,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 137,
        "WPj_g": 478,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 468,
        "WfWPj_Neutre_g": 478,
        "WfWPj_Contrôle_g": 488,
        "Cadrage_renvoyé_WPj": 480,
        "Cadrage_Puissance": 470,
        "Cadrage_Neutre": 480,
        "Cadrage_Contrôle": 490,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 138,
        "WPj_g": 479,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 469,
        "WfWPj_Neutre_g": 479,
        "WfWPj_Contrôle_g": 489,
        "Cadrage_renvoyé_WPj": 480,
        "Cadrage_Puissance": 470,
        "Cadrage_Neutre": 480,
        "Cadrage_Contrôle": 490,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 139,
        "WPj_g": 479,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 469,
        "WfWPj_Neutre_g": 479,
        "WfWPj_Contrôle_g": 489,
        "Cadrage_renvoyé_WPj": 480,
        "Cadrage_Puissance": 470,
        "Cadrage_Neutre": 480,
        "Cadrage_Contrôle": 490,
    },
    {
        "Pj_min_kg": 48,
        "Pj_max_kg": 140,
        "W_min_g": 430,
        "W_max_g": 480,
        "Pj_kg": 140,
        "WPj_g": 480,
        "style_de_jeuinterne_g": 10,
        "Puissance": -1,
        "Neutre": 0,
        "Contrôle": 1,
        "WfWPj_Puissance_g": 470,
        "WfWPj_Neutre_g": 480,
        "WfWPj_Contrôle_g": 490,
        "Cadrage_renvoyé_WPj": 480,
        "Cadrage_Puissance": 470,
        "Cadrage_Neutre": 480,
        "Cadrage_Contrôle": 490,
    },
]



# ------------------------------------------------------------
# 2) URL FIXE POUR LE QR CODE (TON SITE INTERNET)
# ------------------------------------------------------------
URL_QR = "https://recommandation-poids-pala-mbx6hsengztr5ywqbgdfku.streamlit.app/"   # <<< MODIFIE ICI >>>


# ============================================================
# 3) GESTION DES STATS (LOCAL)
# ============================================================

STATS_FILE = "stats.json"

def charger_stats():
    stats_defaut = {
        "nb_visites": 0,
        "nb_exports_pdf": 0,
        "derniere_visite": "Jamais"
    }

    if not os.path.exists(STATS_FILE):
        with open(STATS_FILE, "w") as f:
            json.dump(stats_defaut, f, indent=4)
        return stats_defaut

    with open(STATS_FILE, "r") as f:
        stats = json.load(f)

    # Correction automatique
    for cle, valeur in stats_defaut.items():
        if cle not in stats:
            stats[cle] = valeur

    sauvegarder_stats(stats)
    return stats


def sauvegarder_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)


def incrementer_visite():
    stats = charger_stats()
    stats["nb_visites"] += 1
    stats["derniere_visite"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sauvegarder_stats(stats)


def incrementer_export_pdf():
    stats = charger_stats()
    stats["nb_exports_pdf"] += 1
    sauvegarder_stats(stats)


# ============================================================
# 4) GESTION DES JOUEURS (LOCAL)
# ============================================================

JOUEURS_FILE = "joueurs.json"

def charger_joueurs():
    if not os.path.exists(JOUEURS_FILE):
        with open(JOUEURS_FILE, "w") as f:
            json.dump([], f)
        return []
    with open(JOUEURS_FILE, "r") as f:
        return json.load(f)


def sauvegarder_joueur(nom, prenom, poids, style, poids_pala_poids, poids_pala_style):
    joueurs = charger_joueurs()
    joueurs.append({
        "nom": nom,
        "prenom": prenom,
        "poids": poids,
        "style": style,
        "pala_poids": poids_pala_poids,
        "pala_style": poids_pala_style,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    with open(JOUEURS_FILE, "w") as f:
        json.dump(joueurs, f, indent=4)


# ============================================================
# 5) FONCTIONS DE RECHERCHE
# ============================================================

def get_row_by_weight(poids):
    for row in RAW_DATA:
        if row.get("Pj_kg") == poids:
            return row
    return None


def get_recommandation(poids, style):
    row = get_row_by_weight(poids)
    if row is None:
        return None

    poids_pala_selon_poids = row["Cadrage_renvoyé_WPj"]

    style_lower = style.lower()
    if style_lower == "puissance":
        poids_pala_selon_style = row["Cadrage_Puissance"]
    elif style_lower == "neutre":
        poids_pala_selon_style = row["Cadrage_Neutre"]
    elif style_lower in ("contrôle", "controle"):
        poids_pala_selon_style = row["Cadrage_Contrôle"]
    else:
        return None

    return poids_pala_selon_poids, poids_pala_selon_style


# ============================================================
# 6) EXPORT PDF
# ============================================================

def generate_pdf(contenu_popup):
    incrementer_export_pdf()

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, height - 40, "Recommandation de pala – Résumé joueur")

    c.setFont("Helvetica", 11)

    y = height - 80
    max_width = width - 80

    lignes = contenu_popup.split("\n")

    for line in lignes:
        wrapped_lines = simpleSplit(line, "Helvetica", 11, max_width)

        for wl in wrapped_lines:
            if y < 40:
                c.showPage()
                c.setFont("Helvetica", 11)
                y = height - 40

            c.drawString(40, y, wl)
            y -= 18

        y -= 6

    c.save()
    buffer.seek(0)
    return buffer


# ============================================================
# 7) QR CODE
# ============================================================

def generate_qr_code(url):
    img = qrcode.make(url)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer


# ============================================================
# 8) INTERFACE STREAMLIT
# ============================================================

st.set_page_config(page_title="Poids Pala", page_icon="🏓", layout="centered")

incrementer_visite()

st.title("Application Poids Pala — Version Web")

nom = st.text_input("Nom")
prenom = st.text_input("Prénom")
poids = st.number_input("Poids du joueur (kg)", min_value=48, max_value=140, step=1, value=70)
style = st.selectbox("Style de jeu", ["Puissance", "Neutre", "Contrôle"], index=1)

st.markdown("---")

if "contenu_popup" not in st.session_state:
    st.session_state["contenu_popup"] = ""


# ------------------------------------------------------------
# VALIDATION
# ------------------------------------------------------------
if st.button("Valider"):
    if not nom or not prenom:
        st.error("Veuillez entrer le nom et le prénom.")
    else:
        result = get_recommandation(int(poids), style)

        if result is None:
            st.error("Aucune donnée trouvée pour ce poids.")
        else:
            poids_pala_poids, poids_pala_style = result

            contenu_popup = (
                f"Joueur : {prenom} {nom}\n"
                f"Poids : {poids} Kg\n"
                f"Style de jeu : {style}\n\n"
                f"Poids de la pala selon le poids : {poids_pala_poids} g\n"
                f"Poids de la pala selon le style : {poids_pala_style} g"
            )

            st.session_state["contenu_popup"] = contenu_popup

            st.success("Recommandation générée avec succès.")
            st.text_area("Résumé", contenu_popup, height=350, key="resume_calc")

            pdf_buffer = generate_pdf(contenu_popup)
            st.download_button(
                label="📄 Télécharger le PDF",
                data=pdf_buffer,
                file_name=f"recommandation_{prenom}_{nom}.pdf",
                mime="application/pdf"
            )

            sauvegarder_joueur(nom, prenom, int(poids), style, poids_pala_poids, poids_pala_style)


# ------------------------------------------------------------
# RÉAFFICHAGE DU RÉSUMÉ
# ------------------------------------------------------------
if st.session_state["contenu_popup"]:
    st.text_area("Résumé", st.session_state["contenu_popup"], height=350, key="resume_session")


# ------------------------------------------------------------
# LISTE DES JOUEURS PUBLIC
# ------------------------------------------------------------
#st.markdown("---")
#st.subheader("📋 Liste des joueurs enregistrés")

#joueurs = charger_joueurs()
#
#if joueurs:
#    for j in joueurs:
#        st.write(
 #           f"**{j['prenom']} {j['nom']}** — {j['poids']} kg — {j['style']} — "
 #           f"Pala poids: {j['pala_poids']} g — Style: {j['pala_style']} g — "
 #           f"({j['date']})"
 #       )
#else:
#    st.write("Aucun joueur enregistré pour le moment.")


# ------------------------------------------------------------
# QR CODE FIXE (TON SITE INTERNET)
# ------------------------------------------------------------
st.markdown("---")
st.subheader("Scanner pour ouvrir l'application")

qr_buffer = generate_qr_code(URL_QR)
st.image(qr_buffer, caption=URL_QR, width=250)



# ------------------------------------------------------------
# ZONE PRIVÉE — uniquement si ?admin=1
# ------------------------------------------------------------
st.markdown("---")

params = st.query_params
is_admin = params.get("admin") == "1"

if is_admin:

    st.subheader("Zone privée (admin)")

    # ------------------------------------------------------------
    # STATISTIQUES PRIVÉES
    # ------------------------------------------------------------
    stats = charger_stats()
    st.markdown("### 📊 Statistiques d'utilisation")
    st.write(stats)

    # ------------------------------------------------------------
    # LIENS PERSONNELS (en commentaires pour le moment)
    # ------------------------------------------------------------
 #    st.markdown("### 🔗 Mes liens personnels")
 #
 #    st.write("Profil LinkedIn :")
 #    st.code("# https://www.linkedin.com/in/ton-profil", language="text")
 #
   # st.write("Post LinkedIn :")
   # st.code("# https://www.linkedin.com/posts/ton-post", language="text")
 # #
   # st.write("Site internet :")
   # st.code("# https://www.ton-site.fr", language="text")

    # ------------------------------------------------------------
    # LISTE PRIVÉE DES JOUEURS
    # ------------------------------------------------------------
    st.markdown("### 📋 Liste des joueurs enregistrés")

    joueurs = charger_joueurs()

    if joueurs:
        for j in joueurs:
            st.write(
                f"**{j['prenom']} {j['nom']}** — {j['poids']} kg — {j['style']} — "
                f"Pala poids : {j['pala_poids']} g — Style : {j['pala_style']} g — "
                f"({j['date']})"
            )
    else:
        st.write("Aucun joueur enregistré pour le moment.")

    # ------------------------------------------------------------
    # EXPORT EXCEL
    # ------------------------------------------------------------
    if joueurs:
        df = pd.DataFrame(joueurs)

        excel_buffer = BytesIO()
        df.to_excel(excel_buffer, index=False)
        excel_buffer.seek(0)

        st.download_button(
            label="📥 Télécharger les données en Excel",
            data=excel_buffer,
            file_name="joueurs_palas.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

else:
    st.caption("Zone réservée à l'administrateur.")



