Key Name         Balance      Pending      Address                                                          
---------------- ------------ ------------ ----------------------------------------------------------------
mining_rewards           19.3    -0.800000 e7b97060861016e216f01d09a1ab204528951e9fde9c2ca946d450747da0c3b5
alvin2-address            0.2    +0.300000 e9338c8ddbeeee28075437eaa1aedc2b18195e86dc9139225d33db53b70265c2
alvin-address             0.5    +0.500000 c32420ff4adec5e3fdc8d039cf5c2607cf1e5bfb112ab722cae245f94076c429

1. Previous pending didn't clear off?
    - need to `sync` for it to clear off
    - wallet sync to latest block
2. Some problem with shutting down, seems like transaction_listener socket

Nice to have:
2. Difficulty is fixed (doesn't increase slowly)
3. Only one miner (need dynamic arg for key name)

BlockchainLoader -
    - load the blockchain.json
    - process the `blockchain` with potential side effects (add new block)
    - save the blockchain.json

UnconfirmedPaymentsLoader -
    - load the blockchain_pending.json

ListAddressesCommand -
    - List the aggregated blockchain.json and blockchain_pending.json group by
      the number of keys (accounts)

crytpo.py
    line 29 __get_address_for_key
    - key 'address' is the public key hash converted to hex

Idiosyncracies:
There's only one blockchain.json and blockchain_pending.json (db)
Even when there's multiple accounts, still one db



