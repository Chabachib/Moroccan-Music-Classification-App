import numpy as np
import librosa
import math
import math
import statistics


number_to_genre_dict = {0:"gnawa" , 1:"chaabi", 2:"andalusian", 3:"rai", 4:"imazighn", 5:"rap", 6:"pop"}

def get_class_name(classes):
    print(f'the predicted class is {number_to_genre_dict[statistics.mode(classes)]}')
    return number_to_genre_dict[statistics.mode(classes)]

def class_pred(classifier, file):
    y, sr = librosa.load(file)
    oneSong = []
    for n in range(10):
        start_sample = 22050*3  * n
        end_sample = start_sample + 22050*3

        mfcc = librosa.feature.mfcc(y=y[start_sample:end_sample], sr=sr, n_mfcc=40, n_fft=2048, hop_length = 512)

        mfcc = mfcc.T

        if len(mfcc) == math.ceil( 22050*3 / 512 ):
                oneSong.append(mfcc.tolist())

    oneSong = np.array(oneSong, dtype=object)
    oneSong = nsong = np.asarray(oneSong).astype('float32')
    oneSong.shape

    with open('output.txt', 'w') as file:
      for sublist in oneSong:
          for item in sublist:
              line = ','.join(str(value) for value in item)
              file.write(line + '\n')

    prediction = classifier.predict(oneSong)

    classes_x =np.argmax(prediction,axis=1)
    return classes_x