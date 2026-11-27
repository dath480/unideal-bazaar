# Unideal Bazaar
Look up Hypixel Skyblock Bazaar prices.
Named (appropriately) after observing the prices up in shambles.

## Features
- [x] Fetch the latest prices from the API
- [x] Search the response for the given key and display the price
- [x] Handle the response in-memory instead of writing to disk
- [x] Add error handling for the network request
- [x] Implement not-complete but specific-enough pattern matching
- [x] Implement closest-match suggestion on invalid input
- [x] Cache and reuse the received response in short intervals
- [x] Invalidate and re-populate the cache after a certain duration (e.g. 30 seconds)
- [x] Change the data representation to dictionary of names->prices instead of holding the entire JSON

## Later Features
- [ ] Write tests for the project
- [ ] Move the logic to a backend with an API
- [ ] Implement a frontend interface for the backend
- [ ] Wrap the project in docker for deployment
