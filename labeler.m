numfiles = 60000;

for k = 1:numfiles
  m = sprintf('full_wav/%d.wav', k);
  n = sprintf('full_label/%d.txt',k);
  vad(m,n);
  clc 
  clear
end