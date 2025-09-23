"""
Smart contract interaction for supply chain events.
"""

import json
from web3 import Web3
from ..utils.logger import setup_logger
from ..utils.config import Config

class ContractManager:
    """Manages deployment and interaction with the SupplyChain smart contract."""
    
    def __init__(self):
        """Initialize the contract manager."""
        self.logger = setup_logger(__name__)
        self.config = Config()
        self.w3 = Web3(Web3.HTTPProvider(self.config.get("blockchain.rpc_url", "http://127.0.0.1:7545")))
        self.account = self.w3.eth.account.from_key(self.config.get("blockchain.private_key", "0x..."))
        self.w3.eth.default_account = self.account.address
        self.contract_abi = json.loads(self.config.get("blockchain.abi", '[]'))
        self.contract_address = self.config.get("blockchain.contract_address", "")
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=self.contract_abi) if self.contract_address else None

    def deploy_contract(self, contract_path: str = "../contracts/SupplyChain.sol"):
        """Deploy the SupplyChain smart contract."""
        try:
            with open(contract_path, "r") as f:
                source_code = f.read()
            compiled_sol = self.w3.eth.contract_bytecode_auto_deploy(source_code)
            tx_hash = self.w3.eth.contract(abi=self.contract_abi, bytecode=compiled_sol).deploy()
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            self.contract_address = tx_receipt.contractAddress
            self.config.update("blockchain.contract_address", self.contract_address)
            self.contract = self.w3.eth.contract(address=self.contract_address, abi=self.contract_abi)
            self.logger.info("Contract deployed at %s", self.contract_address)
            return self.contract_address
        except Exception as e:
            self.logger.error("Deployment failed: %s", str(e))
            raise

    def create_product(self, name: str, manufacturer: str, status: str):
        """Create a new product in the supply chain."""
        try:
            tx_hash = self.contract.functions.createProduct(name, manufacturer, status).transact()
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            self.logger.info("Product created: %s", tx_hash.hex())
            return tx_hash.hex()
        except Exception as e:
            self.logger.error("Product creation failed: %s", str(e))
            raise

    def transfer_product(self, product_id: int, to_address: str, new_status: str, location: str):
        """Transfer product ownership with status update."""
        try:
            tx_hash = self.contract.functions.transferProduct(
                product_id, self.w3.to_checksum_address(to_address), new_status, location
            ).transact()
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            self.logger.info("Product transferred: %s", tx_hash.hex())
            return tx_hash.hex()
        except Exception as e:
            self.logger.error("Transfer failed: %s", str(e))
            raise

    def get_product(self, product_id: int):
        """Retrieve product details."""
        try:
            product = self.contract.functions.getProduct(product_id).call()
            self.logger.info("Product %d retrieved", product_id)
            return product
        except Exception as e:
            self.logger.error("Product retrieval failed: %s", str(e))
            raise