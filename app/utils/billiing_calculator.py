def calculate_bill(api_calls: int, data_download_size: int, chatbot_interactions: int):
    # Implement your billing calculation logic here
    total_cost = api_calls * 0.1 + data_download_size * 0.01 + chatbot_interactions * 0.05
    return total_cost
