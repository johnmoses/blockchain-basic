# Basic Blockchain in Python

This is a basoc implementation of a blockchain in Python, built from scratch. It aims at demonstrating the fundamental concepts of blockchain technology including blocks, hashing, proof of work, and decentralized consensus.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

Blockchain technology has gained significant attention for its potential to revolutionize industries by providing transparent, secure, and decentralized data management solutions. This project serves as an educational tool to understand how blockchain works through practical implementation.

## Features

- **Block Structure**: Each block contains an index, timestamp, data, previous hash, and a nonce.
- **Hashing**: Blocks are linked using cryptographic hashing (SHA-256).
- **Proof of Work**: Implements a basic proof of work algorithm for block mining.
- **Web Interface**: Includes a Flask-based web interface to interact with the blockchain (mine new blocks, view the chain).

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/chinnanj666/blockchain-project.git
   cd blockchain-python
   ```

2. **Install dependencies**:

    Ensure you have Python 3 installed. Install Flask if not already installed:

    ```bash
    pip install flask
    ```

3. **Run the blockchain**:
    Start the Flask server to run the blockchain: python3 your_python_filename.py, in mycase app.py

    ```bash
     python app.py
    ```

    The server will start on <http://127.0.0.1:5000/mine>.

## Usage

1. **Mining a New Block**:
    Open a web browser and navigate to <http://127.0.0.1:5000/mine> to mine a new block.

2. **Viewing the Blockchain**:

    Navigate to <http://127.0.0.1:5000/chain> to view the current state of the blockchain.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
