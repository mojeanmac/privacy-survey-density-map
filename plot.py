import matplotlib.pyplot as plt
import seaborn as sns
import csv
from pandas import *

#reordered headers, renamed the first Q88_1 to Q87_1

df = read_csv('privacytest.csv', skiprows=1)

#child protection
birthdate = df['Q75_1']
under13 = df['Q78_1']

child = concat([birthdate, under13])

#third parties
outsidePurchase = df['Q80_1']
targetedAds = df['Q84_1']

thirdparties = concat([outsidePurchase, targetedAds])

#data tracking
gameRecs = df['Q87_1']
orderRecs = df['Q88_1']
friendRecs = df['Q89_1']

datatracking = concat([gameRecs, orderRecs, friendRecs])

#biometric
eyePhoto = df['Q133_1']
handPhoto = df['Q94_1']
facePhoto = df['Q132_1']

photos = concat([eyePhoto, handPhoto, facePhoto])

eyeData = df['Q94_1']
handData = df['Q131_1']
faceData = df['Q95_1']

data = concat([eyeData, handData,faceData])

voice_moderation = df['Q69_1']
voice_buisness = df['Q71_1']

voice = concat([voice_moderation, voice_buisness])

biometric = concat([data, voice])

sns.kdeplot(thirdparties, color = "g", label = "Third Parties")
sns.kdeplot(datatracking, color = "b", label = "Data Tracking")
sns.kdeplot(child, color = "y", label = "Child Safety")
sns.kdeplot(biometric, color = "r", label = "Biometric Data")
plt.xlabel('User Trust')
plt.show()
