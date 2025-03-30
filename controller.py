from handler import ThrottlingRateLimiter, SlidingWindowRateLimiter, time, random


def simulate_message_flow(rate_limiter, limiter_type: str, messages: int = 20):
    """Simulates a message flow to test the rate limiter."""
    print(f"=== Simulating {limiter_type} Rate Limiter ===")
    for message_id in range(1, messages + 1):
        user_id = message_id % 5 + 1  # Simulating users with IDs 1-5
        result = rate_limiter.record_message(str(user_id))
        wait_time = rate_limiter.time_until_next_allowed(str(user_id))
        print(f"Message {message_id:2d} | User {user_id} | "
              f"{'✓ Sent' if result else f'× Wait {wait_time:.1f}s'}")
        time.sleep(random.uniform(0.1, 1.0))  # Simulating random message delays

    print("Waiting for limit reset...")
    time.sleep(10)
    print(f"=== New batch of messages after waiting ===")
    for message_id in range(messages + 1, messages * 2 + 1):
        user_id = message_id % 5 + 1
        result = rate_limiter.record_message(str(user_id))
        wait_time = rate_limiter.time_until_next_allowed(str(user_id))
        print(f"Message {message_id:2d} | User {user_id} | "
              f"{'✓ Sent' if result else f'× Wait {wait_time:.1f}s'}")
        time.sleep(random.uniform(0.1, 1.0))

if __name__ == "__main__":
    print("Select Rate Limiter: 1 - Sliding Window, 2 - Throttling")
    choice = input("Enter choice: ")
    if choice == "1":
        limiter = SlidingWindowRateLimiter(window_size=10, max_requests=1)
        simulate_message_flow(limiter, "Sliding Window")
    elif choice == "2":
        limiter = ThrottlingRateLimiter(min_interval=10.0)
        simulate_message_flow(limiter, "Throttling")
    else:
        print("Invalid choice. Exiting.")