# Uomp Stock Context

[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Chains](https://img.shields.io/badge/Chains-RH%20%7C%20BSC%20%7C%20EVM-lightgrey)](configs/)

**Privacy-preserving portfolio context**

UOMP context provider for portfolio-aware agents: local guard protocol, portfolio profile schema, context signing, cost-basis redaction controls.

## Quick start

```bash
git clone https://github.com/cervemone/uomp-stock-context.git
cd uomp-stock-context
pip install -r requirements.txt
python -m src.main --help
```

## Layout

```
  src/
  guard/
  schemas/
  signing/
  tests/
  docs/
  scripts/
  configs/
  examples/
  integrations/
  benchmarks/
  protocol/
```

## Related

- `stock-token-index` — registry of tokenized equities
- `stock-analyst-agent` — the agent that consumes this repo
- `rh-stock-token-sdk` — SDK for Robinhood Chain stock tokens

## License

MIT
