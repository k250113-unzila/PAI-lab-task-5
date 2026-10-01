import requests

API_URL = "https://api.example.com/predict"


def local_predict(text):
    cleaned = text.strip().lower()

    if not cleaned:
        return "Neutral", 0.0

    positive_words = [
        "good", "happy", "excellent", "love", "great", "positive",
        "wonderful", "nice", "success", "amazing"
    ]
    negative_words = [
        "bad", "sad", "angry", "hate", "poor", "negative", "terrible",
        "awful", "worst", "problem"
    ]

    positive_count = sum(1 for word in positive_words if word in cleaned)
    negative_count = sum(1 for word in negative_words if word in cleaned)

    if positive_count > negative_count:
        return "Positive", 0.85
    elif negative_count > positive_count:
        return "Negative", 0.82
    return "Neutral", 0.60


def call_prediction_api(text):
    try:
        response = requests.get(API_URL, params={"input": text}, timeout=10)

        if response.status_code == 200:
            data = response.json()

            if isinstance(data, dict):
                prediction = data.get("prediction", "Unknown")
                confidence = data.get("confidence", 0.0)
                return prediction, confidence

        elif response.status_code == 404:
            print("Prediction result was not found.")
        elif response.status_code == 400:
            print("Invalid input was provided.")
        else:
            print("API request failed.")
            print("Status Code:", response.status_code)

    except requests.exceptions.ConnectionError:
        print("Could not connect to the API. Falling back to local prediction.")
    except requests.exceptions.Timeout:
        print("The request took too long. Falling back to local prediction.")
    except requests.exceptions.HTTPError:
        print("There was an HTTP error. Falling back to local prediction.")
    except ValueError:
        print("The API returned invalid JSON. Falling back to local prediction.")
    except requests.exceptions.RequestException:
        print("Something went wrong while contacting the API. Falling back to local prediction.")

    return None


try:
    text = input("Enter text: ")

    result = call_prediction_api(text)

    if result is None:
        prediction, confidence = local_predict(text)
        print("\nInput:", text)
        print("Prediction:", prediction)
        print("Confidence:", confidence)
    else:
        prediction, confidence = result
        print("\nInput:", text)
        print("Prediction:", prediction)
        print("Confidence:", confidence)

except EOFError:
    print("\nNo input provided.")