"""Synthetic encrypted-traffic-like dataset with a planted shortcut.

Story:
  - 6 "attack indicator" channels (2 per modality group): benign traffic sits
    near 0, attacks shift up. These are the *real* evidence.
  - 1 "shortcut" feature: almost perfectly correlated with the label in the
    training data (think: a superficial fingerprint that happened to separate
    classes during collection).
  - "broken" (evasive) test samples: the shortcut relation is INVERTED and
    exaggerated, while true indicators are suppressed — an attack that spoofs
    the superficial pattern and hides its real behavior (and vice versa for
    benign lookalikes).

The draw order inside make_x is part of the frozen spec (determinism).
"""
import hashlib

import numpy as np

from config import (
    N_TRAIN, N_TEST, D, INDICATORS, IND_SHIFT, IND_NOISE,
    SHORTCUT, U_CLEAN, U_BROKEN, SC_JITTER, SUPPRESS,
    SEED_LABELS,
)


def content_digest(*arrays):
    """Environment-independent dataset hash (array contents, not file bytes)."""
    h = hashlib.sha256()
    for a in arrays:
        h.update(np.ascontiguousarray(a).tobytes())
    return h.hexdigest()


def make_labels():
    rng = np.random.default_rng(SEED_LABELS)
    y_train = rng.integers(0, 2, N_TRAIN)
    y_test = rng.integers(0, 2, N_TEST)
    return y_train, y_test


def make_x(y, seed, broken_frac=0.0, sc_scale=1.0, inf_scale=1.0):
    r = np.random.default_rng(seed)
    n = len(y)
    x = r.normal(0, 1, (n, D))
    sign = y * 2 - 1
    broken = r.random(n) < broken_frac
    ind_gain = np.where(broken, SUPPRESS, 1.0) * inf_scale
    for j in INDICATORS:
        # dedicated indicator channels: benign near 0, attacks shift up
        x[:, j] = r.normal(0, IND_NOISE, n) + IND_SHIFT * y * ind_gain
    u = r.uniform(*U_CLEAN, n)
    sc = u * sign
    sc[broken] = -r.uniform(*U_BROKEN, broken.sum()) * sign[broken]
    x[:, SHORTCUT] = sc * sc_scale + r.normal(0, SC_JITTER, n)
    return x, broken
