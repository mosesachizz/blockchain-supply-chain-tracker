"""
Script to deploy the SupplyChain smart contract.
"""

from src.blockchain.contract import ContractManager
from src.utils.logger import setup_logger

if __name__ == "__main__":
    logger = setup_logger(__name__)
    contract_manager = ContractManager()
    address = contract_manager.deploy_contract()
    logger.info("Deployed at %s", address)