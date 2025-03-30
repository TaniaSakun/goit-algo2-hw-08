# goit-algo2-hw-08
The repository for the 8th GoItNeo Design and Analysis of Algorithms homework

### Task 1:  Implementation of a Rate Limiter using the Sliding Window algorithm to limit the frequency of messages in a chat.

In the chat system, a mechanism to limit users' message frequency to prevent spam must be implemented. The implementation should use the Sliding Window algorithm for precise control of time intervals, which allows tracking the number of messages within a given time window and restricting users from sending messages if the limit is exceeded.

#### Requirements:

1. The implementation should use the Sliding Window algorithm for precise time interval control.

2. Basic system parameters: window size (window_size) — 10 seconds and maximum number of messages in the window (max_requests) — 1.

3. Implement the SlidingWindowRateLimiter class.

4. Implement the class methods:

- _cleanup_window — for clearing outdated requests from the window and updating the active time window;

- can_send_message — for checking the ability to send a message in the current time window;

- record_message — for recording a new message and updating the user's history;

- time_until_next_allowed — for calculating the waiting time until the next message can be sent.

5. Data structure for storing message history — collections.deque.

#### Results:
```
Select Rate Limiter: 1 - Sliding Window, 2 - Throttling
Enter choice: 1
=== Simulating Sliding Window Rate Limiter ===
Message  1 | User 2 | ✓ Sent
Message  2 | User 3 | ✓ Sent
Message  3 | User 4 | ✓ Sent
Message  4 | User 5 | ✓ Sent
Message  5 | User 1 | ✓ Sent
Message  6 | User 2 | × Wait 7.4s
Message  7 | User 3 | × Wait 7.6s
Message  8 | User 4 | × Wait 7.3s
Message  9 | User 5 | × Wait 7.1s
Message 10 | User 1 | × Wait 6.9s
Message 11 | User 2 | × Wait 4.4s
Message 12 | User 3 | × Wait 4.8s
Message 13 | User 4 | × Wait 4.6s
Message 14 | User 5 | × Wait 4.2s
Message 15 | User 1 | × Wait 4.1s
Message 16 | User 2 | × Wait 1.5s
Message 17 | User 3 | × Wait 1.7s
Message 18 | User 4 | × Wait 1.4s
Message 19 | User 5 | × Wait 0.8s
Message 20 | User 1 | × Wait 0.5s
Waiting for limit reset...
=== New batch of messages after waiting ===
Message 21 | User 2 | ✓ Sent
Message 22 | User 3 | ✓ Sent
Message 23 | User 4 | ✓ Sent
Message 24 | User 5 | ✓ Sent
Message 25 | User 1 | ✓ Sent
Message 26 | User 2 | × Wait 6.5s
Message 27 | User 3 | × Wait 6.3s
Message 28 | User 4 | × Wait 6.2s
Message 29 | User 5 | × Wait 6.2s
Message 30 | User 1 | × Wait 6.5s
Message 31 | User 2 | × Wait 3.1s
Message 32 | User 3 | × Wait 3.7s
Message 33 | User 4 | × Wait 3.8s
Message 34 | User 5 | × Wait 3.7s
Message 35 | User 1 | × Wait 4.1s
Message 36 | User 2 | × Wait 1.0s
Message 37 | User 3 | × Wait 1.2s
Message 38 | User 4 | × Wait 1.9s
Message 39 | User 5 | × Wait 1.9s
Message 40 | User 1 | × Wait 2.6s
```
### Task 2: Implementation of a Rate Limiter using the Throttling algorithm to limit the frequency of messages in the chat

In the chat system, a mechanism to limit the frequency of user messages to prevent spam must be implemented. The implementation should use a Throttling algorithm to control the time intervals between messages, which ensures a fixed waiting period between user messages and limits the sending frequency if this interval is not adhered to.

#### Requirements:

1. The implementation should use the Throttling algorithm to control time intervals.

2. Basic system parameter: minimum interval between messages (min_interval) — 10 seconds.

3. Implement the ThrottlingRateLimiter class.

4. Implement the class methods:

can_send_message — to check the possibility of sending a message based on the time of the last message;

record_message — for recording a new message with the update of the last message's time;

time_until_next_allowed — for calculating the time until the next message can be sent.

5. The data structure for storing the time of the last message is Dict[str, float].

#### Results:
```
Select Rate Limiter: 1 - Sliding Window, 2 - Throttling
Enter choice: 2
=== Simulating Throttling Rate Limiter ===
Message  1 | User 2 | ✓ Sent
Message  2 | User 3 | ✓ Sent
Message  3 | User 4 | ✓ Sent
Message  4 | User 5 | ✓ Sent
Message  5 | User 1 | ✓ Sent
Message  6 | User 2 | × Wait 7.3s
Message  7 | User 3 | × Wait 6.8s
Message  8 | User 4 | × Wait 6.6s
Message  9 | User 5 | × Wait 7.1s
Message 10 | User 1 | × Wait 6.9s
Message 11 | User 2 | × Wait 4.0s
Message 12 | User 3 | × Wait 3.6s
Message 13 | User 4 | × Wait 3.5s
Message 14 | User 5 | × Wait 3.7s
Message 15 | User 1 | × Wait 3.9s
Message 16 | User 2 | × Wait 1.1s
Message 17 | User 3 | × Wait 1.1s
Message 18 | User 4 | × Wait 0.4s
Message 19 | User 5 | × Wait 1.2s
Message 20 | User 1 | × Wait 1.1s
Waiting for limit reset...
=== New batch of messages after waiting ===
Message 21 | User 2 | ✓ Sent
Message 22 | User 3 | ✓ Sent
Message 23 | User 4 | ✓ Sent
Message 24 | User 5 | ✓ Sent
Message 25 | User 1 | ✓ Sent
Message 26 | User 2 | × Wait 6.8s
Message 27 | User 3 | × Wait 6.9s
Message 28 | User 4 | × Wait 6.7s
Message 29 | User 5 | × Wait 7.0s
Message 30 | User 1 | × Wait 7.1s
Message 31 | User 2 | × Wait 4.2s
Message 32 | User 3 | × Wait 4.6s
Message 33 | User 4 | × Wait 4.3s
Message 34 | User 5 | × Wait 4.5s
Message 35 | User 1 | × Wait 4.7s
Message 36 | User 2 | × Wait 1.7s
Message 37 | User 3 | × Wait 2.1s
Message 38 | User 4 | × Wait 1.9s
Message 39 | User 5 | × Wait 2.4s
Message 40 | User 1 | × Wait 2.6s
```
