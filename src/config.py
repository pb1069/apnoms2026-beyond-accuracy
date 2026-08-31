"""FROZEN SPEC — APNOMS 2026 Tutorial 1 "Beyond Accuracy"

Every constant here is part of the pinned artifact. Changing any value
invalidates expected_outputs/. Do NOT edit for demo runs.
"""

# ---- dataset geometry -------------------------------------------------
N_TRAIN = 6000
N_TEST = 4000
D = 30                                # 30 flow features, 3 modality groups of 10

# attack indicators (one-sided channels: benign ~ N(0, IND_NOISE), attack shifted)
INDICATORS = [0, 1, 10, 11, 20, 21]
IND_SHIFT = 0.45
IND_NOISE = 0.22

# shortcut feature: near-perfect label correlation in training data
SHORTCUT = 12
U_CLEAN = (0.3, 1.2)                  # clean shortcut strength range
U_BROKEN = (1.40, 1.60)               # evasive samples: stronger AND inverted
SC_JITTER = 0.05
SUPPRESS = 0.25                       # evasion suppresses true indicators to 25%
BROKEN_FRAC = 0.30                    # fraction of evasive samples in test set

# ---- seeds ------------------------------------------------------------
SEED_LABELS = 42
SEED_TRAIN_X = 1
SEED_TEST_X = 2
SEED_DRIFT_X = 7

# ---- baseline model (single MLP, heavily regularized -> soft probs) ---
BASE_HIDDEN = (16,)
BASE_ALPHA = 8.0
BASE_MAX_ITER = 500
BASE_SEED = 0
BASE_TOL = 1e-5

# ---- expert ensemble (diversity-constrained feature subsets) ----------
K_EXPERTS = 40
N_SC_EXPERTS = K_EXPERTS // 4         # only 10/40 experts may see the shortcut
SUB_SIZE = 12
EXPERT_HIDDEN = (8,)
EXPERT_ALPHA = 3e-2
EXPERT_MAX_ITER = 400
EXPERT_TOL = 1e-5
SUBSET_SEED_BASE = 200

# ---- drift scenario ---------------------------------------------------
DRIFT_SIGMAS = [0.0, 1.0, 3.0]
DRIFT_BROKEN_STEP = 0.12              # broken_frac = BROKEN_FRAC + step * sigma
DRIFT_SC_GAIN = 0.35                  # sc_scale   = 1 + gain * sigma
DRIFT_INF_DECAY = 0.25                # inf_scale  = 1 / (1 + decay * sigma)

# ---- verification -----------------------------------------------------
TOLERANCE = 5e-3                      # |result - expected| per metric
