from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder


def transform(dataset):
    encoder = LabelEncoder()
    dataset['pets_encoded'] = encoder.fit_transform(dataset['pets'])
    dataset['purpose_encoded'] = encoder.fit_transform(dataset['purpose'])
    dataset['time_encoded'] = encoder.fit_transform(dataset['time'])

    # Split the dataset into features (X) and target (y)
    X = dataset[['size', 'pets_encoded', 'effort',
                 'purpose_encoded', 'time_encoded']]
    y_light = dataset['light']
    y_light = y_light.astype(float)  # Convert light values to float

    # Create and train the model
    model = DecisionTreeRegressor()
    model.fit(X, y_light)

# Function to convert user input to search values using the trained model


def convert_input_to_search_value(parameter, user_input):
    if parameter == 'size':
        # Convert user input to numeric value
        if user_input.isdigit():
            return int(user_input)
        else:
            # Handle invalid input (e.g., non-numeric values)
            return None
    elif parameter == 'pets':
        # Encode user input
        pets_encoded = encoder.transform([user_input])[0]
        return pets_encoded
    elif parameter == 'light':
        # Use the trained model to predict the light value based on user input
        size = int(input('Enter the size: '))
        pets = input('Enter the pet: ')
        effort = int(input('Enter the effort: '))
        purpose = input('Enter the purpose: ')
        time = input('Enter the time: ')

        # Encode user input
        pets_encoded = encoder.transform([pets])[0]
        purpose_encoded = encoder.transform([purpose])[0]
        time_encoded = encoder.transform([time])[0]

        # Create user input for prediction
        user_input = [[size, pets_encoded, effort,
                       purpose_encoded, time_encoded]]

        # Predict the light value using the trained model
        predicted_light = model.predict(user_input)
        return predicted_light[0]
    else:
        # Handle other parameters as needed
        return None
