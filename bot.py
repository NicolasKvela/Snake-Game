"""
Greedy-move SnakeBot + training/demo scaffold
Uses simple logic to move toward food while avoiding walls.
"""

import random

# ------------------------------- Smarter Bot ---------------------------- #
class SnakeBot:
    DIRECTIONS = ("UP", "DOWN", "LEFT", "RIGHT")

    def next_move(self, state):
        head = state["snake_head"]
        food = state["food"]
        width = state["board_width"]
        height = state["board_height"]
        snake = state["snake"]

        def is_safe(pos):
            x, y = pos
            return (
                0 <= x < width and
                0 <= y < height and
                pos not in snake
            )

        def get_next_pos(direction):
            x, y = head
            if direction == "UP":    return (x, y - 1)
            if direction == "DOWN":  return (x, y + 1)
            if direction == "LEFT":  return (x - 1, y)
            if direction == "RIGHT": return (x + 1, y)

        # Prefer directions that move toward the food and are safe
        moves = []
        if food[0] < head[0]: moves.append("LEFT")
        if food[0] > head[0]: moves.append("RIGHT")
        if food[1] < head[1]: moves.append("UP")
        if food[1] > head[1]: moves.append("DOWN")

        # Filter to safe moves only
        safe_moves = [m for m in moves if is_safe(get_next_pos(m))]
        if safe_moves:
            return random.choice(safe_moves)

        # No greedy move possible, try any safe direction
        fallback = [d for d in self.DIRECTIONS if is_safe(get_next_pos(d))]
        return random.choice(fallback) if fallback else random.choice(self.DIRECTIONS)

# --------------------------- Training loop ----------------------------- #
N_EPISODES = 20
BLANK_LINES_BEFORE_DEMO = 17

def train_and_demo():
    import snake_game

    bot      = SnakeBot()
    comps    = []   # composite scores
    raw_food = []   # plain scores

    print(f"\nRunning {N_EPISODES} head‑less training games …")
    for ep in range(1, N_EPISODES + 1):
        res = snake_game.run_episode(bot, render=False)
        comps.append(res["composite"])
        raw_food.append(res["score"])
        print(f"Episode {ep:3d}: "
              f"score={res['score']:2d}  ticks={res['ticks']:4d}  "
              f"comp={res['composite']:4d}",
              flush=True)

    avg_comp = sum(comps) / len(comps)
    avg_food = sum(raw_food) / len(raw_food)
    print(f"\nTraining finished. Avg food = {avg_food:.2f} "
          f"| Avg composite = {avg_comp:.2f}\n")

    print("\n" * BLANK_LINES_BEFORE_DEMO)
    print("=== Demo game with rendering ===\n")
    snake_game.run_episode(bot, render=True)

if __name__ == "__main__":
    train_and_demo()
