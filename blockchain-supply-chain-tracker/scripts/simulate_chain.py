"""
Script to simulate a full supply chain tracking flow.
"""

from src.blockchain.tracker import SupplyChainTracker
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

tracker = SupplyChainTracker()
tracker.start_tracking()

# Create product
tx_create = tracker.contract_manager.create_product("Electronics Widget", "Tech Corp", "Manufactured")
tracker.chain_manager.mine_block()

# Log events
tracker.log_event(1, "Shipped", "Factory to Warehouse")
tracker.chain_manager.mine_block()

tracker.log_event(1, "Delivered", "Warehouse to Retailer")
tracker.chain_manager.mine_block()

# Query history
history = tracker.query_history(1)
logger.info("Full history: %s", history)