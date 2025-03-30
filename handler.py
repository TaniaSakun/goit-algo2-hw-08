import time
import random
from collections import deque
from typing import Dict

class ThrottlingRateLimiter:
    """
    Implements a throttling rate limiter that allows a message to be sent only if a minimum interval has passed.
    """
    def __init__(self, min_interval: float = 10.0):
        self.min_interval = min_interval
        self.messages: Dict[str, float] = {}

    def can_send_message(self, user_id: str) -> bool:
        """Checks if a user is allowed to send a message based on the minimum interval."""
        if user_id not in self.messages:
            return True
        return time.monotonic() - self.messages[user_id] >= self.min_interval

    def record_message(self, user_id: str) -> bool:
        """Records the message timestamp if allowed."""
        if self.can_send_message(user_id):
            self.messages[user_id] = time.monotonic()
            return True
        return False

    def time_until_next_allowed(self, user_id: str) -> float:
        """Calculates the remaining time before a user can send another message."""
        if user_id not in self.messages:
            return 0.0
        remaining = self.messages[user_id] + self.min_interval - time.monotonic()
        return max(0.0, remaining)


class SlidingWindowRateLimiter:
    """
    Implements a sliding window rate limiter that allows a fixed number of messages within a given time window.
    """
    def __init__(self, window_size: int = 10, max_requests: int = 1):
        self.window_size = window_size
        self.max_requests = max_requests
        self.user_messages: Dict[str, deque] = {}

    def _cleanup_window(self, user_id: str, current_time: float) -> None:
        """Removes expired timestamps from the sliding window."""
        if user_id in self.user_messages:
            messages = self.user_messages[user_id]
            while messages and messages[0] < current_time - self.window_size:
                messages.popleft()
            if not messages:
                del self.user_messages[user_id]

    def can_send_message(self, user_id: str) -> bool:
        """Checks if a user can send a message based on the sliding window rule."""
        current_time = time.monotonic()
        self._cleanup_window(user_id, current_time)
        return user_id not in self.user_messages or len(self.user_messages[user_id]) < self.max_requests

    def record_message(self, user_id: str) -> bool:
        """Records the message timestamp if allowed."""
        if self.can_send_message(user_id):
            current_time = time.monotonic()
            if user_id not in self.user_messages:
                self.user_messages[user_id] = deque()
            self.user_messages[user_id].append(current_time)
            return True
        return False

    def time_until_next_allowed(self, user_id: str) -> float:
        """Calculates the remaining time before a user can send another message."""
        current_time = time.monotonic()
        self._cleanup_window(user_id, current_time)
        if user_id not in self.user_messages:
            return 0.0
        last_message = self.user_messages[user_id][-1]
        return max(0.0, last_message + self.window_size - current_time)