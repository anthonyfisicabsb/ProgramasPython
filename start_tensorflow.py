"""First example with TensorFlow"""

import tensorflow as tf

sess = tf.Session()
tens1 = tf.constant([[[1, 2], [2, 3]], [[3, 4], [5, 6]]])

print(sess.run(tens1)[1, 1, 0])
