"""FROZEN SPEC (CIC-IDS2017 track) — companion to config.py.

Same rule applies: every constant is part of the pinned artifact.
"""

# ---- source ----------------------------------------------------------
KAGGLE_DATASET = "chethuhn/network-intrusion-dataset"  # CIC-IDS2017 MachineLearningCSV mirror (anonymous download OK)

# day tags derived from file names (lowercased substring match)
DAY_OF_FILE = {
    "monday": "mon", "tuesday": "tue", "wednesday": "wed",
    "thursday": "thu", "friday": "fri",
}

# ---- cleaning --------------------------------------------------------
LABEL_COL = "Label"
BENIGN = "BENIGN"
DROP_DUPLICATE_COLS = ["Fwd Header Length.1"]

# ---- splits ----------------------------------------------------------
SEED_CIC = 2026
# standard split (demos 1-2): tue+wed+thu pool, stratified subsample
STD_DAYS = ("tue", "wed", "thu")
N_STD_TRAIN = 30000
N_STD_TEST = 15000
# drift split (demo 3): train on tue+wed, evaluate on held-out tue/wed,
# then thu (new attack families), then fri (botnet/portscan/DDoS)
DRIFT_TRAIN_DAYS = ("tue", "wed")
N_DRIFT_TRAIN = 30000
N_DRIFT_EVAL = 10000                          # per evaluation slice

# ---- models (reuse architecture family from config.py) ---------------
CIC_BASE_HIDDEN = (16,)
CIC_BASE_ALPHA = 8.0
CIC_K_EXPERTS = 40
CIC_N_UNRESTRICTED = 10                       # experts allowed to see ALL features
CIC_SUB_SIZE = 24                             # feature-subset size per expert
CIC_EXPERT_HIDDEN = (8,)
CIC_EXPERT_ALPHA = 3e-2
CIC_MAX_ITER = 300
CIC_TOL = 1e-4
# the notorious shortcut candidate in CIC-IDS2017
SHORTCUT_FEATURE = "Destination Port"
