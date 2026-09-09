import math
import random

class IsingModelGibbsSampler:
    """Gibbs sampling on 1D/2D Ising spin lattices."""
    def sample(self, num_spins: int, j_coupling: float = 1.0, ext_field: float = 0.0,
               beta: float = 1.0, sweeps: int = 100) -> dict:
        # Initialize random spins (+1 or -1)
        spins = [random.choice([1, -1]) for _ in range(num_spins)]

        for _ in range(sweeps):
            for i in range(num_spins):
                # Periodic boundary neighbors
                left = spins[(i - 1) % num_spins]
                right = spins[(i + 1) % num_spins]
                effective_field = j_coupling * (left + right) + ext_field
                # P(s_i = +1) = 1 / (1 + exp(-2 * beta * effective_field))
                p_up = 1.0 / (1.0 + math.exp(-2.0 * beta * effective_field))
                spins[i] = 1 if random.random() < p_up else -1

        # Total energy
        energy = sum(-j_coupling * spins[i] * spins[(i + 1) % num_spins] for i in range(num_spins)) - ext_field * sum(spins)
        magnetization = sum(spins) / num_spins

        return {
            "num_spins": num_spins,
            "total_energy": round(energy, 4),
            "magnetization": round(magnetization, 4),
            "spins": spins
        }
