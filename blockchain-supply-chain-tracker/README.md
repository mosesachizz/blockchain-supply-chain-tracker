# Blockchain-based Supply Chain Tracker

A decentralized supply chain tracking system using Python and Ethereum smart contracts. This project enables immutable logging of product events (production, shipment, delivery) on a blockchain, ensuring transparency and tamper-proof records. It includes a Solidity smart contract for event management, Python backend for interactions, CLI simulation, and tests. It also showcases modular architecture, error handling, logging, and CI/CD.

## Problem Statement
Traditional supply chains lack transparency, leading to fraud, delays, and disputes. Blockchain provides an immutable ledger for tracking products from manufacturer to consumer, enabling real-time verification and trust.

## Solution
This project implements a **Blockchain-based Supply Chain Tracker** that:
- **Logs events immutably** using Ethereum smart contracts.
- **Queries history** with full provenance for any product.
- **Simulates flows** with a local Ganache blockchain.
- **Scales with Web3.py** for mainnet integration.
- **Monitors performance** with logging and metrics.

## Tech Stack
- **Python**: Backend logic and Web3 interactions.
- **Solidity**: Smart contracts for event logging.
- **Ethereum/Ganache**: Local blockchain for development.
- **Web3.py**: Contract deployment and queries.
- **PyTest**: Unit and integration testing.
- **YAML**: Configuration management.

## Architecture Decisions
- **Modular Design**: Separates contract, chain, and tracker logic for maintainability.
- **Local Development**: Uses Ganache for simulation without external dependencies.
- **Event-Driven**: Smart contract emits events for verifiable tracking.
- **Security**: Uses private keys for transactions and onlyOwner modifiers.
- **Testing**: Comprehensive tests for contract functions and tracker methods.

## Key Feature: Event Logging
Below is a code snippet from `src/blockchain/tracker.py`, showcasing type hints, error handling, and metrics.

```python
def log_event(self, product_id: int, event_type: str, details: str):
    """Log a supply chain event (e.g., shipped, delivered)."""
    try:
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


---

### Setup and Deployment Instructions

1. **Create Directory Structure**:
```bash
mkdir -p blockchain-supply-chain-tracker/{src/{blockchain,utils},tests,scripts,configs,contracts,ganache}
cd blockchain-supply-chain-tracker

2. **Install Dependencies**:
pip install -r requirements.txt

3. **Start Ganache**:
ganache-cli -p 7545 -a 10 -h 0.0.0.0

4. **Deploy Contract**:
python scripts/deploy_contract.py

5. **Run Simulation**:
python scripts/simulate_chain.py

6. **Run Main App**:
python src/main.py

7. **Run Tests**:
pytest tests/

8. **Push to GitHub**:
git init
git add .
git commit -m "Initial commit: Blockchain Supply Chain Tracker"
git remote add origin https://github.com/mosesachizz/blockchain-supply-chain-tracker.git
git push -u origin main

## License

This project is licensed under the MIT License - see the LICENSE file for details.