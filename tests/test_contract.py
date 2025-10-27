"""
Unit tests for the ContractManager class.
"""

import pytest
from web3 import Web3
from src.blockchain.contract import ContractManager
from src.utils.config import Config

@pytest.fixture
def contract_manager():
    """Fixture for ContractManager instance."""
    config = Config()
    config.config["blockchain"] = {
        "rpc_url": "http://127.0.0.1:7545",
        "private_key": "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80",  # Ganache default
        "abi": json.loads('[{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"manufacturer","type":"string"},{"internalType":"string","name":"status","type":"string"}],"name":"createProduct","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"productId","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"string","name":"newStatus","type":"string"},{"internalType":"string","name":"location","type":"string"}],"name":"transferProduct","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"productId","type":"uint256"}],"name":"getProduct","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"manufacturer","type":"string"},{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"string","name":"status","type":"string"},{"internalType":"string","name":"location","type":"string"}],"internalType":"struct SupplyChain.Product","name":"","type":"tuple"}],"stateMutability":"view","type":"function"}]')
    return ContractManager()

def test_deploy_contract(contract_manager):
    """Test contract deployment."""
    address = contract_manager.deploy_contract()
    assert address is not None

def test_create_product(contract_manager):
    """Test product creation."""
    tx_hash = contract_manager.create_product("Test Product", "Test Manufacturer", "Test Status")
    assert tx_hash is not None