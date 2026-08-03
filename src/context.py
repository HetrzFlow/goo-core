"""Build signed UOMP context for agents."""
import hashlib, json
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class PortfolioEntry:
    ticker: str
    qty: float
    cost_basis: float

@dataclass
class UOMPContext:
    entries: List[PortfolioEntry] = field(default_factory=list)
    profile: str = "moderate"
    horizon_months: int = 12

    def redacted(self) -> Dict:
        # Agent sees tickers + qty, NOT cost basis, unless authorized.
        return {"holdings": [{"ticker": e.ticker, "qty": e.qty} for e in self.entries],
                "profile": self.profile, "horizon_months": self.horizon_months}

    def sign(self, key: bytes) -> str:
        payload = json.dumps(self.redacted(), sort_keys=True).encode()
        return hashlib.sha256(key + payload).hexdigest()
