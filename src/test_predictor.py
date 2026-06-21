from predictor import predict_match

prediction, probs = predict_match(
    "Brazil",
    "Argentina"
)

print("Prediction:")

print(prediction)

print()

print("Probabilities:")

print(probs)