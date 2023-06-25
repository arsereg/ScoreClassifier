from factories.ScoreFactory import ScoreFactory
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder

scoreFactory = ScoreFactory()

def createScores():
    scoresQuantity = 10_000_000
    scores = scoreFactory.createScores(n=scoresQuantity)
    #save scores to csv
    scoresDf = pd.DataFrame([score.to_dict() for score in scores])
    scoresDf.to_csv('scores.csv', index=False)

def trainNewModel():
    data = pd.read_csv('scores.csv')
    features = data[['value','modifier']]
    labels = data['classification']

    features = features.apply(pd.to_numeric)

    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(labels)

    datasetPercentageForTraining = 0.8
    train_size = int(datasetPercentageForTraining * len(features))
    train_features, train_labels = features[:train_size], labels[:train_size]
    test_features, test_labels = features[train_size:], labels[train_size:]

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(2,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

    model.compile(optimizer='adam', loss='mean_squared_error')

    epochSize = 10

    model.fit(train_features, train_labels, epochs=epochSize)

    loss = model.evaluate(test_features, test_labels)
    print('Loss: ', loss)

    model.save(f'trained_model_{epochSize}_epochs_loss_{loss}')

    new_data = pd.DataFrame({'value': [16, 8, 20], 'modifier': [3, -1, 5]})
    new_data = new_data.apply(pd.to_numeric)
    predictions = model.predict(new_data)
    print('Predictions: ', predictions)



if __name__ == '__main__':
    trainNewModel()
