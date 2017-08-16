#Use
# -*- coding: GBK -*-
import time
from iching import iching
#####0. Set iching time
birthdata = input();
td = time.strftime('%Y%m%d',time.localtime(time.time()))
ichindData = str(birthdata)+str(td);
print('your input is',int(ichindData));
iching.ichingDate(int(ichindData))
# e.g., 19850526 is your birthday and 20150704 is the prediction time.
# of course, your can also input more precise time.
#####1. Start to predict

iching.getPredict()
#####2. Get the iching name

fixPred, changePred   = iching.getPredict()
iching.ichingName(fixPred, changePred  )
#####3. Get the iching text

print(iching.ichingText(fixPred, iching));

"""
#####4. Understand Three Changes

data = 50 - 1
sky, earth, firstChange, data = iching.getChange(data)
print(sky, '\n', earth, '\n',firstChange, '\n', data)

sky, earth, secondChange, data = iching.getChange(data)
print(sky, '\n', earth, '\n',secondChange, '\n', data)

sky, earth, thirdChange, data = iching.getChange(data)
print(sky, '\n', earth, '\n',thirdChange, '\n', data)
"""
"""
#####5. Plot transitions
import matplotlib.pyplot as plt
import pylab
fig = plt.figure(figsize=(15, 10),facecolor='white')
plt.subplot(2, 2, 1)
iching.plotTransition(1000, w = 50)
plt.subplot(2, 2, 2)
iching.plotTransition(1000, w = 50)
plt.subplot(2, 2, 3)
iching.plotTransition(1000, w = 50)
plt.subplot(2, 2, 4)
iching.plotTransition(1000, w = 50)
pylab.show()
"""
