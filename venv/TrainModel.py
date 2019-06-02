import tensorflow as tf
import DataForMovingPieces as dm
import DataForFieldPicking as df

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(input_shape=(8, 8, 6), filters=6, kernel_size=(3, 3), padding="same",
                           kernel_regularizer=tf.keras.regularizers.l2(0.001),
                           kernel_initializer=tf.keras.initializers.normal(stddev=1)),
    tf.keras.layers.Conv2D(input_shape=(8, 8, 12,), filters=12, kernel_size=(3, 3), padding="same",
                           kernel_regularizer=tf.keras.regularizers.l2(0.001),
                           kernel_initializer=tf.keras.initializers.normal(stddev=0.01)),
    tf.keras.layers.Conv2D(input_shape=(8, 8, 24), filters=24, kernel_size=(3, 3), padding="same",
                           kernel_regularizer=tf.keras.regularizers.l2(0.001),
                           kernel_initializer=tf.keras.initializers.normal(stddev=0.01)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu',
                          kernel_initializer=tf.keras.initializers.normal(stddev=0.01)),
    tf.keras.layers.Dense(128, activation='relu',
                          kernel_initializer=tf.keras.initializers.normal(stddev=0.01)),
    tf.keras.layers.Dense(64, activation='softmax')

])

model.compile(optimizer='adam',
              loss="categorical_crossentropy",
              metrics=['accuracy'])
dm.createData(2000, 2)
model.fit(games, labels, epochs=15, validation_split=0.8, batch_size=100)
model.save("Models/modelMovePawn")
