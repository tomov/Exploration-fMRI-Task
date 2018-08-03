avg_iti = 3
avg_isi = 2
choice = 2
feedback = 1
nBlocks = 4
nTrials = 10
avg_ibi = 6
avg_iri = 10
nRuns = 8

runDuration = nTrials*(choice + avg_iti + avg_isi + feedback)*nBlocks + avg_ibi*nBlocks
print runDuration

print runDuration/60

expDuration = (runDuration + avg_iri)*nRuns

print expDuration/60
