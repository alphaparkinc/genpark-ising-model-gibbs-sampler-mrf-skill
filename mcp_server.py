import sys
import json
from client import IsingModelGibbsSampler

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "sample":
        s = IsingModelGibbsSampler()
        return s.sample(params.get("num_spins", 10), params.get("j", 1.0),
                        params.get("field", 0.0), params.get("beta", 1.0), params.get("sweeps", 50))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
