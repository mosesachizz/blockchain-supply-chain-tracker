"""
Blockchain node management for local development with Ganache.
"""

from web3 import Web3
from ..utils.logger import setup_logger
from ..utils.config import Config

class ChainManager:
    """Manages the local blockchain instance with Ganache."""
    
    def __init__(self):
        """Initialize the chain manager."""
        self.logger = setup_logger(__name__)
        self.config = Config()
        self.rpc_url = self.config.get("blockchain.rpc_url", "http://127.0.0.1:7545")
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))

    def connect(self):
        """Connect to the blockchain node."""
        if self.w3.is_connected():
            self.logger.info("Connected to blockchain at %s", self.rpc_url)
            return True
        else:
            self.logger.error("Failed to connect to blockchain")
            return False

    def get_latest_block(self):
        """Get the latest block number."""
        try:
            latest_block = self.w3.eth.block_number
            self.logger.debug("Latest block: %d", latest_block)
            return latest_block
        except Exception as e:
            self.logger.error("Failed to get latest block: %s", str(e))
            raise

    def mine_block(self):
        """Mine a new block (simulate with Ganache)."""
        try:
            self.w3.eth.generate_block()
            self.logger.info("New block mined")
            return self.get_latest_block()
        except Exception as e:
            self.logger.error("Mining failed: %s", str(e))
            raise