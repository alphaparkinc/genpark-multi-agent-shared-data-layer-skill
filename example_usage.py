from client import MultiAgentSharedDataLayerClient

def main():
    client = MultiAgentSharedDataLayerClient()
    res = client.sync_shared_record("ecommerce_orders", {"order_id": "ORD-5501", "total_usd": 120.00})
    print(f"Sync Status: {res['sync_status']}")
    print(f"Record ID: {res['record_id']}")

if __name__ == "__main__":
    main()
