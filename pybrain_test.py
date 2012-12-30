from pybrain.tools.shortcuts import buildNetwork
net = buildNetwork(2, 3, 1)
net.activate([2, 1])

from pybrain.datasets import SupervisedDataSet
ds = SupervisedDataSet(2, 1)

ds.addSample((0, 0), (0,))
ds.addSample((0, 1), (1,))
ds.addSample((1, 0), (1,))
ds.addSample((1, 1), (0,))

print len(ds)

for inpt, target in ds :
	print inpt, target

print ds['input']

from pybrain.supervised.trainers import BackpropTrainer
net = buildNetwork(2, 3, 1, bias=True, hiddenclass=TanhLayer)
trainer = BackpropTrainer(net, ds)

print trainer.train()
print trainer.trainUntilConvergence()


