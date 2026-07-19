"""ProjectMind research library — evidence frontier continuity.
Author: Haxhijaha, Agim ORCID 0009-0002-3234-7765
"""
from .engine import ProjectMindEngine
from .types import (
    AUTHORITY_VIOLATION,
    CONTINUITY_DRIFT,
    CONTINUITY_OK,
    CONTRACT_MISMATCH,
    INCOMPLETE_EVIDENCE,
    PENDING,
    STALE_FRONTIER,
)
__version__ = "5.0.0"
__all__ = [
    "ProjectMindEngine", "CONTINUITY_OK", "CONTINUITY_DRIFT",
    "AUTHORITY_VIOLATION", "STALE_FRONTIER", "INCOMPLETE_EVIDENCE",
    "CONTRACT_MISMATCH", "PENDING", "__version__",
]
