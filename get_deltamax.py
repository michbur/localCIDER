import michalcider
from michalcider.sequenceParameters import SequenceParameters

# create a SequenceParameters object with your amino acid sequence
#SeqOb = SequenceParameters("EKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEK")
SeqOb = SequenceParameters("SYSYSYSYSYSYSYSYSYSYSYSYSY")


print("Seq: SYSYSYSYSYSYSYSYSYSYSYSYSY")

print("Delta:")
print(SeqOb.get_delta()) 

print("DeltaMax:")
print(SeqOb.get_deltaMax()) 


print("Kappa:")
print(SeqOb.get_kappa()) 
