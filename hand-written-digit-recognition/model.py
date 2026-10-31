# baseline cnn model for mnist
from numpy import mean
from numpy import std
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.optimizers import SGD
import keras

# scale pixels
def prep_pixels(train, test):
	# convert from integers to floats
	train_norm = train.astype('float32')
	test_norm = test.astype('float32')
	# normalize to range 0-1
	train_norm = train_norm / 255.0
	test_norm = test_norm / 255.0
	# return normalized images
	return train_norm, test_norm

# define cnn model
def define_model():
	model = Sequential()
	model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
	model.add(MaxPooling2D((2, 2)))
	model.add(Flatten())
	model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(10, activation='softmax'))
	# compile model
	opt = SGD(learning_rate=0.01, momentum=0.9)
	model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
	return model


# Function to load the pre-trained CNN model
def load_model(model_path: str = "best_model.keras"):
    """
    Nạp mô hình CNN với bộ tham số tối ưu đã huấn luyện trước.
    Trả về model ở trạng thái sẵn sàng dự đoán.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Không tìm thấy file trọng số: {model_path}. "
            f"Hãy chạy train_model.py để tạo file này trước."
        )

    model = keras.models.load_model(model_path)
    return model