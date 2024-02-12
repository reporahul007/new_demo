import tensorflow as tf
print("tensorflow version",tf.__version__)
tf.compat.v1.disable_eager_execution()
a = tf.compat.v1.placeholder(tf.int64, shape=(3,1))
b = tf.compat.v1.placeholder(tf.int64, shape=(1,3))
c = tf.matmul(a,b)

with tf.compat.v1.Session() as sess:
    print(sess.run(c, feed_dict={a:[[3],[6],[9]],b:[[6,7,88888]]}))
