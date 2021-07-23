
numfiles = 40000;

for k = 1:numfiles
  m = sprintf('cnn_data/%d.m4a', k);
  [y,Fs] = audioread(m);
  wavFilename = sprintf('cnn_wav/%d.wav', k);
  audiowrite(wavFilename,y,Fs);
  delete(m);
  clc 
  clear
end
%2282