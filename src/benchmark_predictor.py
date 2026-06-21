import time
from predictor import predict_match

start = time.time()

for _ in range(1000):
    predict_match("Argentina", "France")

end = time.time()

print(
    "1000 predictions:",
    round(end - start, 2),
    "seconds"
)