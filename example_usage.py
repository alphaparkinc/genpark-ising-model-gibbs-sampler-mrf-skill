from client import IsingModelGibbsSampler

def main():
    print("=== Ising Model MRF Gibbs Sampler ===")
    sampler = IsingModelGibbsSampler()

    # Low temperature (beta=3.0) strong coupling (J=2.0) leads to aligned magnetization
    res = sampler.sample(num_spins=20, j_coupling=2.0, beta=3.0, sweeps=50)
    print("Sampling Result:", res)
    assert abs(res["magnetization"]) >= 0.5

    print("Ising Model Gibbs Sampler verified successfully!")

if __name__ == "__main__":
    main()
