// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SupplyChain {
    struct Product {
        uint id;
        string name;
        string manufacturer;
        uint timestamp;
        address owner;
        string status;
        string location;
    }

    Product[] public products;
    mapping(uint => address) public productOwners;

    event ProductCreated(uint id, string name, string manufacturer, string status);
    event ProductTransferred(uint id, address from, address to, string status, string location);

    modifier onlyOwner(uint productId) {
        require(msg.sender == productOwners[productId], "Not the owner");
        _;
    }

    function createProduct(string memory name, string memory manufacturer, string memory status) public {
        uint id = products.length + 1;
        products.push(Product(id, name, manufacturer, block.timestamp, msg.sender, status, ""));
        productOwners[id] = msg.sender;
        emit ProductCreated(id, name, manufacturer, status);
    }

    function transferProduct(uint productId, address to, string memory newStatus, string memory location) public onlyOwner(productId) {
        Product storage product = products[productId - 1];
        address from = product.owner;
        product.status = newStatus;
        product.location = location;
        product.owner = to;
        product.timestamp = block.timestamp;
        productOwners[productId] = to;
        emit ProductTransferred(productId, from, to, newStatus, location);
    }

    function getProduct(uint productId) public view returns (Product memory) {
        require(productId > 0 && productId <= products.length, "Invalid product ID");
        return products[productId - 1];
    }

    function getProductHistory(uint productId) public view returns (Product[] memory) {
        // Simplified: Returns the latest product state (extend for full history if needed)
        require(productId > 0 && productId <= products.length, "Invalid product ID");
        Product[] memory history = new Product[](1);
        history[0] = products[productId - 1];
        return history;
    }
}