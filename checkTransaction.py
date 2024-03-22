import web3

# Get the Ethereum node endpoint
node_endpoint = "https://api.etherscan.io/api/v1/mempool?network={network}"

# Create a web3 instance
web3 = web3.Web3(Web3.HTTPProvider(node_endpoint))

# Get the address to monitor
monitored_address = "0xYOUR_ADDRESS"

# Create a function to check the mempool for transactions of the monitored address
def check_mempool():
    # Get all the transactions in the mempool
    mempool_transactions = web3.eth.get_pending_transactions()

    # Iterate over the transactions
    for transaction in mempool_transactions:
        # Check if the transaction is from the monitored address
        if transaction["to"] == monitored_address:
            # Print the transaction information
            print(transaction)

# Start a loop to check the mempool every 10 seconds
while True:
    check_mempool()
    time.sleep(10)

