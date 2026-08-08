from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model and location encoder
model, location_encoder = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            # Get user input
            location = request.form["location"].strip().lower()
            size = int(request.form["size"])
            sqft = float(request.form["total_sqft"])
            bath = int(request.form["bath"])
            balcony = int(request.form["balcony"])

            # Convert dataset locations to lowercase
            location_classes = [loc.lower() for loc in location_encoder.classes_]

            # Check if location exists
            if location in location_classes:
                location_encoded = location_classes.index(location)
            else:
                raise ValueError("Location not found")

            # Predict
            prediction = model.predict([
                [location_encoded, size, sqft, bath, balcony]
            ])[0]

        except:
            error = "Invalid input or location not found."

    return render_template(
        "index.html",
        prediction=prediction,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)