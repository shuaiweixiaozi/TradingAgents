from datetime import date

from tradingagents.default_config import DEFAULT_CONFIG
from tradingagents.graph.trading_graph import TradingAgentsGraph

config = DEFAULT_CONFIG.copy()

graph = TradingAgentsGraph(
    selected_analysts=["market", "news"],
    config=config,
    debug=True,
)

state, decision = graph.propagate(
    "AAPL",
    date.today().isoformat(),
)

print(decision)
report = graph.save_reports(state, "AAPL")
print(report)