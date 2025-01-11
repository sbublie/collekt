class EbayAdapter:
    def __init__(self, ebay_client):
        self.ebay_client = ebay_client

    def search(self, query):
        return self.ebay_client.search(query)