"""
Supply chain tracker for logging and querying events.
"""

from .contract import ContractManager
from .chain import ChainManager
from ..utils.logger import setup_logger
from ..utils.metrics import MetricsCollector

class SupplyChainTracker:
    """Tracks products through the supply chain using blockchain."""
    
    def __init__(self):
        """Initialize the tracker."""
        self.logger = setup_logger(__name__)
        self.contract_manager = ContractManager()
        self.chain_manager = ChainManager()
        self.metrics = MetricsCollector()

    def start_tracking(self):
        """Start the tracking system by connecting to the chain."""
        if self.chain_manager.connect():
            if not self.contract_manager.contract:
                self.contract_manager.deploy_contract()
            self.logger.info("Supply chain tracker started")
            return True
        return False

    def log_event(self, product_id: int, event_type: str, details: str):
        """Log a supply chain event (e.g., shipped, delivered)."""
        try:
            # Simulate transfer for event logging
            to_address = self.contract_manager.account.address  # Current owner
            new_status = event_type
            location = details
            tx_hash = self.contract_manager.transfer_product(product_id, to_address, new_status, location)
            self.chain_manager.mine_block()
            self.metrics.record_event_logged()
            self.logger.info("Event logged for product %d: %s", product_id, event_type)
            return tx_hash
        except Exception as e:
            self.logger.error("Event logging failed: %s", str(e))
            self.metrics.record_error()
            raise

    def query_history(self, product_id: int):
        """Query the full history of a product."""
        try:
            history = self.contract_manager.get_product_history(product_id)
            self.metrics.record_query_success()
            self.logger.info("History queried for product %d", product_id)
            return history
        except Exception as e:
            self.logger.error("History query failed: %s", str(e))
            self.metrics.record_error()
            raise