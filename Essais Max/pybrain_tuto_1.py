from pybrain.structure import FeedForwardNetwork
n = FeedForwardNetwork()

from pybrain.structure import LinearLayer, SigmoidLayer
inLayer = LinearLayer(2)
hiddenLayer = SigmoidLayer(3)
outLayer = LinearLayer(1)

n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)

