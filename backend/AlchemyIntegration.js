const { Alchemy, Network } = require("alchemy-sdk");

const config = {
  apiKey: "YOUR_API_KEY",
  network: Network.ETH_MAINNET,
};
const alchemy = new Alchemy(config);

async function main() {
  const latestBlock = await alchemy.core.getBlockNumber();
  console.log("The latest block number is:", latestBlock);
}

main();
