#		python code
#		script_name:
#
#		author:Jingwen Huang
#		description:In U1M5, 16 measures music fade in at the beginning and fade out at the end



from earsketch import *

init()
setTempo(96)

#Music

m1=YG_POP_MELODY_10
m2=YG_POP_MELODY_7
m3=YG_POP_MELODY_8
m4=YG_POP_MELODY_9
g=YG_POP_GUITAR_1
c=YG_EDM_CLAP_4
shasha=YG_RNB_TAMBOURINE_1


fitMedia(m1, 1, 1, 5)
fitMedia(m2, 2, 4.75, 7)
fitMedia(m3, 3, 6.75, 9)
fitMedia(m4,4, 9, 17)
fitMedia(g, 5, 1, 16.75)
fitMedia(c, 6, 4, 17)
fitMedia(shasha, 7, 3, 17)


setEffect(5,VOLUME, GAIN, -2, 2.5, -2, 15)
setEffect(5,VOLUME, GAIN, -2, 15, -35, 17)
setEffect(4,VOLUME, GAIN, 0, 11, -10, 14)
setEffect(4,VOLUME, GAIN, -10, 15, -50, 17)
setEffect(6, VOLUME, GAIN, -4, 3, -4, 17)
setEffect(6,VOLUME, GAIN, -4, 15, -40, 17)
setEffect(7,VOLUME, GAIN, -3, 15, -40, 17)
setEffect(1,VOLUME,GAIN, -20, 1, 0, 2.5)
setEffect(5,VOLUME, GAIN, -17, 1, -2, 2.5)

finish()
