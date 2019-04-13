import os
import tensorflow as tf

from abc import ABC, abstractmethod
from tensorflow.python.saved_model import tag_constants

class BaseNeuralNetwork(ABC):

    def __init__(self, save_dir='results'):
        self.save_dir = save_dir
        self.save_path = os.path.join(self.save_dir, 'best.ckpt')
        self.session = None
        self.x_t = None
        self.y_t = None
        self._logits = None
        self.init = None

    def init_model(self, X, y):
        self.session = tf.Session(config=tf.ConfigProto(log_device_placement=True))
        self.prediction
        self.optimize
        self.error
        self.init = tf.global_variables_initializer()
        self.session.run(self.init)

    def save(self, save_path):
        inputs = {"x_t": self.x_t}
        outputs = {"pred_proba": self.prediction}
        tf.saved_model.simple_save(self.session, save_path, inputs, outputs)

    def restore(self, save_path):
        graph = tf.Graph()
        self.session = tf.Session(graph=graph)
        tf.saved_model.loader.load(
            self.session,
            [tag_constants.SERVING],
            save_path,
        )
        self.x_t = graph.get_tensor_by_name('x_input:0')
        self.y_proba = graph.get_tensor_by_name('dnn/y_proba:0')

    @property
    @abstractmethod
    def prediction(self):
        pass

    @property
    @abstractmethod
    def loss(self):
        pass

    @property
    @abstractmethod
    def optimize(self):
        pass

    @property
    @abstractmethod
    def error(self):
        pass