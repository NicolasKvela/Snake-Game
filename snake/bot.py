"""
Random‑move baseline + training/demo scaffold
adapted to richer reward dict from snake_game.run_episode.
"""

import random

# ------------------------------- Bot ----------------------------------- #
class SnakeBot:
    DIRECTIONS = ("UP", "DOWN", "LEFT", "RIGHT")

    def next_move(self, state):
        return random.choice(self.DIRECTIONS)

# --------------------------- Training loop ----------------------------- #
N_EPISODES = 20            # ← adjust here
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

    # push logs up so the clear‑screen in the demo doesn't hide them
    print("\n" * BLANK_LINES_BEFORE_DEMO)

    print("=== Demo game with rendering ===\n")
    snake_game.run_episode(bot, render=True)

if __name__ == "__main__":
    train_and_demo()
