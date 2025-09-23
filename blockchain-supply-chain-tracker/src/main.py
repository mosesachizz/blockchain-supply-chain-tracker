"""
Entry point for the Blockchain Supply Chain Tracker.
"""

import sys
from blockchain.tracker import SupplyChainTracker
from utils.logger import setup_logger

def main():
    """Main function to run the supply chain simulation."""
    logger = setup_logger(__name__)
    tracker = SupplyChainTracker()
    
    if not tracker.start_tracking():
        logger.error("Failed to start tracker")
        sys.exit(1)
    
    # Example simulation
    product_id = 1
    tx_hash = tracker.contract_manager.create_product("Widget A", "Manufacturer Inc.", "Produced")
    tracker.chain_manager.mine_block()
    
    tracker.log_event(product_id, "Shipped", "Warehouse 1")
    tracker.chain_manager.mine_block()
    
    history = tracker.query_history(product_id)
    logger.info("Product history: %s", history)
    
    logger.info("Simulation complete")

if __name__ == "__main__":
    main()