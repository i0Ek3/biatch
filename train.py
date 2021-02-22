#!/usr/bin/env python
# coding=utf-8

import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() 

def train(a):
    w = tf.Variable(0, dtype=tf.float32)
    x = tf.placeholder(tf.float32, [3,1])
    
    cost = w ** 2 - 10 * w + 25
    train = tf.train.GradientDescentOptimizer(a).minimize(cost)

    init = tf.global_variables_initializer()
    with tf.Session() as session:
        session.run(init)
        print(session.run(w))
